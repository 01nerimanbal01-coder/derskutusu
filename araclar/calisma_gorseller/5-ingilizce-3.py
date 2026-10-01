"""5. sınıf İngilizce 3. hafta (Revision 2: jobs, places, seaside, sea animals, advice, food) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#f3e2b3'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def bina(cx, yt, renk, no, pikto):
    """Krokideki bina: çatı + gövde + numara + piktogram (cx, cy merkezli)."""
    ic = f'<path d="M{cx - 32} {yt + 9} L{cx} {yt} L{cx + 32} {yt + 9} Z" fill="{renk}"/>'
    ic += kutu(cx - 28, yt + 9, 56, 24, '#fff', renk, 2, 1.4) + rozet(cx - 18, yt + 21, no, renk, 7)
    return ic + pikto(cx + 8, yt + 21)


def p_ekmek(x, y):
    return f'<ellipse cx="{x}" cy="{y}" rx="11" ry="6" fill="#e0a860"/>' + ''.join(f'<line x1="{x + d}" y1="{y - 4}" x2="{x + d + 2}" y2="{y - 1}" stroke="#a9702c" stroke-width="1.2"/>' for d in (-6, -1, 4))


def p_arti(x, y):
    return f'<rect x="{x - 3}" y="{y - 9}" width="6" height="18" fill="{YES}"/><rect x="{x - 9}" y="{y - 3}" width="18" height="6" fill="{YES}"/>'


def p_muze(x, y):
    return (f'<path d="M{x - 12} {y - 4} L{x} {y - 10} L{x + 12} {y - 4} Z" fill="{MOR}"/>'
            f'<path d="M{x - 8} {y - 3} v11 M{x} {y - 3} v11 M{x + 8} {y - 3} v11 M{x - 12} {y + 9} h24" stroke="{MOR}" stroke-width="2"/>')


def p_meyve(x, y):
    return (f'<circle cx="{x - 6}" cy="{y + 2}" r="6" fill="{TUR}"/><circle cx="{x + 6}" cy="{y + 2}" r="6" fill="{KIR}"/>'
            f'<path d="M{x + 6} {y - 4} q4 -6 8 -3 q-4 4 -8 3" fill="{YES}"/>')


def kroki():
    """Mahalle krokisi: 1 fırın, 2 eczane, 3 müze, 4 manav; ortada yol."""
    ic = kutu(4, 4, 352, 92, '#f7f9fc', GRI, 8, 1.2)
    ic += '<rect x="4" y="43" width="352" height="14" fill="#d9dee8"/>' + ''.join(f'<rect x="{x}" y="49" width="12" height="2" fill="#fff"/>' for x in range(14, 350, 28))
    ic += bina(60, 6, TUR, '1', p_ekmek) + bina(190, 6, YES, '2', p_arti)
    ic += bina(130, 60, MOR, '3', p_muze) + bina(290, 60, KIR, '4', p_meyve)
    return svg(360, 100, ic, 'Mahalle krokisi: 1 fırın (ekmek), 2 eczane (yeşil artı), 3 müze (sütunlar), 4 manav (meyve)', 22)


def meslek_nesneleri():
    """Stetoskop, termometre ve hastane tabelası (doktor)."""
    ic = kutu(4, 4, 352, 62, GRI_A, GRI, 8, 1.2)
    # stetoskop
    ic += (f'<path d="M50 14 v16 a18 18 0 0 0 36 0 v-16" fill="none" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
           f'<path d="M68 48 v6 q0 8 10 8 h20 q10 0 10 -8 v-4" fill="none" stroke="{LAC}" stroke-width="3"/>'
           f'<circle cx="108" cy="42" r="9" fill="{CAM}"/><circle cx="108" cy="42" r="4" fill="#fff"/>'
           f'<circle cx="50" cy="12" r="3" fill="{LAC}"/><circle cx="86" cy="12" r="3" fill="{LAC}"/>')
    # termometre
    ic += (f'<rect x="170" y="12" width="10" height="36" rx="5" fill="#fff" stroke="{LAC}" stroke-width="1.6"/><circle cx="175" cy="52" r="7" fill="{KIR}"/>'
           f'<rect x="172.5" y="30" width="5" height="22" fill="{KIR}"/>' + ''.join(f'<line x1="181" y1="{y}" x2="185" y2="{y}" stroke="{LAC}" stroke-width="1.2"/>' for y in (18, 24, 30, 36)))
    # hastane tabelası
    ic += kutu(236, 14, 100, 40, '#fff', MAVI, 6, 1.6) + f'<rect x="248" y="24" width="6" height="20" fill="{KIR}"/><rect x="241" y="31" width="20" height="6" fill="{KIR}"/>'
    ic += yazi(298, 39, 'HOSPITAL', 11.5, MAVI)
    return svg(360, 70, ic, 'Meslek nesneleri: stetoskop, termometre, hastane tabelası', 16)


def aile_isleri():
    """Efe'nin aile kartları: Mum teacher, Dad farmer, Aunt singer, Grandad doctor."""
    kisiler = [('Mum', 'teacher', MAVI, MAVI_A), ('Dad', 'farmer', YES, YES_A), ('Aunt', 'singer', MOR, MOR_A), ('Grandad', 'doctor', KIR, KIR_A)]
    ic = ''
    for i, (kim, is_, renk, acik) in enumerate(kisiler):
        x0 = 4 + i * 89; cx = x0 + 42
        ic += kutu(x0, 4, 84, 72, acik, renk, 8, 1.2) + yazi(cx, 19, kim, 11.5, renk) + yazi(cx, 70, is_, 11, LAC, 'middle', True)
        if i == 0:  # yazı tahtası
            ic += kutu(cx - 16, 27, 32, 22, '#fff', renk, 2, 1.2) + yazi(cx, 42, 'ABC', 10, renk) + f'<rect x="{cx - 4}" y="49" width="8" height="5" fill="{renk}"/>'
        elif i == 1:  # fide + toprak
            ic += (f'<rect x="{cx - 18}" y="46" width="36" height="8" rx="2" fill="{KAHVE}"/><path d="M{cx} 46 v-14" stroke="{YES}" stroke-width="2.4"/>'
                   f'<path d="M{cx} 36 q-12 -10 -12 -2 q0 6 12 2 M{cx} 30 q12 -10 12 -2 q0 6 -12 2" fill="{YES}"/>')
        elif i == 2:  # mikrofon
            ic += f'<circle cx="{cx}" cy="34" r="9" fill="{renk}"/><rect x="{cx - 3}" y="42" width="6" height="14" rx="2" fill="{LAC}"/><rect x="{cx - 8}" y="54" width="16" height="3" fill="{LAC}"/>'
        else:  # doktor çantası
            ic += kutu(cx - 16, 32, 32, 22, '#fff', renk, 3, 1.4) + f'<rect x="{cx - 6}" y="27" width="12" height="5" rx="1" fill="{renk}"/>' + f'<rect x="{cx - 2}" y="36" width="4" height="14" fill="{renk}"/><rect x="{cx - 7}" y="41" width="14" height="4" fill="{renk}"/>'
    return svg(360, 80, ic, "Efe'nin aile kartları: Mum teacher, Dad farmer, Aunt singer, Grandad doctor", 18)


def deniz_afisi():
    """Afiş: denizde plastik torba yanında deniz kaplumbağası, kumda çöp, uyarı üçgeni."""
    ic = f'<rect x="4" y="4" width="352" height="34" rx="8" fill="{CAM_A}"/><rect x="4" y="30" width="352" height="46" fill="{MAVI_A}"/><rect x="4" y="30" width="352" height="46" fill="none" stroke="{CAM}" stroke-width="1.4"/>'
    ic += f'<rect x="4" y="62" width="352" height="14" fill="{KUM}"/>'
    ic += ''.join(f'<path d="M{x} 36 q6 -4 12 0 t12 0" fill="none" stroke="{CAM}" stroke-width="1.4"/>' for x in range(20, 340, 60))
    # kaplumbağa
    ic += (f'<ellipse cx="110" cy="52" rx="22" ry="11" fill="{YES}"/><path d="M96 48 h28 M104 43 v18 M116 43 v18" stroke="#0c7a3c" stroke-width="1.2"/>'
           f'<circle cx="136" cy="50" r="6" fill="#7cc27c"/><circle cx="138" cy="49" r="1.2" fill="{LAC}"/>'
           f'<path d="M92 58 l-8 6 M128 58 l8 6 M96 44 l-8 -5 M124 44 l8 -5" stroke="#7cc27c" stroke-width="3" stroke-linecap="round"/>')
    # plastik torba
    ic += (f'<path d="M186 42 q4 -8 8 0 q4 -8 8 0 h6 l3 20 h-28 l3 -20 z" fill="#fff" stroke="{SOLUK}" stroke-width="1.3"/>'
           f'<path d="M190 42 q4 -6 8 0 M202 42 q-4 -6 -8 0" fill="none" stroke="{SOLUK}" stroke-width="1"/>')
    # kumda çöp
    ic += f'<path d="M262 72 l4 -8 l6 3 l5 -6 l4 11 z" fill="{GRI}"/><rect x="284" y="66" width="10" height="6" rx="1" fill="{KIR}"/>'
    # uyarı üçgeni
    ic += f'<path d="M320 12 L338 40 H302 Z" fill="{ALTIN}" stroke="{LAC}" stroke-width="1.4"/><rect x="318.5" y="20" width="3" height="10" fill="{LAC}"/><circle cx="320" cy="34" r="1.8" fill="{LAC}"/>'
    return svg(360, 80, ic, 'Afiş: denizde plastik torbanın yanında deniz kaplumbağası, kumda çöp, uyarı üçgeni', 18)


def plaj_tabelasi():
    """Plaj tabelası: 1 kırmızı bayrak (yasak), 2 çöp kutusu (temiz tut), 3 su şişesi ve güneş, 4 güneş ve 12:00 gösteren saat."""
    ic = kutu(4, 4, 352, 62, '#fff', LAC, 6, 1.6) + f'<rect x="4" y="4" width="352" height="14" rx="6" fill="{LAC}"/><rect x="4" y="12" width="352" height="6" fill="{LAC}"/>' + yazi(180, 14.5, 'AT THE BEACH', 9.5, '#fff')
    renk = [KIR, YES, TUR, TUR]
    for i in range(4):
        cx = 48 + i * 88
        ic += rozet(cx - 30, 40, str(i + 1), renk[i], 7)
        if i == 0:  # kırmızı bayrak
            ic += f'<rect x="{cx - 8}" y="24" width="2.5" height="34" fill="{LAC}"/><path d="M{cx - 5.5} 24 h22 l-5 7 l5 7 h-22 z" fill="{KIR}"/>'
        elif i == 1:  # çöp kutusu + ok
            ic += (f'<path d="M{cx - 8} 32 h20 l-3 26 h-14 z" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/><rect x="{cx - 10}" y="27" width="24" height="4" rx="1" fill="{YES}"/>'
                   f'<path d="M{cx + 20} 30 v-8 h6 M{cx + 20} 30 l-3 -4 M{cx + 20} 30 l3 -4" fill="none" stroke="{YES}" stroke-width="1.8"/>')
        elif i == 2:  # su şişesi + güneş
            ic += (f'<rect x="{cx - 6}" y="30" width="12" height="28" rx="3" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/><rect x="{cx - 3}" y="24" width="6" height="6" fill="{MAVI}"/>'
                   f'<circle cx="{cx + 20}" cy="30" r="6" fill="{ALTIN}"/>' + ''.join(f'<line x1="{cx + 20 + 8 * math.cos(k * math.pi / 4):.1f}" y1="{30 + 8 * math.sin(k * math.pi / 4):.1f}" x2="{cx + 20 + 11 * math.cos(k * math.pi / 4):.1f}" y2="{30 + 11 * math.sin(k * math.pi / 4):.1f}" stroke="{ALTIN}" stroke-width="1.4"/>' for k in range(8)))
        else:  # öğle güneşi ve 12:00 gösteren saat
            ic += (f'<circle cx="{cx - 8}" cy="33" r="6" fill="{ALTIN}"/>' + ''.join(f'<line x1="{cx - 8 + 8 * math.cos(k * math.pi / 4):.1f}" y1="{33 + 8 * math.sin(k * math.pi / 4):.1f}" x2="{cx - 8 + 11 * math.cos(k * math.pi / 4):.1f}" y2="{33 + 11 * math.sin(k * math.pi / 4):.1f}" stroke="{ALTIN}" stroke-width="1.4"/>' for k in range(8))
                   + kutu(cx + 4, 42, 30, 14, '#fff', LAC, 2, 1.2) + yazi(cx + 19, 52.5, '12:00', 9.5, LAC))
    return svg(360, 70, ic, 'Plaj tabelası: 1 kırmızı bayrak, 2 çöp kutusu ve ok, 3 su şişesi ve güneş, 4 güneş ve 12:00 gösteren saat', 16)


def boy_grafigi():
    """Uzunluk grafiği: dolphin 2 m, sea turtle 1 m, crab 20 cm."""
    ic = yazi(180, 14, 'How long are they?', 12, LAC)
    veri = [('dolphin', 240, '2 m', MAVI), ('sea turtle', 120, '1 m', YES), ('crab', 24, '20 cm', TUR)]
    for i, (ad, uz, deger, renk) in enumerate(veri):
        y = 26 + i * 20
        ic += yazi(74, y + 12, ad, 11.5, LAC, 'end', True) + f'<rect x="82" y="{y}" width="{uz}" height="15" rx="3" fill="{renk}"/>' + yazi(88 + uz, y + 12, deger, 11, LAC, 'start')
    return svg(360, 84, ic, 'Uzunluk grafiği: dolphin 2 m, sea turtle 1 m, crab 20 cm', 18)


def yemek_tepsisi():
    """Öğle tepsisi: broccoli, chips, fish, sweets, yoghurt, chocolate (adlarıyla)."""
    ic = kutu(4, 4, 352, 78, '#fbf5e6', KAHVE, 10, 1.4)
    adlar = ['broccoli', 'chips', 'fish', 'sweets', 'yoghurt', 'chocolate']
    for i, ad in enumerate(adlar):
        cx = 34 + i * 58; cy = 36
        if i == 0:
            ic += f'<rect x="{cx - 3}" y="{cy}" width="6" height="14" fill="#7cc27c"/>' + ''.join(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="7" fill="#0c7a3c"/>' for dx, dy in ((-8, -2), (8, -2), (0, -9)))
        elif i == 1:
            ic += f'<path d="M{cx - 12} {cy - 2} h24 l-3 18 h-18 z" fill="{KIR}"/>' + ''.join(f'<rect x="{cx + dx}" y="{cy - 16 + abs(dx)}" width="4" height="16" rx="1" fill="{ALTIN}"/>' for dx in (-9, -3, 3, 9))
        elif i == 2:
            ic += f'<ellipse cx="{cx - 2}" cy="{cy + 4}" rx="14" ry="8" fill="{MAVI}"/><path d="M{cx + 10} {cy + 4} l10 -8 v16 z" fill="{MAVI}"/><circle cx="{cx - 9}" cy="{cy + 2}" r="1.6" fill="#fff"/>'
        elif i == 3:
            ic += f'<ellipse cx="{cx}" cy="{cy + 4}" rx="10" ry="7" fill="#f28ab2"/><path d="M{cx - 10} {cy + 4} l-8 -6 v12 z M{cx + 10} {cy + 4} l8 -6 v12 z" fill="#f28ab2"/>'
        elif i == 4:
            ic += f'<path d="M{cx - 11} {cy - 8} h22 l-3 24 h-16 z" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/><rect x="{cx - 13}" y="{cy - 11}" width="26" height="4" rx="1" fill="{MAVI}"/>'
        else:
            ic += f'<rect x="{cx - 13}" y="{cy - 6}" width="26" height="20" rx="2" fill="{KAHVE}"/><path d="M{cx - 4} {cy - 6} v20 M{cx + 5} {cy - 6} v20 M{cx - 13} {cy + 4} h26" stroke="#5a3717" stroke-width="1.2"/>'
        ic += yazi(cx, 72, ad, 10.5, LAC, 'middle', True)
    return svg(360, 86, ic, 'Öğle tepsisi: broccoli, chips, fish, sweets, yoghurt, chocolate', 19)


def takvim():
    """Haftalık takvim: yalnız pazar günü pazar sepeti."""
    gunler = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ic = yazi(180, 13, "Ece's mum · going to the market", 11.5, LAC)
    for i, g in enumerate(gunler):
        x0 = 6 + i * 50
        ic += kutu(x0, 20, 46, 16, MAVI if i == 6 else MAVI_A, MAVI, 3, 1) + yazi(x0 + 23, 32, g, 10.5, '#fff' if i == 6 else LAC)
        ic += kutu(x0, 38, 46, 24, '#fff', MAVI, 3, 1)
    cx = 6 + 6 * 50 + 23
    ic += f'<path d="M{cx - 11} 46 h22 l-3 12 h-16 z" fill="{TUR}"/><path d="M{cx - 6} 46 q6 -9 12 0" fill="none" stroke="{KAHVE}" stroke-width="2"/><circle cx="{cx - 3}" cy="45" r="2.5" fill="{KIR}"/><circle cx="{cx + 4}" cy="44" r="2.5" fill="{YES}"/>'
    return svg(360, 66, ic, "Haftalık takvim: Ece'nin annesi yalnız pazar günü pazara gidiyor", 15)


def kartpostal():
    ic = kutu(4, 4, 352, 92, '#fffdf7', KAHVE, 6, 1.4) + kutu(316, 10, 30, 24, '#fff', GRI, 2, 1) + f'<circle cx="331" cy="22" r="7" fill="{TUR_A}" stroke="{TUR}" stroke-width="1"/>'
    satirlar = ['Dear Ali,', "I'm at the seaside with my family. Yesterday", 'we went diving and saw a sea turtle. This', 'morning we bought fresh fish at the market.', 'See you soon, Deniz']
    for k, m in enumerate(satirlar):
        ic += yazi(16, 22 + k * 15.5, m, 11.5, LAC, 'start', k not in (0, 4))
    return svg(360, 100, ic, "Kartpostal: Deniz ailesiyle deniz kenarında; dün dalıp deniz kaplumbağası gördü; bu sabah pazardan taze balık aldı", 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kroki()
    s[2]['gorsel'] = meslek_nesneleri()
    s[3]['gorsel'] = aile_isleri()
    s[5]['gorsel'] = deniz_afisi()
    s[6]['gorsel'] = plaj_tabelasi()
    s[7]['gorsel'] = boy_grafigi()
    s[9]['gorsel'] = yemek_tepsisi()
    s[10]['gorsel'] = takvim()
    s[12]['gorsel'] = kartpostal()
