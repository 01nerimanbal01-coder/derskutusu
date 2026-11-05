"""6. sınıf Din Kültürü ve Ahlak Bilgisi 14. hafta çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#475569'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: Takva - İhlas - Öz Denetim üçlü kart
    ic0 = kutu(4, 4, 352, 107, GRI_A, GRI)
    kartlar = [
        ('TAKVA', 'Günahlardan sakınma', 'Bakara · 183', YES, YES_A),
        ('İHLAS', 'Gösterişsiz samimiyet', 'Yalnız Allah için', MAVI, MAVI_A),
        ('ÖZ DENETİM', 'İrade ve nefis terbiyesi', 'İçsel kontrol', MOR, MOR_A),
    ]
    for i, (b, a1, a2, c, d) in enumerate(kartlar):
        x = 10 + i * 115
        ic0 += kutu(x, 11, 110, 93, d, c)
        ic0 += yazi(x + 55, 31, b, 9.6, c)
        ic0 += f'<line x1="{x+10}" y1="40" x2="{x+100}" y2="40" stroke="{c}" stroke-width="0.7"/>'
        ic0 += yazi(x + 55, 62, a1, 8.3, LAC)
        ic0 += yazi(x + 55, 84, a2, 8.0, SOLUK, ince=True)
    s[0]['gorsel'] = svg(ic0, 'Takva, ihlas ve öz denetim kavram kartları')

    # s[1]: Bakara 183. ayet levhası ve hilal motifi
    ic1 = kutu(6, 6, 348, 103, YES_A, YES)
    # Hilal ve yıldız (geometrik, insansız)
    ic1 += f'<path d="M48,32 A24,24 0 1,0 48,82 A19,19 0 1,1 48,32 Z" fill="{YES}"/>'
    ic1 += kutu(76, 15, 266, 85, '#f8fafc', YES, r=6, kalin=0.8)
    ic1 += yazi(209, 34, 'Bakara Suresi · 183. Ayet Meali', 9.2, YES)
    ic1 += yazi(209, 55, '«Ey iman edenler! Allah’a karşı gelmekten', 8.5, LAC, ince=True)
    ic1 += yazi(209, 71, 'sakınmanız (takvaya ulaşmanız) için oruç', 8.5, LAC)
    ic1 += yazi(209, 87, 'sizden öncekiler gibi size de farz kılındı.»', 8.5, LAC, ince=True)
    s[1]['gorsel'] = svg(ic1, 'Bakara Suresi 183. ayet meali levhası')

    # s[2]: 3 Hadis / İlke sütunu
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [
        ('1. Hadis İlkesi', '«Oruç sabrın', 'yarısıdır.»', MAVI, MAVI_A),
        ('2. Hadis İlkesi', '«Oruç kalkandır;', 'kavga etmesin.»', TUR, TUR_A),
        ('3. İftar Bilinci', 'Bir yudum suyun', 'değerini anlama', CAM, CAM_A),
    ]
    for i, (b, s1, s2, c, d) in enumerate(ilkeler):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        ic2 += yazi(x + 55, 29, b, 8.8, c)
        ic2 += f'<line x1="{x+10}" y1="38" x2="{x+100}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic2 += yazi(x + 55, 62, s1, 8.5, LAC)
        ic2 += yazi(x + 55, 80, s2, 8.5, LAC)
    s[2]['gorsel'] = svg(ic2, 'Sabır, kalkan ve şükür ilkeleri')

    # s[5]: Dilin ve Kalbin Orucu hadis kartı
    ic5 = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic5 += yazi(180, 24, 'Bütün Organların Orucu · Hadis-i Şerif', 9.4, TUR)
    ic5 += kutu(18, 34, 324, 64, '#f8fafc', TUR, r=5, kalin=0.8)
    ic5 += yazi(180, 54, '«Kim yalan konuşmayı ve yalanla iş yapmayı terk etmezse,', 8.4, LAC)
    ic5 += yazi(180, 72, 'Allah’ın o kimsenin yemesini ve içmesini', 8.4, LAC, ince=True)
    ic5 += yazi(180, 88, 'bırakmasına hiçbir ihtiyacı yoktur.» (Buhârî)', 8.4, KIR)
    s[5]['gorsel'] = svg(ic5, 'Yalandan sakınma konulu hadis kartı')

    # s[6]: Neden-sonuç zinciri (Açlığı tatma -> Empati ve Merhamet -> ?)
    ic6 = kutu(4, 4, 352, 107, GRI_A, GRI)
    zincir = [
        ('1. Tecrübe', 'Açlık ve susuzluğu', 'bizzat yaşama', MAVI, MAVI_A),
        ('2. Duyuşsal Etki', 'Yoksullarla empati', 've merhamet kurma', YES, YES_A),
        ('3. Toplumsal Sonuç', '?', 'Fitre · Zekât · İftar', KIR, KIR_A),
    ]
    for i, (b, a1, a2, c, d) in enumerate(zincir):
        x = 10 + i * 115
        ic6 += kutu(x, 12, 108, 91, d, c)
        ic6 += yazi(x + 54, 30, b, 8.6, c)
        ic6 += yazi(x + 54, 58, a1, 12.0 if a1 == '?' else 8.3, c if a1 == '?' else LAC)
        ic6 += yazi(x + 54, 82, a2, 8.0, SOLUK, ince=True)
        if i < 2:
            ic6 += f'<polygon points="{x+109},57 {x+114},52 {x+114},62" fill="{c}"/>'
    s[6]['gorsel'] = svg(ic6, 'Empatiden toplumsal dayanışmaya neden-sonuç zinciri')

    # s[7]: Kalkan sembolü (geometrik kalkan + ahlaki koruma)
    ic7 = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic7 += f'<path d="M56,18 L92,28 L92,58 C92,80 74,94 56,100 C38,94 20,80 20,58 L20,28 Z" fill="#f8fafc" stroke="{MAVI}" stroke-width="1.5"/>'
    ic7 += yazi(56, 56, 'ORUÇ', 9.5, MAVI) + yazi(56, 72, 'KALKANI', 8.0, LAC)
    ic7 += kutu(112, 18, 228, 36, '#f8fafc', MAVI, r=5, kalin=0.8)
    ic7 += yazi(226, 34, 'Kötü söz ve kavgadan korur', 8.8, MAVI)
    ic7 += yazi(226, 48, 'Öfke anında öz denetim sağlar', 8.0, SOLUK, ince=True)
    ic7 += kutu(112, 62, 228, 36, YES_A, YES, r=5, kalin=0.8)
    ic7 += yazi(226, 78, 'Tartışma çıkarsa ne denir?', 8.6, YES)
    ic7 += yazi(226, 92, '«Ben oruçluyum.» (Hadis-i Şerif)', 8.4, LAC)
    s[7]['gorsel'] = svg(ic7, 'Oruç kalkanı ve öfke kontrolü şeması')

    # s[8]: 4 aşamalı şükür ve paylaşım akışı
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    akis = [
        ('1. İmsak–İftar', 'Sabırla oruç', MAVI, MAVI_A),
        ('2. Farkındalık', 'Nimetin kıymeti', TUR, TUR_A),
        ('3. Şükür', 'İsraftan kaçınma', YES, YES_A),
        ('4. Paylaşma', 'Fitre ve sadaka', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(akis):
        x = 10 + i * 86
        ic8 += kutu(x, 14, 80, 87, d, c)
        ic8 += yazi(x + 40, 40, b, 8.6, c)
        ic8 += f'<line x1="{x+8}" y1="50" x2="{x+72}" y2="50" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 74, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic8 += f'<polygon points="{x+81},57 {x+85},52 {x+85},62" fill="{c}"/>'
    s[8]['gorsel'] = svg(ic8, 'Oruçtan şükür ve paylaşıma 4 adım')

    # s[9]: Ramazan vakit disiplini, sağlık ve kültür kartları
    ic9 = kutu(4, 4, 352, 107, GRI_A, GRI)
    k4 = [
        ('Zaman Bilinci', 'Sahur · İmsak · İftar', MAVI, MAVI_A),
        ('Beden Sağlığı', 'Ölçülü beslenme', YES, YES_A),
        ('Ramazan Kültürü', 'Mukabele · Teravih', TUR, TUR_A),
        ('Samimi Kulluk', 'Riyadan (gösterişten) uzak', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(k4):
        x = 10 + i * 86
        ic9 += kutu(x, 13, 80, 89, d, c)
        ic9 += yazi(x + 40, 36, b, 8.2, c)
        ic9 += f'<line x1="{x+7}" y1="46" x2="{x+73}" y2="46" stroke="{c}" stroke-width="0.7"/>'
        ic9 += yazi(x + 40, 72, alt, 7.6, LAC, ince=True)
    s[9]['gorsel'] = svg(ic9, 'Orucun zaman, sağlık, kültür ve ihlas boyutları')
