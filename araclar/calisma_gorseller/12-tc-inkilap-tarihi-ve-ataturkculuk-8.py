"""12. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 8. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.5, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Millî Mücadele hazırlık dönemi belgeleri', [('Millî Kongre', 'Kuvâ-yı Millîye adı', YES, YES_A), ('Havza Genelgesi', 'Protesto mitingleri', MAVI, MAVI_A), ('Amasya Genelgesi', 'Amaç ve yöntem', TUR, TUR_A), ('Amasya Görüşmesi', 'Temsil Heyeti tanındı', MOR, MOR_A)])

def g1():
    return uclu('Mondros sonrası kurulan cemiyetlerin sınıflandırılması', 'MONDROS ATEŞKES ANTLAŞMASI SONRASI CEMİYETLER', ('Millî Cemiyetler', 'Kilikyalılar · Trakya · İzmir', YES, YES_A), ('Azınlık Cemiyetleri', 'Mavri Mira · Pontus · Hınçak', KIR, KIR_A), ('Millî Varlığa Düşman', 'İngiliz Muhipleri · Wilson', TUR, TUR_A), YES, YES_A)

def g2():
    return pano('Erzurum Kongresi toplanışı ve kararları', 'ERZURUM KONGRESİ (23 TEMMUZ - 7 AĞUSTOS 1919)', 'Toplanış Şekli: Bölgesel (Doğu illeri) · Aldığı Kararlar: Ulusal (Tüm vatan)', '"Millî sınırlar içinde vatan bir bütündür" ve "Manda ve himaye kabul olunamaz" (İlk kez).', MOR, MOR_A, '#f5f0ff')

def g3():
    return kart4('Hazırlık dönemi önemli gelişmeleri', [('Hadisat·Albayrak', 'Doğu Anadolu basını', MAVI, MAVI_A), ('Sine-i Millet', 'Erzurum istifası', TUR, TUR_A), ('Salih Paşa', 'Amasya Görüşmeleri', MOR, MOR_A), ('Ali Fuat Paşa', 'Batı Cephesi ataması', YES, YES_A)])

def g5():
    return akis4('Millî Mücadele hazırlık kronolojisi', [('19 Mayıs 1919', 'Samsun Çıkışı', MAVI, MAVI_A), ('22 Haziran 1919', 'Amasya Genelgesi', TUR, TUR_A), ('4-11 Eylül 1919', 'Sivas Kongresi', YES, YES_A), ('20-22 Ekim 1919', 'Amasya Görüşmesi', MOR, MOR_A)])

def g6():
    return pano('Temsil Heyeti ilk siyasi başarısı', 'SİVAS KONGRESİ SONRASI SİYASİ ZAFER VE AMASYA GÖRÜŞMELERİ', 'İstanbul ile haberleşme kesildi → Damat Ferit Hükûmeti istifa etti (İlk Siyasi Başarı)', 'Yeni kurulan Ali Rıza Paşa Hükûmeti, Amasya Görüşmeleri ile Temsil Heyetini tanıdı.', YES, YES_A, '#eaf8f0')

def g7():
    return uclu('Merkez Ordusu, Erzurum ve İrade-i Millîye', 'MİLLÎ MÜCADELE ÖRGÜTLENME UNSURLARI', ('Merkez Ordusu', 'Pontus isyanını bastırdı', KIR, KIR_A), ('Erzurum Kongresi', 'Manda ilk kez reddedildi', MOR, MOR_A), ('İrade-i Millîye', 'Sivas Kongresi gazetesi', MAVI, MAVI_A), MAVI, MAVI_A)

def g8():
    return kart4('Yararlı ve zararlı cemiyetler', [('Kars İslam Şûrası', 'İlk kurulan yararlı', YES, YES_A), ('Trabzon M. Hukuk', 'Pontus iddiasına karşı', MAVI, MAVI_A), ('Mavri Mira', 'Megali İdea (Rum)', KIR, KIR_A), ('Hınçak ve Taşnak', 'Ermeni iddiaları', TUR, TUR_A)])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
