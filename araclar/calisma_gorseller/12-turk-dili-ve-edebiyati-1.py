"""12. sınıf Edebiyat 1. hafta (Edebiyatın İlişkileri ve Sözlükler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_tarihi_sozluk_karti():
    sozlukler = [
        ('1. Divânu Lugât', '11. yy · Kaşgarlı Mahmud', MAVI, MAVI_A),
        ('2. Mukaddime', '12. yy · Zemahşerî', YES, YES_A),
        ('3. Muhâkemetü', '15. yy · Ali Şîr Nevâî', TUR, TUR_A),
        ('4. Kamus-ı Türkî', '19. yy · Şemsettin Sami', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(sozlukler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' · ')[1], 8.8, LAC, ince=True)
    return svg(360, 110, ic, 'Dört tarihî Türkçe sözlük bilgi kartı.', 34)


def edebiyat_bilim_iliskisi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'EDEBİYATIN BİLİM DALLARIYLA ETKİLEŞİMİ', 10.6, YES)
    ic += kutu(16, 38, 98, 56, MAVI_A, MAVI)
    ic += yazi(65, 56, 'Felsefe', 9.8, MAVI)
    ic += yazi(65, 74, 'Varlık sorgusu', 9.0, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, TUR_A, TUR)
    ic += yazi(180, 56, 'Psikoloji [?]', 9.8, TUR)
    ic += yazi(180, 74, 'Bilinç akışı &amp; içsel', 9.0, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, MOR_A, MOR)
    ic += yazi(295, 56, 'Sosyoloji', 9.8, MOR)
    ic += yazi(295, 74, 'Toplum &amp; insan', 9.0, LAC, ince=True)
    return svg(360, 110, ic, 'Edebiyatın diğer bilim dallarıyla kurduğu bağ şeması.', 34)


def kasgarli_tanitim_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'DİVÂNU LUGÂTİ’T-TÜRK (11. YÜZYIL)', 10.6, MAVI)
    ic += yazi(180, 52, 'Kaşgarlı Mahmud · İlk Türkçe Sözlük ve Dil Ansiklopedisi', 10.0, LAC)
    ic += yazi(180, 76, 'Türkçenin zenginliğini ve Araplara Türkçeyi öğretmeyi hedefler.', 9.3, MAVI, ince=True)
    return svg(360, 110, ic, 'Kaşgarlı Mahmud ve ilk Türkçe sözlük tanıtım panosu.', 34)


def edebiyat_felsefe_ortak_alan():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Edebiyat ve Felsefe', 10.2, YES)
    ic += yazi(91, 50, 'Varlığı ve insanı sorgular', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Dilsel anlatım aracılığı', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Psikolojik Derinlik', 10.2, TUR)
    ic += yazi(269, 50, 'Ruhsal çözümlemeler', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'İç konuşma &amp; çatışma', 9.4, TUR)
    return svg(360, 110, ic, 'Edebiyat ve düşünce disiplinleri ortak alanı.', 34)


def sozlukler_kronoloji_siralamasi():
    sozlukler = [
        ('1. Divânu Lugât', '11. yy · Karahanlı', MAVI, MAVI_A),
        ('2. Mukaddime', '12. yy · Harezm', YES, YES_A),
        ('3. Muhâkemetü', '15. yy · Çağatay', TUR, TUR_A),
        ('4. Kamus-ı Türkî', '19. yy · Osmanlı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(sozlukler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Türk sözlükçülük tarihi kronolojik sıralaması.', 34)


def metin_tahlil_felsefe_karti():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'METİN TAHLİLİ · VAROLUŞ SORGUSU', 10.6, MOR)
    ic += yazi(180, 52, '“İnsan, seçimleriyle kendi özünü inşa eder; adalet vicdanda başlar.”', 10.0, LAC)
    ic += yazi(180, 76, 'Edebiyat ve felsefe; insan varoluşunu dille sorgulayan ortak alanlardır.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Metin tahlili ve felsefe ilişkisi panosu.', 34)


def dort_alan_tanim_karti():
    alanlar = [
        ('Felsefe', 'Soyut Varlık Sorgusu', MAVI, MAVI_A),
        ('Psikoloji', 'Ruhsal Süreç Tahlili', YES, YES_A),
        ('Sözlükçülük', 'Söz Varlığı Kaydı', TUR, TUR_A),
        ('Dil Değişimi', 'Tarihsel Dönüşüm', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(alanlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört araştırma alanı ve nitelikleri kartı.', 34)


def sifre_edebiyat_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'TÜRKÇENİN SÖZLÜK MİRASI VE DİLİN ZENGİNLİĞİ', 10.8, CAM)
    ic += yazi(180, 50, 'SAMİ · ÖZLEM · ZEMAHŞERÎ · LUGAT · ÜSLUP · KAŞGARLI', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli edebiyat terimini (6 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre edebiyat kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_tarihi_sozluk_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = edebiyat_bilim_iliskisi()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = kasgarli_tanitim_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = edebiyat_felsefe_ortak_alan()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = sozlukler_kronoloji_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = metin_tahlil_felsefe_karti()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_alan_tanim_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_edebiyat_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
