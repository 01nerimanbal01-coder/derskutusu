"""7. sınıf İngilizce 2. hafta (Appearance and Personality: Kişi Tanıtma ve Not Tablosu) çalışma kâğıdı görselleri.
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


def konusma_not_karti():
    notlar = [
        ('Height', 'of medium height', MAVI, MAVI_A),
        ('Weight', 'of medium weight', TUR, TUR_A),
        ('Hair', 'long · wavy · fair', MOR, MOR_A),
        ('Personality', 'friendly · honest', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(notlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 25, bas, 10.8, r)
        ic += f'<line x1="{x + 14}" y1="32" x2="{x + 128}" y2="32" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 71, 53, alt, 10.1, LAC, ince=True)
    return svg(600, 80, ic, 'Dinleme sırasında başlıklara göre alınan kısa not kartları.', 15)


def tanim_sifat_kartlari():
    kartlar = [
        ('1. Kart · never changes mind', 'Eşleşen sıfat: stubborn', MAVI, MAVI_A),
        ('2. Kart · doesn’t worry', 'Eşleşen sıfat: easy-going', YES, YES_A),
        ('3. Kart · only thinks of himself', 'Eşleşen sıfat: generous (!)', KIR, KIR_A),
        ('4. Kart · loves meeting people', 'Eşleşen sıfat: outgoing', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'İngilizce davranış tanımlarından kişilik sıfatına geçiş kartları.', 16)


def dil_bilgisi_rehberi():
    ic = kutu(6, 6, 286, 76, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Fiil Seçim Kuralı (is · has · likes)', 10.8, MAVI)
    ic += yazi(149, 46, '• Boy, kilo, yaş ve kişilik → is (She is tall)', 10.0, LAC, ince=True)
    ic += yazi(149, 65, '• Saç ve göz → has (She has hazel eyes)', 10.0, MAVI)

    ic += kutu(308, 6, 286, 76, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Belirsiz Artikel Kuralı (a · an)', 10.8, YES)
    ic += yazi(451, 46, '• Ünlü sesle başlayan sıfat → an easy-going', 10.0, LAC, ince=True)
    ic += yazi(451, 65, '• Ünsüz sesle başlayan sıfat → a punctual', 10.0, YES)
    return svg(600, 88, ic, 'Kişi tanıtımında is, has, likes ve a, an kuralları.', 16)


def ayirt_edici_ipucu_panosu():
    kartlar = [
        ('Arda’nın Özellikleri', 'Boy: tall · Göz: brown', 'Aksesuar: yok', MAVI, MAVI_A),
        ('Bora’nın Özellikleri', 'Boy: tall · Göz: brown', 'Ayırt edici: wears glasses', YES, YES_A),
        ('Can’ın Özellikleri', 'Boy: tall · Göz: brown', 'Aksesuar: yok', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.8, r)
        ic += yazi(x + 96, 46, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.2, r)
    return svg(600, 86, ic, 'Üç öğrencinin ortak özellikleri ve Bora yı ayıran wears glasses ipucu.', 16)


def dinleme_aktarma_adimlari():
    adimlar = [
        ('1. Başlıkları Yaz', 'Height, Weight, Hair...', MAVI, MAVI_A),
        ('2. Kısa Not Al', 'Anahtar sözcükleri yaz', TUR, TUR_A),
        ('3. Eksiği Dinle', 'Boş başlığa odaklan', MOR, MOR_A),
        ('4. Cümleye Çevir', 'is, has ve likes kullan', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Dinlerken not alma ve tam cümleye çevirme basamakları.', 15)


def hatali_defter_karti():
    ic = kutu(6, 6, 286, 70, KIR_A, KIR, 8, 1.5)
    ic += yazi(149, 25, 'Hatalı Cümle 1 (Boy ve Kilo)', 10.8, KIR)
    ic += yazi(149, 48, '“He has tall and slim.” (Yanlış fiil!)', 10.3, LAC, ince=True)
    ic += yazi(149, 65, 'Boy ve kilo “has” ile söylenmez.', 10.0, KIR)

    ic += kutu(308, 6, 286, 70, KIR_A, KIR, 8, 1.5)
    ic += yazi(451, 25, 'Hatalı Cümle 2 (Göz Rengi)', 10.8, KIR)
    ic += yazi(451, 48, '“He is green eyes.” (Yanlış fiil!)', 10.3, LAC, ince=True)
    ic += yazi(451, 65, 'Göz ve saç “is” ile söylenmez.', 10.0, KIR)
    return svg(600, 82, ic, 'Boy-kilo ve saç-göz anlatımında yapılan fiil hataları kartı.', 15)


def defne_profil_tablosu():
    sutunlar = [
        ('Name', 'Defne', LAC, GRI_A),
        ('Appearance', 'slim · short, wavy hair', MAVI, MAVI_A),
        ('Personality', 'polite · helpful', YES, YES_A),
        ('Hobbies', 'riding a bike', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(sutunlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 25, bas, 10.8, r)
        ic += f'<line x1="{x + 12}" y1="32" x2="{x + 130}" y2="32" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 71, 53, alt, 10.0, LAC, ince=True)
    return svg(600, 80, ic, 'Defne nin görünüş, kişilik ve hobi notlarını içeren tablo.', 15)


def iki_soru_fark_karti():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 25, '1. Soru: What does Emre look like?', 10.6, MAVI)
    ic += yazi(149, 47, 'Odak: Appearance (Dış görünüş)', 10.1, LAC, ince=True)
    ic += yazi(149, 64, 'İpucu: tall, slim, dark hair, brown eyes', 10.0, MAVI)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 25, '2. Soru: What is Emre like?', 10.6, YES)
    ic += yazi(451, 47, 'Odak: Personality (Kişilik özellikleri)', 10.1, LAC, ince=True)
    ic += yazi(451, 64, 'İpucu: generous, outgoing, honest', 10.0, YES)
    return svg(600, 84, ic, 'look like ve be like soru kalıplarının karşılaştırma kartı.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = konusma_not_karti()
    s[1]['gorsel'] = tanim_sifat_kartlari()
    s[3]['gorsel'] = dil_bilgisi_rehberi()
    s[5]['gorsel'] = ayirt_edici_ipucu_panosu()
    s[6]['gorsel'] = dinleme_aktarma_adimlari()
    s[7]['gorsel'] = hatali_defter_karti()
    s[8]['gorsel'] = defne_profil_tablosu()
    s[11]['gorsel'] = iki_soru_fark_karti()
