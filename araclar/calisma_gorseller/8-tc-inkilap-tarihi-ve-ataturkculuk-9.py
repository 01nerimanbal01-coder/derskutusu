"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 9. hafta (Havza Genelgesi, Amasya Genelgesi ve Erzurum Kongresi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def havza_genelgesi_karti():
    """Soru 2 (s[1]): Havza Genelgesi (28 Mayıs 1919) bilgi kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Havza Genelgesi (28 Mayıs 1919) · İlk Ulusal Tepki', MAVI, boy=10.6)
    ic += kutu(12, 28, 162, 54, '#fff', MAVI, 6)
    ic += yazi(93, 45, 'Alınan Kararlar:', MAVI, boy=10.2)
    ic += yazi(93, 62, '• Protesto mitingleri yapılacak', LAC, ince=True, boy=9.5)
    ic += yazi(93, 76, '• Kınama telgrafları çekilecek', LAC, ince=True, boy=9.5)

    ic += kutu(186, 28, 162, 54, YES_A, YES, 6)
    ic += yazi(267, 45, 'Güvenlik Tedbiri:', YESIL_K, boy=10.2)
    ic += yazi(267, 62, '• Azınlıklara zarar verilmeyecek', LAC, ince=True, boy=9.5)
    ic += yazi(267, 76, '• Silahlar teslim edilmeyecek', YESIL_K, boy=9.5)
    return svg(360, 94, ic, 'Havza Genelgesi maddeleri ve güvenlik önlemleri kartı.', 15)


def amasya_unsur_kartlari():
    """Soru 3 (s[2]): Amasya Genelgesi Gerekçe, Amaç-Yöntem ve Kurumsallaşma kartları."""
    kartlar = [
        (4, 'Gerekçe (Neden)', 'Vatan tehlikededir ·', 'Hükümet acizdir', TUR, TUR_A),
        (124, 'Amaç ve Yöntem', 'Bağımsızlığı milletin', 'azim ve kararı kurtarır', MAVI, MAVI_A),
        (244, 'Kurumsallaşma', 'Millî bir kurul ve', 'Sivas Kongresi kararı', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 4, 112, 80, z, r, 8)
        ic += yazi(x + 56, 22, bas, r, boy=10.4)
        ic += yazi(x + 56, 44, s1, LAC, ince=True, boy=9.6)
        ic += yazi(x + 56, 64, s2, LAC, boy=9.6)
    return svg(360, 88, ic, 'Amasya Genelgesi gerekçe, amaç, yöntem ve kurumsallaşma kartları.', 14)


def amasya_cok_imzali_sema():
    """Soru 6 (s[5]): Amasya Genelgesi'nin çok imzalı yayımlanması şeması."""
    ic = kutu(4, 4, 352, 84, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Amasya Genelgesi (22 Haziran 1919) · Çok İmzalı Onay Süreci', KAHVE, boy=10.5)
    ic += kutu(12, 28, 162, 50, MAVI_A, MAVI, 6)
    ic += yazi(93, 46, 'Bizzat İmzalayanlar', MAVI, boy=10.0)
    ic += yazi(93, 66, 'M. Kemal · Rauf · Refet · Ali Fuat', LAC, ince=True, boy=9.4)

    ic += kutu(186, 28, 162, 50, YES_A, YES, 6)
    ic += yazi(267, 46, 'Telgrafla Onaylayanlar', YESIL_K, boy=10.0)
    ic += yazi(267, 66, 'Kâzım Karabekir · Cemal Paşa', LAC, ince=True, boy=9.4)
    return svg(360, 92, ic, 'Amasya Genelgesini imzalayan ve telgrafla onaylayan komutanlar şeması.', 15)


def erzurum_bolgesel_ulusal_sema():
    """Soru 7 (s[6]): Erzurum Kongresi Bölgesel Toplanış vs Ulusal Kararlar şeması."""
    ic = kutu(4, 4, 172, 84, TUR_A, TUR, 8)
    ic += yazi(90, 21, 'Toplanış Biçimi: BÖLGESEL', TUR, boy=10.3)
    ic += yazi(90, 43, '• Doğu Anadolu ve Karadeniz', LAC, ince=True, boy=9.6)
    ic += yazi(90, 61, '  savunması için toplandı', LAC, ince=True, boy=9.6)
    ic += yazi(90, 78, '• Doğu illeri delegeleri katıldı', TUR, boy=9.5)

    ic += kutu(184, 4, 172, 84, MAVI_A, MAVI, 8)
    ic += yazi(270, 21, 'Aldığı Kararlar: ULUSAL', MAVI, boy=10.3)
    ic += yazi(270, 43, '• «Millî sınırlar içinde vatan', LAC, ince=True, boy=9.6)
    ic += yazi(270, 61, '   bir bütündür, parçalanamaz.»', LAC, ince=True, boy=9.6)
    ic += yazi(270, 78, '• Tüm vatanı kapsayan karar!', MAVI, boy=9.5)
    return svg(360, 92, ic, 'Erzurum Kongresi bölgesel toplanış ve ulusal kararlar karşılaştırma şeması.', 15)


def amasya_ihtilal_belge_karti():
    """Soru 8 (s[7]): Amasya Genelgesi 3. madde (İhtilal bildirgesi) kartı."""
    ic = kutu(4, 4, 352, 82, KIR_A, KIR, 8)
    ic += yazi(180, 21, 'Amasya Genelgesi · 3. Madde Analizi', KIR, boy=10.6)
    ic += yazi(180, 44, '«Milletin bağımsızlığını, yine milletin azim ve kararı kurtaracaktır.»', LAC, boy=10.2)
    ic += yazi(180, 68, 'Amaç: Milletin bağımsızlığı  |  Yöntem ve İrade: Milletin azim ve kararı', KIR, ince=True, boy=9.6)
    return svg(360, 90, ic, 'Amasya Genelgesi üçüncü maddesi amaç ve yöntem analizi kartı.', 14)


def hazirlik_kronoloji_seridi():
    """Soru 9 (s[8]): Mayıs - Ağustos 1919 kronoloji şeridi."""
    adimlar = [
        (4, '1. Havza', '28 Mayıs 1919', 'Millî bilinç', MAVI, MAVI_A),
        (93, '2. Amasya', '22 Haziran 1919', 'Amaç · Yöntem', TUR, TUR_A),
        (182, '3. İstifa', '7–8 Temmuz 1919', 'Sine-i millet', MOR, MOR_A),
        (271, '4. Erzurum', '23 Temmuz 1919', 'Manda reddi', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.2)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.4)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.4)
    return svg(360, 88, ic, '1919 yılı Millî Mücadele hazırlık dönemi kronoloji şeridi.', 14)


def erzurum_dort_karar_karti():
    """Soru 10 (s[9]): Erzurum Kongresi 4 karar kartı."""
    kartlar = [
        (4, 4, 'I. Karar · Millî İrade', 'Kuvâ-yı Millîye’yi etkin, millî iradeyi hâkim kılmak', MAVI, MAVI_A),
        (184, 4, 'II. Karar · Bağımsızlık', 'Manda ve himaye kesinlikle kabul olunamaz', YES, YES_A),
        (4, 52, 'III. Karar · Eşitlik', 'Azınlıklara siyasi dengeyi bozacak imtiyaz verilemez', TUR, TUR_A),
        (184, 52, 'IV. Karar · Denetim', 'Mebusan Meclisi toplanmalı, hükümet denetlenmeli', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.0)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=8.6)
    return svg(360, 100, ic, 'Erzurum Kongresi dört temel karar kartı.', 15)


def iki_ilke_karsilastirma_karti():
    """Soru 12 (s[11]): Millî egemenlik ve Tam bağımsızlık karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(90, 22, '1. Karar İfadesi', MAVI, boy=10.4)
    ic += yazi(90, 44, '«Kuvâ-yı Millîye’yi etkin,', LAC, ince=True, boy=9.8)
    ic += yazi(90, 62, 'millî iradeyi hâkim kılmak»', LAC, ince=True, boy=9.8)
    ic += yazi(90, 78, 'Temsil Ettiği İlke: ?', MAVI, boy=9.8)

    ic += kutu(184, 4, 172, 82, YES_A, YES, 8)
    ic += yazi(270, 22, '2. Karar İfadesi', YESIL_K, boy=10.4)
    ic += yazi(270, 44, '«Manda ve himaye', LAC, ince=True, boy=9.8)
    ic += yazi(270, 62, 'kesinlikle kabul olunamaz»', LAC, ince=True, boy=9.8)
    ic += yazi(270, 78, 'Temsil Ettiği İlke: ?', YESIL_K, boy=9.8)
    return svg(360, 90, ic, 'Erzurum Kongresi kararlarının millî egemenlik ve tam bağımsızlık ilkeleriyle ilişkisi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = havza_genelgesi_karti()
    s[2]['gorsel'] = amasya_unsur_kartlari()
    s[5]['gorsel'] = amasya_cok_imzali_sema()
    s[6]['gorsel'] = erzurum_bolgesel_ulusal_sema()
    s[7]['gorsel'] = amasya_ihtilal_belge_karti()
    s[8]['gorsel'] = hazirlik_kronoloji_seridi()
    s[9]['gorsel'] = erzurum_dort_karar_karti()
    s[11]['gorsel'] = iki_ilke_karsilastirma_karti()
