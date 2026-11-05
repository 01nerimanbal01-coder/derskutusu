"""7. sınıf Türkçe 10. hafta (Millî Mücadele Sergisi / Kahraman Çocuklar, Fiillerde Anlam Kayması, Yazım Kuralları ve Söz Sanatları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def sergi_kahraman_cocuklar_karti():
    ic = kutu(6, 6, 348, 78, KIR_A, KIR)
    ic += yazi(180, 22, 'MİLLÎ MÜCADELE SERGİSİ · KAHRAMAN ÇOCUKLAR', 10.0, KIR)
    ic += yazi(180, 42, '• Cephe gerisinde kağnılarla cephane ve erzak ulaştırdılar.', 9.3, LAC, ince=True)
    ic += yazi(180, 58, '• Kâzım Karabekir Paşa’nın kurduğu Gürbüzler Ordusu’nda', 9.3, LAC, ince=True)
    ic += yazi(180, 74, '  okuma yazma, sanat ve meslek öğrenerek vatanı yücelttiler.', 9.3, MAVI)
    return svg(360, 90, ic, 'Millî Mücadele Sergisi ve Kahraman Çocuklar tanıtım kartı.', 15)


def anlam_kaymasi_tablo_kartlari():
    kartlar = [
        ('1. Fiş (-yor)', '1919’da çıkıyor', MAVI, MAVI_A),
        ('2. Fiş (-ur)', 'Haftaya buluşuruz', YES, YES_A),
        ('3. Fiş (-yor)', 'Her sabah yapıyor', TUR, TUR_A),
        ('4. Fiş (-a)', 'Yolunuz açık ola!', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.8"/>'
        ic += yazi(x + 41, 54, alt, 9.0, LAC, ince=True)
    return svg(360, 82, ic, 'Fiillerde anlam kayması içeren dört cümle fişi.', 14)


def yazim_kurallari_levhalari():
    levhalar = [
        (4, 4, '1. Levha (Bayram Adı)', '29 Ekim Cumhuriyet Bayramı', MAVI, MAVI_A),
        (184, 4, '2. Levha (Tarihî Olay)', 'kurtuluş savaşı’nda cephe', KIR, KIR_A),
        (4, 50, '3. Levha (Dönem Adı)', 'Millî Mücadele’nin çocukları', YES, YES_A),
        (184, 50, '4. Levha (Belirli Tarih)', '24 Kasım 2026 Salı günü', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in levhalar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.6, r)
        ic += yazi(x + 86, y + 34, alt, 9.1, LAC, ince=True)
    return svg(360, 96, ic, 'Büyük harflerin ve kesme işaretinin yazımıyla ilgili dört levha.', 15)


def soz_sanatlari_kartlari():
    kartlar = [
        (4, 4, '1. Kart · Benzetme', 'Aslan gibi kükreyen Mehmetçik', MAVI, MAVI_A),
        (184, 4, '2. Kart · Kişileştirme', 'Hüzünle ağlayan kağnı tekeri', YES, YES_A),
        (4, 50, '3. Kart · (?)', 'Al bayrak: «Beni zirveye taşı!»', KIR, KIR_A),
        (184, 50, '4. Kart · Abartma', 'Gökyüzüne ulaşan zafer sevinci', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.6, r)
        ic += yazi(x + 86, y + 34, alt, 9.0, LAC, ince=True)
    return svg(360, 96, ic, 'Benzetme, kişileştirme, konuşturma ve abartma söz sanatı kartları.', 15)


def kip_kaymasi_analiz_karti():
    ic = kutu(6, 6, 348, 74, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Tarihî Anlatımda Kip (Anlam) Kayması Analizi', 10.0, MAVI)
    ic += yazi(180, 44, '«Kâzım Karabekir Paşa, Doğu Cephesi’nde kimsesiz kalan', 9.4, LAC, ince=True)
    ic += yazi(180, 64, 'binlerce çocuğu koruma altına alır.» (Biçim: -ır / Anlam: ?)', 9.4, KIR)
    return svg(360, 86, ic, 'Tarihî cümlede geniş zaman kipinin geçmiş zaman yerine kullanımı.', 14)


def dinleme_surec_semasi():
    adimlar = [
        ('1. Öncesi', 'Başlık / Tahmin', MAVI, MAVI_A),
        ('2. Sırası', 'Not Alma', YES, YES_A),
        ('3. Tasnif', 'Sınıflandırma', TUR, TUR_A),
        ('4. Sonrası', 'Derin Çıkarım', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += yazi(x + 41, 52, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'Dinleme ve izleme metnini çözümlemenin dört aşaması.', 14)


def dusunceyi_gelistirme_panosu():
    kartlar = [
        (4, 4, '1. Tanımlama', '«... nedir?» sorusuna yanıt verir', MAVI, MAVI_A),
        (184, 4, '2. Sayısal Veriler', 'İstatistik ve oranlarla kanıtlar', YES, YES_A),
        (4, 50, '3. Tanık Gösterme', 'Uzman sözünü tırnak içinde aktarır', TUR, TUR_A),
        (184, 50, '4. Karşılaştırma', 'İki unsuru benzer/farklı kıyaslar', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.6, r)
        ic += yazi(x + 86, y + 34, alt, 8.9, LAC, ince=True)
    return svg(360, 96, ic, 'Düşünceyi geliştirme yolları bilgi panosu.', 15)


def medya_degerlendirme_karti():
    ic = kutu(6, 6, 170, 74, CAM_A, CAM)
    ic += yazi(91, 22, '1. Ölçüt · İçerik Doğruluğu', 9.8, CAM)
    ic += yazi(91, 43, '• Tarihî belgelere dayanma', 9.2, LAC, ince=True)
    ic += yazi(91, 63, '• Tarafsız ve güvenilir kaynak', 9.2, CAM)

    ic += kutu(184, 6, 170, 74, YES_A, YES)
    ic += yazi(269, 22, '2. Ölçüt · Hedef Kitle Uyumu', 9.8, YES)
    ic += yazi(269, 43, '• Yaş düzeyine uygun anlatım', 9.2, LAC, ince=True)
    ic += yazi(269, 63, '• Millî ve manevi değerlere saygı', 9.2, YES)
    return svg(360, 86, ic, 'Medya içeriklerini değerlendirme ölçütleri kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sergi_kahraman_cocuklar_karti()
    s[2]['gorsel'] = anlam_kaymasi_tablo_kartlari()
    s[5]['gorsel'] = yazim_kurallari_levhalari()
    s[6]['gorsel'] = soz_sanatlari_kartlari()
    s[7]['gorsel'] = kip_kaymasi_analiz_karti()
    s[8]['gorsel'] = dinleme_surec_semasi()
    s[9]['gorsel'] = dusunceyi_gelistirme_panosu()
    s[11]['gorsel'] = medya_degerlendirme_karti()
