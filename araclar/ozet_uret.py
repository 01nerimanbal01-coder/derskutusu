#!/usr/bin/env python3
"""Haftalık konu özetlerini (araclar/ozetler/<sinif>-<ders>-<hafta>.json) durağan HTML sayfalarına çevirir.

Çıktı : public/ozet/<sinif>-<ders>-hafta-<n>.html  (sitenin üst/alt bölümüyle; kalemle üzerine yazılabilir)
        public/veri/icerikler.json → tür "Konu anlatımı" kaydı (sınıf ve ders sayfalarında görünür)
        public/sitemap.xml → özet adresleri
Özet metinleri özgündür (MEB kitabından cümle alınmaz); örneklerde "Cevabı göster" düğmesi <details> ile çalışır.
Çalıştırma: LC_ALL=en_US.UTF-8 python3 araclar/ozet_uret.py
"""
import html
import importlib.util
import json
import re
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
PUBLIC = ARACLAR.parent / 'public'
_spec = importlib.util.spec_from_file_location('sayfa_uret', ARACLAR / 'sayfa_uret.py')
_sayfa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sayfa)          # iç sayfaları da yeniler (idempotent)

KAR = re.compile(r'\{(aci|olcu|dogru|isin|parca|uzunluk|us|kesir|koyu):([^}]+)\}')
SEMBOL = {  # MEB 5. sınıf matematik programındaki gösterimler (⊥, //, AB doğrusu, [AB], |AB|, [AB, m(ABC), şapkalı ABC)
    'aci': '<span class="s-aci" role="img" aria-label="{0} açısı">{0}</span>',
    'olcu': 'm(<span class="s-aci" role="img" aria-label="{0} açısı">{0}</span>)',
    'dogru': '<span class="s-dogru" role="img" aria-label="{0} doğrusu">{0}</span>',
    'isin': '[{0}', 'parca': '[{0}]', 'uzunluk': '|{0}|',
    'koyu': '<b>{0}</b>',   # olumsuz kökteki vurgu: {koyu:değildir}
}


def _us(ic):
    taban, _, us = ic.partition('|')   # {us:2|3} → 2³
    return f'{taban}<sup>{us}</sup>'


def _kesir(ic):
    pay, _, payda = ic.partition('|')   # {kesir:3|4} → pay üstte, payda altta (MEB gösterimi)
    return (f'<span class="s-kesir" role="math" aria-label="{pay} bölü {payda}">'
            f'<span>{pay}</span><span>{payda}</span></span>')


def e(metin):
    # Önce kaçış, sonra {aci:ABC} gibi sembol işaretleri MEB gösterimine çevrilir.
    metin = html.escape(str(metin)).replace(' · ', '\u00a0·\u00a0').replace(' × ', '\u00a0×\u00a0')   # çarpımlar satır sonunda bölünmez
    ozel = {'us': _us, 'kesir': _kesir}
    return KAR.sub(lambda m: ozel[m.group(1)](m.group(2)) if m.group(1) in ozel else SEMBOL[m.group(1)].format(m.group(2)), metin)
KUTU = {'dikkat': 'Dikkat', 'bilgi': 'Bilgi', 'kural': 'Kural', 'tanim': 'Tanım'}


def paragraflar(liste):
    return ''.join(f'<p>{e(p)}</p>' for p in liste or [])


def tablo(t):
    if not t:
        return ''
    bas = ''.join(f'<th>{e(b)}</th>' for b in t['basliklar'])
    gov = ''.join('<tr>' + ''.join(f'<td>{e(h)}</td>' for h in s) + '</tr>' for s in t['satirlar'])
    return f'<div class="ozet-tablo"><table><thead><tr>{bas}</tr></thead><tbody>{gov}</tbody></table></div>'


HARF = 'ABCDE'


def _geri(metin=''):
    return f'<p class="etk-geri" hidden><b></b><span>{e(metin) if metin else ""}</span></p>'


def etkinlik_html(liste):
    """Etkinlikler (MEB kitabındaki bilgilerle): coktan | dy | eslestir | bosluk | ogretici. Davranış public/etkinlik.js'te."""
    import random
    parca = []
    for no, x in enumerate(liste, 1):
        tur, rnd = x['tur'], random.Random(no * 7919 + len(str(x)))
        bas = f'<p class="etk-soru"><span class="etk-no">{no}</span><span>{e(x.get("soru") or x.get("yonerge", ""))}</span></p>'
        if tur == 'coktan':
            sec = ''.join(f'<button type="button" class="etk-sec" data-i="{i}"><span class="etk-harf">{HARF[i]}</span><span>{e(s)}</span></button>'
                          for i, s in enumerate(x['secenekler']))
            parca.append(f'<li class="etk etk-coktan" data-dogru="{x["dogru"]}">{bas}<div class="etk-secenekler">{sec}</div>{_geri(x.get("aciklama"))}</li>')
        elif tur == 'dy':
            satir = ''.join(f'<li class="etk-dy-satir" data-dogru="{"D" if i["dogru"] else "Y"}"><span class="etk-dy-metin">{e(i["metin"])}</span>'
                            '<span class="etk-dy-dugmeler"><button type="button" data-c="D">Doğru</button><button type="button" data-c="Y">Yanlış</button></span>'
                            f'{_geri(i.get("aciklama"))}</li>' for i in x['ifadeler'])
            parca.append(f'<li class="etk etk-dy">{bas}<ul>{satir}</ul></li>')
        elif tur == 'eslestir':
            sira = list(range(len(x['ciftler'])))
            while sira == sorted(sira) and len(sira) > 1:
                rnd.shuffle(sira)
            sol = ''.join(f'<button type="button" class="etk-sec" data-sol="{i}">{e(a)}</button>' for i, (a, _) in enumerate(x['ciftler']))
            sag = ''.join(f'<button type="button" class="etk-sec" data-sag="{i}">{e(x["ciftler"][i][1])}</button>' for i in sira)
            parca.append(f'<li class="etk etk-eslestir">{bas}<p class="etk-ipucu-kucuk">Soldan bir öğeye, sonra sağdaki eşine dokunun.</p>'
                         f'<div class="etk-sutunlar"><div class="etk-sutun">{sol}</div><div class="etk-sutun">{sag}</div></div>{_geri()}</li>')
        elif tur == 'bosluk':
            kelimeler = [c['cevap'] for c in x['cumleler']] + x.get('fazla', [])
            sira = list(range(len(kelimeler))); rnd.shuffle(sira)
            cip = ''.join(f'<button type="button" class="etk-kelime" data-k="{i}">{e(kelimeler[i])}</button>' for i in sira)
            cumle = ''
            for c in x['cumleler']:
                on, _, arka = c['metin'].partition('___')
                cumle += f'<li>{e(on)}<button type="button" class="etk-bosluk-yer" data-cevap="{e(c["cevap"])}" aria-label="Boşluk"></button>{e(arka)}</li>'
            parca.append(f'<li class="etk etk-bosluk">{bas}<div class="etk-kelimeler">{cip}</div><ol class="etk-cumleler">{cumle}</ol>'
                         '<p class="etk-uyari" hidden>Önce bütün boşlukları doldurun.</p><button type="button" class="dugme etk-kontrol">Kontrol et</button>'
                         f'{_geri()}</li>')
        elif tur == 'ogretici':
            ip = ''.join(f'<p class="etk-ipucu" hidden><b>{k}. ipucu:</b> {e(s)}</p>' for k, s in enumerate(x.get('ipuclari', []), 1))
            ilk = '1. ipucunu göster' if x.get('ipuclari') else 'Cevabı göster'
            parca.append(f'<li class="etk etk-ogretici">{bas}{ip}<button type="button" class="dugme etk-ipucu-dugme">{ilk}</button>'
                         f'<p class="etk-cevap" hidden><b>Cevap:</b> {e(x["cevap"])}</p></li>')
    return ('<section class="ozet-bolum" id="etkinlikler"><div class="etk-bas"><h2>Etkinlikler</h2><p class="etk-puan"></p>'
            '<button type="button" class="dugme etk-sifirla">Baştan başla</button></div>'
            '<p class="etk-aciklama">Soruları çözün; her cevaptan sonra doğru mu yanlış mı olduğunu hemen göreceksiniz.</p>'
            f'<ol class="etk-liste">{"".join(parca)}</ol></section>')


def sayfa_uret(o, dersler, icerikler):
    ad = dersler['dersler'][o['ders']]
    dosya = f'{o["sinif"]}-{o["ders"]}-hafta-{o["hafta"]}.html'
    baglar = [i for i in icerikler if i.get('sinif') == o['sinif'] and i.get('ders') == o['ders'] and i.get('tur') != 'Konu anlatımı']
    ilgili = ''.join(
        f'<li><a href="/{i.get("goruntule") or i.get("dosya") or ""}">{e(i["baslik"])}</a> <span>{e(i["tur"])}</span></li>'
        for i in baglar if i.get('goruntule') or i.get('dosya'))
    bolumler = ''
    for b in o['bolumler']:
        kutu = b.get('kutu')
        bolumler += (f'<section class="ozet-bolum"><h2>{e(b["baslik"])}</h2>{paragraflar(b.get("metin"))}'
                     + (f'<figure class="ozet-gorsel">{b["gorsel"]}</figure>' if b.get('gorsel') else '')
                     + tablo(b.get('tablo'))
                     + (f'<aside class="ozet-kutu {kutu["tur"]}"><strong>{KUTU.get(kutu["tur"], "Not")}</strong><p>{e(kutu["metin"])}</p></aside>' if kutu else '')
                     + '</section>')
    ornekler = ''.join(
        f'<li class="ornek"><p class="ornek-soru"><span class="ornek-no">Örnek {n}</span>{e(x["soru"])}</p>'
        + (f'<figure class="ozet-gorsel">{x["gorsel"]}</figure>' if x.get('gorsel') else '')
        + f'<details><summary>Cevabı göster</summary><p>{e(x["cevap"])}</p></details></li>'
        for n, x in enumerate(o['ornekler'], 1))
    ozet = ''.join(f'<li>{e(x)}</li>' for x in o.get('ozet', []))
    ciktilar = ''.join(f'<li>{e(c)}</li>' for c in o['ciktilar'])
    govde = f'''  <section class="sayfa-bas ozet-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/sinif.html?no={o["sinif"]}">{o["sinif"]}. sınıf</a><span aria-hidden="true">/</span><a href="/icerikler.html?sinif={o["sinif"]}&amp;ders={o["ders"]}">{e(ad)}</a><span aria-hidden="true">/</span><span>{o["hafta"]}. hafta</span></nav>
      <p class="ust-baslik">{o["sinif"]}. sınıf · {e(ad)} · {o["hafta"]}. hafta ({e(o["tarih"])})</p>
      <h1>{e(o["konu"])}</h1>
      <p>{e(o["unite"])} teması · Konu özeti</p>
      <div class="g-dugmeler y-ust"><button class="dugme ana" type="button" onclick="window.kalemAc &amp;&amp; window.kalemAc()"><span aria-hidden="true">✎</span>Kalemle yaz</button><button class="dugme" type="button" onclick="document.querySelectorAll('.ornek details').forEach(d=&gt;d.open=!d.open)">Bütün cevapları aç/kapat</button>{'<a class="dugme" href="#etkinlikler">Etkinlikler</a>' if o.get('etkinlikler') else ''}</div>
    </div>
  </section>
  <article class="bolum ozet">
    <div class="kap ozet-ic">
      <aside class="ozet-cikti"><strong>Öğrenme çıktısı</strong><ul>{ciktilar}</ul></aside>
      <p class="ozet-giris">{e(o["giris"])}</p>
      {bolumler}
      <section class="ozet-bolum"><h2>Örnekler</h2><ol class="ornekler">{ornekler}</ol></section>
      {etkinlik_html(o['etkinlikler']) if o.get('etkinlikler') else ''}
      <section class="ozet-bolum ozet-son"><h2>Kısaca</h2><ul>{ozet}</ul></section>
      {f'<section class="ozet-bolum ozet-ilgili"><h2>Bu dersin öteki kaynakları</h2><ul>{ilgili}</ul></section>' if ilgili else ''}
    </div>
  </article>'''
    baslik = f'{o["sinif"]}. Sınıf {ad} {o["hafta"]}. Hafta: {o["konu"]}'
    aciklama = f'{o["sinif"]}. sınıf {ad} {o["hafta"]}. hafta konu özeti: {o["konu"]}. Çözümlü örnekler ve cevaplar.'
    (PUBLIC / 'ozet').mkdir(exist_ok=True)
    betik = ('etkinlik.js',) if o.get('etkinlikler') else ()
    (PUBLIC / 'ozet' / dosya).write_text(_sayfa.sayfa(f'ozet/{dosya}', baslik, aciklama, govde, betik), encoding='utf-8')
    return {'sinif': o['sinif'], 'ders': o['ders'], 'tur': 'Konu anlatımı', 'kitle': 'ogrenci', 'baslik': baslik,
            'aciklama': f'{o["unite"]}: {o["konu"]}. Konu özeti, {len(o["ornekler"])} örnek ve cevapları' + (f', {len(o["etkinlikler"])} etkileşimli etkinlik' if o.get('etkinlikler') else '') + '; akıllı tahtada kalemle yazılabilir.',
            'goruntule': f'ozet/{dosya}', 'kaynak': 'Ders Kutusu', 'hafta': o['hafta'], 'tarih': '2026-09-29'}


def main():
    dersler = json.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))
    veri = json.loads((PUBLIC / 'veri' / 'icerikler.json').read_text(encoding='utf-8'))
    icerikler = [i for i in veri['icerikler'] if i.get('tur') != 'Konu anlatımı' or not str(i.get('goruntule', '')).startswith('ozet/')]
    yeni = [sayfa_uret(json.loads(f.read_text(encoding='utf-8')), dersler, icerikler) for f in sorted((ARACLAR / 'ozetler').glob('*.json'))]
    veri['icerikler'] = icerikler + yeni
    (PUBLIC / 'veri' / 'icerikler.json').write_text(json.dumps(veri, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    harita = (PUBLIC / 'sitemap.xml').read_text(encoding='utf-8')
    harita = re.sub(r'\s*<url><loc>https://derskutusu\.com/ozet/[^<]+</loc></url>', '', harita)
    ek = ''.join(f'\n  <url><loc>https://derskutusu.com/{y["goruntule"]}</loc></url>' for y in yeni)
    (PUBLIC / 'sitemap.xml').write_text(harita.replace('\n</urlset>', ek + '\n</urlset>'), encoding='utf-8')
    print(f'{len(yeni)} konu özeti üretildi')


if __name__ == '__main__':
    main()
