"""7. sınıf Fen Bilimleri 5. hafta (Fiziksel Anlamda İş, İşin Koşulları ve Hesaplanması) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); eğik kesir yok (K155); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_durum_is_karti():
    """Soru 1: 4 farklı durumda kuvvet ve hareket doğrultusu kartları."""
    kartlar = [
        ('1. Bebek Arabası İtme', 'Kuvvet: → · Hareket: →', YES, YES_A),
        ('2. Duvarı İtme', 'Kuvvet: → · Hareket: Yok', KIR, KIR_A),
        ('3. Kovayı Kuyudan Çekme', 'Kuvvet: ↑ · Hareket: ↑', MAVI, MAVI_A),
        ('4. Elde Çantayla Yürüme', 'Kuvvet: ↑ · Hareket: →', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Dört farklı olayda kuvvet ve hareket doğrultularını gösteren kartlar.', 16)


def is_hesaplama_olcum_kartlari():
    """Soru 2: Kuvvet ve yol ölçüm kartları."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Fiziksel Anlamda İş Bağıntısı: W = F · x', KAHVE)
    kartlar = [
        ('Kuvvet (F)', 'Birim: Newton (N)', MAVI, MAVI_A, 10),
        ('Alınan Yol (x)', 'Birim: Metre (m)', TUR, TUR_A, 126),
        ('Yapılan İş (W)', 'Birim: Joule (J)', YES, YES_A, 242),
    ]
    for bas, alt, r, z, x in kartlar:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Kuvvet, alınan yol ve yapılan işin birimlerini gösteren şema.', 16)


def xyz_vagon_verileri():
    """Soru 4: X, Y ve Z vagonlarına uygulanan kuvvet ve alınan yol kartları."""
    vagonlar = [
        ('X Vagonu', 'F = 20 N', 'x = 3 m', MAVI, MAVI_A, 6),
        ('Y Vagonu', 'F = 15 N', 'x = 3 m', TUR, TUR_A, 126),
        ('Z Vagonu', 'F = 20 N', 'x = 5 m', YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 88, '#f8fafc', GRI, 8, 1.3)
    for ad, f_s, x_s, r, z, x in vagonlar:
        ic += kutu(x, 10, 108, 76, z, r, 7, 1.4)
        ic += yazi(x + 54, 28, ad, r)
        ic += yazi(x + 54, 50, f_s, LAC)
        ic += yazi(x + 54, 72, x_s, LAC, 'middle', True)
    return svg(360, 96, ic, 'X, Y ve Z vagonlarına uygulanan kuvvet ve alınan yol değerleri.', 16)


def paket_rafa_kaldirma_sema():
    """Soru 5: 30 N paketi 120 cm yüksekliğe kaldırma şeması."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Depo Rafına Paket Kaldırma (100 cm = 1 m)', YESIL_K)
    ic += kutu(14, 28, 158, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 47, 'Paket Ağırlığı (Kuvvet)', MAVI)
    ic += yazi(93, 67, 'F = 30 N (Yukarı ↑)', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(267, 47, 'Raf Yüksekliği (Yol)', TUR)
    ic += yazi(267, 67, 'h = 120 cm (Yukarı ↑)', LAC, 'middle', True)
    return svg(360, 94, ic, 'Otuz Newton ağırlığındaki paketin yüz yirmi santimetre yüksekliğe çıkarılması.', 16)


def halter_iki_asama_karti():
    """Soru 7: Halter kaldırma ve sabit tutma 2 aşama karşılaştırması."""
    ic = kutu(4, 4, 172, 88, YES_A, YES, 8, 1.4)
    ic += yazi(90, 22, '1. Aşama · Kaldırma', YESIL_K)
    ic += yazi(90, 45, 'Kuvvet: F = 500 N (↑)', LAC, 'middle', True)
    ic += yazi(90, 64, 'Yol: h = 2 m (↑)', LAC, 'middle', True)
    ic += yazi(90, 82, 'İş = 1000 Joule', YESIL_K)

    ic += kutu(184, 4, 172, 88, KIR_A, KIR, 8, 1.4)
    ic += yazi(270, 22, '2. Aşama · Sabit Tutma', KIR)
    ic += yazi(270, 45, 'Kuvvet: F = 500 N (↑)', LAC, 'middle', True)
    ic += yazi(270, 64, 'Yol: x = 0 m (Hareketsiz)', LAC, 'middle', True)
    ic += yazi(270, 82, 'İş = 0 Joule', KIR)
    return svg(360, 96, ic, 'Halterin kaldırılması ve sabit tutulması aşamalarında yapılan iş karşılaştırması.', 16)


def dinamometre_deney_adimlari():
    """Soru 8: Dinamometre ve metre ile iş ölçümü 4 adım."""
    adimlar = [
        ('1. Çekme', 'Sabit süratle çek', MAVI, MAVI_A, 6),
        ('2. Kuvvet', 'Dinamometreyi oku', TUR, TUR_A, 94),
        ('3. Mesafe', 'Metreyle yolu ölç', MOR, MOR_A, 182),
        ('4. Hesap', 'W = F · x çarp', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Dinamometre ve metre kullanarak yapılan işi belirleme basamakları.', 15)


def kl_is_yol_grafigi():
    """Soru 9: K (İş=60 J, Yol=3 m -> F_K=20 N) ve L (İş=40 J, Yol=4 m -> F_L=10 N) sütun tablosu."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'K ve L Cisimlerine Ait İş – Yol Verileri (F = W ÷ x)', MAVI)
    ic += kutu(14, 28, 158, 54, '#fff', MAVI, 6, 1.3)
    ic += yazi(93, 46, 'K Cismi Verileri', MAVI)
    ic += yazi(93, 68, 'İş = 60 J · Yol = 3 m', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 54, '#fff', TUR, 6, 1.3)
    ic += yazi(267, 46, 'L Cismi Verileri', TUR)
    ic += yazi(267, 68, 'İş = 40 J · Yol = 4 m', LAC, 'middle', True)
    return svg(360, 96, ic, 'K ve L cisimlerine yapılan iş ve alınan yol değerleri kartı.', 16)


def dik_dogrultu_sepet_karti():
    """Soru 12: Elde taşınan sepette kuvvet ve hareket doğrultularının dik olması."""
    ic = kutu(4, 4, 352, 86, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, 'Doğrultu Analizi: Elde Sepet Taşıyarak Düz Yürüme', KIR)
    ic += kutu(14, 28, 158, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Uygulanan Kuvvet Yönü', MAVI)
    ic += yazi(93, 66, 'Düşey Yukarı (↑ 25 N)', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(267, 46, 'Yer Değiştirme Yönü', TUR)
    ic += yazi(267, 66, 'Yatay İleri (→ 10 m · Dik!)', LAC, 'middle', True)
    return svg(360, 94, ic, 'Düşey kuvvet ile yatay yer değiştirmenin birbirine dik olduğunu gösteren şema.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_durum_is_karti()
    s[1]['gorsel'] = is_hesaplama_olcum_kartlari()
    s[3]['gorsel'] = xyz_vagon_verileri()
    s[4]['gorsel'] = paket_rafa_kaldirma_sema()
    s[6]['gorsel'] = halter_iki_asama_karti()
    s[7]['gorsel'] = dinamometre_deney_adimlari()
    s[8]['gorsel'] = kl_is_yol_grafigi()
    s[11]['gorsel'] = dik_dogrultu_sepet_karti()
