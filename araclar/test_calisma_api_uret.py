#!/usr/bin/env python3
"""calisma_api_uret.py birim sınamaları (API'siz, Chrome'suz): python3 -m unittest araclar/test_calisma_api_uret.py"""
import copy
import json
import sys
import tempfile
import types
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calisma_api_uret as c  # noqa: E402
import ozet_api_uret as oz  # noqa: E402


def ornek_kagit():
    """Doğrulamadan geçen bir model çıktısı (yayımlanmış 7-matematik-8 kâğıdından)."""
    return c.api_bicimi(c.gorselli_yukle('7-matematik-8'))


class OzelKimlik(unittest.TestCase):
    def test_gidis_donus(self):
        for h, k in ((9, '7-matematik'), (16, '9-kuran-i-kerim'), (3, '12-din-kulturu-ve-ahlak-bilgisi'), (12, '10-tde')):
            for tur in 'idg':
                cid = c.ozel_kimlik(h, k, tur)
                self.assertLessEqual(len(cid), 64)
                self.assertEqual(c.ozel_coz(cid), (h, k, tur))

    def test_en_uzun_ders(self):
        kimlikler = {p.stem.rsplit('-', 1)[0] for p in c.OZETLER.glob('*.json')}
        for k in kimlikler:
            self.assertEqual(c.ozel_coz(c.ozel_kimlik(16, k, 'g')), (16, k, 'g'))

    def test_baska_bot_kimligi(self):
        self.assertEqual(c.ozel_coz('h9-7-matematik-i'), (None, None, None))     # özet botu
        self.assertEqual(c.ozel_coz('ck-h9-7-matematik-x'), (None, None, None))
        self.assertEqual(oz._ozel_coz(c.ozel_kimlik(9, '7-matematik', 'i')), (None, None, None))
        with self.assertRaises(ValueError):
            c.ozel_kimlik(9, '7-matematik', 'x')


class Eksikler(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.oz, self.ck = self.tmp / 'ozetler', self.tmp / 'calisma'
        self.oz.mkdir()
        self.ck.mkdir()
        for ad, tarih in (('5-deneme-9', '2026-11-20'), ('5-deneme-10', '2026-11-27'), ('7-deneme-9', '2026-11-18'),
                          ('7-deneme-10', '2026-11-25'), ('7-baska-9', '2026-11-19'), ('9-deneme-12', '2026-12-10')):
            (self.oz / f'{ad}.json').write_text(json.dumps({'yayin_tarihi': tarih}))
        (self.ck / '7-deneme-9.json').write_text('{}')
        (self.oz / 'bozuk.json').write_text('{}')

    def ad(self, **k):
        return [c.birim_ad(*b) for b in c.eksikler(ozet_dizin=self.oz, kagit_dizin=self.ck, **k)]

    def test_hepsi_tarih_sirali(self):
        self.assertEqual(self.ad(), ['7-baska-9', '5-deneme-9', '7-deneme-10', '5-deneme-10', '9-deneme-12'])

    def test_suzgecler(self):
        self.assertEqual(self.ad(haftalar=c.aralik('9-10'), siniflar=c.aralik('5-7')), ['7-baska-9', '5-deneme-9', '7-deneme-10', '5-deneme-10'])
        self.assertEqual(self.ad(dersler={'baska', '5-deneme'}), ['7-baska-9', '5-deneme-9', '5-deneme-10'])
        self.assertEqual(self.ad(en_cok=2), ['7-baska-9', '5-deneme-9'])
        self.assertEqual(self.ad(haftalar={12}), ['9-deneme-12'])

    def test_aralik(self):
        self.assertEqual(c.aralik('9-12,14'), {9, 10, 11, 12, 14})
        self.assertIsNone(c.aralik(''))
        with self.assertRaises(ValueError):
            c.aralik('9-a')

    def test_gercek_depo(self):
        # gerçek eksik listesi: özeti olan, kâğıdı olmayan; sıralı
        liste = c.eksikler(haftalar={9})
        self.assertTrue(liste)
        for b in liste:
            self.assertTrue((c.OZETLER / f'{c.birim_ad(*b)}.json').exists())
            self.assertFalse((c.CALISMA / f'{c.birim_ad(*b)}.json').exists())


class Dogrulama(unittest.TestCase):
    def sorunlar(self, d, sinif=7):
        return c.sema_denetle(d, sinif) or c.icerik_denetle(d)

    def test_yayimlanmis_kagit_gecer(self):
        self.assertEqual(self.sorunlar(ornek_kagit()), [])

    def test_konu_duz_metin(self):
        # 11.11.2026: "m{us:|3}" başlığı <title> içine ham basılmış, yayın denetimi durmuştu.
        d = ornek_kagit()
        d['konu'] = 'Hacim ölçme: m{us:|3} ve dm{us:|3}'
        self.assertTrue(any('düz metin' in s for s in self.sorunlar(d)))
        d['konu'] = 'Hacim ölçme: m³ ve dm³'
        self.assertEqual(self.sorunlar(d), [])

    def test_duz_baslik(self):
        import calisma_uret as cu
        self.assertEqual(cu.duz_baslik('Hacim ölçme'), 'Hacim ölçme')
        self.assertEqual(cu.duz_baslik('Hacim: m{us:|3} ve cm{us:|3}'), 'Hacim: m³ ve cm³')
        self.assertEqual(cu.duz_baslik('{us:x|2} ve H{alt:2}O, {alt:H|2}'), 'x² ve H₂O, H₂')
        self.assertEqual(cu.duz_baslik('{us:a|n + k}'), 'a üssü n + k')
        self.assertEqual(cu.duz_baslik('{kesir:3|4} ile {kesir:1|1|2}'), '3 bölü 4 ile 1 tam 1 bölü 2')
        self.assertEqual(cu.duz_baslik('{kok:16 + 9}, {kok:−27|3}'), 'karekök 16 + 9, küpkök −27')
        self.assertEqual(cu.duz_baslik('{koyu:Önemli} {kesir:{us:x|2}|3}'), 'Önemli x² bölü 3')
        for ham in ('m{us:|3}', '{kesir:1|2}', '{kok:2}', '{aci:ABC}', '{bilinmeyen:a|b}', 'yarım {us:x'):
            self.assertNotRegex(cu.duz_baslik(ham), r'[{}√]')

    def tur_sorusu(self, d, tur):
        return next(s for s in d['sorular'] if s['tur'] == tur)

    def test_coktan(self):
        d = ornek_kagit()
        s = self.tur_sorusu(d, 'coktan')
        s['secenekler'] = s['secenekler'][:3]
        self.assertTrue(any('4 ya da 5' in x for x in self.sorunlar(d)))
        d = ornek_kagit()
        self.tur_sorusu(d, 'coktan')['dogru'] = 7
        self.assertTrue(any('0 tabanlı' in x for x in self.sorunlar(d)))
        d = ornek_kagit()
        self.tur_sorusu(d, 'coktan')['secenekler'].append('E şıkkı')
        self.assertTrue(any('4 şıklı' in x for x in self.sorunlar(d, 7)))
        self.assertFalse(any('4 şıklı' in x for x in c.sema_denetle(d, 10)))

    def test_sifre(self):
        d = ornek_kagit()
        d['sorular'][0] = {'tur': 'sifre', 'duzey': 'hatirla', 'soru': 'Şifreyi çözünüz.', 'sonuc': 'ışık',
                           'satirlar': [{'ipucu': 'a', 'cevap': 'ırmak', 'anahtar': 0}, {'ipucu': 'b', 'cevap': 'kuş', 'anahtar': 2},
                                        {'ipucu': 'c', 'cevap': 'ilk', 'anahtar': 0}, {'ipucu': 'd', 'cevap': 'kara', 'anahtar': 0}]}
        self.assertTrue(any('anahtar harfleri' in x for x in c.sema_denetle(d, 7)))     # I-Ş-İ-K ≠ IŞIK
        d['sorular'][0]['sonuc'] = 'ışık'
        d['sorular'][0]['satirlar'][2] = {'ipucu': 'c', 'cevap': 'ısı', 'anahtar': 0}
        self.assertEqual(c.sema_denetle(d, 7), [])
        d['sorular'][0]['satirlar'][1]['anahtar'] = 0
        self.assertTrue(any('anahtar harfleri' in x for x in c.sema_denetle(d, 7)))
        d['sorular'][0]['satirlar'][1]['anahtar'] = 9
        self.assertTrue(any('anahtar sırası' in x for x in c.sema_denetle(d, 7)))

    def test_duzey_ve_tur(self):
        d = ornek_kagit()
        d['sorular'][0]['duzey'] = 'analiz'
        self.assertTrue(any('duzey' in x for x in self.sorunlar(d)))
        d = ornek_kagit()
        d['sorular'][0]['tur'] = 'bulmaca'
        self.assertTrue(any('tur geçersiz' in x for x in self.sorunlar(d)))
        d = ornek_kagit()
        d['sorular'] = d['sorular'][:11]
        self.assertTrue(any('12-14' in x for x in self.sorunlar(d)))

    def test_svg(self):
        d = ornek_kagit()
        no = next(iter(d['gorseller']))
        d['gorseller'][no] = '<svg viewBox="0 0 100 50"><text>A &nbsp; B</text></svg>'
        self.assertTrue(any('XML' in x for x in self.sorunlar(d)))
        d['gorseller'][no] = '<svg viewBox="0 0 100 50"><text x="5" y="20">3/4 litre</text></svg>'
        self.assertTrue(any('yatay kesir' in x for x in self.sorunlar(d)))
        d['gorseller'][no] = '<svg viewBox="0 0 100 50"><script>x()</script></svg>'
        self.assertTrue(any('script' in x for x in self.sorunlar(d)))
        d['gorseller'][no] = '<svg viewBox="0 0 900 50"></svg>'
        self.assertTrue(any('600' in x for x in self.sorunlar(d)))
        d['gorseller']['99'] = '<svg viewBox="0 0 10 10"></svg>'
        self.assertTrue(any('"99"' in x for x in self.sorunlar(d)))

    def test_metin_kurallari(self):
        for metin, beklenen in (('Ders kitabındaki tabloya göre hangisi doğrudur?', 'atıf'),
                                ('Konu özetinde verilen bilgiye göre hangisi doğrudur?', 'dış gönderme'),
                                ('Bir şişenin 3/4 kadarı doludur. Hangisi doğrudur?', 'yatay kesir'),
                                ('Bir şişenin {kesir:3|4} kadarı {renk:doludur}. Hangisi doğrudur?', None),
                                ('Haritanın ölçeği 1/100 000 olduğuna göre hangisi doğrudur?', None),
                                ('{xyz:a} hangisidir?', 'tanımsız gösterim')):
            d = ornek_kagit()
            s = next(x for x in d['sorular'] if x['tur'] == 'coktan')
            s['soru'] = metin
            sorun = c.icerik_denetle(d)
            if beklenen:
                self.assertTrue(any(beklenen in x for x in sorun), (metin, sorun))
            else:
                self.assertEqual(sorun, [], metin)

    def test_gorsel_gondermesi_gorselsiz(self):
        d = ornek_kagit()
        i = next(i for i, x in enumerate(d['sorular']) if x['tur'] == 'coktan')
        d['sorular'][i]['soru'] = 'Görseldeki kartlardan hangisi doğrudur?'
        d['gorseller'].pop(str(i + 1), None)
        self.assertTrue(any('K164' in x for x in c.icerik_denetle(d)))

    def test_ortusme(self):
        onceki = c.api_bicimi(c.gorselli_yukle('7-matematik-7'))
        d = ornek_kagit()
        self.assertEqual(c.ortusme(d, '7-matematik', 8), [])
        d['sorular'][0] = copy.deepcopy(onceki['sorular'][2])
        self.assertTrue(any('örtüşüyor' in x for x in c.ortusme(d, '7-matematik', 8)))
        self.assertEqual([x for x in c.ortusme(d, '7-matematik', 8, haric=range(1, 8)) if 'sorular[0]' in x], [])


class Tamamlama(unittest.TestCase):
    def test_bot_alanlari_ve_modul(self):
        d = ornek_kagit()
        kagit, gorseller = c.tamamla(d, 7, 'matematik', 9, 'claude-opus-5-5')
        self.assertEqual((kagit['sinif'], kagit['ders'], kagit['hafta']), (7, 'matematik', 9))
        self.assertRegex(kagit['yayin_tarihi'], r'^\d{4}-\d{2}-\d{2}$')
        self.assertTrue(kagit['tarih'] and kagit['ciktilar'])
        self.assertTrue(all(isinstance(k, int) for k in gorseller))
        tmp = Path(tempfile.mkdtemp())
        eski = dict(c.YAZ)
        try:
            for k in c.YAZ:
                c.YAZ[k] = tmp / k
            c.taslak_yaz('7-matematik-9', {'metin': '{}'})
            c.kaydet(kagit, gorseller, '7-matematik-9')
            self.assertIsNone(c.taslak_oku('7-matematik-9'))       # kayıtla taslak silinir
            o = c.gorselli_yukle('7-matematik-9', tmp / 'kagit', tmp / 'gorsel')
            self.assertEqual({i for i, s in enumerate(o['sorular'], 1) if s.get('gorsel')}, set(gorseller))
            self.assertEqual(c.sema_denetle(c.api_bicimi(o), 7), [])
        finally:
            c.YAZ.update(eski)

    def test_goz_sorunlari(self):
        bulgular = c.goz_coz('{"sorunlar": [{"soru": 2, "agirlik": "ciddi", "sorun": "yazı taşıyor"}, {"soru": 0, "agirlik": "kucuk", "sorun": "boşluk"}]}')
        m = c.goz_sorunlari(bulgular, [3, 1, 2])
        self.assertIn('basılı 2. soru = JSON sorular[0]', m[0])
        self.assertIn('sayfa geneli', m[1])
        self.assertIsNone(c.goz_coz('yanıt yok'))


# ------------------------------------------------------------------ toplu istek listesi: başka botların istekleri

class _Batches:
    def __init__(self, liste):
        self.liste = liste

    def list(self, limit=50):
        return iter(self.liste)

    def results(self, kimlik):
        return iter([])


def _istemci(*kimlikler):
    simdi = datetime.now(timezone.utc)
    liste = [types.SimpleNamespace(id=k, processing_status='in_progress', created_at=simdi) for k in kimlikler]
    return types.SimpleNamespace(messages=types.SimpleNamespace(batches=_Batches(liste)))


class BaskaBotlar(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.eski = (oz.DURUM, oz._DURUM, c.DURUM)
        (self.tmp / 'calisma_toplu_durum.json').write_text(json.dumps({'gonderilen': {'msgbatch_ck': {'istekler': ['ck-h9-7-matematik-i']}}, 'toplanan': ['msgbatch_ck_eski']}))
        (self.tmp / 'toplu_durum.json').write_text(json.dumps({'gonderilen': {'msgbatch_oz': {'istekler': ['h40-7-matematik-i']}}, 'toplanan': []}))

    def tearDown(self):
        oz.DURUM, oz._DURUM, c.DURUM = self.eski

    def test_ozet_botu_calisma_isteklerini_bilinmeyen_saymaz(self):
        oz.DURUM, oz._DURUM = self.tmp / 'toplu_durum.json', None
        args = types.SimpleNamespace(model='claude-opus-5-5', caba='medium')
        t = oz.topla(_istemci('msgbatch_ck', 'msgbatch_ck_eski', 'msgbatch_oz'), args, {}, oz.Sayac('claude-opus-5-5'),
                     float('inf'), oz.Butce(0, 1), bekle_bilinmeyen=False)
        self.assertFalse(t['bilinmeyen'])
        self.assertEqual(t['bekleyen'], {(40, '7-matematik')})
        oz._DURUM = None
        t = oz.topla(_istemci('msgbatch_baska'), args, {}, oz.Sayac('claude-opus-5-5'), float('inf'), oz.Butce(0, 1), bekle_bilinmeyen=False)
        self.assertTrue(t['bilinmeyen'])          # hiçbir kayıtta olmayan süren istek yine durdurur

    def test_calisma_botu_ozet_isteklerini_bilinmeyen_saymaz(self):
        c.DURUM = oz.DURUM = self.tmp / 'calisma_toplu_durum.json'
        oz._DURUM = None
        args = types.SimpleNamespace(model='claude-opus-5-5', caba='medium', durum_gonder=False)
        ctx = {'gecici': self.tmp, 'model': 'claude-opus-5-5'}
        eski_yaz = dict(c.YAZ)
        c.YAZ['taslak'] = self.tmp / 'taslak'
        try:
            t = c.topla(_istemci('msgbatch_ck', 'msgbatch_oz'), args, ctx, c.Sayac('claude-opus-5-5'), float('inf'),
                        oz.Butce(0, 1), bekle_bilinmeyen=False)
            self.assertFalse(t['bilinmeyen'])
            self.assertEqual(t['bekleyen'], {'7-matematik-9'})
            oz._DURUM = None
            t = c.topla(_istemci('msgbatch_baska'), args, ctx, c.Sayac('claude-opus-5-5'), float('inf'), oz.Butce(0, 1), bekle_bilinmeyen=False)
            self.assertTrue(t['bilinmeyen'])
        finally:
            c.YAZ.update(eski_yaz)


if __name__ == '__main__':
    unittest.main()
