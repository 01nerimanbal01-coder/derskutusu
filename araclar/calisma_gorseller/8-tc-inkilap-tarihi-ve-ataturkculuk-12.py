"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 12. hafta (BMM’ye Karşı Ayaklanmalar ve Sevr Antlaşması) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def bmm_yasama_yargi_semasi():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'Hıyanet-i Vataniye Kanunu', MAVI, kalin=True)
    ic += yazi(92, 54, '29 Nisan 1920’de çıkarıldı', LAC)
    ic += yazi(92, 82, 'Yetki: YASAMA (Kanun Yapma)', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'İstiklal Mahkemeleri', YES, kalin=True)
    ic += yazi(269, 54, 'Üyeleri milletvekillerinden seçildi', LAC)
    ic += yazi(269, 82, 'Yetki: YARGI (Mahkeme)', YES, kalin=True)
    return svg(ic, 'BMM’nin yasama ve yargı yetkilerini kullanması şeması.')


def bmm_dort_tedbir_panosu():
    kartlar = [
        (6, 6, '1. Karşı Fetva (Rıfat Börekçi)', 'Dinî ve Toplumsal Tedbir', YES, YES_A),
        (184, 6, '2. Anadolu Ajansı & Basın', 'İletişim ve Kamuoyu Tedbiri', MAVI, MAVI_A),
        (6, 60, '3. Hıyanet-i Vataniye Kanunu', 'Hukuki (Yasama-Yargı) Tedbir', TUR, TUR_A),
        (184, 60, '4. Düzenli Ordunun Kurulması', 'Askerî ve Savunma Tedbiri', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'BMM’nin ayaklanmalara karşı aldığı dört temel tedbir.')


def sevr_maddeleri_karti():
    kartlar = [
        (6, 6, 'Boğazlar Komisyonu', 'Türk üye yok (Egemenlik)', MAVI, MAVI_A),
        (184, 6, 'Kapitülasyonlar & Maliye', 'Bütçe İtilaf kontrolünde (Ekonomi)', KIR, KIR_A),
        (6, 60, 'Ordu Sınırlandırması', 'Ağır silah yok (Savunma)', TUR, TUR_A),
        (184, 60, 'Sınırlar ve Topraklar', 'Anadolu parçalanıyor (Siyasi)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Sevr Antlaşması’nın siyasi, askerî ve ekonomik maddeleri.')


def olu_dogmus_antlasma_karti():
    ic = kutu(6, 6, 348, 103, KIR_A, KIR)
    ic += yazi(180, 26, 'Hukuki Değerlendirme: Neden «Ölü Doğmuş Antlaşma»?', KIR, kalin=True)
    ic += yazi(180, 54, 'Osmanlı Anayasası Kanun-ı Esasi’ye göre bir antlaşmanın geçerli olması', LAC)
    ic += yazi(180, 76, 'için Mebusan Meclisi’nin onayı şarttı. Meclis kapalı olduğu için Sevr’i', LAC)
    ic += yazi(180, 96, 'yalnızca Saltanat Şûrası imzalamış, antlaşma hukuken geçersiz kalmıştır!', MAVI, kalin=True)
    return svg(ic, 'Sevr Antlaşması’nın hukuken geçersiz olma nedenini açıklayan kart.')


def duzenli_orduya_gecis_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 26, 'Eski Kuvâ-yı Milliyecilerin İsyanı (Çerkez Ethem & Demirci Mehmet Efe)', TUR, kalin=True)
    ic += yazi(180, 54, 'Sebep: Bağımsız hareket etmeye alışmış birliklerin düzenli ordu emrine girmeyi reddetmesi', LAC)
    ic += yazi(180, 82, 'Sonuç: BMM’nin kurduğu DÜZENLİ ORDU tarafından bastırıldı!', YES, kalin=True)
    return svg(ic, 'Çerkez Ethem ve Demirci Mehmet Efe isyanlarının nedeni ve sonucu.')


def kronoloji_1920_kartlari():
    adimlar = [
        (6, '16 Mart 1920', 'İstanbul’un İşgali', KIR, KIR_A),
        (94, '23 Nisan 1920', 'BMM’nin Açılması', YES, YES_A),
        (182, '29 Nisan 1920', 'Hıyanet-i Vataniye', MAVI, MAVI_A),
        (270, '10 Ağustos 1920', 'Sevr’e Tepki', TUR, TUR_A),
    ]
    ic = ''
    for x, tarih, olay, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, tarih, r, kalin=True)
        ic += yazi(x + 42, 70, olay, LAC, kalin=True)
    return svg(ic, '1920 yılındaki dört önemli tarihsel gelişmenin kronolojik sırası.')


def mustafa_kemal_sevr_tepki():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 26, 'Mustafa Kemal Paşa’nın Sevr Antlaşması’na Tepkisi', YES, kalin=True)
    ic += yazi(180, 54, '«Siyasi, adli, ekonomik ve mali bağımsızlığımızı yok etmeye ve', LAC)
    ic += yazi(180, 76, 'sonuç olarak yaşama hakkımızı inkâra ve ortadan kaldırmaya yönelik olan', LAC)
    ic += yazi(180, 96, 'Sevr Antlaşması bizce mevcut değildir!» (Tam Bağımsızlık Kararlılığı)', KIR, kalin=True)
    return svg(ic, 'Mustafa Kemal Paşa’nın Sevr Antlaşması’nı reddeden tarihsel sözü.')


def sevr_ve_direnis_karti():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 26, 'İtilaf Devletlerinin Planı', KIR, kalin=True)
    ic += yazi(92, 54, '• Yunan ordusunu ileri sürerek', LAC)
    ic += yazi(92, 76, 'Anadolu işgallerini genişletmek', LAC)
    ic += yazi(92, 96, '• Sevr’i zorla kabul ettirmek', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Türk Milletinin Yanıtı', YES, kalin=True)
    ic += yazi(269, 54, '• BMM etrafında kenetlenmek', LAC)
    ic += yazi(269, 76, '• Düzenli orduyla direnmek', LAC)
    ic += yazi(269, 96, '• Sevr’i tarihe gömmek!', YES, kalin=True)
    return svg(ic, 'İtilaf Devletlerinin Sevr baskısı ve Türk milletinin direnişi.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bmm_yasama_yargi_semasi()
    s[2]['gorsel'] = bmm_dort_tedbir_panosu()
    s[5]['gorsel'] = sevr_maddeleri_karti()
    s[6]['gorsel'] = olu_dogmus_antlasma_karti()
    s[7]['gorsel'] = duzenli_orduya_gecis_karti()
    s[8]['gorsel'] = kronoloji_1920_kartlari()
    s[9]['gorsel'] = mustafa_kemal_sevr_tepki()
    s[11]['gorsel'] = sevr_ve_direnis_karti()
