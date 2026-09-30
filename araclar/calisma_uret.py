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
PDF: başsız Chrome (yazı tipleri Montserrat ve Noto Sans, OFL; 03-ARACLAR/_calisma/font).
Sayfa düzeni ölçümle kurulur (olc + yerlesim): her sorunun gerçek boyu başsız Chrome'da ölçülür; 2 sayfaya sığan en büyük ölçek
(1.10 … 0.78) seçilir, sorular sırayı bozmadan iki sayfanın sütunlarına dağıtılır, sütunlar sayfa altına yayılır. "sutun" alanı
yalnız ölçüm yapılamazsa kullanılır. Sayfa doluluğu: 03-ARACLAR/_calisma/doluluk.py.
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

def sembol(metin):
    # Mutlak değerin açılış çizgisinden sonra satır bölünmesin (|−3| tek parça kalsın).
    return re.sub(r'\|(?=[−+\d])', '|\u2060', ozet_uret.e(metin))


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
        ic += f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" font-size="{10.5 if len(metin) > 14 else 12}" font-weight="700"{renk}{sinif} font-family="Noto Sans, sans-serif">{yazi}</text>'
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
            k = [k[i] for i in karistir(len(k), ad + str(s.get('_tohum', no)))]
            kel = '<div class="ck-kelimeler">' + ''.join(f'<span>{sembol(x)}</span>' for x in k) + '</div>'
        cum = ''
        for c in s['cumleler']:
            on, _, arka = c['metin'].partition('___')
            cum += f'<li>{sembol(on)}<span class="ck-bos">{cvp(c["cevap"])}</span>{sembol(arka)}</li>'
        govde = kel + f'<ol class="ck-bosluk-liste">{cum}</ol>'
    elif t == 'eslestir':
        c = s['ciftler']
        sira = karistir(len(c), ad + str(s.get('_tohum', no)))
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
        sira = karistir(len(o), ad + str(s.get('_tohum', no)))
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


MM = 96 / 25.4
SAYFA_BOY = (297 - 9 - 11) * MM  # baskı alanının yüksekliği (px); calisma.css @page kenar boşluklarıyla aynı olmalı
SAYFA_EN = '191mm'               # 210 − 2 × 9.5
PAY = 2 * MM                     # ölçüm ile baskı arasındaki küçük farklar için güvenlik payı
OLCEKLER = [round(1.10 - 0.02 * i, 2) for i in range(17)]


def olc(o, ad, font_css):
    """Her ölçek için {'ust': soruların başladığı yükseklik, 'boy': [soru boyları]} (px; baskı genişliğinde, cevaplı)."""
    stil = (PUBLIC / 'calisma.css').read_text(encoding='utf-8')
    logo = (PUBLIC / 'logo.svg').as_uri()
    govde = ''.join(kagit_html(o, ad, True, olcum=True).replace('<article class="ck', f'<article style="--ck-olcek: {k}" class="ck', 1)
                    for k in OLCEKLER).replace('src="/logo.svg"', f'src="{logo}"')
    betik = """<pre id="ck-olcum"></pre><script>
Promise.all([...document.fonts].map(f => f.load())).then(() => document.fonts.ready).then(() => {
  document.getElementById('ck-olcum').textContent = JSON.stringify([...document.querySelectorAll('article.ck')].map(a => {
    const boy = {};
    a.querySelectorAll('.ck-soru').forEach(e => { boy[e.querySelector('.ck-no').textContent] = e.getBoundingClientRect().height; });
    return {ust: a.querySelector('.ck-sorular').getBoundingClientRect().top - a.getBoundingClientRect().top, boy};
  }));
});</script>"""
    belge = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{font_css}{stil}\n'
             f'body {{ margin: 0; }} .ck {{ width: {SAYFA_EN} !important; padding: 0 !important; margin: 0 0 40px !important; box-shadow: none !important; }}'
             f'</style></head><body>{govde}{betik}</body></html>')
    IS.mkdir(parents=True, exist_ok=True)
    gecici = IS / f'{ad}-olcum.html'
    gecici.write_text(belge, encoding='utf-8')
    r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--allow-file-access-from-files', '--window-size=1200,1600',
                        '--virtual-time-budget=8000', '--dump-dom', gecici.as_uri()], capture_output=True, text=True, timeout=180)
    gecici.unlink()
    m = re.search(r'<pre id="ck-olcum">(\[.*?\])</pre>', r.stdout, re.S)
    if not m:
        return None
    n = len(o['sorular'])
    return {k: {'ust': v['ust'], 'boy': [v['boy'][str(i)] for i in range(1, n + 1)]}
            for k, v in zip(OLCEKLER, json.loads(html.unescape(m.group(1))))}


def blok_bol(idx, boy, g):
    """İki sütunlu bir bölümün sorularını (idx, özgün sıra) sütunlara en dengeli biçimde dağıtır: (sol, sag, L, R).
    İlk soru solda kalır; sütun içinde özgün sıra korunur; eşit dengede özgün sıraya en yakın dağılım seçilir.
    Sonra sorular sütun sütun (önce sol, sonra sağ) yeniden numaralanır (sirala)."""
    m, en = len(idx), None
    for maske in range(1, 1 << m, 2):
        sol = [idx[j] for j in range(m) if maske >> j & 1]
        sag = [idx[j] for j in range(m) if not maske >> j & 1]
        L = sum(boy[i] for i in sol) + g * (len(sol) - 1)
        R = sum(boy[i] for i in sag) + g * max(0, len(sag) - 1)
        kayma = sum(abs(k - idx.index(i)) for k, i in enumerate(sol + sag))
        puan = (round(abs(L - R) / 12), kayma)
        if en is None or puan < en[0]:
            en = (puan, sol, sag, L, R)
    return en[1:]


def sayfa_doldur(boy, tam, i0, H, g, hepsi):
    """i0'dan başlayan soruları bir sayfaya (yükseklik H) yerleştirir. hepsi=True: kalan soruların tamamı sığmalı (yoksa None);
    False: sığan en çok soru. Döner: (son soru + 1, bölümler, en alttaki sütun boyları).
    Bölüm: ('tam', i, y) | ('iki', [sol], [sag], y, sol boy, sag boy); iki sütunlu bölümde sorular blok_bol ile dengelenir."""
    n = len(boy)
    for i1 in ([n] if hepsi else range(n, i0, -1)):
        bolumler, y, j, sigar, dolu = [], 0.0, i0, True, (H, H)
        while j < i1 and sigar:
            if j in tam:
                sigar = y + boy[j] <= H
                bolumler.append(('tam', j, y)); y += boy[j] + g; dolu = (H, H); j += 1
            else:
                k = j
                while k < i1 and k not in tam:
                    k += 1
                sol, sag, L, R = blok_bol(list(range(j, k)), boy, g)
                sigar = y + max(L, R) <= H
                bolumler.append(('iki', sol, sag, y, L, R)); dolu = (y + L, y + R); y += max(L, R) + g; j = k
        if sigar:
            return i1, bolumler, dolu
    return None


def sayfa1_onek(boy, H, g, geri=3):
    """1. sayfa (tam genişlikli soru yokken): sığan en uzun önek (ya da en çok `geri` soru kısası) dengeli sütunlara bölünür, sonra
    sütun altındaki boşluklara sonraki sorulardan sığanlar en iyi sığdıkları sütuna eklenir. Böylece 2. sayfaya kalan hiçbir soru
    1. sayfadaki boşluğa sığmaz (kullanıcı 30.09.2026: "soru sığabilecekken mizanpaj ve soru yeri değiştirerek boş bırakma").
    Önek seçimi: yayılamayan boşluk, taşınan soru sayısı, en büyük boşluk en az olan. Döner: (2. sayfaya kalanlar, bölümler) ya da None."""
    s = sayfa_doldur(boy, set(), 0, H, g, False)
    if not s:
        return None
    en = None
    for p in range(s[0], max(1, s[0] - geri) - 1, -1):
        sol, sag, L, R = blok_bol(list(range(p)), boy, g)
        sut, dolu, kalan, tasinan = [list(sol), list(sag)], [L, R], [], 0
        for i in range(p, len(boy)):
            yer = [j for j in (0, 1) if dolu[j] + boy[i] + (g if sut[j] else 0) <= H]
            if yer:
                j = min(yer, key=lambda j: H - dolu[j])
                dolu[j] += boy[i] + (g if sut[j] else 0)
                sut[j].append(i)
                tasinan += 1
            else:
                kalan.append(i)
        artik = [max(0.0, H - dolu[j] - max(0, len(sut[j]) - 1) * YAYMA_SINIRI) for j in (0, 1)]
        puan = (round(max(artik) / MM), tasinan, round(max(H - d for d in dolu) / (4 * MM)), -p)
        if en is None or puan < en[0]:
            en = (puan, kalan, [('iki', sut[0], sut[1], 0.0, dolu[0], dolu[1])])
    return en[1], en[2]


def sirala(o, plan):
    """Sayfa planındaki okuma sırasına göre (sayfa sayfa; bölümde önce sol sütun, sonra sağ) soruları yeniden dizer ve planı yeni sıraya çevirir.
    Seçenek/eşleştirme karıştırma tohumu özgün numarada kalır (_tohum): ölçülen boylar değişmez."""
    sira = [i for sayfa in plan for b in sayfa for i in ([b[1]] if b[0] == 'tam' else b[1] + b[2])]
    for no, s in enumerate(o['sorular'], 1):
        s.setdefault('_tohum', no)
    o['sorular'] = [o['sorular'][i] for i in sira]
    yeni = {eski: k for k, eski in enumerate(sira)}
    return [[('tam', yeni[b[1]]) if b[0] == 'tam' else ('iki', [yeni[i] for i in b[1]], [yeni[i] for i in b[2]], b[3]) for b in sayfa] for sayfa in plan]


YAYMA_SINIRI = 12 * MM  # sütunu sayfa altına yayarken sorular arasına eklenebilecek en büyük boşluk


def yerlesim(o, olcum):
    """Sayfa planı adayları [(ölçek, plan, sütun altı boşlukları mm)], önce seçilen.
    Seçim: 1. sayfası derli toplu olan (sütunlar, sorular arasına en çok YAYMA_SINIRI eklenerek sayfa altına varıyor) en büyük ölçek;
    yoksa 1. sayfada en az boşluk bırakan ölçek. 2. sayfa da derli toplu ise yayılır, değilse üstten dizilir (altı boş kalır: soru eklenmeli)."""
    tam = {i for i, s in enumerate(o['sorular']) if s.get('genislik') == 'tam'}
    adaylar = []
    for k in OLCEKLER:
        boy, g = olcum[k]['boy'], 7 * k
        H1, H2 = SAYFA_BOY - PAY - olcum[k]['ust'], SAYFA_BOY - PAY
        if not tam:
            r = sayfa1_onek(boy, H1, g)
            if not r:
                continue
            kalan, b1 = r
            sayfalar = [(b1, H1)]
            if kalan:
                sol, sag, L, R = blok_bol(kalan, boy, g)
                if max(L, R) > H2:
                    continue
                sayfalar.append(([('iki', sol, sag, 0.0, L, R)], H2))
        else:
            s1 = sayfa_doldur(boy, tam, 0, H1, g, False)
            sayfalar = [(s1[1], H1)]
            if s1[0] < len(boy):
                s2 = sayfa_doldur(boy, tam, s1[0], H2, g, True)
                if not s2:
                    continue
                sayfalar.append((s2[1], H2))
        plan, bosluk, daginik = [], [], []
        for bolumler, H in sayfalar:
            son = bolumler[-1]
            if son[0] == 'iki':
                _, sol, sag, y, L, R = son
                kalan = [H - y - L, H - y - R]
                ek = [kalan[j] / (len(liste) - 1) if len(liste) > 1 else (kalan[j] if liste else 0) for j, liste in enumerate((sol, sag))]
            else:
                kalan = [H - son[2] - boy[son[1]]] * 2
                ek = kalan
            bosluk += [round(x / MM) for x in kalan]
            daginik.append(max(ek))
            cikti = []
            for b in bolumler:
                if b[0] == 'tam':
                    cikti.append(('tam', b[1]))
                else:
                    yay = b is son and (len(plan) == 0 or max(ek) <= YAYMA_SINIRI)
                    ara = [g + min(YAYMA_SINIRI, ek[j]) if yay and len(b[1 + j]) > 1 else g for j in (0, 1)]
                    cikti.append(('iki', b[1], b[2], ara))
            plan.append(cikti)
        adaylar.append((k, plan, bosluk, daginik[0]))
    derli = [a for a in adaylar if a[3] <= YAYMA_SINIRI]
    ilk = derli[0] if derli else min(adaylar, key=lambda a: a[3], default=None)
    return [a[:3] for a in ([ilk] + [a for a in adaylar if a[0] < ilk[0]] if ilk else [])]


def plan_html(plan, sorular_html, baski):
    """Sayfa planını HTML'e çevirir. Baskıda (PDF) 2. sayfa zorunlu sayfa sonuyla başlar ve sütun aralıkları plana göre açılır."""
    cikti = ''
    for sira, sayfa_ in enumerate(plan):
        ic = ''
        for b in sayfa_:
            if b[0] == 'tam':
                ic += sorular_html[b[1]]
            else:
                _, sol, sag, ara = b
                stil = [f' style="--ck-ara: {a:.1f}px"' if baski else '' for a in ara]
                ic += (f'<div class="ck-iki"><div class="ck-sutun"{stil[0]}>{"".join(sorular_html[i] for i in sol)}</div>'
                       f'<div class="ck-sutun"{stil[1]}>{"".join(sorular_html[i] for i in sag)}</div></div>')
        cikti += f'<div class="ck-sorular{" ck-sayfa-sonu" if baski and sira else ""}">{ic}</div>'
    return cikti


def kagit_html(o, ad, cevapli=False, plan=None, baski=False, olcum=False):
    ders = DERSLER.get(o['ders'], o['ders'])
    parcalar = [(i, s, soru_html(s, i, ad)) for i, s in enumerate(o['sorular'], 1)]
    if olcum:  # ölçüm belgesi: yarım sorular tek sütunda alt alta, tam genişlikliler ayrı
        sorular = ('<div class="ck-sorular"><div class="ck-iki"><div class="ck-sutun">' + ''.join(h for _, s, h in parcalar if s.get('genislik') != 'tam')
                   + '</div><div class="ck-sutun"></div></div>' + ''.join(h for _, s, h in parcalar if s.get('genislik') == 'tam') + '</div>')
    elif plan:
        sorular = plan_html(plan, [h for _, _, h in parcalar], baski)
    else:
        sorular = f'<div class="ck-sorular">{dizilim(parcalar)}</div>'
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
  {sorular}
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


def pdf_yap(o, ad, cevapli, font_css, plan=None, olcek=None):
    from pypdf import PdfReader
    cikti = PUBLIC / 'calisma' / 'pdf' / f'{ad}{"-cevapli" if cevapli else ""}.pdf'
    cikti.parent.mkdir(parents=True, exist_ok=True)
    stil = (PUBLIC / 'calisma.css').read_text(encoding='utf-8')
    logo = (PUBLIC / 'logo.svg').as_uri()
    for olcek in ([olcek] if plan else (1.0, 0.95, 0.9, 0.86, 0.82, 0.78)):
        govde = kagit_html(o, ad, cevapli, plan, baski=True).replace('src="/logo.svg"', f'src="{logo}"')
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


def web_sayfasi(o, ad, plan=None):
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
  <section class="bolum"><div class="kap ck-sayfalar">{kagit_html(o, ad, plan=plan)}</div></section>'''
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
        olcum = olc(o, ad, font_css)
        adaylar = yerlesim(o, olcum) if olcum else []
        if not adaylar:
            print(f'{ad}: ÖLÇÜMLÜ YERLEŞİM YOK ({"ölçüm alınamadı" if not olcum else "2 sayfaya sığmıyor"}); eski yöntemle üretiliyor')
            adaylar = [(None, None, [])]
        asil = list(o['sorular'])
        for olcek, plan, bosluk in adaylar:  # ölçüm baskıyla uyuşmazsa (3. sayfa) bir küçük ölçeğe inilir
            o['sorular'] = list(asil)
            if plan:
                plan = sirala(o, plan)
            s1, k1 = pdf_yap(o, ad, False, font_css, plan, olcek)
            s2, k2 = pdf_yap(o, ad, True, font_css, plan, olcek)
            if max(s1, s2) <= 2:
                break
        kayitlar.append(web_sayfasi(o, ad, plan))
        print(f'{ad}: {len(o["sorular"])} soru, görselli {gorselli} (%{100 * gorselli // len(o["sorular"])}); PDF {s1} sayfa (ölçek {k1}), cevaplı {s2} sayfa (ölçek {k2})'
              + (f'; sütun altı boşluk (mm, yayılmadan önce) {bosluk}' + ('  ← KISA: soru eklenmeli' if max(bosluk[2:] or [0]) > 45 else '') if plan else ''))
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
