"""6. sınıf DKAB 7. hafta (Bir Sure Öğreniyorum: Felak Suresi ve Anlamı — 1. Ünite Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155); ayet levhası yok (K055)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def sure_kimlik_karti():
    ic = kutu(8, 6, 584, 96, YES_A, YES, 9, 1.6)
    ic += kutu(8, 6, 584, 24, YES, YES, 9, 1)
    ic += yazi(300, 22, 'FELAK SURESİ KİMLİK KARTI (113. SURE)', 11.2, '#fff')
    alanlar = [
        ('İndirildiği Dönem', '? (1)', MAVI, MAVI_A),
        ('Ayet Sayısı', '? (2)', TUR, TUR_A),
        ('Adının Anlamı', '? (3)', MOR, MOR_A),
    ]
    for i, (bas, deger, renk, arka) in enumerate(alanlar):
        x = 20 + i * 190
        ic += kutu(x, 38, 178, 56, arka, renk, 7, 1.4)
        ic += yazi(x + 89, 58, bas, 10.6, LAC)
        ic += yazi(x + 89, 80, deger, 11.4, renk)
    return svg(600, 108, ic, 'Felak suresi kimlik kartı: indirildiği dönem, ayet sayısı ve adının anlamı soru işaretli.', 22)


def okuma_panosu():
    satirlar = [
        ('1. Ayet', 'Kul eûzü birabbi’l-felak.', YES, YES_A),
        ('2. Ayet', 'Min şerri mâ halak.', MAVI, MAVI_A),
        ('3. Ayet', 'Ve min şerri gâsikın izâ vekab.', CAM, CAM_A),
        ('4. Ayet', '?  (Boş bırakılan ayet)', TUR, TUR_A),
        ('5. Ayet', 'Ve min şerri hâsidin izâ hased.', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, okunus, renk, arka) in enumerate(satirlar):
        x = 8 + (i % 2) * 296 if i < 4 else 156
        y = 6 + (i // 2) * 34 if i < 4 else 74
        w = 288 if i < 4 else 288
        ic += kutu(x, y, w, 28, arka, renk, 6, 1.4)
        ic += kutu(x, y, 72, 28, renk, renk, 6, 1)
        ic += yazi(x + 36, y + 18, no, 10.4, '#fff')
        ic += yazi(x + 180, y + 18, okunus, 10.4, LAC, ince=(i != 3))
    return svg(600, 108, ic, 'Felak suresinin beş ayetlik okunuş panosu; 4. ayet soru işaretli.', 23)


def ayet_meal_kartlari():
    kartlar = [
        ('1. Ayet', 'Kul eûzü birabbi’l-felak → Sabahın Rabbine sığınırım', YES, YES_A),
        ('2. Ayet', 'Halak = Yarattığı varlıklar · Şer = Kötülük', MAVI, MAVI_A),
        ('3. Ayet', 'Gâsikın izâ vekab = Karanlığı çöktüğü zaman gece', CAM, CAM_A),
        ('5. Ayet', 'Hâsidin izâ hased = Kıskandığı vakit kıskanç (hasetçi)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ipucu, renk, arka) in enumerate(kartlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(51, y + 15, bas, 10.4, '#fff')
        ic += yazi(106, y + 15, ipucu, 10.3, LAC, 'start', ince=True)
    return svg(600, 112, ic, 'Felak suresi ayet ve kavram ipucu kartları.', 22)


def gece_sabah_semasi():
    ic = kutu(8, 8, 260, 84, '#1e293b', LAC, 9, 1.6)
    ic += f'<circle cx="52" cy="48" r="18" fill="#fde68a"/><circle cx="60" cy="42" r="15" fill="#1e293b"/>'
    ic += yazi(162, 38, 'Zifiri Gece Karanlığı (Gâsık)', 10.8, '#fff')
    ic += yazi(162, 62, 'Korku, darlık ve tehlikeler', 10.2, '#cbd5e1', ince=True)

    ic += f'<line x1="276" y1="50" x2="320" y2="50" stroke="{TUR}" stroke-width="2.4"/>'
    ic += f'<polygon points="320,44 332,50 320,56" fill="{TUR}"/>'
    ic += yazi(302, 38, 'el-Felak', 10.4, TUR)

    ic += kutu(336, 8, 256, 84, TUR_A, TUR, 9, 1.6)
    ic += f'<circle cx="380" cy="50" r="18" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(486, 38, 'Sabah Aydınlığı (Tan Yeri)', 10.8, LAC)
    ic += yazi(486, 62, 'Ferahlık, güven ve ilahi koruma', 10.2, SOLUK, ince=True)
    return svg(600, 100, ic, 'Gece karanlığından sabah aydınlığına geçişi gösteren el-Felak şeması.', 22)


def haset_gipta_kartlari():
    ic = kutu(8, 8, 284, 86, KIR_A, KIR, 9, 1.6)
    ic += kutu(8, 8, 284, 24, KIR, KIR, 9, 1)
    ic += yazi(150, 24, 'Kerem’in Düşüncesi (1. Kart)', 10.8, '#fff')
    ic += yazi(150, 52, '“Keşke arkadaşımın proje ödevi', 10.4, LAC, ince=True)
    ic += yazi(150, 72, 'kaybolsa da birinci olamasa!”', 10.4, KIR)

    ic += kutu(308, 8, 284, 86, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 24, YES, YES, 9, 1)
    ic += yazi(450, 24, 'Mert’in Düşüncesi (2. Kart)', 10.8, '#fff')
    ic += yazi(450, 52, '“Arkadaşım çok güzel çalışmış; Rabbim', 10.4, LAC, ince=True)
    ic += yazi(450, 72, 'bana da böyle başarı nasip etsin.”', 10.4, YES)
    return svg(600, 102, ic, 'Kerem’in haset içeren düşüncesi ile Mert’in gıpta içeren düşüncesini karşılaştıran iki kart.', 22)


def dort_kalkan_kartlari():
    kartlar = [
        ('1. Kalkan', 'Tedbir alıp Allah’a dua etmek', YES, YES_A),
        ('2. Kalkan', 'Dedikodu ve fitneden uzak durmak', MAVI, MAVI_A),
        ('3. Kalkan', 'Muavvizeteyn surelerini okumak', CAM, CAM_A),
        ('4. Kalkan', 'Falcı ve büyücülere inanmak (!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 78, 30, renk, renk, 6, 1)
        ic += yazi(x + 45, y + 25, bas, 10.4, '#fff')
        ic += yazi(x + 188, y + 25, metin, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Dört kalkan kartı: tedbir ve dua, fitneden uzak durma, Muavvizeteyn okuma ve falcıya inanma.', 22)


def batil_istiaze_karsilastirma():
    ic = kutu(8, 8, 284, 82, KIR_A, KIR, 9, 1.6)
    ic += yazi(150, 28, 'Batıl İnanç Nesneleri (Yanlış)', 10.8, KIR)
    ic += yazi(150, 50, 'Nazar boncuğu, at nalı, kurşun dökme', 10.3, LAC, ince=True)
    ic += yazi(150, 70, '→ Cansız nesnelerden koruma beklemek', 10.2, KIR)

    ic += kutu(308, 8, 284, 82, YES_A, YES, 9, 1.6)
    ic += yazi(450, 28, 'İstiâze Bilinci (Tevhid İnancı)', 10.8, YES)
    ic += yazi(450, 50, '“Kul eûzü birabbi’l-felak” duası', 10.3, LAC, ince=True)
    ic += yazi(450, 70, '→ Yalnızca Yüce Allah’a sığınmak', 10.2, YES)
    return svg(600, 98, ic, 'Batıl inanç nesneleri ile istiâze bilincini karşılaştıran iki bilgi kartı.', 22)


def unite_degerlendirme_panosu():
    adimlar = [
        ('1. Peygamberler', 'İnsanlara rehber ve örnek olur', MAVI, MAVI_A),
        ('2. İlahi Kitaplar', 'İyi ile kötüyü vahiyle açıklar', MOR, MOR_A),
        ('3. Felak Suresi', 'Kötülüklerden Allah’a sığındırır', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 76, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 24, renk, renk, 9, 1)
        ic += yazi(x + 94, 24, bas, 10.8, '#fff')
        ic += yazi(x + 94, 56, alt, 10.3, LAC, ince=True)
    return svg(600, 92, ic, '1. ünite genel değerlendirme panosu: Peygamberler, İlahi Kitaplar ve Felak Suresi.', 22)


def unite_kavram_agi():
    kutular = [
        ('1. Kutu: Peygamber Sıfatları', 'Sıdk · Emanet · Fetanet · İsmet · Tebliğ', MAVI, MAVI_A),
        ('2. Kutu: İlahi Kitap Eşlemesi (!)', 'Tevrat → Hz. Davut (?) · Zebur → Hz. Musa (?)', KIR, KIR_A),
        ('3. Kutu: Vahyin Amacı', 'Akla rehberlik ve dünya-ahiret mutluluğu', YES, YES_A),
        ('4. Kutu: Muavvizeteyn', 'Felak (113) ve Nâs (114) koruyucu sureleri', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kutular):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 10.5, renk)
        ic += yazi(x + 144, y + 34, alt, 10.1, LAC, ince=True)
    return svg(600, 104, ic, '1. ünite kavram ağı: dört kutudan ikincisinde Tevrat ve Zebur eşleştirmesi ters verilmiş.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sure_kimlik_karti()
    s[4]['gorsel'] = okuma_panosu()
    s[5]['gorsel'] = ayet_meal_kartlari()
    s[6]['gorsel'] = gece_sabah_semasi()
    s[8]['gorsel'] = haset_gipta_kartlari()
    s[9]['gorsel'] = dort_kalkan_kartlari()
    s[10]['gorsel'] = batil_istiaze_karsilastirma()
    s[12]['gorsel'] = unite_degerlendirme_panosu()
    s[13]['gorsel'] = unite_kavram_agi()
