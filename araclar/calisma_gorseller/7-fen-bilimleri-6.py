"""7. sınıf Fen Bilimleri 6. hafta (İşin Bağlı Olduğu Değişkenler, İş ve Enerji İlişkisi) çalışma kâğıdı görselleri.
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


def kuvvet_degisken_deneyi():
    ic = f'<rect x="8" y="6" width="282" height="92" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Deney Düzeneği (Yol Sabit = 2 m)', 12, MAVI)
    ic += f'<rect x="28" y="42" width="56" height="32" rx="4" fill="#fde68a" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(56, 62, 'Kutu', 12, LAC)
    ic += f'<line x1="84" y1="58" x2="148" y2="58" stroke="{KIR}" stroke-width="2.2"/>'
    ic += f'<rect x="148" y="48" width="68" height="20" rx="4" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(182, 62, '5N - 15N', 12, MAVI)
    ic += yazi(149, 88, 'Ağırlık eklendikçe kuvvet artıyor', 12, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="92" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Ölçüm Sonuçları Tablosu', 12, YES)
    ic += yazi(451, 48, '1. Deneme : F = 5 N  · x = 2 m · W = 10 J', 12, LAC, ince=True)
    ic += yazi(451, 68, '2. Deneme : F = 10 N · x = 2 m · W = 20 J', 12, LAC, ince=True)
    ic += yazi(451, 88, '3. Deneme : F = 15 N · x = 2 m · W = 30 J', 12, LAC, ince=True)
    return svg(600, 104, ic, 'Yol sabitken kuvvetin değiştirildiği iş deneyi ve tablosu.', 20)


def is_enerji_aktarim_kartlari():
    kartlar = [
        ('1. Duran topa vurma', 'Top hızlanır', MAVI, MAVI_A),
        ('2. Vinçle yük çekme', 'Yük yükselir', TUR, TUR_A),
        ('3. Su değirmeni', 'Çark döner', CAM, CAM_A),
        ('4. Sıkışmış yay', 'Araba fırlar', YES, YES_A),
    ]
    ic = ''
    for i, (no, ad, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, no, 12, renk)
        ic += yazi(x + 70, 56, ad, 12, LAC, ince=True)
    return svg(600, 84, ic, 'İş yoluyla enerji aktarımını gösteren dört olay kartı.', 19)


def klm_is_veri_tablosu():
    satirlar = [
        ('K Denemesi', 'Kuvvet: 6 N', 'Yol: 2 m', 'İş = 12 J', MAVI, MAVI_A),
        ('L Denemesi', 'Kuvvet: 6 N', 'Yol: 6 m', 'İş = 36 J', YES, YES_A),
        ('M Denemesi', 'Kuvvet: 18 N', 'Yol: 6 m', 'İş = 108 J', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, f_str, x_str, w_str, renk, arka) in enumerate(satirlar):
        x = 8 + i * 198
        ic += f'<rect x="{x}" y="6" width="188" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 94, 26, ad, 12, renk)
        ic += yazi(x + 94, 48, f'{f_str} · {x_str}', 12, LAC, ince=True)
        ic += yazi(x + 94, 72, w_str, 12, renk)
    return svg(600, 96, ic, 'K, L ve M denemelerinde kuvvet, yol ve yapılan iş verileri.', 20)


def vinc_sandik_svg():
    ic = f'<rect x="8" y="6" width="584" height="90" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += f'<rect x="44" y="16" width="90" height="10" rx="3" fill="{LAC}"/>'
    ic += f'<line x1="110" y1="26" x2="110" y2="54" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<rect x="86" y="54" width="48" height="30" rx="4" fill="#fde68a" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(110, 73, '400 N', 12, LAC)
    ic += yazi(220, 42, 'Yükseklik (Yol): h = 5 m', 12, MAVI)
    ic += yazi(220, 68, 'Uygulanan Kuvvet: F = 400 N', 12, TUR)
    ic += f'<rect x="356" y="18" width="220" height="66" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(466, 42, 'Yapılan İş (W) = ? Joule', 12, YES)
    ic += yazi(466, 66, 'Kazanılan Enerji = ? Joule', 12, KIR)
    return svg(600, 102, ic, '400 N ağırlığındaki sandığı 5 m yükselten vinç düzeneği.', 20)


def duran_ve_yuvarlanan_top():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Durum · Hareketsiz Top', 12, KIR)
    ic += f'<circle cx="52" cy="60" r="13" fill="{KIR}"/><rect x="92" y="46" width="36" height="28" rx="3" fill="#fde68a" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(205, 54, 'Sürat = 0 · Enerji yok', 12, LAC, ince=True)
    ic += yazi(205, 76, 'Kutuyu itemez (İş = 0)', 12, KIR)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Durum · Hızla Yuvarlanan Top', 12, YES)
    ic += f'<circle cx="348" cy="60" r="13" fill="{YES}"/><rect x="404" y="46" width="36" height="28" rx="3" fill="#fde68a" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(516, 54, 'Kinetik enerji var', 12, LAC, ince=True)
    ic += yazi(516, 76, 'Kutuyu 3 m iter (İş yapar)', 12, YES)
    return svg(600, 100, ic, 'Hareketsiz ve yuvarlanan topun kutuya etkisi karşılaştırması.', 20)


def yol_hipotezi_adimlari():
    adimlar = [
        ('1. Adım', 'Kuvveti 10 N sabit tut', MAVI, MAVI_A),
        ('2. Adım', 'Yolu 1m, 2m, 3m değiştir', TUR, TUR_A),
        ('3. Adım', 'İşleri 10J, 20J, 30J bul', MOR, MOR_A),
        ('4. Adım', 'Doğru orantıyı doğrula', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'İşin yola bağlılığı hipotezini test etme adımları.', 19)


def dort_enerji_turu_karti():
    kartlar = [
        ('1. Kart', 'Dönen değirmen kanadı', MAVI, MAVI_A),
        ('2. Kart', 'Hızla akan nehir suyu', CAM, CAM_A),
        ('3. Kart', 'Pistte koşan atlet', YES, YES_A),
        ('4. Kart', 'Üst rafta duran vazo', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="74" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, acik, 12, LAC, ince=True)
    return svg(600, 86, ic, 'Üçü kinetik biri potansiyel enerjiye sahip dört cisim kartı.', 19)


def koli_tutma_kaldirma_svg():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Durum · Koliyi Sabit Tutma', 12, KIR)
    ic += yazi(149, 50, 'Kuvvet var · Yer değiştirme x = 0', 12, LAC, ince=True)
    ic += yazi(149, 74, 'Enerji harcanır ama iş yapılmaz', 12, KIR)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Durum · Koliyi Rafa Kaldırma', 12, YES)
    ic += yazi(451, 50, 'Yukarı kuvvet · Yukarı yer değiştirme', 12, LAC, ince=True)
    ic += yazi(451, 74, 'İş yapılır ve koliye enerji aktarılır', 12, YES)
    return svg(600, 100, ic, 'Koliyi sabit tutma ve rafa kaldırma durumlarında iş karşılaştırması.', 20)


def enerji_kaynak_eslestirme():
    satirlar = [
        ('1. Satır', 'Bacak kasları', 'Elektrik (Yanlış)', KIR_A, KIR),
        ('2. Satır', 'Asansör motoru', 'Besinler (Yanlış)', TUR_A, TUR),
        ('3. Satır', 'Yel değirmeni', 'Rüzgâr (Doğru)', YES_A, YES),
        ('4. Satır', 'Kamyon motoru', 'Durgun su (Yanlış)', MOR_A, MOR),
    ]
    ic = ''
    for i, (no, arac, kaynak, arka, renk) in enumerate(satirlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="84" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 26, no, 12, renk)
        ic += yazi(x + 70, 50, arac, 12, LAC, ince=True)
        ic += yazi(x + 70, 74, kaynak, 12, renk)
    return svg(600, 96, ic, 'Günlük yaşamda iş yapan sistemler ve enerji kaynakları kartları.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kuvvet_degisken_deneyi()
    s[1]['gorsel'] = is_enerji_aktarim_kartlari()
    s[3]['gorsel'] = klm_is_veri_tablosu()
    s[4]['gorsel'] = vinc_sandik_svg()
    s[6]['gorsel'] = duran_ve_yuvarlanan_top()
    s[7]['gorsel'] = yol_hipotezi_adimlari()
    s[8]['gorsel'] = dort_enerji_turu_karti()
    s[11]['gorsel'] = koli_tutma_kaldirma_svg()
    s[12]['gorsel'] = enerji_kaynak_eslestirme()
