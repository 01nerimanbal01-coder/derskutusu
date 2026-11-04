"""5. sınıf Din Kültürü ve Ahlak Bilgisi 5. hafta (Allah’ın Güzel İsimleri: Hâlık, Rezzak, Âlim, Semi, Basir ve Kadir) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def gunluk_yasam_baglam_kartlari():
    kartlar = [
        ('1. Kart · er-Rezzak', 'Fidanın meyve verip besin olması', YES, YES_A),
        ('2. Kart · el-Basir (!)', 'Sessizce edilen duanın duyulması', KIR, KIR_A),
        ('3. Kart · es-Semi (!)', 'Gizli yapılan iyiliğin görülmesi', TUR, TUR_A),
        ('4. Kart · el-Hâlık (!)', 'Keresteden masa imal edilmesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Günlük yaşam olayları ve güzel isimlerin bağlam kartları.', 20)


def alim_semi_basir_tablosu():
    satirlar = [
        ('Güzel İsim: K', 'İnsan öğrenir ve unutur; Allah her şeyi her an bilir.', MAVI, MAVI_A),
        ('Güzel İsim: es-Semi', 'İnsan yakını duyar; Allah en kısık fısıltıyı bile işitir.', YES, YES_A),
        ('Güzel İsim: el-Basir', 'İnsan ışığa muhtaçtır; Allah ise: L', MOR, MOR_A),
    ]
    ic = ''
    for i, (sol, sag, renk, arka) in enumerate(satirlar):
        y = 6 + i * 31
        ic += kutu(6, y, 588, 27, arka, renk, 7, 1.3)
        ic += kutu(6, y, 160, 27, renk, renk, 7, 1)
        ic += yazi(86, y + 18, sol, '#fff', kalin=True)
        ic += yazi(178, y + 18, sag, LAC, 'start', kalin=(i in (0, 2)))
    return svg(600, 100, ic, 'Âlim, Semi ve Basir isimlerinin insan özellikleriyle karşılaştırma tablosu.', 20)


def dort_ayet_tefekkur_kartlari():
    kartlar = [
        ('1. Zâriyât Suresi 58. Ayet', 'Kullarına nimet ve besin ulaştırması', YES, YES_A),
        ('2. Şûrâ Suresi 11. Ayet', 'Her sesi ve duayı aracısız duyması', MAVI, MAVI_A),
        ('3. Mülk Suresi 14. Ayet', 'Gönüllerdeki gizli niyetleri bilmesi', TUR, TUR_A),
        ('4. Yâsîn Suresi 82. Ayet', 'Dilediği her şeye gücünün yetmesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört ayet vurgusu ve esmayıhüsna eşleştirme kartları.', 20)


def kadir_calisma_panosu():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, 'A Kartı · Yanlış Anlayış', KIR, kalin=True)
    ic += yazi(149, 50, '“Allah Kadir olduğu için hiç', LAC)
    ic += yazi(149, 72, 'çalışmasam da sınavı kazanırım.”', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'B Kartı · Doğru Anlayış', YESIL_K, kalin=True)
    ic += yazi(451, 50, '“Önce düzenli çalışıp görevimi yapar,', LAC)
    ic += yazi(451, 72, 'sonucu Kadir olan Allah’tan dilerim.”', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'el-Kadir isminin çalışma ve dua ile ilişkisini gösteren A ve B kartları.', 20)


def tohum_ekmek_sureci():
    kartlar = [
        ('1. Aşama · el-Hâlık', 'Tohum ve toprağın yaratılması', MAVI, MAVI_A),
        ('2. Aşama · el-Âlim', 'Tohumun ihtiyacının bilinmesi', TUR, TUR_A),
        ('3. Aşama · el-Kadir', 'Yağmurla başak çıkarılması', MOR, MOR_A),
        ('4. Aşama · er-Rezzak', 'Ekmeğin sofraya sunulması', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Buğday tohumundan sofradaki ekmeğe uzanan süreçte tecelli eden isimler.', 20)


def durustluk_olay_karti():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'ÖRNEK DAVRANIŞ KARTI · KİMSE GÖRMEZKEN DÜRÜSTLÜK', '#fff', kalin=True)
    ic += yazi(300, 50, 'Issız koridorda yerde bir cüzdan bulan öğrenci, etrafta kimse olmamasına rağmen', LAC)
    ic += yazi(300, 74, '“Rabbim yaptığım her davranışı görür ve kalbimdeki niyeti bilir.” diyerek teslim eder.', LAC, kalin=True)
    return svg(600, 98, ic, 'Kimse görmezken dürüst davranan öğrencinin hatırladığı güzel isimler kartı.', 20)


def yapma_yaratma_karti():
    ic = kutu(6, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(149, 25, 'İnsanın Yapması (Üretmesi)', TUR, kalin=True)
    ic += yazi(149, 50, '• Hazır malzemeyi (ağaç, demir) kullanır.', LAC, kalin=True)
    ic += yazi(149, 74, '• Gücü sınırlıdır; yaptığı eşya zamanla eskir.', LAC)

    ic += kutu(308, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(451, 25, 'Allah’ın Yaratması (el-Hâlık)', MAVI, kalin=True)
    ic += yazi(451, 50, '• Örneksiz ve yoktan var eder.', LAC, kalin=True)
    ic += yazi(451, 74, '• Sınırsızdır; kurduğu düzen kusursuz işler.', LAC)
    return svg(600, 98, ic, 'İnsanın yapması ile Allah’ın yaratması arasındaki farkları gösteren kart.', 20)


def davranis_yansima_panosu():
    kartlar = [
        ('er-Rezzak Bilinci', 'Nimete şükretmek ve paylaşmak', YES, YES_A),
        ('el-Basir & el-Âlim', 'Her yerde dürüst ve samimi olmak', MAVI, MAVI_A),
        ('el-Hâlık Bilinci', 'Yaratılan her canlıya merhamet', TUR, TUR_A),
        ('el-Kadir Bilinci', 'Zorlukta çalışıp umudu korumak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Güzel isimlerin günlük davranışlarımıza yansımasını özetleyen pano.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gunluk_yasam_baglam_kartlari()
    s[4]['gorsel'] = alim_semi_basir_tablosu()
    s[5]['gorsel'] = dort_ayet_tefekkur_kartlari()
    s[6]['gorsel'] = kadir_calisma_panosu()
    s[7]['gorsel'] = tohum_ekmek_sureci()
    s[8]['gorsel'] = durustluk_olay_karti()
    s[10]['gorsel'] = yapma_yaratma_karti()
    s[11]['gorsel'] = davranis_yansima_panosu()
