#!/usr/bin/env python3
"""Haftalık çalışma kâğıtları: araclar/calisma/<sinif>-<ders>-<hafta>.json → web sayfası + cevapsız/cevaplı PDF (A4, en çok 2 sayfa).

İçerik JSON'u (DKOZET yazar; yalnız MEB kitabındaki bilgiler, özgün):
  sinif, ders, hafta, tarih, konu, ciktilar[], hatirla[] (kısa bilgi maddeleri),
  sorular[]: ortak alanlar {tur, duzey: hatirla|uygula|ust, genislik: yarim|tam, soru, gorsel?(SVG)}
    coktan   {secenekler[4], dogru}             dy       {ifadeler[{metin, dogru}]}
    bosluk   {cumleler[{metin "___", cevap}], kelimeler?: true, fazla?[]}
    eslestir {ciftler[[sol, sag]]}               kisa/acik {cevap, satir}
    tablo    {basliklar[], satirlar[[hücre | {"b": cevap}]]}
    siralama {ogeler[] (doğru sırada)}           sifre    {satirlar[{ipucu, cevap, anahtar}], sonuc}
    sutun?: sol|sag (iki sütunlu bölümde sütunu elle seçer; yoksa yükseklikçe dengelenir)
    kavram   {merkez, dallar[metin | {"b": cevap, "ipucu"?: kısa açıklama (boş kutunun üstüne/altına)}]}
Görseller: araclar/calisma_gorseller/<ad>.py → def uygula(o) (ozet_gorsel.py yardımcıları).
Çıktı: public/calisma/<ad>.html, public/calisma/pdf/<ad>.pdf ve <ad>-cevapli.pdf; icerikler.json "Çalışma kâğıdı"; sitemap.
PDF: başsız Chrome (yazı tipleri Montserrat ve Noto Sans, OFL; 03-ARACLAR/_calisma/font). 2 sayfayı aşarsa ölçek küçültülür.
Çalıştırma: cd SITE && PYTHONPATH=../03-ARACLAR/_pylib LC_ALL=en_US.UTF-8 python3 araclar/calisma_uret.py [ad …]
"""
import html
import importlib.util
import json
import random
import re
import subprocess
import sys
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
SITE = ARACLAR.parent
PUBLIC = SITE / 'public'
KOK = SITE.parent
IS = KOK / '03-ARACLAR' / '_calisma'
FONT_KAYNAK = KOK / '02-KAYNAKLAR' / 'FONT'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
sys.path.insert(0, str(ARACLAR))
sys.path.insert(0, str(KOK / '03-ARACLAR' / '_pylib'))

import ozet_uret  # noqa: E402  (sembol dönüşümü e(), sayfa şablonu)

sembol = ozet_uret.e
sayfa = ozet_uret._sayfa.sayfa
DERSLER = json.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))['dersler']
TUR_AD = {'coktan': 'Çoktan seçmeli', 'dy': 'Doğru mu, yanlış mı?', 'bosluk': 'Boşluk doldurma', 'eslestir': 'Eşleştirme',
          'kisa': 'Kısa cevap', 'acik': 'Açık uçlu', 'tablo': 'Tabloyu tamamla', 'siralama': 'Sıralama', 'sifre': 'Şifreli kelime',
          'kavram': 'Kavram haritası'}
BUYUK = str.maketrans('iıçğöşü', 'İIÇĞÖŞÜ')


def tr_buyuk(s):
    return s.translate(BUYUK).upper()


def cvp(metin):
    return f'<span class="cvp">{sembol(metin)}</span>'


def satirlar(n, cevap=None):
    ic = ''.join('<div class="ck-satir"></div>' for _ in range(max(1, n)))
    return f'<div class="ck-satirlar">{ic}{cvp(cevap) if cevap else ""}</div>'


def karistir(n, tohum):
    sira = list(range(n))
    r = random.Random(tohum)
    for _ in range(20):
        r.shuffle(sira)
        if n < 2 or any(i != j for i, j in enumerate(sira)):
            break
    return sira


def kavram_svg(merkez, dallar):
    n = len(dallar)
    ipuclu = any(isinstance(d, dict) and d.get('ipucu') for d in dallar)
    W, H = 360, (226 if ipuclu else 190)
    cx, cy = W / 2, H / 2
    ic = f'<rect x="{cx - 62}" y="{cy - 17}" width="124" height="34" rx="17" fill="#0b2257"/>'
    ic += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="14" font-weight="800" fill="#fff" font-family="Montserrat, sans-serif">{html.escape(merkez)}</text>'
    import math
    for i, d in enumerate(dallar):
        aci = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + 128 * math.cos(aci), cy + 70 * math.sin(aci)
        bos = isinstance(d, dict)
        metin = d['b'] if bos else d
        ic += f'<line x1="{cx + 64 * math.cos(aci):.1f}" y1="{cy + 19 * math.sin(aci):.1f}" x2="{x - 50 * math.cos(aci):.1f}" y2="{y - 14 * math.sin(aci):.1f}" stroke="#9aa6bd" stroke-width="1.6"/>'
        dolgu, cizgi = ('#fff', '#ee7d12') if bos else ('#e8eefe', '#2451d6')
        kesik = ' stroke-dasharray="4 3"' if bos else ''
        ic += f'<rect x="{x - 52}" y="{y - 14}" width="104" height="28" rx="8" fill="{dolgu}" stroke="{cizgi}" stroke-width="1.5"{kesik}/>'
        yazi = html.escape(metin)
        sinif = ' class="cvp"' if bos else ''
        renk = '' if bos else ' fill="#0b2257"'
        ic += f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" font-size="12" font-weight="700"{renk}{sinif} font-family="Noto Sans, sans-serif">{yazi}</text>'
        if bos and d.get('ipucu'):
            iy = y - 19 if math.sin(aci) < -0.05 else y + 25
            ic += f'<text x="{x}" y="{iy:.1f}" text-anchor="middle" font-size="10.5" font-style="italic" fill="#5b6479" font-family="Noto Sans, sans-serif">{html.escape(d["ipucu"])}</text>'
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Kavram haritası: {html.escape(merkez)}">{ic}</svg>'


def soru_html(s, no, ad):
    t = s['tur']
    duzey = {'hatirla': '', 'uygula': ' d-uygula', 'ust': ' d-ust'}.get(s.get('duzey', 'hatirla'), '')
    genis = ' tam' if s.get('genislik') == 'tam' else ''
    bas = (f'<div class="ck-soru-bas"><span class="ck-no">{no}</span><span class="ck-tur">{TUR_AD.get(t, t)}</span></div>'
           + (f'<p class="ck-soru-metin">{sembol(s["soru"])}</p>' if s.get('soru') else ''))
    gorsel = f'<div class="ck-gorsel">{s["gorsel"]}</div>' if s.get('gorsel') else ''
    govde = ''
    if t == 'coktan':
        govde = '<ol class="ck-sec">' + ''.join(
            f'<li class="{"dogru" if i == s["dogru"] else ""}"><b>{"ABCD"[i]}</b><span>{sembol(x)}</span></li>' for i, x in enumerate(s['secenekler'])) + '</ol>'
    elif t == 'dy':
        govde = '<table class="ck-dy"><tr class="ck-dy-bas"><td></td><td class="k">D</td><td class="k">Y</td></tr>' + ''.join(
            f'<tr><td>{sembol(i["metin"])}</td><td class="k"><span class="ck-kutu">{cvp("✓") if i["dogru"] else ""}</span></td>'
            f'<td class="k"><span class="ck-kutu">{"" if i["dogru"] else cvp("✓")}</span></td></tr>' for i in s['ifadeler']) + '</table>'
    elif t == 'bosluk':
        kel = ''
        if s.get('kelimeler', True):
            k = [c['cevap'] for c in s['cumleler']] + s.get('fazla', [])
            k = [k[i] for i in karistir(len(k), ad + str(no))]
            kel = '<div class="ck-kelimeler">' + ''.join(f'<span>{sembol(x)}</span>' for x in k) + '</div>'
        cum = ''
        for c in s['cumleler']:
            on, _, arka = c['metin'].partition('___')
            cum += f'<li>{sembol(on)}<span class="ck-bos">{cvp(c["cevap"])}</span>{sembol(arka)}</li>'
        govde = kel + f'<ol class="ck-bosluk-liste">{cum}</ol>'
    elif t == 'eslestir':
        c = s['ciftler']
        sira = karistir(len(c), ad + str(no))
        harf = {j: 'abcdefgh'[k] for k, j in enumerate(sira)}
        sol = ''.join(f'<div><span class="ck-kutu">{cvp(harf[i])}</span><span>{i + 1}. {sembol(a)}</span></div>' for i, (a, _) in enumerate(c))
        sag = ''.join(f'<div><span class="harf">{"abcdefgh"[k]})</span><span>{sembol(c[j][1])}</span></div>' for k, j in enumerate(sira))
        govde = f'<div class="ck-esle"><div style="display:grid;gap:4px">{sol}</div><div style="display:grid;gap:4px">{sag}</div></div>'
    elif t in ('kisa', 'acik'):
        govde = satirlar(s.get('satir', 2 if t == 'kisa' else 3), s.get('cevap'))
    elif t == 'tablo':
        bas_ = ''.join(f'<th>{sembol(x)}</th>' for x in s['basliklar'])
        gov = ''.join('<tr>' + ''.join(
            f'<td class="bos">{cvp(h["b"])}</td>' if isinstance(h, dict) else f'<td>{sembol(h)}</td>' for h in r) + '</tr>' for r in s['satirlar'])
        govde = f'<table class="ck-tablo"><thead><tr>{bas_}</tr></thead><tbody>{gov}</tbody></table>'
    elif t == 'siralama':
        o = s['ogeler']
        sira = karistir(len(o), ad + str(no))
        govde = '<ol class="ck-sira">' + ''.join(
            f'<li><span class="ck-kutu">{cvp(str(j + 1))}</span><span>{sembol(o[j])}</span></li>' for j in sira) + '</ol>'
    elif t == 'sifre':
        govde = '<div class="ck-sifre">'
        for r in s['satirlar']:
            kelime = tr_buyuk(r['cevap'])
            kutular = ''.join(
                f'<span class="ck-harf{" anahtar" if i == r["anahtar"] else ""}{" bosyer" if h == " " else ""}">{cvp(h) if h != " " else ""}</span>' for i, h in enumerate(kelime))
            govde += f'<div class="ck-sifre-satir"><span class="ck-sifre-ipucu">{sembol(r["ipucu"])}</span><span class="ck-harfler">{kutular}</span></div>'
        govde += f'<p class="ck-sifre-sonuc">Turuncu kutulardaki harfler yukarıdan aşağıya: <span class="ck-bos">{cvp(tr_buyuk(s["sonuc"]))}</span></p></div>'
        anahtar = ''.join(tr_buyuk(r['cevap'])[r['anahtar']] for r in s['satirlar'])
        assert anahtar == tr_buyuk(s['sonuc']).replace(' ', ''), f'{ad} soru {no}: şifre sonucu {anahtar} ≠ {s["sonuc"]}'
    elif t == 'kavram':
        govde = f'<div class="ck-gorsel kavram">{kavram_svg(s["merkez"], s["dallar"])}</div>'
    else:
        raise ValueError(f'{ad}: bilinmeyen soru türü {t}')
    return f'<section class="ck-soru{genis}{duzey}">{bas}{gorsel}{govde}</section>'


def tahmini_boy(s):
    """Sorunun kâğıttaki yaklaşık yüksekliği (mm; iki sütuna dengeli dağıtmak için)."""
    t = s['tur']
    boy = 11 + 4.6 * (len(s.get('soru', '')) // 52 + 1)
    if s.get('gorsel'):
        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s['gorsel'])
        g, y = (float(m.group(1)), float(m.group(2))) if m else (4, 3)
        boy += min(40, 88 * y / g) + 3
    boy += {'coktan': 11 if max(len(x) for x in s.get('secenekler', ['']) ) < 22 else 20,
            'dy': 7 + 6.2 * len(s.get('ifadeler', [])), 'bosluk': 9 + 6.4 * len(s.get('cumleler', [])),
            'eslestir': 7.5 * len(s.get('ciftler', [])), 'kisa': 6 * s.get('satir', 2), 'acik': 6 * s.get('satir', 3),
            'tablo': 7.5 * (len(s.get('satirlar', [])) + 1), 'siralama': 6.2 * len(s.get('ogeler', [])),
            'sifre': 6 * len(s.get('satirlar', [])) + 9, 'kavram': 44}.get(t, 10)
    return boy


def dizilim(liste):
    """Tam genişlikli sorular arasındaki bölümlerde yarım soruları iki sütuna yükseklikçe dengeli dağıtır."""
    parca, kume = [], []
    for no, s, html_ in liste:
        if s.get('genislik') == 'tam':
            if kume: parca.append(('iki', kume)); kume = []
            parca.append(('tam', html_))
        else:
            kume.append((no, s, html_))
    if kume: parca.append(('iki', kume))
    cikti = ''
    for tur, ic in parca:
        if tur == 'tam':
            cikti += ic; continue
        sol, sag, hs, hg = [], [], 0.0, 0.0
        for no, s, html_ in ic:
            b = tahmini_boy(s)
            if s.get('sutun') == 'sag' or (s.get('sutun') != 'sol' and hs > hg): sag.append(html_); hg += b
            else: sol.append(html_); hs += b
        cikti += f'<div class="ck-iki"><div class="ck-sutun">{"".join(sol)}</div><div class="ck-sutun">{"".join(sag)}</div></div>'
    return cikti


def kagit_html(o, ad, cevapli=False):
    ders = DERSLER.get(o['ders'], o['ders'])
    sorular = dizilim([(i, s, soru_html(s, i, ad)) for i, s in enumerate(o['sorular'], 1)])
    hatirla = ''.join(f'<li>{sembol(x)}</li>' for x in o.get('hatirla', []))
    return f'''<article class="ck{' cevapli' if cevapli else ''}">
  <header class="ck-bant">
    <div class="ck-marka"><img src="/logo.svg" alt=""><div><b>DERS <span>KUTUSU</span></b><small>DERSKUTUSU.COM</small></div></div>
    <div class="ck-bant-orta"><span class="ck-etiket">ÇALIŞMA KÂĞIDI</span><span class="ck-etiket cevapli-etiket">CEVAPLI</span>
      <div class="ck-bilgi">{o["sinif"]}. Sınıf · {html.escape(ders)} · {o["hafta"]}. Hafta</div></div>
    <div class="ck-ogrenci"><span>Ad Soyad:<i></i></span><span>Sınıf / No:<i></i></span><span>Tarih:<i></i></span></div>
  </header>
  <div class="ck-konu"><h1>{sembol(o["konu"])}</h1><p>{" · ".join(html.escape(c) for c in o["ciktilar"])}</p></div>
  {f'<div class="ck-hatirla"><div class="ck-hatirla-bas">HATIRLAYALIM</div><ul>{hatirla}</ul></div>' if hatirla else ''}
  <div class="ck-sorular">{sorular}</div>
  <footer class="ck-alt"><span>derskutusu.com · © Ders Kutusu · Tüm hakları saklıdır.</span><span>{o["sinif"]}. Sınıf {html.escape(ders)} · {o["hafta"]}. Hafta</span></footer>
</article>'''


def yazi_tipleri():
    """PDF için sabit ağırlıklı OFL yazı tipleri (bir kez üretilir)."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
    hedef = IS / 'font'
    hedef.mkdir(parents=True, exist_ok=True)
    liste = [('Montserrat', FONT_KAYNAK / 'Montserrat-wght.ttf', w, {'wght': w}) for w in (600, 700, 800)]
    liste += [('Noto Sans', FONT_KAYNAK / 'NotoSans-wdth-wght.ttf', w, {'wght': w, 'wdth': 100}) for w in (400, 600, 700)]
    css = ''
    for aile, kaynak, w, eksen in liste:
        dosya = hedef / f'{aile.replace(" ", "")}-{w}.ttf'
        if not dosya.exists():
            instantiateVariableFont(TTFont(kaynak), eksen).save(dosya)
        css += f'@font-face {{ font-family: "{aile}"; font-weight: {w}; src: url("{dosya.as_uri()}"); }}\n'
    italik = hedef / 'NotoSans-700.ttf'
    css += f'@font-face {{ font-family: "Noto Sans"; font-weight: 700; font-style: italic; src: url("{italik.as_uri()}"); }}\n'
    return css


def pdf_yap(o, ad, cevapli, font_css):
    from pypdf import PdfReader
    cikti = PUBLIC / 'calisma' / 'pdf' / f'{ad}{"-cevapli" if cevapli else ""}.pdf'
    cikti.parent.mkdir(parents=True, exist_ok=True)
    stil = (PUBLIC / 'calisma.css').read_text(encoding='utf-8')
    logo = (PUBLIC / 'logo.svg').as_uri()
    for olcek in (1.0, 0.95, 0.9, 0.86, 0.82, 0.78):
        govde = kagit_html(o, ad, cevapli).replace('src="/logo.svg"', f'src="{logo}"')
        belge = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{font_css}{stil}\n.ck {{ --ck-olcek: {olcek}; }}</style></head>'
                 f'<body>{govde}</body></html>')
        gecici = IS / f'{ad}{"-cevapli" if cevapli else ""}.html'
        IS.mkdir(parents=True, exist_ok=True)
        gecici.write_text(belge, encoding='utf-8')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--allow-file-access-from-files',
                        f'--print-to-pdf={cikti}', gecici.as_uri()], capture_output=True, timeout=180)
        sayfa_sayisi = len(PdfReader(str(cikti)).pages)
        if sayfa_sayisi <= 2:
            return sayfa_sayisi, olcek
    return sayfa_sayisi, olcek


def web_sayfasi(o, ad):
    ders = DERSLER.get(o['ders'], o['ders'])
    baslik = f'{o["sinif"]}. Sınıf {ders} {o["hafta"]}. Hafta Çalışma Kâğıdı: {o["konu"]}'
    ozet = f'ozet/{o["sinif"]}-{o["ders"]}-hafta-{o["hafta"]}.html'
    ozet_bag = f'<a class="dugme" href="/{ozet}">Konu özeti</a>' if (PUBLIC / ozet).exists() else ''
    govde = f'''  <link rel="stylesheet" href="/calisma.css?v={ozet_uret._sayfa.SURUM}">
  <section class="sayfa-bas ck-web-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/sinif.html?no={o["sinif"]}">{o["sinif"]}. sınıf</a><span aria-hidden="true">/</span><a href="/icerikler.html?sinif={o["sinif"]}&amp;ders={o["ders"]}">{html.escape(ders)}</a><span aria-hidden="true">/</span><span>Çalışma kâğıdı</span></nav>
      <p class="ust-baslik">{o["sinif"]}. sınıf · {html.escape(ders)} · {o["hafta"]}. hafta ({html.escape(o.get("tarih", ""))})</p>
      <h1>{sembol(o["konu"])}: çalışma kâğıdı</h1>
      <p>{len(o["sorular"])} soru. Yazdırmak için PDF'i indirin; cevaplı sürüm öğretmenler için.</p>
      <div class="g-dugmeler y-ust">
        <a class="dugme ana" href="/calisma/pdf/{ad}.pdf" download><svg><use href="#s-indir"/></svg>PDF indir</a>
        <a class="dugme" href="/calisma/pdf/{ad}-cevapli.pdf" download><svg><use href="#s-indir"/></svg>Cevaplı PDF</a>
        <button class="dugme" type="button" onclick="document.body.classList.toggle('cevapli');this.textContent=document.body.classList.contains('cevapli')?'Cevapları gizle':'Cevapları göster'">Cevapları göster</button>
        {ozet_bag}
      </div>
    </div>
  </section>
  <section class="bolum"><div class="kap ck-sayfalar">{kagit_html(o, ad)}</div></section>'''
    aciklama = f'{o["sinif"]}. sınıf {ders} {o["hafta"]}. hafta çalışma kâğıdı: {o["konu"]}. Görselli, çeşitli sorular; cevaplı ve cevapsız PDF.'
    (PUBLIC / 'calisma').mkdir(exist_ok=True)
    (PUBLIC / 'calisma' / f'{ad}.html').write_text(sayfa(f'calisma/{ad}.html', baslik, aciklama, govde), encoding='utf-8')
    return {'sinif': o['sinif'], 'ders': o['ders'], 'tur': 'Çalışma kâğıdı', 'kitle': 'ogrenci', 'baslik': baslik,
            'aciklama': f'{len(o["sorular"])} soruluk, görselli çalışma kâğıdı; cevapsız ve cevaplı PDF.', 'goruntule': f'calisma/{ad}.html',
            'dosya': f'calisma/pdf/{ad}.pdf', 'kaynak': 'Ders Kutusu', 'hafta': o['hafta'], 'tarih': '2026-09-29'}


def main():
    adlar = sys.argv[1:] or [p.stem for p in sorted((ARACLAR / 'calisma').glob('*.json'))]
    font_css = yazi_tipleri()
    kayitlar = []
    for ad in adlar:
        p = ARACLAR / 'calisma' / f'{ad}.json'
        o = json.loads(p.read_text(encoding='utf-8'))
        modul = ARACLAR / 'calisma_gorseller' / f'{ad}.py'
        if modul.exists():
            spec = importlib.util.spec_from_file_location(f'ck_{ad.replace("-", "_")}', modul)
            m = importlib.util.module_from_spec(spec)
            sys.modules.setdefault('ozet_gorsel', importlib.import_module('ozet_gorsel'))
            spec.loader.exec_module(m)
            m.uygula(o)
        gorselli = sum(1 for s in o['sorular'] if s.get('gorsel') or s['tur'] in ('kavram', 'sifre', 'tablo'))
        kayitlar.append(web_sayfasi(o, ad))
        s1, k1 = pdf_yap(o, ad, False, font_css)
        s2, k2 = pdf_yap(o, ad, True, font_css)
        print(f'{ad}: {len(o["sorular"])} soru, görselli {gorselli} (%{100 * gorselli // len(o["sorular"])}); PDF {s1} sayfa (ölçek {k1}), cevaplı {s2} sayfa (ölçek {k2})')
    # içerik listesi ve site haritası (bütün çalışma kâğıtları yeniden taranır)
    veri = json.loads((PUBLIC / 'veri' / 'icerikler.json').read_text(encoding='utf-8'))
    hepsi = {k['goruntule']: k for k in veri['icerikler'] if k.get('tur') == 'Çalışma kâğıdı'}
    hepsi.update({k['goruntule']: k for k in kayitlar})
    veri['icerikler'] = [k for k in veri['icerikler'] if k.get('tur') != 'Çalışma kâğıdı'] + list(hepsi.values())
    (PUBLIC / 'veri' / 'icerikler.json').write_text(json.dumps(veri, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    harita = (PUBLIC / 'sitemap.xml').read_text(encoding='utf-8')
    harita = re.sub(r'\s*<url><loc>https://derskutusu\.com/calisma/[^<]+</loc></url>', '', harita)
    ek = ''.join(f'\n  <url><loc>https://derskutusu.com/{k}</loc></url>' for k in hepsi)
    (PUBLIC / 'sitemap.xml').write_text(harita.replace('\n</urlset>', ek + '\n</urlset>'), encoding='utf-8')


if __name__ == '__main__':
    main()
