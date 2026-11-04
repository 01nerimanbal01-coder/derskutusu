"""7. sınıf Sosyal Bilgiler 8. hafta (Bölgesel ve Küresel Sorunların Çözümünde Türkiye'nin Rolü ve Uluslararası Kuruluşlar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
CAM, CAM_A = '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def bm_uzmanlik_panosu():
    kartlar = [
        ('1 · UNICEF', 'Çocuk hakları ve eğitimi', MAVI, MAVI_A),
        ('2 · FAO', 'Gıda, tarım ve açlıkla mücadele', YES, YES_A),
        ('3 · UNESCO', 'Bilim, kültür ve dünya mirası', MOR, MOR_A),
        ('4 · WHO (DSÖ)', 'Salgınlar ve küresel sağlık', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="286" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 56, y + 27, bas, 12, renk)
        ic += f'<line x1="{x + 110}" y1="{y + 6}" x2="{x + 110}" y2="{y + 38}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 198, y + 27, acik, 12, LAC, ince=True)
    return svg(600, 106, ic, 'Birleşmiş Milletler dört uzmanlık kuruluşu panosu.', 20)


def turkiye_girisim_kartlari():
    kartlar = [
        ('Sıfır Atık', '30 Mart BM Günü', YES, YES_A),
        ('Tahıl Koridoru', 'Gıda Güvenliği', TUR, TUR_A),
        ('AFAD - Kızılay - TİKA', 'İnsani Yardım', KIR, KIR_A),
        ('Paris Anlaşması', '2053 Net Sıfır', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, alt, 12, LAC, ince=True)
    return svg(600, 84, ic, 'Türkiye’nin dört küresel girişim kartı.', 19)


def iklim_zinciri_svg():
    adimlar = [
        ('1. Neden', 'Fosil Yakıtlar', TUR, TUR_A),
        ('2. Süreç', 'Sera Gazı Artışı', MOR, MOR_A),
        ('3. Etki', 'Küresel Isınma', KIR, KIR_A),
        ('4. Sonuç', '? (İklim Krizi)', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'Küresel iklim değişikliği neden-sonuç zinciri.', 19)


def sifir_atik_rozet_svg():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'BM GENEL KURULU KARARI : 30 MART ULUSLARARASI SIFIR ATIK GÜNÜ', 12, YES)
    ic += yazi(160, 54, 'Öncü Ülke : Türkiye', 12, LAC)
    ic += f'<line x1="290" y1="36" x2="290" y2="80" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(440, 50, 'Hedef : İsrafı önlemek, atığı azaltmak', 12, LAC, ince=True)
    ic += yazi(440, 72, 've geri dönüşümü yaygınlaştırmak', 12, LAC, ince=True)
    return svg(600, 98, ic, '30 Mart Uluslararası Sıfır Atık Günü bilgi kartı.', 20)


def insani_diplomasi_pano():
    ic = f'<rect x="8" y="6" width="584" height="90" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'TÜRKİYE’NİN İNSANİ DİPLOMASİ VE BARIŞ PANOSU', 12, TUR)
    ic += yazi(155, 52, 'İlke : «Yurtta barış, dünyada barış»', 12, LAC)
    ic += yazi(450, 52, 'Kurumlar : AFAD · Türk Kızılay · TİKA', 12, KIR)
    ic += yazi(155, 76, 'Arabuluculuk : Barış ve Tahıl Koridoru', 12, LAC, ince=True)
    ic += yazi(450, 76, 'Kapsam : Tüm mazlum coğrafyalara destek', 12, YES)
    return svg(600, 102, ic, 'Türkiye’nin insani diplomasi ve barış panosu.', 20)


def kriz_cozum_akisi_svg():
    adimlar = [
        ('1. Aşama', 'Kuraklık - Çatışma', KIR, KIR_A),
        ('2. Aşama', 'Zorunlu Göç Dalgası', TUR, TUR_A),
        ('3. Aşama', 'Küresel Boyut', MOR, MOR_A),
        ('4. Aşama', 'Uluslararası Çözüm', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'Bölgesel krizden küresel çözüme dört aşamalı akış şeması.', 19)


def iklim_cozum_panosu():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'İKLİM DOSTU VE SÜRDÜRÜLEBİLİR ÇÖZÜMLER PANOSU', 12, CAM)
    ic += yazi(155, 52, '1 · Güneş ve rüzgâr enerjisine geçiş', 12, YES)
    ic += yazi(450, 52, '2 · Ormanların korunması ve ağaçlandırma', 12, YES)
    ic += yazi(155, 74, '3 · Sanayi baca filtreleri ve Sıfır Atık', 12, YES)
    ic += yazi(450, 74, '4 · Karbon ayak izinin azaltılması', 12, MAVI)
    return svg(600, 98, ic, 'İklim dostu çözümler panosu.', 20)


def kuresel_vatandas_karti():
    ic = f'<rect x="8" y="6" width="282" height="84" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 28, '1. Sorumluluk · Su ve Enerji', 12, MAVI)
    ic += yazi(149, 52, 'Muslukları ve lambaları', 12, LAC, ince=True)
    ic += yazi(149, 72, 'tasarruflu kullanmak', 12, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="84" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 28, '2. Sorumluluk · Doğa ve Atık', 12, YES)
    ic += yazi(451, 52, 'Geri dönüşüm kutularını kullanmak', 12, LAC, ince=True)
    ic += yazi(451, 72, 've fidan dikimine katılmak', 12, LAC, ince=True)
    return svg(600, 96, ic, 'Küresel vatandaşlık bireysel sorumluluk kartları.', 20)


def dort_kurulus_sema():
    kartlar = [
        ('NATO', 'Ortak savunma ve güvenlik', MAVI, MAVI_A),
        ('UNICEF', 'Dünya çocuklarına yardım', MOR, MOR_A),
        ('KEİ', 'Karadeniz ekonomik iş birliği', TUR, TUR_A),
        ('WHO', 'Küresel sağlık çalışmaları', YES, YES_A),
    ]
    ic = ''
    for i, (ad, acik, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, ad, 12, renk)
        ic += yazi(x + 70, 56, acik, 12, LAC, ince=True)
    return svg(600, 84, ic, 'Türkiye’nin üyesi olduğu dört uluslararası kuruluş kartı.', 19)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bm_uzmanlik_panosu()
    s[1]['gorsel'] = turkiye_girisim_kartlari()
    s[3]['gorsel'] = iklim_zinciri_svg()
    s[4]['gorsel'] = sifir_atik_rozet_svg()
    s[6]['gorsel'] = insani_diplomasi_pano()
    s[7]['gorsel'] = kriz_cozum_akisi_svg()
    s[8]['gorsel'] = iklim_cozum_panosu()
    s[11]['gorsel'] = kuresel_vatandas_karti()
    s[12]['gorsel'] = dort_kurulus_sema()
