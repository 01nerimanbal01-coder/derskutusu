"""8. sınıf İngilizce 2. hafta (Unit 1: Friendship — Personal Traits, Inquiries, Accepting & Refusing) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def durum_oneri_kartlari():
    kartlar = [
        ('1. Thirsty (Susamış)', 'Would you like to drink water?', MAVI, MAVI_A),
        ('2. Hungry (Aç)', 'What about eating something?', TUR, TUR_A),
        ('3. Tired (Yorgun)', 'Let’s have a rest!', YES, YES_A),
        ('4. Empty Fridge (Boş)', 'Why don’t we go shopping?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 25, bas, 10.4, r)
        ic += yazi(x + 71, 52, alt, 9.7, LAC, ince=True)
    return svg(600, 80, ic, 'İçinde bulunulan duruma göre yapılan İngilizce teklif kartları.', 15)


def karakter_kanit_kartlari():
    kartlar = [
        ('1. Kart · keeps my secrets', 'Eşleşen sıfat: trustworthy', MAVI, MAVI_A),
        ('2. Kart · never tells lies', 'Eşleşen sıfat: honest', YES, YES_A),
        ('3. Kart · sees bad sides', 'Eşleşen sıfat: cheerful (!)', KIR, KIR_A),
        ('4. Kart · always backs me up', 'Eşleşen sıfat: supportive', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Davranış kanıtları ile eşleştirilen kişilik sıfatları panosu.', 16)


def davet_kalip_panosu():
    ic = kutu(6, 6, 286, 76, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Müsaitlik ve Teklif Kalıpları', 10.8, MAVI)
    ic += yazi(149, 45, '• Are you busy? → No, not at all. (Müsait)', 10.0, LAC, ince=True)
    ic += yazi(149, 64, '• How / What about + V-ing  |  Let’s + V1', 10.0, MAVI)

    ic += kutu(308, 6, 286, 76, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Kabul ve Mazeretli Ret', 10.8, TUR)
    ic += yazi(451, 45, '• I’d love to, but I can’t. (Mazeretli ret)', 10.0, LAC, ince=True)
    ic += yazi(451, 64, '• I’m full / stuffed. (Yalnız yiyecek reddi)', 10.0, TUR)
    return svg(600, 88, ic, 'Müsaitlik sorma, kabul ve mazeretli ret kuralları panosu.', 16)


def bisiklet_turu_mesajlari():
    yanitlar = [
        ('Jack', '“Yeah, why not? I love cycling!”', YES, YES_A),
        ('Sam', '“I’m sorry, I can’t. I have an exam.”', KIR, KIR_A),
        ('Mary', '“Sure, that sounds awesome!”', MAVI, MAVI_A),
        ('Kate', '“I’d love to, but I will visit my aunt.”', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, met, r, z) in enumerate(yanitlar):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, f'{ad}’in Yanıtı:', 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, met, 9.9, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'David in bisiklet turu davetine dört arkadaşının verdiği yanıtlar.', 16)


def telefon_diyalog_adimlari():
    adimlar = [
        ('1. Müsaitlik Sor', 'Are you busy Saturday?', MAVI, MAVI_A),
        ('2. Müsaitlik Yanıtı', 'No, not at all. Why?', TUR, TUR_A),
        ('3. Daveti Yap', 'Would you like to go...?', MOR, MOR_A),
        ('4. Kabul ve Saat', 'Sure! Let’s meet at 2.', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.4, r)
        ic += yazi(x + 71, 50, alt, 9.9, LAC, ince=True)
    return svg(600, 78, ic, 'Telefon konuşmasında müsaitlik sorma, davet ve kabul sırası.', 15)


def icecek_ikram_karti():
    ic = kutu(6, 6, 286, 70, YES_A, YES, 8, 1.5)
    ic += yazi(149, 24, 'İkram: Would you like some orange juice?', 10.4, YES)
    ic += yazi(149, 46, '1) Accepting (Kabul tepkisi):', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'Yes, I’d love some. / Yeah, great.', 10.1, YES)

    ic += kutu(308, 6, 286, 70, KIR_A, KIR, 8, 1.5)
    ic += yazi(451, 24, 'Tok Olduğunu Belirterek Reddetme', 10.4, KIR)
    ic += yazi(451, 46, '2) Refusing (Tokluk mazereti):', 10.1, LAC, ince=True)
    ic += yazi(451, 63, 'No, thanks. I’m full / stuffed.', 10.1, KIR)
    return svg(600, 82, ic, 'Portakal suyu ikramını kabul ve tok olduğu için reddetme kartı.', 15)


def angel_jenny_diyalog():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Angel (Teklif Yapan)', 10.8, MAVI)
    ic += yazi(149, 46, '“Jenny! Would you like to drink', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'some fruit juice at the café?”', 10.1, MAVI)

    ic += kutu(308, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Jenny (Mazeret Bildiren)', 10.8, TUR)
    ic += yazi(451, 46, '“___________, because I have to', 10.1, LAC)
    ic += yazi(451, 63, 'take my little sister home right now.”', 10.0, TUR, ince=True)
    return svg(600, 84, ic, 'Angel ve Jenny arasındaki teklif ve mazeret diyaloğu.', 16)


def kevin_davetiye_karti():
    ic = kutu(6, 6, 286, 72, MOR_A, MOR, 8, 1.5)
    ic += yazi(149, 24, 'Kevin’s Birthday Invitation', 10.8, MOR)
    ic += yazi(149, 46, '“Would you like to come to my', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'birthday party tomorrow evening?”', 10.1, MOR)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Senin Planın (Yanıt İpuçları)', 10.8, YES)
    ic += yazi(451, 46, '• Mazeret: Kuzenin yarın geliyor', 10.0, LAC, ince=True)
    ic += yazi(451, 63, '• Yeni öneri: Pazar günü sinema', 10.0, YES)
    return svg(600, 84, ic, 'Kevin in doğum günü davetiyesi ve mazeretli yeni zaman önerisi.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = durum_oneri_kartlari()
    s[1]['gorsel'] = karakter_kanit_kartlari()
    s[3]['gorsel'] = davet_kalip_panosu()
    s[5]['gorsel'] = bisiklet_turu_mesajlari()
    s[6]['gorsel'] = telefon_diyalog_adimlari()
    s[7]['gorsel'] = icecek_ikram_karti()
    s[8]['gorsel'] = angel_jenny_diyalog()
    s[11]['gorsel'] = kevin_davetiye_karti()
