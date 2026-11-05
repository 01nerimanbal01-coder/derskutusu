"""12. sınıf Fizik 2. hafta (Emniyetli Dönüş Şartları) çalışma kâğıdı görselleri.
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


def dort_viraj_modeli_karti():
    modeller = [
        ('1. Yatay Viraj', 'Fs ≥ m·v² / r dengesi', MAVI, MAVI_A),
        ('2. Eğimli Viraj', 'tan α = v² / (g·r)', YES, YES_A),
        ('3. Düşey En Alt', 'T = Fm + mg (Maksimum)', TUR, TUR_A),
        ('4. Düşey En Üst', 'T = Fm - mg (Minimum)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(modeller):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        if ' (' in alt:
            ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel viraj ve dinamik emniyet modeli.', 34)


def yatay_viraj_hesap_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'YATAY VİRAJ MAKSİMUM SÜRAT HESAP MODELİ', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Veriler: k = 0,4 · r = 100 m', 9.8, YES)
    ic += yazi(95, 74, 'g = 10 m/s² (Yer çekimi)', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'v² = k·g·r = 0,4·10·100 = 400', 9.8, TUR)
    ic += yazi(265, 74, 'v_max = √400 = 20 m/s', 10.0, LAC)
    return svg(360, 110, ic, 'Yatay virajda maksimum güvenli hız hesabı.', 34)


def egimli_viraj_kutle_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'EĞİMLİ VİRAJ VE KÜTLE BAĞIMSIZLIĞI', 10.6, MAVI)
    ic += yazi(180, 52, 'tan α = (m·v² / r) / (m·g)  →  tan α = v² / (g·r)', 10.2, LAC)
    ic += yazi(180, 76, 'Kütle (m) formülde sadeleştiği için emniyetli hız kütleden bağımsızdır.', 9.4, MAVI, ince=True)
    return svg(360, 110, ic, 'Eğimli virajda kütle bağımsızlığı ispatı panosu.', 34)


def viraj_dinamik_vektor_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Yatay Viraj Dengesi', 10.4, YES)
    ic += yazi(91, 50, 'Fs = k·m·g = m·v² / r', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'v_max = √(k·g·r)', 9.6, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Eğimli Viraj Dengesi', 10.4, TUR)
    ic += yazi(269, 50, 'N·sin α = m·v² / r', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'N·cos α = m·g', 9.6, TUR)
    return svg(360, 110, ic, 'Yatay ve eğimli viraj serbest cisim diyagramı özeti.', 34)


def dusey_ip_gerilmesi_siralamasi():
    konumlar = [
        ('1. En Alt Nokta', 'T = Fm + mg (En büyük)', KIR, KIR_A),
        ('2. Yatay Seviye', 'T = Fm (Ağırlık dik)', TUR, TUR_A),
        ('3. Üst Ara Konum', 'T = Fm - mg·cos θ', MAVI, MAVI_A),
        ('4. En Üst Nokta', 'T = Fm - mg (En küçük)', YES, YES_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(konumlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        if ' (' in alt:
            ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Düşey çemberde ip gerilmesi sıralaması.', 34)


def dairesel_ray_tepki_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'DÜŞEY RAYDA EN ÜST NOKTADAN GEÇİŞ KRİTERİ', 10.6, MOR)
    ic += yazi(180, 52, 'F_merkezcil = N + mg  →  Minimum Hızda Ray Tepkisi: N = 0', 10.0, LAC)
    ic += yazi(180, 76, 'Cisim ancak geçiyorsa merkezcil kuvveti sadece cismin kendi ağırlığı karşılar.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Dairesel rayda en üst noktada ray tepkisi analizi.', 34)


def dort_dairesel_duzenek_karti():
    duzenekler = [
        ('Konik Sarkaç', 'Yatay ip dairesi', MAVI, MAVI_A),
        ('Döner Silindir', 'Duvar sürtünmesi', YES, YES_A),
        ('Lunapark Treni', 'Düşey ray döngüsü', TUR, TUR_A),
        ('Eğimli Pist', 'Açılı viraj yolu', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(duzenekler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört farklı dairesel hareket uygulama düzeneği.', 34)


def sifre_viraj_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'VİRAJLAR VE DİNAMİK EMNİYET KAVRAM PANOSU', 10.8, MAVI)
    ic += yazi(180, 50, 'SÜRTÜNME · AÇI · RADYAN · KUVVET · AĞIRLIK · CİSİM', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli dinamik terimini (6 harf) bulunuz.', 9.4, MAVI, ince=True)
    return svg(360, 110, ic, 'Şifre viraj kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_viraj_modeli_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = yatay_viraj_hesap_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = egimli_viraj_kutle_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = viraj_dinamik_vektor_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = dusey_ip_gerilmesi_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = dairesel_ray_tepki_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_dairesel_duzenek_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_viraj_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
