"""5. sınıf Sosyal Bilgiler 9. hafta (Yaşadığımız İlde Doğal ve Beşerî Çevredeki Değişim, Sürdürülebilir Çevre) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def camlibel_elli_yil_degisim():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Çamlıbel · 1975 Fotoğrafı', 10.2, YESIL_K)
    ic += yazi(91, 44, '• Geniş çam ormanları ve ova', 9.7, LAC, ince=True)
    ic += yazi(91, 64, '• Tek şeritli toprak yol, az ev', 9.7, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'Çamlıbel · 2026 Fotoğrafı', 10.2, MAVI)
    ic += yazi(269, 44, '• Çok katlı konutlar, fabrikalar', 9.7, LAC, ince=True)
    ic += yazi(269, 64, '• Otoyol tüneli, viyadük ve baraj', 9.7, MAVI)
    return svg(360, 88, ic, 'Çamlıbel ilinin 1975 ve 2026 yıllarındaki çevresel görünümü.', 15)


def dort_cevre_uygulamasi():
    kartlar = [
        ('1. Dağa Tünel', 'Hızlı ulaşım', YES, YES_A),
        ('2. Ovaya Konut', 'Tarım kaybı', KIR, KIR_A),
        ('3. Su Arıtma', 'Temiz nehir', MAVI, MAVI_A),
        ('4. Dereye Yol', 'Taşkın riski', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, 'Dört çevresel müdahale ve sonuç kartı.', 15)


def belediye_yatirim_onerileri():
    oneriler = [
        ('1. Güneş Paneli', 'Temiz enerji üretimi', YES, YES_A),
        ('2. Deltaya Fabrika', 'Sulak alanı kurutma', KIR, KIR_A),
        ('3. Biyolojik Arıtma', 'Atık suları temizleme', MAVI, MAVI_A),
        ('4. Kent Ormanı', 'Kıraç tepeye fidan', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(oneriler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, alt, 9.5, LAC, ince=True)
    return svg(360, 94, ic, 'Belediye meclisine sunulan dört çevre ve yatırım önerisi.', 16)


def baraj_oncesi_sonrasi():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'Baraj Öncesi Akarsu Vadisi', 10.1, TUR)
    ic += yazi(91, 44, '• Dar vadide akan coşkun nehir', 9.6, LAC, ince=True)
    ic += yazi(91, 64, '• Vadi tabanında eski yol ve ağaçlar', 9.4, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 22, 'Baraj Sonrası Görünüm', 10.1, CAM)
    ic += yazi(269, 44, '• Geniş baraj gölü ve elektrik üretimi', 9.5, LAC, ince=True)
    ic += yazi(269, 64, '• Vadi tabanı su altında kaldı', 9.5, CAM)
    return svg(360, 88, ic, 'Akarsu vadisine baraj yapılmadan önceki ve sonraki değişim.', 15)


def dere_yatagi_taskin_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, 'Hatalı Yerleşim (Riskli)', 10.2, KIR)
    ic += yazi(91, 44, 'Dere yatağı doldurulup', 9.8, LAC, ince=True)
    ic += yazi(91, 64, 'üzerine bina ve yol yapıldı', 9.8, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Doğru Planlama (Güvenli)', 10.2, YESIL_K)
    ic += yazi(269, 44, 'Dere yatağı açık bırakılıp', 9.8, LAC, ince=True)
    ic += yazi(269, 64, 'çevresi yeşil kuşakla korundu', 9.8, YESIL_K)
    return svg(360, 88, ic, 'Dere yatağının kapatılması ve korunması karşılaştırması.', 15)


def cevre_cozum_akis_kartlari():
    adimlar = [
        ('A Adımı', 'Bilimsel rapor hazırlama', MAVI, MAVI_A),
        ('B Adımı', 'Kirliliğin ortaya çıkması', KIR, KIR_A),
        ('C Adımı', 'Doğanın yeniden iyileşmesi', YES, YES_A),
        ('D Adımı', 'Filtre ve arıtma kurulumu', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 55, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Çevre sorununun tespiti ve sürdürülebilir çözümü adımları.', 15)


def ekolojik_denge_panosu():
    ic = kutu(6, 6, 348, 78, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Ekolojik Denge ve Sürdürülebilir Kentleşme İlkeleri', 10.4, MAVI)
    ic += yazi(180, 42, '• İnsanların inşa ettiği her yapı doğal çevrede değişim meydana getirir.', 9.6, LAC, ince=True)
    ic += yazi(180, 58, '• Madencilik ve yol inşası sonrası bozulan yamaçlar ağaçlandırılmalıdır.', 9.6, LAC, ince=True)
    ic += yazi(180, 74, '• Su tasarrufu ve geri dönüşüm doğal kaynakların ömrünü uzatır.', 9.6, YESIL_K)
    return svg(360, 90, ic, 'Ekolojik denge ve sürdürülebilir kentleşme ilkeleri panosu.', 15)


def gelecek_kusak_gorev_karti():
    ic = kutu(6, 6, 348, 74, YES_A, YES)
    ic += yazi(180, 22, 'Sürdürülebilir Çevre · Vatandaşlık Sorumluluğumuz', 10.4, YESIL_K)
    ic += yazi(180, 44, '«Doğayı atalarımızdan miras değil, gelecek kuşaklardan emanet aldık.»', 9.8, LAC)
    ic += yazi(180, 64, 'Hedef: Sıfır Atık · Su ve Enerji Tasarrufu · Yeşil Alanları Korumak', 9.6, YESIL_K, ince=True)
    return svg(360, 86, ic, 'Sürdürülebilir çevre için bireysel sorumluluk kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = camlibel_elli_yil_degisim()
    s[2]['gorsel'] = dort_cevre_uygulamasi()
    s[5]['gorsel'] = belediye_yatirim_onerileri()
    s[6]['gorsel'] = baraj_oncesi_sonrasi()
    s[7]['gorsel'] = dere_yatagi_taskin_karti()
    s[8]['gorsel'] = cevre_cozum_akis_kartlari()
    s[9]['gorsel'] = ekolojik_denge_panosu()
    s[11]['gorsel'] = gelecek_kusak_gorev_karti()
