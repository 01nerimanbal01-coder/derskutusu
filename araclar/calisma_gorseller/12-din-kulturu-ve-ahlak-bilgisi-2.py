"""12. sınıf Din Kültürü 2. hafta (Bilim Kurumları ve Kevnî Ayetler) çalışma kâğıdı görselleri.
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


def dort_bilim_kurumu_karti():
    kurumlar = [
        ('1. Beytülhikme', 'Tercüme &amp; Büyük Kütüphane', YES, YES_A),
        ('2. Darüşşifa', 'Tıp Eğitimi &amp; Klinik Tedavi', MAVI, MAVI_A),
        ('3. Rasathane', 'Gözlemevi &amp; Astronomi Cetveli', TUR, TUR_A),
        ('4. Medrese', 'Dini &amp; Pozitif Bilimler', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kurumlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel İslam bilim kurumu bilgi kartı.', 34)


def beytulhikme_harita_karti():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'İSLAM BİLİM HAVZALARI VE BEYTÜLHİKME (BAĞDAT)', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Tercüme Hareketi', 10.0, YES)
    ic += yazi(95, 74, 'Grekçe, Süryanice, Farsça', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Özgün Üretim', 10.0, TUR)
    ic += yazi(265, 74, 'Matematik, astronomi, tıp', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Beytülhikme ve bilim havzaları şeması.', 34)


def meraga_rasathane_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'MERAGA RASATHANESİ VE ASTRONOMİ MİRASI', 10.6, MAVI)
    ic += yazi(180, 52, 'Kurucu: Nasîrüddin Tûsî (1259) · Meraga (İran)', 10.0, LAC)
    ic += yazi(180, 76, 'Zîc-i İlhânî adlı astronomi cetveliyle gezegen hareketleri hesaplandı.', 9.3, MAVI, ince=True)
    return svg(360, 110, ic, 'Meraga Rasathanesi tanıtım panosu.', 34)


def akil_vahiy_butunlugu_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Vahyin Rehberliği', 10.4, YES)
    ic += yazi(91, 50, 'Ahlaki gaye &amp; varoluş', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Kevnî ayetlerle tefekkür', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Aklın İşlevi', 10.4, TUR)
    ic += yazi(269, 50, 'Deney, gözlem &amp; ispat', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'Evrendeki nizamı çözümler', 9.4, TUR)
    return svg(360, 110, ic, 'Akıl ve vahiy bütünlüğü kartı.', 34)


def egitim_kurumlari_tarih_siralamasi():
    adımlar = [
        ('1. Suffe', 'Mescid-i Nebevî mektebi', YES, YES_A),
        ('2. Beytülhikme', 'Bağdat tercüme sarayı', MAVI, MAVI_A),
        ('3. Nizamiye', 'Selçuklu medreseleri', TUR, TUR_A),
        ('4. Rasathane', 'Semerkant gözlemevi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Eğitim ve bilim kurumları ortaya çıkış kronolojisi.', 34)


def al_i_imran_ayet_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'ÂL-İ İMRÂN SURESİ 190. AYET TAHLİLİ', 10.6, MOR)
    ic += yazi(180, 52, '“Göklerin ve yerin yaratılışında, akıl sahipleri için deliller vardır.”', 10.0, LAC)
    ic += yazi(180, 76, 'Kevnî ayetler insanı evrendeki fiziksel ve kozmik nizamı incelemeye çağırır.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Âl-i İmrân 190. ayet panosu.', 34)


def dort_bilgin_karti():
    bilginler = [
        ('Harezmi', 'Cebir &amp; Algoritma', MAVI, MAVI_A),
        ("İbnü-l Heysem", "Optik &amp; Işık Bilimi", YES, YES_A),
        ('İbn Sina', 'El-Kanun &amp; Tıp', TUR, TUR_A),
        ('Biruni', 'Astronomi &amp; Trigonometri', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(bilginler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört büyük Müslüman bilgin kartı.', 34)


def sifre_din_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'İSLAM MEDENİYETİ VE ASTRONOMİ PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'RASATHANE · AKIL · SUFFE · ASTRONOMİ · TEFEKKÜR', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli gökbilim kavramını (5 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre din kültürü kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_bilim_kurumu_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = beytulhikme_harita_karti()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = meraga_rasathane_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = akil_vahiy_butunlugu_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = egitim_kurumlari_tarih_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = al_i_imran_ayet_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_bilgin_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_din_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
