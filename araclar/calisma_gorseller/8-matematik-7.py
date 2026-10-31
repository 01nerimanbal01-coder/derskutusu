"""8. sınıf Matematik 7. hafta (Kareköklü İfadeleri Tahmin Etme, a kök b Biçiminde Yazma ve Sıralama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 punto (K150 EK); kesirler yalnız dikey (K155); tek parça vektörel kök sembolü."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kok_ciz(cx, y, katsayi, ic_metin, boy=11.5, renk=LAC):
    """cx merkezli, y taban çizgili, üst çizgisi bitişik vektörel karekök ifadesi çizer."""
    ic_str = str(ic_metin)
    kat_str = str(katsayi) if katsayi else ''
    w_ic = max(12, len(ic_str) * (boy * 0.62) + 4)
    w_kat = len(kat_str) * (boy * 0.62) + (2 if kat_str else 0)
    toplam_w = w_kat + 10 + w_ic
    sol = cx - toplam_w / 2
    out = ''
    if kat_str:
        out += yazi(sol + w_kat - 1, y, kat_str, boy, renk, 'end')
    rx = sol + w_kat
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.5
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.5:.1f} {orta_y - 1.5:.1f} '
            f'L{rx + 5.5:.1f} {alt_y:.1f} L{rx + 9.5:.1f} {ust_y:.1f} '
            f'H{rx + 10 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.35" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 10 + w_ic / 2, y, ic_str, boy, renk, 'middle')
    return out


def tam_kare_komsular_semasi():
    """Soru 1: Karekök 40 sayısının alt (36) ve üst (49) tam kare komşuları şeması."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    ic += yazi(180, 20, 'Tam Kare Komşularla Yaklaşık Değer Bulma Örneği', 11, MAVI)
    # Sol kutu: alt sınır
    ic += kutu(14, 28, 98, 50, YES_A, YES, 7, 1.3)
    ic += yazi(63, 44, 'Alt Tam Kare', 10.5, YES)
    ic += kok_ciz(44, 66, '', '36', 11.5, LAC)
    ic += yazi(80, 66, '= 6', 11.5, YES)
    # Orta kutu: aranan sayı
    ic += kutu(131, 28, 98, 50, MAVI_A, MAVI, 7, 1.4)
    ic += kok_ciz(180, 48, '', '40', 12, MAVI)
    ic += yazi(180, 68, '6 ile 7 arası', 10.5, LAC)
    # Sağ kutu: üst sınır
    ic += kutu(248, 28, 98, 50, TUR_A, TUR, 7, 1.3)
    ic += yazi(297, 44, 'Üst Tam Kare', 10.5, TUR)
    ic += kok_ciz(278, 66, '', '49', 11.5, LAC)
    ic += yazi(314, 66, '= 7', 11.5, TUR)
    # Oklar ve farklar
    ic += yazi(121.5, 55, '+4', 10.5, YES)
    ic += yazi(238.5, 55, '+9', 10.5, TUR)
    return svg(360, 90, ic, 'Tam kare komşular şeması: karekök 36 eşittir 6 ile karekök 49 eşittir 7 arasında karekök 40; 36ya 4 birim, 49a 9 birim uzaklıkta.', 14)


def sayi_dogrusu_k_noktasi():
    """Soru 3: Sayı doğrusunda 8 ile 9 arasında ve 8'e daha yakın K noktası."""
    ic = kutu(4, 4, 352, 78, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 20, 'Sayı Doğrusunda K Noktasının Konumu', 11, MAVI)
    ic += f'<line x1="28" y1="54" x2="332" y2="54" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<path d="M24 54 l7 -4 v8 z M336 54 l-7 -4 v8 z" fill="{LAC}"/>'
    noktalar = [(50, '7', '49'), (136, '8', '64'), (222, '9', '81'), (308, '10', '100')]
    for x, tam, kk in noktalar:
        ic += f'<line x1="{x}" y1="48" x2="{x}" y2="60" stroke="{LAC}" stroke-width="1.6"/>'
        ic += yazi(x, 73, tam, 11.5, LAC)
        ic += kok_ciz(x, 41, '', kk, 10.5, SOLUK)
    # Orta nokta 8,5 çizgisi (x = 179) ve K noktası (x = 158, 8'e daha yakın)
    ic += f'<line x1="179" y1="50" x2="179" y2="58" stroke="{GRI}" stroke-width="1.2" stroke-dasharray="2 2"/>'
    kx = 158
    ic += f'<circle cx="{kx}" cy="54" r="5" fill="{KIR}" stroke="#fff" stroke-width="1.2"/>'
    ic += kutu(kx - 16, 25, 32, 18, KIR_A, KIR, 5, 1.2)
    ic += yazi(kx, 38, 'K', 11, KIR)
    return svg(360, 86, ic, 'Sayı doğrusu üzerinde 7, 8, 9 ve 10 doğal sayıları; K noktası 8 ile 9 arasında ve 8e daha yakın.', 14)


def dort_esitlik_karti():
    """Soru 5: Dört numaralı a kök b eşitlik kartı (II. kart hatalı)."""
    kartlar = [
        ('I. kart', '48', '4', '3', MAVI, MAVI_A),
        ('II. kart', '72', '4', '6', TUR, TUR_A),
        ('III. kart', '125', '5', '5', YES, YES_A),
        ('IV. kart', '180', '6', '5', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sol_k, kat, sag_k, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 12, y + 16, bas, 10.5, r, 'start')
        ic += kok_ciz(x + 56, y + 34, '', sol_k, 11, LAC)
        ic += yazi(x + 88, y + 34, '=', 11.5, r)
        ic += kok_ciz(x + 122, y + 34, kat, sag_k, 11, LAC)
    return svg(360, 96, ic, 'Dört eşitlik kartı: I karekök 48 eşittir 4 kök 3, II karekök 72 eşittir 4 kök 6, III karekök 125 eşittir 5 kök 5, IV karekök 180 eşittir 6 kök 5.', 14)


def iki_kare_bahce():
    """Soru 6: Alanı 60 m² ve 92 m² olan iki karesel bahçe."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    # 1. Bahçe
    ic += kutu(20, 12, 140, 66, YES_A, YES, 7, 1.4)
    ic += yazi(90, 30, '1. Kare Bahçe', 11, YES)
    ic += yazi(90, 49, 'Alan = 60 m²', 11.5, LAC)
    ic += yazi(90, 68, 'Kenar = ? m', 10.5, YES)
    # 2. Bahçe
    ic += kutu(200, 12, 140, 66, TUR_A, TUR, 7, 1.4)
    ic += yazi(270, 30, '2. Kare Bahçe', 11, TUR)
    ic += yazi(270, 49, 'Alan = 92 m²', 11.5, LAC)
    ic += yazi(270, 68, 'Kenar = ? m', 10.5, TUR)
    return svg(360, 90, ic, 'İki karesel bahçe: 1. bahçenin alanı 60 metrekare, 2. bahçenin alanı 92 metrekare.', 14)


def cetvel_kalem_semasi():
    """Soru 7: 0-8 cm cetvel ve boyu 6 ile 7 arasında 7'ye yakın kalem."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    # Kalem çizimi (x=24 -> 0 cm; her cm = 38 px; 6 cm = 252, 7 cm = 290; kalem ucu = 279 -> ~6,71 cm)
    ic += f'<rect x="24" y="16" width="232" height="16" rx="2" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="256,16 279,24 256,32" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3"/>'
    ic += f'<polygon points="272,21.5 279,24 272,26.5" fill="{KIR}"/>'
    ic += yazi(140, 28, 'Kalem Uzunluğu = ? cm', 10.5, LAC)
    ic += f'<line x1="24" y1="12" x2="24" y2="44" stroke="{KIR}" stroke-width="1.2" stroke-dasharray="3 2"/>'
    ic += f'<line x1="279" y1="24" x2="279" y2="44" stroke="{KIR}" stroke-width="1.2" stroke-dasharray="3 2"/>'
    # Cetvel gövdesi
    ic += kutu(14, 44, 332, 34, '#fff', LAC, 5, 1.3)
    for cm in range(9):
        cx = 24 + cm * 38
        ic += f'<line x1="{cx}" y1="44" x2="{cx}" y2="54" stroke="{LAC}" stroke-width="1.4"/>'
        ic += yazi(cx, 69, str(cm), 11, LAC)
        if cm < 8:
            ic += f'<line x1="{cx + 19}" y1="44" x2="{cx + 19}" y2="50" stroke="{GRI}" stroke-width="1.1"/>'
    return svg(360, 90, ic, 'Cetvel üzerinde sol ucu 0da, sağ ucu 6 ile 7 santimetre arasında ve 7ye daha yakın duran kalem.', 14)


def carpan_panosu_72():
    """Soru 9: Karekök 72 = a kök b eşitliği ve a, b pozitif tam sayı koşul panosu."""
    ic = kutu(4, 4, 352, 76, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Kareköklü İfadenin Farklı a kök b Yazılışları', 11, MOR)
    ic += kutu(14, 28, 154, 44, '#fff', MOR, 6, 1.2)
    ic += kok_ciz(58, 55, '', '72', 12, LAC)
    ic += yazi(88, 55, '=', 12, MOR)
    ic += kok_ciz(122, 55, 'a', 'b', 12, MOR)
    ic += kutu(178, 28, 168, 44, '#fff', MAVI, 6, 1.2)
    ic += yazi(262, 46, 'a ve b pozitif tam sayı', 10.5, MAVI)
    ic += yazi(262, 64, 'a + b toplamı = ?', 11, LAC)
    return svg(360, 84, ic, 'Karekök 72 eşittir a kök b eşitlik kartı; a ve b pozitif tam sayı.', 14)


def oyuncak_arac_sayi_dogrusu():
    """Soru 10: Sayı doğrusunda 9 noktasından sağa 2 kök 7 birim ilerleyen araç ve L noktası."""
    ic = kutu(4, 4, 352, 80, CAM_A, CAM, 8, 1.3)
    ic += yazi(180, 20, 'Sayı Doğrusunda İlerleme Şeması', 11, CAM)
    ic += f'<line x1="24" y1="60" x2="336" y2="60" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<path d="M20 60 l7 -4 v8 z M340 60 l-7 -4 v8 z" fill="{LAC}"/>'
    # Başlangıç: 9 noktası (x=68), bitiş: L noktası (x=276)
    ic += f'<circle cx="68" cy="60" r="4.5" fill="{MAVI}"/>'
    ic += yazi(68, 75, '9 (Başlangıç)', 10.5, MAVI)
    ic += f'<circle cx="276" cy="60" r="4.5" fill="{KIR}"/>'
    ic += yazi(276, 75, 'L = ?', 11, KIR)
    # Sıçrama yayı
    ic += f'<path d="M72 56 Q172 18 270 55" fill="none" stroke="{TUR}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += f'<polygon points="272,56 263,51 266,46" fill="{TUR}"/>'
    ic += kutu(126, 26, 92, 24, '#fff', TUR, 6, 1.2)
    ic += kok_ciz(172, 43, '+2', '7', 11, TUR)
    return svg(360, 88, ic, 'Sayı doğrusunda 9 noktasından sağa doğru 2 kök 7 birim ilerleyerek L noktasına ulaşma şeması.', 14)


def uc_yuruyus_parkuru():
    """Soru 13: K = 4 kök 5 km, L = 6 kök 2 km ve M = 5 kök 3 km parkur kartları."""
    parkurlar = [
        ('K Parkuru', '4', '5', MAVI, MAVI_A, 4),
        ('L Parkuru', '6', '2', TUR, TUR_A, 122),
        ('M Parkuru', '5', '3', YES, YES_A, 240),
    ]
    ic = ''
    for bas, kat, k_ic, r, z, x in parkurlar:
        ic += kutu(x, 4, 116, 72, z, r, 8, 1.3)
        ic += yazi(x + 58, 22, bas, 11, r)
        ic += kutu(x + 8, 28, 100, 38, '#fff', r, 6, 1.1)
        ic += kok_ciz(x + 46, 52, kat, k_ic, 11.5, LAC)
        ic += yazi(x + 84, 52, 'km', 11, SOLUK, 'middle', True)
    return svg(360, 80, ic, 'Üç yürüyüş parkuru: K parkuru 4 kök 5 km, L parkuru 6 kök 2 km, M parkuru 5 kök 3 km.', 14)


def negatif_karsilastirma_karti():
    """Soru 14: X = −3 kök 5 ve Y = −2 kök 11 negatif kareköklü sayı karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 74, KIR_A, KIR, 8, 1.3)
    ic += yazi(90, 22, '1. Negatif Sayı Kartı', 11, KIR)
    ic += kutu(16, 28, 148, 38, '#fff', KIR, 6, 1.1)
    ic += yazi(58, 52, 'X =', 11.5, LAC)
    ic += kok_ciz(104, 52, '−3', '5', 11.5, KIR)

    ic += kutu(184, 4, 172, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(270, 22, '2. Negatif Sayı Kartı', 11, MAVI)
    ic += kutu(196, 28, 148, 38, '#fff', MAVI, 6, 1.1)
    ic += yazi(236, 52, 'Y =', 11.5, LAC)
    ic += kok_ciz(284, 52, '−2', '11', 11.5, MAVI)
    return svg(360, 82, ic, 'İki negatif kareköklü sayı kartı: X eşittir eksi 3 kök 5 ve Y eşittir eksi 2 kök 11.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = tam_kare_komsular_semasi()
    s[2]['gorsel'] = sayi_dogrusu_k_noktasi()
    s[4]['gorsel'] = dort_esitlik_karti()
    s[5]['gorsel'] = iki_kare_bahce()
    s[6]['gorsel'] = cetvel_kalem_semasi()
    s[8]['gorsel'] = carpan_panosu_72()
    s[9]['gorsel'] = oyuncak_arac_sayi_dogrusu()
    s[12]['gorsel'] = uc_yuruyus_parkuru()
    s[13]['gorsel'] = negatif_karsilastirma_karti()
