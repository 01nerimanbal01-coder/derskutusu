#!/usr/bin/env python3
"""Çevrimiçi test soru havuzu (kullanıcı 13.10.2026: "öğrenci modülüne online soru havuzu; her konuya ve çıktıya özel sorular
otomatik seçilsin, çok soru olsun").

Kaynaklar (sitedeki yapılandırılmış sorular; ders kitabıyla uyumlu özgün metinler):
- araclar/ozetler/<sinif>-<ders>-<hafta>.json: etkinlikler (coktan, dy, eslestir, bosluk, ogretici) ve ornekler
- araclar/calisma/<sinif>-<ders>-<n>.json: sorular (coktan, dy, bosluk, eslestir, siralama, kisa, acik; tablo/sifre/kavram alınmaz)
- araclar/sorular/<sinif>-<ders>.json: elle ya da ek olarak yazılan sorular (aynı biçim, "konu" kodu ve "cikti" kodlarıyla)
Görsele dayanan sorular (görsel, resim, harita, grafik, tablo...) havuza girmez.

Çıktı: public/veri/soru/<sinif>-<ders>.json (konular, çıktılar, sorular; metinler ozet_uret.e ile HTML'e çevrilmiş)
       public/veri/soru/dizin.json (ders başına sayılar: konu, çıktı, tür) — test.js kurulum ekranı bunu okur.
Çalıştırma: LC_ALL=C.UTF-8 python3 araclar/soru_havuzu_uret.py
"""
import importlib.util
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
PUBLIC = ARACLAR.parent / 'public'
CIKTI = PUBLIC / 'veri' / 'soru'
_spec = importlib.util.spec_from_file_location('ozet_uret', ARACLAR / 'ozet_uret.py')
_ozet = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ozet)
e = _ozet.e   # kaçış + {kesir:3|4}, {kok:2}, {us:2|3}, {ar:...} gibi gösterimler

KOD = re.compile(r'^\s*([A-ZÇĞİÖŞÜ]{1,6}\.\d+(?:\.\d+)+)\.?\s*(.*)$')
# Kâğıttaki görsele/tabloya dayanan sorular ekranda tek başına çözülemez
GORSEL = re.compile(r'görsel|resim|harita|grafi[kğ]|tablo(da|daki|ya|yu|nun)|şekilde|şekli\b|numaralı|yukarıdaki|aşağıdaki (şekil|görsel|tablo|harita|grafik)|çizimde|karekod', re.I)
OTOMATIK = ('coktan', 'dy', 'bosluk', 'eslestir', 'siralama')


def kisa(t):
    return re.sub(r'[^a-z0-9çğıöşü]+', '-', str(t).lower().replace('I', 'ı').replace('İ', 'i')).strip('-')


def cikti_kodlari(liste):
    """'MAT.5.3.1. Temel geometrik...' → [('MAT.5.3.1', 'Temel geometrik...')]"""
    out = []
    for c in liste or []:
        m = KOD.match(str(c))
        if m:
            out.append((m.group(1), m.group(2).strip()))
    return out


def konu_bul(agac, hafta, konu_adi):
    """Haftayı içeren konu; aynı adlı konu varsa o. Ağaç yoksa addan üretilen kod."""
    if not agac:
        return kisa(konu_adi), konu_adi, ''
    adaylar = [(u['ad'], k) for u in agac['uniteler'] for k in u['konular'] if hafta in (k.get('haftalar') or [])]
    if not adaylar:
        adaylar = [(u['ad'], k) for u in agac['uniteler'] for k in u['konular'] if kisa(k['ad']) == kisa(konu_adi)]
    if not adaylar:
        return kisa(konu_adi), konu_adi, ''
    ayni = [a for a in adaylar if kisa(a[1]['ad']) == kisa(konu_adi)]
    unite, k = (ayni or adaylar)[0]
    return k['kod'], k['ad'], unite


def temiz(metin):
    return e(metin) if metin not in (None, '') else ''


def gorsel_ister(*metinler):
    return any(GORSEL.search(str(m or '')) for m in metinler)


def etkinlik_sorusu(x):
    t = x.get('tur')
    if t == 'coktan' and isinstance(x.get('secenekler'), list) and len(x['secenekler']) >= 2 and isinstance(x.get('dogru'), int):
        return {'tur': 'coktan', 'soru': temiz(x['soru']), 'secenekler': [temiz(s) for s in x['secenekler']], 'dogru': x['dogru'], 'aciklama': temiz(x.get('aciklama'))}
    if t == 'dy' and x.get('ifadeler'):
        return {'tur': 'dy', 'soru': temiz(x.get('yonerge') or x.get('soru') or 'Doğru mu, yanlış mı?'),
                'ifadeler': [{'metin': temiz(i['metin']), 'dogru': bool(i['dogru']), 'aciklama': temiz(i.get('aciklama'))} for i in x['ifadeler']]}
    if t == 'eslestir' and x.get('ciftler') and len(x['ciftler']) >= 2:
        return {'tur': 'eslestir', 'soru': temiz(x.get('yonerge') or x.get('soru') or 'Eşleştiriniz.'), 'ciftler': [[temiz(a), temiz(b)] for a, b in x['ciftler']]}
    if t == 'bosluk' and x.get('cumleler'):
        cumleler = [{'metin': temiz(c['metin']), 'cevap': temiz(c['cevap'])} for c in x['cumleler'] if '___' in str(c.get('metin', ''))]
        if cumleler:
            return {'tur': 'bosluk', 'soru': temiz(x.get('yonerge') or x.get('soru') or 'Boşlukları doldurunuz.'), 'cumleler': cumleler, 'fazla': [temiz(f) for f in x.get('fazla') or []]}
    if t == 'siralama' and x.get('ogeler') and len(x['ogeler']) >= 3:
        return {'tur': 'siralama', 'soru': temiz(x['soru']), 'ogeler': [temiz(o) for o in x['ogeler']]}
    if t in ('kisa', 'acik', 'ogretici') and x.get('cevap'):
        return {'tur': 'acik', 'soru': temiz(x['soru']), 'cevap': temiz(x['cevap']), 'ipuclari': [temiz(i) for i in x.get('ipuclari') or []]}
    return None


def ders_dosyalari():
    """<sinif>-<ders> anahtarına göre kaynak dosyaları toplar."""
    gruplar = defaultdict(lambda: {'ozet': [], 'calisma': [], 'ek': []})
    for f in sorted((ARACLAR / 'ozetler').glob('*.json')):
        m = re.match(r'(\d+)-(.+)-(\d+)\.json$', f.name)
        if m:
            gruplar[f'{m.group(1)}-{m.group(2)}']['ozet'].append(f)
    for f in sorted((ARACLAR / 'calisma').glob('*.json')):
        m = re.match(r'(\d+)-(.+)-(\d+)\.json$', f.name)
        if m:
            gruplar[f'{m.group(1)}-{m.group(2)}']['calisma'].append(f)
    ek = ARACLAR / 'sorular'
    if ek.is_dir():
        for f in sorted(ek.glob('*.json')):
            m = re.match(r'(\d+)-(.+)\.json$', f.name)
            if m:
                gruplar[f'{m.group(1)}-{m.group(2)}']['ek'].append(f)
    return gruplar


def uret(anahtar, kaynaklar, dersler):
    sinif, ders = anahtar.split('-', 1)
    sinif = int(sinif)
    agac_yolu = PUBLIC / 'veri' / 'agac' / f'{anahtar}.json'
    agac = json.loads(agac_yolu.read_text(encoding='utf-8')) if agac_yolu.exists() else None
    konular, ciktilar, sorular = {}, {}, []
    sayac = Counter()

    def ekle(kayit, kimlik, hafta, konu_adi, cikti_listesi, kaynak, duzey=None):
        if gorsel_ister(kayit.get('soru'), *(kayit.get('secenekler') or []), *(c['metin'] for c in kayit.get('cumleler') or [])):
            sayac['gorsel-atlandi'] += 1
            return
        kod, ad, unite = konu_bul(agac, hafta, konu_adi)
        konular.setdefault(kod, {'ad': ad, 'unite': unite, 'haftalar': set()})
        if hafta:
            konular[kod]['haftalar'].add(hafta)
        kodlar = []
        for c, ifade in cikti_kodlari(cikti_listesi):
            ciktilar.setdefault(c, ifade)
            if c not in kodlar:   # aynı kod iki kez listelenmişse bir kez sayılır
                kodlar.append(c)
        kayit.update({'id': kimlik, 'kaynak': kaynak, 'hafta': hafta, 'konu': kod, 'cikti': kodlar})
        if duzey:
            kayit['duzey'] = duzey
        sorular.append(kayit)
        sayac[kayit['tur']] += 1

    for f in kaynaklar['ozet']:
        o = json.loads(f.read_text(encoding='utf-8'))
        h = int(o['hafta'])
        for i, x in enumerate(o.get('etkinlikler') or []):
            k = etkinlik_sorusu(x)
            if k:
                ekle(k, f'o-{anahtar}-{h}-e{i + 1}', h, o.get('konu', ''), o.get('ciktilar'), 'ozet')
        for i, x in enumerate(o.get('ornekler') or []):
            if x.get('soru') and x.get('cevap'):
                ekle({'tur': 'acik', 'soru': temiz(x['soru']), 'cevap': temiz(x['cevap']), 'ipuclari': []}, f'o-{anahtar}-{h}-x{i + 1}', h, o.get('konu', ''), o.get('ciktilar'), 'ozet')
    for f in kaynaklar['calisma']:
        o = json.loads(f.read_text(encoding='utf-8'))
        h = int(o['hafta'])
        for i, x in enumerate(o.get('sorular') or []):
            k = etkinlik_sorusu(x)
            if k:
                ekle(k, f'c-{anahtar}-{h}-s{i + 1}', h, o.get('konu', ''), o.get('ciktilar'), 'calisma', x.get('duzey'))
    for f in kaynaklar['ek']:
        o = json.loads(f.read_text(encoding='utf-8'))
        for i, x in enumerate(o.get('sorular') or []):
            k = etkinlik_sorusu(x)
            if not k:
                raise ValueError(f'{f.name} #{i + 1}: tanınmayan ya da eksik soru ({x.get("tur")})')
            konu_adi = x.get('konu_adi') or next((kk['ad'] for u in (agac or {'uniteler': []})['uniteler'] for kk in u['konular'] if kk['kod'] == x.get('konu')), x.get('konu', ''))
            ekle(k, f'y-{anahtar}-{i + 1}', x.get('hafta') or 0, konu_adi, x.get('cikti') or [], 'ek', x.get('duzey'))
            if x.get('konu') and k['konu'] != x['konu'] and agac:   # kod verilmişse ağaçtaki kodu kullan
                k['konu'] = x['konu']
                konular.setdefault(x['konu'], {'ad': konu_adi, 'unite': '', 'haftalar': set()})

    uniteler = []
    if agac:
        for u in agac['uniteler']:
            ks = [{'kod': k['kod'], 'ad': k['ad'], 'haftalar': k.get('haftalar') or [], 'n': sum(1 for s in sorular if s['konu'] == k['kod'])} for k in u['konular']]
            uniteler.append({'ad': u['ad'], 'konular': ks, 'n': sum(k['n'] for k in ks)})
    bilinen = {k['kod'] for u in uniteler for k in u['konular']}
    diger = [{'kod': kod, 'ad': v['ad'], 'haftalar': sorted(v['haftalar']), 'n': sum(1 for s in sorular if s['konu'] == kod)} for kod, v in konular.items() if kod not in bilinen]
    if diger:
        uniteler.append({'ad': 'Diğer konular', 'konular': diger, 'n': sum(k['n'] for k in diger)})
    cikti_sayi = Counter(c for s in sorular for c in s['cikti'])
    veri = {
        'sinif': sinif, 'ders': ders, 'dersAd': dersler['dersler'].get(ders, ders), 'guncelleme': date.today().isoformat(),
        'uniteler': uniteler,
        'ciktilar': [{'kod': kod, 'ifade': ifade, 'n': cikti_sayi.get(kod, 0)} for kod, ifade in sorted(ciktilar.items(), key=lambda x: [int(p) if p.isdigit() else p for p in x[0].replace('.', ' ').split()])],
        'sorular': sorular,
    }
    ozet = {
        'sinif': sinif, 'ders': ders, 'ad': veri['dersAd'], 'toplam': len(sorular), 'otomatik': sum(1 for s in sorular if s['tur'] in OTOMATIK),
        'turler': {t: n for t, n in sayac.items() if t != 'gorsel-atlandi'}, 'konu': sum(1 for u in uniteler for k in u['konular'] if k['n']), 'cikti': len(cikti_sayi),
    }
    return veri, ozet, sayac['gorsel-atlandi']


def main():
    dersler = json.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))
    CIKTI.mkdir(parents=True, exist_ok=True)
    dizin, atlanan = {}, 0
    for anahtar, kaynaklar in sorted(ders_dosyalari().items(), key=lambda x: (int(x[0].split('-')[0]), x[0])):
        veri, ozet, atlandi = uret(anahtar, kaynaklar, dersler)
        atlanan += atlandi
        if not veri['sorular']:
            continue
        (CIKTI / f'{anahtar}.json').write_text(json.dumps(veri, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
        dizin[anahtar] = ozet
    for eski in CIKTI.glob('*.json'):
        if eski.name != 'dizin.json' and eski.stem not in dizin:
            eski.unlink()
    (CIKTI / 'dizin.json').write_text(json.dumps({'guncelleme': date.today().isoformat(), 'dersler': dizin}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    toplam = sum(d['toplam'] for d in dizin.values())
    otomatik = sum(d['otomatik'] for d in dizin.values())
    print(f'{len(dizin)} ders, {toplam} soru ({otomatik} otomatik puanlanan, {toplam - otomatik} açık uçlu); görsel gerektirdiği için atlanan: {atlanan}')


if __name__ == '__main__':
    main()
