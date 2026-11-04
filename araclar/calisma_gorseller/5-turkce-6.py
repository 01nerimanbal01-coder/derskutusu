"""5. sınıf Türkçe 6. hafta (Bir Güzel Hediye & Mustafa: Yüzey Anlam, Anahtar Kelimeler, Söz Sanatları ve Bağlantı İfadeleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ruzgar_soz_sanati_karti():
    ic = kutu(6, 6, 588, 86, MAVI_A, MAVI, 9, 1.5)
    ic += kutu(6, 6, 588, 26, MAVI, MAVI, 9, 1)
    ic += yazi(300, 24, 'SÖZ SANATI İNCELEME KARTI · MUSTAFA METNİ', '#fff', kalin=True)
    ic += yazi(300, 52, '“Selanik’in serin rüzgârı küçük Mustafa’ya vatan sevgisini fısıldıyordu.”', LAC, kalin=True)
    ic += yazi(300, 75, 'İpucu: Cansız varlık olan rüzgâra insana özgü “fısıldama” özelliği verilmiştir.', MAVI)
    return svg(600, 98, ic, 'Rüzgârın fısıldaması örneğiyle kişileştirme söz sanatı kartı.', 21)


def baglanti_ifadeleri_kartlari():
    satirlar = [
        ('1. Kart', 'Mustafa tarih ve edebiyat kitaplarını okumayı çok seviyordu.', MAVI, MAVI_A),
        ('2. Kart (!)', 'Dışarıda şiddetli yağmur yağıyordu fakat çocuklar evde oyun kurdu.', KIR, KIR_A),
        ('3. Kart', 'Selanik’teki pembe boyalı evin geniş ve aydınlık bir bahçesi vardı.', YES, YES_A),
        ('4. Kart', 'Okulumuzda 29 Ekim Cumhuriyet Bayramı törenle kutlandı.', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(102, y + 15, metin, LAC, 'start', kalin=(i == 1))
    return svg(600, 112, ic, 'Bağlantı ifadesi içeren ve içermeyen dört cümle kartı.', 21)


def soz_sanati_tablo_kartlari():
    kartlar = [
        ('1. Kart', 'Pamuk gibi bembeyaz bulutlar', MAVI, MAVI_A),
        ('2. Kart', 'Gülümseyen yaşlı çınar ağacı', YES, YES_A),
        ('3. Kart', 'Çelik kadar sağlam bir irade', TUR, TUR_A),
        ('4. Kart', 'Çocukları özlemle bekleyen kutu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Benzetme ve kişileştirme içeren dört söz sanatı kartı.', 21)


def bir_guzel_hediye_karti():
    ic = kutu(6, 6, 588, 86, TUR_A, TUR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, TUR, TUR, 9, 1)
    ic += yazi(300, 24, 'METİN ÖZETİ · BİR GÜZEL HEDİYE', '#fff', kalin=True)
    ic += yazi(300, 50, 'Ahmet el emeğiyle yaptığı ahşap oyuncağı en yakın arkadaşıyla paylaşır.', LAC, kalin=True)
    ic += yazi(300, 74, 'Bu güzel hediye iki arkadaş arasındaki dostluk bağını ve mutluluğu büyütür.', LAC)
    return svg(600, 98, ic, 'Bir Güzel Hediye metninin anahtar kavramlarını içeren özet kartı.', 21)


def oykuleyici_metin_asamalari():
    kartlar = [
        ('1. Tahmin', 'Başlık ve görsel inceleme', MAVI, MAVI_A),
        ('2. Serim', 'Kişi, yer, zaman girişi', YES, YES_A),
        ('3. Düğüm', 'Olay ve merakın artışı', TUR, TUR_A),
        ('4. Çözüm', 'Sonuç ve ana fikir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Okuma öncesi tahmin, serim, düğüm ve çözüm aşamaları kartları.', 21)


def yazim_denetimi_panosu():
    satirlar = [
        ('I. Cümle', 'Mustafa Kemal 1881 yılında Selanik’te dünyaya geldi.', YES, YES_A),
        ('II. Cümle', 'Babası Ali Rıza Efendi, annesi ise Zübeyde Hanım’dır.', MAVI, MAVI_A),
        ('III. Cümle (!)', 'Okulumuzda 29 ekim Cumhuriyet bayramı coşkuyla kutlandı.', KIR, KIR_A),
        ('IV. Cümle', 'Küçük Mustafa eğitimine Şemsi Efendi Okulunda devam etti.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 92, 22, renk, renk, 6, 1)
        ic += yazi(52, y + 15, no, '#fff', kalin=True)
        ic += yazi(108, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'Büyük harf ve kesme işareti kurallarını içeren dört cümle panosu.', 21)


def konusma_becerisi_karti():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(149, 25, '1. Beden Dili Kuralları', YESIL_K, kalin=True)
    ic += yazi(149, 50, '• Dinleyicilerle göz teması kurmak', LAC, kalin=True)
    ic += yazi(149, 74, '• Doğal jest ve mimik kullanmak', LAC)

    ic += kutu(308, 6, 286, 86, MOR_A, MOR, 9, 1.4)
    ic += yazi(451, 25, '2. Bağlantı ve Geçiş İfadeleri', MOR, kalin=True)
    ic += yazi(451, 50, '• Açıklama: çünkü, özellikle', LAC, kalin=True)
    ic += yazi(451, 74, '• Özetleme: kısacası, sonuç olarak', LAC)
    return svg(600, 98, ic, 'Hazırlıksız konuşmada beden dili ve bağlantı ifadeleri kartı.', 21)


def mustafa_yuzey_anlam_karti():
    ic = kutu(6, 6, 588, 88, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'DİNLEME METNİ BİLGİ KARTI · MUSTAFA', '#fff', kalin=True)
    ic += yazi(300, 50, '• Yer: Selanik · Aile: Zübeyde Hanım ve Ali Rıza Efendi eğitime büyük önem verir.', LAC, kalin=True)
    ic += yazi(300, 74, '• Özellik: Küçük Mustafa tarih, edebiyat ve vatan sevgisi konulu kitapları çok sever.', LAC)
    return svg(600, 100, ic, 'Mustafa metninde doğrudan verilen yüzey anlam bilgilerini içeren kart.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ruzgar_soz_sanati_karti()
    s[4]['gorsel'] = baglanti_ifadeleri_kartlari()
    s[5]['gorsel'] = soz_sanati_tablo_kartlari()
    s[6]['gorsel'] = bir_guzel_hediye_karti()
    s[7]['gorsel'] = oykuleyici_metin_asamalari()
    s[8]['gorsel'] = yazim_denetimi_panosu()
    s[10]['gorsel'] = konusma_becerisi_karti()
    s[11]['gorsel'] = mustafa_yuzey_anlam_karti()
