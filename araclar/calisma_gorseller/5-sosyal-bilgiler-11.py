"""5. sınıf Sosyal Bilgiler 11. hafta (Afet Öncesi, Sırası ve Sonrası, Afet Çantası ve Evimiz Dünya Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def deprem_asamalari_dort_kart():
    kartlar = [
        ('1. Kart', 'Dolapları duvara sabitlemek', MAVI, MAVI_A),
        ('2. Kart', 'Çök - Kapan - Tutun yapmak', TUR, TUR_A),
        ('3. Kart', 'Gaz ve su vanasını kapatmak', YES, YES_A),
        ('4. Kart', 'AFAD ekiplerine bilgi vermek', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, met, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Deprem öncesi, sırası ve sonrasına ait dört davranış kartı.', 15)


def cevre_ve_afet_bolge_kartlari():
    kartlar = [
        ('1. Ağrı Dağı', 'Van Gölü · Doğal', YES, YES_A),
        ('2. Baraj & Tünel', 'İnsan yapımı', MAVI, MAVI_A),
        ('3. Rize Yamaç', 'Dik ve bol yağışlı', TUR, TUR_A),
        ('4. Muğla Orman', 'Yazı sıcak-kurak', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Doğal-beşerî unsurlar ve bölgesel afet riski kartları.', 15)


def afet_cantasi_paket_secimi():
    paketler = [
        ('1. Paket · Beslenme', 'Su · Konserve · Kuru gıda', YES, YES_A),
        ('2. Paket · Uygunsuz!', 'Taze süt · Pişmiş yemek · Vazo', KIR, KIR_A),
        ('3. Paket · Sağlık', 'İlk yardım · İlaç · Hijyen', MAVI, MAVI_A),
        ('4. Paket · İletişim', 'Fener · Pilli radyo · Düdük', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(paketler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, icerik, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Afet ve acil durum çantası için dört malzeme paketi.', 15)


def iki_il_cografi_afet_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'X İli Coğrafi Özellikleri', 10.2, CAM)
    ic += yazi(91, 44, '• Yüksek ve dik dağ yamaçları', 9.5, LAC, ince=True)
    ic += yazi(91, 64, '• Kış mevsiminde yoğun kar yağışı', 9.5, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'Y İli Coğrafi Özellikleri', 10.2, KIR)
    ic += yazi(269, 44, '• Aktif kırık (fay) hattı üzerinde', 9.5, LAC, ince=True)
    ic += yazi(269, 64, '• Gevşek alüvyon ova zemini', 9.5, LAC, ince=True)
    return svg(360, 88, ic, 'X ve Y illerinin coğrafi özellikleri ve afet risk kartları.', 15)


def afet_sonrasi_iletisim_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Doğru İletişim Yöntemi (✔)', 10.1, YESIL_K)
    ic += yazi(91, 44, 'Kısa Mesaj (SMS) ve İnternet', 9.7, LAC)
    ic += yazi(91, 65, 'Hatları meşgul etmez!', 9.4, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'Yanlış İletişim Davranışı (✘)', 10.1, KIR)
    ic += yazi(269, 44, 'Uzun Sesli Telefon Aramaları', 9.7, LAC)
    ic += yazi(269, 65, '112 Acil hattına erişimi kilitler!', 9.4, KIR, ince=True)
    return svg(360, 88, ic, 'Afet sonrasında doğru ve yanlış telefon kullanımı kartı.', 15)


def aile_deprem_zaman_akisi():
    adimlar = [
        ('A · Hazırlık', 'Eşya sabitle & Çanta', MAVI, MAVI_A),
        ('B · Sarsıntı', 'Çök-Kapan-Tutun', TUR, TUR_A),
        ('C · Vanalar', 'Gaz ve elektriği kes', YES, YES_A),
        ('D · Tahliye', 'Toplanma alanına git', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 55, met, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Deprem öncesi, sırası ve sonrasında yapılacaklar akışı.', 15)


def evimiz_dunya_ozet_panosu():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, '2. ÖĞRENME ALANI · EVİMİZ DÜNYA DEĞERLENDİRME PANOSU', 10.2, MAVI)
    ic += yazi(180, 44, '• Göreceli Konum: Türkiye; Asya, Avrupa ve Afrika’nın kesişim noktasındadır.', 9.5, LAC)
    ic += yazi(180, 61, '• Çevre: Beşerî yapılar doğal çevreye zarar vermeden sürdürülebilir yapılmalıdır.', 9.5, YESIL_K)
    ic += yazi(180, 76, '• Afet Bilinci: Doğa olayları engellenemez fakat önlemlerle can kaybı önlenir.', 9.4, MAVI, ince=True)
    return svg(360, 88, ic, 'Evimiz Dünya öğrenme alanı değerlendirme panosu.', 15)


def heyelan_erozyon_farki_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Olay · Erozyon', 10.3, TUR)
    ic += yazi(91, 44, 'Üst toprağın yavaş aşınması', 9.6, LAC)
    ic += yazi(91, 65, 'Çözüm: Ağaçlandırma (TEMA)', 9.4, TUR, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Olay · Heyelan', 10.3, MOR)
    ic += yazi(269, 44, 'Yamaç kütlesinin ani kayması', 9.6, LAC)
    ic += yazi(269, 65, 'Neden: Dik eğim, yağış, kil', 9.4, MOR, ince=True)
    return svg(360, 88, ic, 'Erozyon ve heyelan olaylarının karşılaştırma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = deprem_asamalari_dort_kart()
    s[2]['gorsel'] = cevre_ve_afet_bolge_kartlari()
    s[5]['gorsel'] = afet_cantasi_paket_secimi()
    s[6]['gorsel'] = iki_il_cografi_afet_karti()
    s[7]['gorsel'] = afet_sonrasi_iletisim_karti()
    s[8]['gorsel'] = aile_deprem_zaman_akisi()
    s[9]['gorsel'] = evimiz_dunya_ozet_panosu()
    s[11]['gorsel'] = heyelan_erozyon_farki_karti()
