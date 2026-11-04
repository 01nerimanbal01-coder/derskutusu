"""7. sınıf Fen Bilimleri 8. hafta (Kinetik-Potansiyel Enerji, Enerji Dönüşümleri, Hava ve Su Direnci) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
GRI, CAM, CAM_A = '#9aa6bd', '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def sarkac_klm_svg():
    ic = f'<rect x="8" y="6" width="584" height="108" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<rect x="140" y="12" width="120" height="8" rx="3" fill="{LAC}"/>'
    ic += f'<line x1="200" y1="20" x2="105" y2="70" stroke="{TUR}" stroke-width="2" stroke-dasharray="4 3"/>'
    ic += f'<line x1="200" y1="20" x2="200" y2="92" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<line x1="200" y1="20" x2="295" y2="70" stroke="{TUR}" stroke-width="2" stroke-dasharray="4 3"/>'
    ic += f'<circle cx="105" cy="70" r="14" fill="{TUR}"/><circle cx="200" cy="92" r="14" fill="{MAVI}"/><circle cx="295" cy="70" r="14" fill="{TUR}"/>'
    ic += yazi(105, 74, 'K', 12, '#fff')
    ic += yazi(200, 96, 'L', 12, '#fff')
    ic += yazi(295, 74, 'M', 12, '#fff')
    ic += yazi(72, 102, 'En Üst (h maks)', 12, TUR)
    ic += yazi(200, 110, 'En Alt (v maks)', 12, MAVI)
    ic += f'<rect x="356" y="18" width="222" height="84" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(467, 38, 'Sürtünmesiz Sarkaç', 12, YES)
    ic += yazi(467, 60, 'K ve M : Ep en büyük, Ek = 0', 12, LAC, ince=True)
    ic += yazi(467, 82, 'L noktası : Ek en büyük, Ep en az', 12, LAC, ince=True)
    return svg(600, 120, ic, 'Sürtünmesiz K-L-M sarkacında enerji dönüşümü.', 21)


def enerji_olay_kartlari():
    kartlar = [
        ('1. Olay', 'Daldan düşen elma', YES, YES_A),
        ('2. Olay', 'Yaydan fırlayan araba', TUR, TUR_A),
        ('3. Olay', 'Yukarı atılan top', MAVI, MAVI_A),
        ('4. Olay', 'Fren yapan otomobil', KIR, KIR_A),
    ]
    ic = ''
    for i, (no, ad, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, no, 12, renk)
        ic += yazi(x + 70, 56, ad, 12, LAC, ince=True)
    return svg(600, 84, ic, 'Dört günlük yaşam olayında enerji dönüşümü kartları.', 19)


def enerji_korunum_grafik():
    ic = f'<rect x="8" y="6" width="280" height="96" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(148, 26, 'Başlangıç Konumu (En Üst)', 12, MAVI)
    ic += yazi(148, 50, 'Çekim Potansiyel (Ep) = 120 J', 12, LAC, ince=True)
    ic += yazi(148, 70, 'Kinetik Enerji (Ek) = 0 J', 12, LAC, ince=True)
    ic += yazi(148, 90, 'Mekanik Enerji (Em) = 120 J', 12, YES)

    ic += f'<rect x="312" y="6" width="280" height="96" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(452, 26, 'X Konumu (Yolun Ortası)', 12, TUR)
    ic += yazi(452, 50, 'Çekim Potansiyel (Ep) = ? J', 12, KIR)
    ic += yazi(452, 70, 'Kinetik Enerji (Ek) = 60 J', 12, LAC, ince=True)
    ic += yazi(452, 90, 'Mekanik Enerji (Em) = ? J', 12, KIR)
    return svg(600, 108, ic, 'Sürtünmesiz ortamda düşen topun başlangıç ve X noktası enerji tablosu.', 21)


def kagit_direnci_deneyi():
    ic = f'<rect x="8" y="6" width="280" height="92" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(148, 28, '1. Kâğıt · Buruşturulmuş Top', 12, YES)
    ic += f'<circle cx="60" cy="62" r="16" fill="#fff" stroke="{YES}" stroke-width="2"/>'
    ic += yazi(178, 56, 'Temas yüzeyi küçük', 12, LAC, ince=True)
    ic += yazi(178, 78, 'Hava direnci: AZ', 12, YES)

    ic += f'<rect x="312" y="6" width="280" height="92" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(452, 28, '2. Kâğıt · Düz ve Geniş Yaprak', 12, TUR)
    ic += f'<rect x="332" y="50" width="64" height="18" rx="3" fill="#fff" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(492, 56, 'Temas yüzeyi geniş', 12, LAC, ince=True)
    ic += yazi(492, 78, 'Hava direnci: FAZLA', 12, KIR)
    return svg(600, 104, ic, 'Buruşturulmuş ve düz dosya kâğıdının hava direnci karşılaştırması.', 20)


def dort_tasarim_karti():
    kartlar = [
        ('1. Tasarım', 'Hızlı tren sivri burun', MAVI, MAVI_A),
        ('2. Tasarım', 'Geniş kubbeli paraşüt', TUR, TUR_A),
        ('3. Tasarım', 'V pruvalı gemi gövdesi', CAM, CAM_A),
        ('4. Tasarım', 'Sivri ok biçimli dalış', YES, YES_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="74" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, acik, 12, LAC, ince=True)
    return svg(600, 86, ic, 'Hava ve su direncine yönelik dört tasarım kartı.', 19)


def yayli_rampa_parkuru():
    adimlar = [
        ('1. Aşama', 'Sıkışmış Yay (Ep)', MOR, MOR_A),
        ('2. Aşama', 'Fırlayan Bilye (Ek)', MAVI, MAVI_A),
        ('3. Aşama', 'Rampa Çıkışı (Ep)', TUR, TUR_A),
        ('4. Aşama', 'Sürtünme ve Isı', KIR, KIR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'Yaylı rampa parkurunda dört aşamalı enerji dönüşümü.', 19)


def kinetik_potansiyel_pano():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'KİNETİK ENERJİ (Ek)', 12, MAVI)
    ic += yazi(149, 48, 'Kaynağı: Cismin hareketi', 12, LAC, ince=True)
    ic += yazi(149, 68, 'Değişkenler: Kütle (m) ve Sürat (v)', 12, LAC, ince=True)
    ic += yazi(149, 86, 'Birim: Joule (J)', 12, MAVI)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'POTANSİYEL ENERJİ (Ep)', 12, YES)
    ic += yazi(451, 48, 'Kaynağı: Konum veya esnek durum', 12, LAC, ince=True)
    ic += yazi(451, 68, 'Çekim: Ağırlık - Yükseklik · Yay: Sıkışma', 12, LAC, ince=True)
    ic += yazi(451, 86, 'Birim: Joule (J)', 12, YES)
    return svg(600, 100, ic, 'Kinetik ve potansiyel enerji karşılaştırma panosu.', 20)


def hava_su_borulari_svg():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<rect x="28" y="16" width="36" height="68" rx="6" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<circle cx="46" cy="56" r="9" fill="{TUR}"/>'
    ic += yazi(176, 32, '1. Boru · Hava Ortamı', 12, MAVI)
    ic += yazi(176, 54, 'Tanecikler seyrek', 12, LAC, ince=True)
    ic += yazi(176, 74, 'Direnç kuvveti daha küçük', 12, YES)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += f'<rect x="330" y="16" width="36" height="68" rx="6" fill="#bae6fd" stroke="{CAM}" stroke-width="1.6"/>'
    ic += f'<circle cx="348" cy="34" r="9" fill="{TUR}"/>'
    ic += yazi(478, 32, '2. Boru · Su Ortamı', 12, CAM)
    ic += yazi(478, 54, 'Tanecikler yoğun', 12, LAC, ince=True)
    ic += yazi(478, 74, 'Direnç kuvveti daha büyük', 12, KIR)
    return svg(600, 100, ic, 'Hava ve su dolu özdeş cam borularda bilye düşüşü.', 20)


def surtunmeli_egik_duzlem():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += f'<polygon points="36,84 36,24 260,84" fill="#fde68a" stroke="{TUR}" stroke-width="1.8"/>'
    ic += f'<rect x="74" y="22" width="32" height="20" rx="3" transform="rotate(15 74 22)" fill="{MAVI}"/>'
    ic += yazi(52, 20, 'P', 12, KIR)
    ic += yazi(272, 84, 'R', 12, KIR)
    ic += yazi(430, 32, 'Pürüzlü (Sürtünmeli) Eğik Düzlem', 12, TUR)
    ic += yazi(430, 56, 'P -> R inerken ısı enerjisi açığa çıkar', 12, LAC, ince=True)
    ic += yazi(430, 78, 'Mekanik enerji: ?  ·  Toplam enerji: ?', 12, KIR)
    return svg(600, 104, ic, 'Pürüzlü eğik düzlemde P noktasından R noktasına kayan blok.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sarkac_klm_svg()
    s[1]['gorsel'] = enerji_olay_kartlari()
    s[3]['gorsel'] = enerji_korunum_grafik()
    s[4]['gorsel'] = kagit_direnci_deneyi()
    s[6]['gorsel'] = dort_tasarim_karti()
    s[7]['gorsel'] = yayli_rampa_parkuru()
    s[8]['gorsel'] = kinetik_potansiyel_pano()
    s[11]['gorsel'] = hava_su_borulari_svg()
    s[12]['gorsel'] = surtunmeli_egik_duzlem()
