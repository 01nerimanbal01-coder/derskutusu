"""6. sınıf Türkçe 8. hafta (Vatan Şiiri Çözümlemesi, Şiir-Düzyazı Farkı, Söz Sanatları, Geçiş İfadeleri ve Ekler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def siradaglar_dize_karti():
    ic = kutu(8, 8, 584, 84, KIR_A, KIR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, KIR, KIR, 9, 1)
    ic += yazi(300, 25, 'NURETTİN ÖZDEMİR · “VATAN” ŞİİRİNDEN DİZELER', 12, '#fff')
    ic += yazi(300, 52, '“Hakkâri’de sıradağlar · Ki bölünmez · Yürek yüreğe, el eledir.”', 12, LAC)
    ic += yazi(300, 76, 'İpucu: İnsan dışı varlık olan sıradağlara insani özellik kazandırılmıştır.', 12, KIR, ince=True)
    return svg(600, 100, ic, 'Hakkâri’de sıradağlar ki bölünmez yürek yüreğe el eledir dizeleri kartı.', 22)


def gecis_ifadeleri_karti():
    ic = kutu(8, 8, 584, 86, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 584, 26, MAVI, MAVI, 9, 1)
    ic += yazi(300, 25, 'GEÇİŞ VE BAĞLANTI İFADELERİ · CÜMLE TAMAMLAMA', 12, '#fff')
    ic += yazi(300, 52, '“Tüm Türkiye’yi gezmek istiyorum ___ (1) ___ ülkemizin her köşesi çok güzel,', 12, LAC, ince=True)
    ic += yazi(300, 76, '___ (2) ___ önce hangi şehirden başlayacağıma henüz karar veremiyorum.”', 12, MAVI)
    return svg(600, 102, ic, 'Neden-sonuç ve düşünceyi değiştiren geçiş ifadeleri cümle kartı.', 22)


def vatan_tamlama_kartlari():
    kartlar = [
        ('1. yemyeşil bahçe', 'Sıfat ve İsim (Nasıl?)', YES, YES_A),
        ('2. Kütahya çinisi', '2. isim iyelik eki almış', MAVI, MAVI_A),
        ('3. dağların gözyaşı', 'İki isim de ek almış', TUR, TUR_A),
        ('4. kutsal bir düşünce', 'Sıfat ve İsim (Nasıl?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Vatan şiirinden alınan dört tamlama örneği kartı.', 22)


def yapim_cekim_karti():
    ic = kutu(8, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, '1. Kelime: “duy-gu” (Marşımız duygu dolu)', 12, '#fff')
    ic += yazi(150, 52, 'Kök: duy- (fiil) → Ek: -gu', 12, LAC)
    ic += yazi(150, 74, 'Yeni kavram adı türetmiştir', 12, YES, ince=True)

    ic += kutu(308, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(450, 25, '2. Kelime: “ol-du” (Akşam oldu)', 12, '#fff')
    ic += yazi(450, 52, 'Kök: ol- (fiil) → Ek: -du', 12, LAC)
    ic += yazi(450, 74, 'Anlam değişmemiş, zaman bildirmiştir', 12, TUR, ince=True)
    return svg(600, 100, ic, 'Duygu ve oldu kelimelerinin kök ve ek inceleme kartları.', 22)


def ayni_kokten_tureme_sema():
    adimlar = [
        ('1. Kök', 'düş (İsim kökü)', MAVI, MAVI_A),
        ('2. Fiil Gövdesi', 'düş-ün- (Eylem)', YES, YES_A),
        ('3. Kavram Adı', 'düşün-ce (İsim)', TUR, TUR_A),
        ('4. Nitelik Adı', 'düşünce-li (Sıfat)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Düş kökünden düşün-, düşünce ve düşünceli kelimelerinin türeme zinciri.', 22)


def sehir_imge_panosu():
    kartlar = [
        ('Edirne', '→ Bir ince minaredir (Selimiye)', MAVI, MAVI_A),
        ('Zonguldak', '→ Bir maden işçisidir (Emek)', TUR, TUR_A),
        ('Rize', '→ Çay toplayan bir gelindir', YES, YES_A),
        ('Anıtkabir', '→ Sonsuza dek sönmeyecek meşaledir', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Vatan şiirinde geçen Edirne, Zonguldak, Rize ve Anıtkabir imgeleri.', 22)


def da_de_yazim_kartlari():
    satirlar = [
        ('1. Cümle', 'Antalya’da mavi sular güneşin altında parlıyor. (Bulunma eki)', YES, YES_A),
        ('2. Cümle', 'Anıtkabir’de yanıp da sönmeyecek bir meşaledir. (Ek ve Bağlaç)', MAVI, MAVI_A),
        ('3. Cümle', 'Isparta halısında gül, Kütahya çinisinde lale vardır. (Bulunma eki)', CAM, CAM_A),
        ('4. Cümle (!)', 'Gümüşhane’de ki yemyeşil bahçe de çiçekler açmış. (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 92, 22, renk, renk, 6, 1)
        ic += yazi(54, y + 15, no, 12, '#fff')
        ic += yazi(108, y + 15, metin, 12, LAC, 'start', ince=(i != 3))
    return svg(600, 112, ic, 'Bulunma durumu eki ve bağlaç olan da-de yazım örnekleri; 4. cümle hatalı.', 22)


def siir_duzyazi_sema():
    ic = kutu(8, 8, 284, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MOR, MOR, 9, 1)
    ic += yazi(150, 25, 'Şiir (Manzum Metin)', 12, '#fff')
    ic += yazi(150, 52, 'Dizeler · Dörtlük · Şair · Ana Duygu', 12, LAC)
    ic += yazi(150, 74, 'Kafiye, redif ve söz sanatları', 12, MOR, ince=True)

    ic += kutu(308, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(308, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(450, 25, 'Düzyazı (Mensur Metin)', 12, '#fff')
    ic += yazi(450, 52, 'Cümleler · Paragraflar · Yazar · Ana Fikir', 12, LAC)
    ic += yazi(450, 74, 'Düşünceyi geliştirme yolları', 12, MAVI, ince=True)
    return svg(600, 100, ic, 'Şiir ve düzyazı arasındaki yapısal ve anlamsal farkları gösteren şema.', 22)


def soz_sanatlari_kartlari():
    satirlar = [
        ('1. Kart', 'Sabah erkenden kalkan balıkçılar limandan denize açıldı.', MAVI, MAVI_A),
        ('2. Kart', 'Küçük bir kıvılcımdım, şimdi koskoca dağları tutuşturacak ateş oldum!', KIR, KIR_A),
        ('3. Kart', 'Kütüphanedeki raflarda tarih, bilim ve edebiyat kitapları diziliydi.', YES, YES_A),
        ('4. Kart', 'Okul bahçesindeki tören saat dokuz buçukta İstiklâl Marşı ile başladı.', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 82, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, 12, '#fff')
        ic += yazi(98, y + 15, metin, 12, LAC, 'start', ince=(i != 1))
    return svg(600, 112, ic, 'Dört cümle kartı; 2. kartta küçük kıvılcım ve koskoca dağları tutuşturacak ateş ile karşıtlık ve abartma bir arada.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = siradaglar_dize_karti()
    s[4]['gorsel'] = gecis_ifadeleri_karti()
    s[5]['gorsel'] = vatan_tamlama_kartlari()
    s[6]['gorsel'] = yapim_cekim_karti()
    s[7]['gorsel'] = ayni_kokten_tureme_sema()
    s[8]['gorsel'] = sehir_imge_panosu()
    s[9]['gorsel'] = da_de_yazim_kartlari()
    s[11]['gorsel'] = siir_duzyazi_sema()
    s[12]['gorsel'] = soz_sanatlari_kartlari()
