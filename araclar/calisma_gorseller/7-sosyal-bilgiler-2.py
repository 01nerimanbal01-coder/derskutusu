"""7. sınıf Sosyal Bilgiler 2. hafta (Gruplarda Olumlu İletişim: Yanlış Anlaşılma, Özür ve Uzlaşma) çalışma kâğıdı görselleri.
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


def gunluk_yasam_kartlari():
    kartlar = [
        ('1. Kulüp Toplantısı', 'Söz kesmeden dinleme', MAVI, MAVI_A),
        ('2. Okul Kütüphanesi', 'Sessizlik için kibar rica', YES, YES_A),
        ('3. Sınıf Gezisi Önerisi', 'Farklı ilgilere saygı', TUR, TUR_A),
        ('4. Koridor Panosu', 'Fotoğraf ve çizim uzlaşması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.4, r)
        ic += yazi(x + 71, 52, alt, 9.9, LAC, ince=True)
    return svg(600, 80, ic, 'Günlük yaşamda olumlu iletişim örnek kartları.', 15)


def mesaj_yanlis_anlasilma():
    ic = kutu(6, 6, 286, 78, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(149, 24, '7-A Sınıf Mesaj Grubu', 10.8, MAVI)
    ic += yazi(149, 46, 'Selin: “Bu afişi kim hazırladı?”', 10.2, LAC)
    ic += yazi(149, 66, '(Niyeti: Beğendiği için tebrik etmek)', 10.0, MAVI, ince=True)

    ic += kutu(308, 6, 286, 78, KIR_A, KIR, 9, 1.5)
    ic += yazi(451, 24, 'Eksik Olan İletişim İpuçları', 10.8, KIR)
    ic += yazi(451, 46, '• Ses tonu · Bakış · Beden dili yok', 10.1, LAC, ince=True)
    ic += yazi(451, 66, 'Kerem’in Algısı: Eleştiri sanıp üzüldü', 10.1, KIR)
    return svg(600, 90, ic, 'Yazılı mesajda ses tonu ve beden dili görünmediği için oluşan yanlış anlaşılma.', 16)


def yapboz_birlikte_yasama():
    parcalar = [
        ('Haklara Saygı', 'Eşit değer verme', MAVI, MAVI_A),
        ('Düşünceye Saygı', 'Farklı fikri dinleme', YES, YES_A),
        ('Etkin Dinleme', 'Söz kesmeme', TUR, TUR_A),
        ('Empati ve Özür', 'Dayanışma ve güven', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(parcalar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Birlikte yaşama kültürünü oluşturan dört temel yapboz parçası.', 15)


def catisma_uzlasma_yollari():
    ic = kutu(6, 6, 286, 78, KIR_A, KIR, 9, 1.5)
    ic += yazi(149, 24, 'A Yolu · Çatışmayı Büyütenler', 10.8, KIR)
    ic += yazi(149, 46, '• Suçlamak, alay etmek, söz kesmek', 10.1, LAC, ince=True)
    ic += yazi(149, 66, '• Yalnız kendi fikrinde ısrar etmek', 10.1, KIR)

    ic += kutu(308, 6, 286, 78, YES_A, YES, 9, 1.5)
    ic += yazi(451, 24, 'B Yolu · Uzlaşmaya Götürenler', 10.8, YES)
    ic += yazi(451, 46, '• Dinlemek, empati ve ben dili kullanmak', 10.1, LAC, ince=True)
    ic += yazi(451, 66, '• İki fikrin güçlü yanlarını birleştirmek', 10.1, YES)
    return svg(600, 90, ic, 'Fikir ayrılığında çatışmayı büyüten A yolu ile uzlaşmayı sağlayan B yolu.', 16)


def icten_ozur_adimlari():
    adimlar = [
        ('1. Dur ve Yardım Et', 'Dağılanları birlikte topla', MAVI, MAVI_A),
        ('2. Göz Teması Kur', 'Önemsediğini hissettir', TUR, TUR_A),
        ('3. Hatanı Açıkla', 'Sorumluluğu dürüstçe al', MOR, MOR_A),
        ('4. Özür ve Kabul', 'Samimi ses ve anlayış', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.4, r)
        ic += yazi(x + 71, 50, alt, 9.9, LAC, ince=True)
    return svg(600, 78, ic, 'İçten bir özrün dört uygulama basamağı.', 15)


def iki_ozur_karsilastirma():
    ic = kutu(6, 6, 286, 72, KIR_A, KIR, 8, 1.5)
    ic += yazi(149, 24, '1. Kişinin Özür Biçimi', 10.8, KIR)
    ic += yazi(149, 46, 'Yere bakarak ve isteksiz sesle:', 10.1, LAC, ince=True)
    ic += yazi(149, 63, '“Tamam, özür dilerim işte!”', 10.2, KIR)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, '2. Kişinin Özür Biçimi', 10.8, YES)
    ic += yazi(451, 46, 'Göz teması kurup samimi sesle:', 10.1, LAC, ince=True)
    ic += yazi(451, 63, '“Sözümü tutamadım, özür dilerim.”', 10.2, YES)
    return svg(600, 84, ic, 'İsteksiz özür ile göz teması kurularak dilenen içten özrün karşılaştırılması.', 16)


def sorgulama_basamak_sema():
    kutular = [
        ('1. Merak Et', 'Örnek durumu incele', MAVI, MAVI_A),
        ('2. Soru Hazırla', 'İletişim sorusu yaz', TUR, TUR_A),
        ('3. Bilgi Topla', 'Kaynakları araştır', MOR, MOR_A),
        ('4. ? (Değerlendir)', 'Kaynakları karşılaştır', KIR, KIR_A),
        ('5. Çıkarım Yap', 'Özgün ürünle anlat', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 66, z, r, 8, 1.4)
        ic += yazi(x + 56, 26, bas, 10.2, r)
        ic += yazi(x + 56, 50, alt, 9.6, LAC, ince=True)
    return svg(600, 78, ic, 'Etkili iletişimi sorgulama basamakları şeması.', 15)


def dijital_mesaj_cozum_karti():
    ic = kutu(6, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(149, 24, 'Belirsiz Mesaj (Yanlış Anlaşmaya Açık)', 10.5, TUR)
    ic += yazi(149, 46, '“Bu resmi sen mi çizdin?”', 10.3, LAC)
    ic += yazi(149, 63, 'Yüz ifadesi olmadığı için eleştiri sanıldı', 9.9, TUR, ince=True)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Doğru İletişim Çözümü', 10.5, YES)
    ic += yazi(451, 46, '1) Yazan: Niyetini ve beğenisini açıkça yazar', 10.0, LAC, ince=True)
    ic += yazi(451, 63, '2) Okuyan: Kırılmadan önce niyetini sorar', 10.0, YES)
    return svg(600, 84, ic, 'Dijital mesajdaki belirsizliği giderme yolları kartı.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = gunluk_yasam_kartlari()
    s[1]['gorsel'] = mesaj_yanlis_anlasilma()
    s[3]['gorsel'] = yapboz_birlikte_yasama()
    s[5]['gorsel'] = catisma_uzlasma_yollari()
    s[6]['gorsel'] = icten_ozur_adimlari()
    s[7]['gorsel'] = iki_ozur_karsilastirma()
    s[8]['gorsel'] = sorgulama_basamak_sema()
    s[11]['gorsel'] = dijital_mesaj_cozum_karti()
