"""5. sınıf Türkçe 10. hafta (Gazi Mustafa Kemal ve Sığırtmaç Mustafa: Hikâye Unsurları, Yapım-Çekim Ekleri ve Söz Sanatları) çalışma kâğıdı görselleri.
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


def dort_kelime_ek_ayrimi():
    kartlar = [
        ('1. Kart', 'çift - lik - te', MAVI, MAVI_A),
        ('2. Kart', 'ceviz - ler - im', YES, YES_A),
        ('3. Kart', 'yol - cu - lar - ın', TUR, TUR_A),
        ('4. Kart', 'hasta - lık - tan', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ekler, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 23, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="31" x2="{x + 74}" y2="31" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, ekler, 9.1, LAC)
    return svg(360, 86, ic, 'Yapım ve çekim eklerine ayrılmış dört kelime kartı.', 15)


def soz_sanatlari_dort_kart():
    kartlar = [
        ('1. Cümle', 'Çakmak taşı gibi göz', MAVI, MAVI_A),
        ('2. Cümle', 'El sallayan yaşlı çınar', YES, YES_A),
        ('3. Cümle', 'Pamuk kadar bulutlar', TUR, TUR_A),
        ('4. Cümle', 'Fısıldayan sonbahar rüzgârı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, orn, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, orn, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Benzetme ve kişileştirme içeren dört örnek kart.', 16)


def diyalog_noktalama_panosu():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 22, 'Metinden Karşılıklı Konuşma (Diyalog) Kesiti', 10.3, TUR)
    ic += yazi(180, 44, 'Atatürk küçük çobana gülümseyerek sordu ( 1 )', 9.7, LAC, ince=True)
    ic += yazi(180, 64, '( 2 ) Bu cevizleri bana satar mısın ( 3 ) Mustafa sevinçle başını salladı ( 4 )', 9.3, LAC)
    return svg(360, 88, ic, 'İki nokta, konuşma çizgisi, soru işareti ve nokta uygulaması.', 15)


def metin_ici_karsilastirma_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Metnin Başında Mustafa', 10.1, TUR)
    ic += yazi(91, 44, 'Sıtma hastası, cılız, okuma', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'yazma bilmeyen küçük çoban', 9.4, TUR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Metnin Sonunda Mustafa', 10.1, YESIL_K)
    ic += yazi(269, 44, 'Sağlığına kavuşmuş, okumuş,', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'vatansever genç Türk subayı', 9.4, YESIL_K)
    return svg(360, 88, ic, 'Sığırtmaç Mustafa’nın metnin başındaki ve sonundaki durumu.', 15)


def koylulerimizden_ek_analizi():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Sözcükte Yapı ve Ek Dizilişi Çözümleme Kartı', 10.4, MAVI)
    ic += yazi(180, 46, '[ köy ]  +  [ -lü ]  +  [ -ler ]  +  [ -imiz ]  +  [ -den ]', 10.6, LAC)
    ic += yazi(180, 67, 'Kök + Yapım Eki + Çoğul Eki + İyelik Eki + Ayrılma Hali Eki', 9.3, MAVI, ince=True)
    return svg(360, 88, ic, 'Köylülerimizden sözcüğünün kök, yapım eki ve çekim ekleri şeması.', 15)


def sigirtmac_olay_orgusu_kartlari():
    adimlar = [
        ('Bölüm A', 'Yolu şaşırıp karşılaşma', MAVI, MAVI_A),
        ('Bölüm B', 'Ceviz ve para diyaloğu', TUR, TUR_A),
        ('Bölüm C', 'Hastanede tedavi süreci', MOR, MOR_A),
        ('Bölüm D', 'Okul ve subay olma', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 55, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'Gazi Mustafa Kemal ve Sığırtmaç Mustafa metninin olay örgüsü.', 15)


def baglanti_ve_yazim_panosu():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 21, 'Bağlantı İfadeleri ve Özel İsimlerin Yazımı Panosu', 10.3, MAVI)
    ic += yazi(180, 40, 'I) yoksuldu ama gönlü zengindi   |   II) İstanbul’daki hastanede', 9.4, LAC, ince=True)
    ic += yazi(180, 58, 'III) iyileşti çünkü tedavisi yapıldı   |   IV) Yalova’lı köylüler (?)', 9.4, KIR)
    ic += yazi(180, 75, 'Kural: Özel adlara gelen yapım ekleri (-lı, -lik, -ce) kesmeyle ayrılmaz!', 9.3, MAVI)
    return svg(360, 92, ic, 'Bağlantı ifadeleri ve özel isimlere gelen yapım eklerinin yazımı.', 16)


def ataturk_kisilik_ozellikleri_karti():
    kartlar = [
        ('Halkla İç İçe Oluşu', 'Küçük çobanla samimi sohbet', MAVI, MAVI_A),
        ('Şefkat ve Merhamet', 'Hastanede tedavi ettirmesi', YES, YES_A),
        ('Eğitime Verdiği Önem', 'Okula yazdırıp yetiştirmesi', TUR, TUR_A),
        ('Vefa ve İnsani Değer', 'Mustafa’yı hiç unutmaması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Metinde öne çıkan Atatürk’ün liderlik ve insani özellikleri.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_kelime_ek_ayrimi()
    s[2]['gorsel'] = soz_sanatlari_dort_kart()
    s[5]['gorsel'] = diyalog_noktalama_panosu()
    s[6]['gorsel'] = metin_ici_karsilastirma_karti()
    s[7]['gorsel'] = koylulerimizden_ek_analizi()
    s[8]['gorsel'] = sigirtmac_olay_orgusu_kartlari()
    s[9]['gorsel'] = baglanti_ve_yazim_panosu()
    s[11]['gorsel'] = ataturk_kisilik_ozellikleri_karti()
