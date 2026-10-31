"""6. sınıf Türkçe 4. hafta (Açıklayıcı Metin Yapısı, Türkçenin Gelişimi ve “Türküz, Türkçe Konuşuruz” Şiiri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048); görsel içi yazı sayfa puntosunda (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=13, renk=LAC, hiza='start', ara=16):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def harf_kutu(x, y, h, renk=LAC):
    return f'<rect x="{x - 10}" y="{y - 10}" width="20" height="20" rx="5" fill="{renk}"/>' + yazi(x, y + 4.5, h, 12, '#fff')


def metin_plani():
    """Açıklayıcı metnin üç bölümü: Tanıtım (K), Açıklama/detaylandırma (L), Sonuç (M)."""
    ic = kutu(4, 4, 352, 22, LAC, LAC, 6, 1) + yazi(180, 19.5, 'AÇIKLAYICI METİN TASLAĞI · Okul Kütüphanesinin Kullanımı', 11.5, '#fff')
    bolumler = [
        ('1. Tanıtım', 'K', MAVI, MAVI_A, 4),
        ('2. Açıklama / Detaylandırma', 'L', TUR, TUR_A, 122),
        ('3. Sonuç', 'M', YES, YES_A, 240),
    ]
    for bas, harf, renk, zemin, x in bolumler:
        ic += kutu(x, 32, 114, 66, zemin, renk, 7, 1.3)
        ic += f'<rect x="{x}" y="32" width="114" height="20" rx="7" fill="{renk}"/><rect x="{x}" y="44" width="114" height="8" fill="{renk}"/>'
        ic += yazi(x + 57, 46, bas, 10, '#fff')
        ic += harf_kutu(x + 24, 74, harf, renk)
        ic += yazi(x + 68, 78, '? içeriği', 11.5, LAC)
    return svg(360, 102, ic, 'Açıklayıcı metin taslağı: Okul Kütüphanesinin Kullanımı. Üç bölüm kutusu: 1. Tanıtım K içeriği, 2. Açıklama ve Detaylandırma L içeriği, 3. Sonuç M içeriği.', 25)


def karagoz_karti():
    """Gölge oyunu sahnesi ve iki baş oyuncunun konuşma biçimi kartları (insan figürü yok, sahne perdesi ve zil/tef simgesi)."""
    ic = kutu(4, 4, 352, 88, KUM, KAHVE, 8, 1.4)
    ic += f'<path d="M4 12 q22 10 44 0 t44 0 t44 0 t44 0 t44 0 t44 0 t44 0 t44 0 V4 H4 Z" fill="{KIR}"/>'
    ic += yazi(180, 26, 'HAYAL PERDESİ (GÖLGE OYUNU)', 11.5, KAHVE)
    ic += kutu(14, 34, 158, 50, KIR_A, KIR, 6, 1.2)
    ic += yazi(93, 50, 'Karagöz', 12, KIR)
    ic += duz(93, 65, ['Halk diliyle, içten ve', 'çekinmeden konuşur.'], 10.5, LAC, 'middle', 13)
    ic += kutu(188, 34, 158, 50, YES_A, YES, 6, 1.2)
    ic += yazi(267, 50, 'Hacivat', 12, YES)
    ic += duz(267, 65, ['Öğrenim görmüş, süslü', 've bilgili konuşur.'], 10.5, LAC, 'middle', 13)
    return svg(360, 96, ic, 'Hayal perdesi gölge oyunu şeması: solda Karagöz kartı halk diliyle içten konuşur, sağda Hacivat kartı öğrenim görmüş ve bilgili konuşur.', 24)


def kabuk_kartlari():
    """Beş varlık ve kabuk çizimi (insan yok; kaplumbağa kabuğu, böcek kanadı, elma dilimi, ahlat meyvesi, salyangoz kavkısı)."""
    adlar = ['Kaplumbağa', 'Böcek', 'Meyve', 'Ahlat', 'Salyangoz']
    renkler = [(YES, YES_A), (MOR, MOR_A), (KIR, KIR_A), (KAHVE, KUM), (MAVI, MAVI_A)]
    ic = ''
    for i, x in enumerate([2, 74, 146, 218, 290]):
        r, z = renkler[i]
        cx = x + 34
        ic += kutu(x, 2, 68, 86, z, r, 7, 1.3)
        if i == 0:  # kaplumbağa sırt kabuğu
            ic += f'<path d="M{cx - 22} 46 a22 18 0 0 1 44 0 z" fill="{YES}" stroke="{LAC}" stroke-width="1.2"/>'
            ic += f'<path d="M{cx - 10} 32 l10 -4 l10 4 l4 14 h-28 z" fill="none" stroke="#fff" stroke-width="1.1"/>'
        elif i == 1:  # böcek sırt kabuğu
            ic += f'<ellipse cx="{cx}" cy="38" rx="13" ry="16" fill="{MOR}" stroke="{LAC}" stroke-width="1.2"/>'
            ic += f'<line x1="{cx}" y1="22" x2="{cx}" y2="54" stroke="#fff" stroke-width="1.2"/>'
        elif i == 2:  # elma/meyve
            ic += f'<circle cx="{cx}" cy="40" r="14" fill="{KIR}"/><path d="M{cx} 26 q4 -6 10 -4" fill="none" stroke="{YES}" stroke-width="2"/>'
        elif i == 3:  # ahlat (yaban armudu)
            ic += f'<path d="M{cx} 24 q-8 0 -10 10 q-4 14 10 18 q14 -4 10 -18 q-2 -10 -10 -10 z" fill="#c99a3e" stroke="{KAHVE}" stroke-width="1.2"/>'
        else:  # salyangoz burma kabuğu
            ic += f'<circle cx="{cx}" cy="38" r="15" fill="#7aa6e8" stroke="{MAVI}" stroke-width="1.4"/>'
            ic += f'<path d="M{cx} 38 a5 5 0 1 1 5 5 a9 9 0 1 1 -9 -9 a13 13 0 1 1 13 13" fill="none" stroke="#fff" stroke-width="1.4"/>'
        ic += yazi(cx, 76, adlar[i], 11, LAC)
    return svg(362, 92, ic, 'Beş kabuk görseli: Kaplumbağa kabuğu, Böcek sırtı, Meyve, Ahlat ve Salyangoz burma kabuğu.', 21)


def canli_karsilastirma():
    """Salyangoz (gözü boynuz) ve sümüklüböcek (izi yaldız) karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 22, 'Salyangoz (“gözü boynuz”)', 11.5, MAVI)
    ic += f'<path d="M36 62 q30 -4 64 0 q12 -2 16 -8" fill="none" stroke="{KAHVE}" stroke-width="4" stroke-linecap="round"/>'
    ic += f'<circle cx="66" cy="48" r="14" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.3"/>'
    ic += f'<path d="M66 48 a5 5 0 1 1 5 5 a9 9 0 1 1 -9 -9" fill="none" stroke="{KAHVE}" stroke-width="1.2"/>'
    ic += f'<line x1="112" y1="54" x2="120" y2="42" stroke="{KAHVE}" stroke-width="1.6"/><circle cx="120" cy="41" r="2.2" fill="{LAC}"/>'
    ic += f'<line x1="115" y1="56" x2="125" y2="46" stroke="{KAHVE}" stroke-width="1.6"/><circle cx="125" cy="45" r="2.2" fill="{LAC}"/>'
    ic += yazi(90, 84, 'burma kavkısı var', 10.5, LAC)

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 22, 'Sümüklüböcek (“izi yaldız”)', 11.5, TUR)
    ic += f'<path d="M204 62 h38" stroke="{ALTIN}" stroke-width="4" stroke-dasharray="5 3" stroke-linecap="round"/>'
    ic += f'<path d="M242 60 q28 -8 58 0 q10 -2 14 -7" fill="none" stroke="#a66a38" stroke-width="5" stroke-linecap="round"/>'
    ic += f'<ellipse cx="270" cy="55" rx="7" ry="3.5" fill="#d8b08c" stroke="{KAHVE}" stroke-width="1"/>'
    ic += yazi(270, 84, 'parlak iz · tırnak kadar kabuk', 10.5, LAC)
    return svg(360, 100, ic, 'Solda Salyangoz gözü boynuz: sırtında burma kavkı ve boynuz benzeri duyargalar. Sağda Sümüklüböcek izi yaldız: ardında parlak iz ve sırtında tırnak büyüklüğünde kabuk.', 22)


def yazit_seridi():
    """Orhon Yazıtları zaman şeridi: 720 Tonyukuk, 732 Kül Tigin, 735 Bilge Kağan; Moğolistan / Karakurum."""
    ic = kutu(4, 4, 352, 98, KUM, GRI, 8, 1.2)
    ic += yazi(180, 20, 'ORHON YAZITLARI · Moğolistan (Karakurum yakınları)', 11.5, LAC)
    ic += f'<line x1="28" y1="56" x2="332" y2="56" stroke="{SOLUK}" stroke-width="2"/>'
    veriler = [
        (68, '720', 'Tonyukuk Yazıtı', 'Vezir adına', MAVI, MAVI_A),
        (180, '732', 'Kül Tigin Yazıtı', 'Hükümdar adına', TUR, TUR_A),
        (292, '735', 'Bilge Kağan Yazıtı', 'Hükümdar adına', YES, YES_A),
    ]
    for x, yil, ad, rol, renk, zemin in veriler:
        ic += f'<circle cx="{x}" cy="56" r="5" fill="{renk}"/>'
        ic += kutu(x - 50, 28, 100, 22, renk, renk, 5, 1) + yazi(x, 43.5, f'{yil} · {ad}', 10, '#fff')
        ic += kutu(x - 48, 66, 96, 26, zemin, renk, 5, 1.1) + yazi(x, 83, rol, 10.5, LAC)
    return svg(360, 106, ic, 'Orhon Yazıtları zaman şeridi, Moğolistan Karakurum yakınları: 720 Tonyukuk Yazıtı Vezir adına, 732 Kül Tigin Yazıtı Hükümdar adına, 735 Bilge Kağan Yazıtı Hükümdar adına.', 20)


def yazim_panosu():
    """Dört bilgi fişi: III. fişte '13. ve 14. satırlar' yanlış yazılmış (doğrusu 13 ve 14. satırlar)."""
    fisler = [
        ('I. fiş', ['Karagöz doğru dürüst bir', 'işte çalışmaz.'], MAVI, MAVI_A),
        ('II. fiş', ['Oyun adıyla sanıyla Türk', 'kültürüne özgüdür.'], YES, YES_A),
        ('III. fiş', ['Yazıtın 13. ve 14. satırları', 'birliğin gücünü anlatır.'], TUR, TUR_A),
        ('IV. fiş', ['Dilimiz yabancı sözlere karşı', 'ayakta durmaya çalışır.'], MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, satirlar, renk, zemin) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 42, zemin, renk, 7, 1.3)
        ic += f'<rect x="{x + 6}" y="{y + 6}" width="38" height="16" rx="4" fill="{renk}"/>' + yazi(x + 25, y + 18, bas, 10, '#fff')
        ic += duz(x + 50, y + 17, satirlar, 10.5, LAC, 'start', 14)
    return svg(360, 100, ic, 'Dört bilgi fişi. I. fiş: Karagöz doğru dürüst bir işte çalışmaz. II. fiş: Oyun adıyla sanıyla Türk kültürüne özgüdür. III. fiş: Yazıtın 13. ve 14. satırları birliğin gücünü anlatır. IV. fiş: Dilimiz yabancı sözlere karşı ayakta durmaya çalışır.', 22)


def sozcuk_turetme():
    """Yabancı 'faks' yerine Türkçe 'belge + geçer -> belgegeçer' türetme şeması."""
    ic = kutu(4, 4, 352, 76, KUM, GRI, 8, 1.2)
    ic += kutu(12, 16, 86, 52, KIR_A, KIR, 6, 1.3)
    ic += yazi(55, 36, 'faks', 13, KIR) + yazi(55, 54, '(yabancı sözcük)', 9.5, SOLUK)
    ic += f'<line x1="104" y1="42" x2="128" y2="42" stroke="{SOLUK}" stroke-width="2"/><path d="M124 37 l7 5 l-7 5 z" fill="{SOLUK}"/>'
    ic += kutu(134, 16, 104, 52, MAVI_A, MAVI, 6, 1.3)
    ic += yazi(186, 36, 'belge + geçer', 12, MAVI) + yazi(186, 54, '(tanıdık kökler)', 9.5, SOLUK)
    ic += f'<line x1="244" y1="42" x2="268" y2="42" stroke="{YES}" stroke-width="2"/><path d="M264 37 l7 5 l-7 5 z" fill="{YES}"/>'
    ic += kutu(274, 16, 74, 52, YES_A, YES, 6, 1.4)
    ic += yazi(311, 36, 'belgegeçer', 11.5, YES) + yazi(311, 54, '(Türkçe karşılık)', 9, SOLUK)
    return svg(360, 84, ic, 'Sözcük türetme şeması: yabancı sözcük faks yerine tanıdık kökler belge artı geçer birleştirilerek Türkçe karşılık belgegeçer türetilir.', 19)


def siir_tablosu():
    """Türküz, Türkçe Konuşuruz şiirinin 8 dörtlüğünde özellik dağılımı çizelgesi."""
    ic = kutu(4, 4, 352, 96, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(96, 19, 'Özellik / Dörtlük No.', 10.5, '#fff')
    for d in range(1, 9):
        x = 182 + (d - 1) * 21
        ic += yazi(x, 19, str(d), 11, '#fff')
    satirlar = [
        ('“Türkçem” ile başlama', {1, 4, 5, 7}, MAVI),
        ('Tırnak işareti kullanma', {2, 4}, TUR),
        ('Şehir adı (Kırşehir) geçme', {7}, YES),
    ]
    for r, (etiket, kume, renk) in enumerate(satirlar):
        y = 42 + r * 22
        ic += f'<line x1="10" y1="{y - 14}" x2="350" y2="{y - 14}" stroke="{GRI_A}" stroke-width="1"/>'
        ic += yazi(12, y, etiket, 10.5, LAC, 'start')
        for d in range(1, 9):
            x = 182 + (d - 1) * 21
            if d in kume:
                ic += f'<circle cx="{x}" cy="{y - 4}" r="5.5" fill="{renk}"/>'
            else:
                ic += f'<line x1="{x - 3}" y1="{y - 4}" x2="{x + 3}" y2="{y - 4}" stroke="{GRI}" stroke-width="1.3"/>'
    return svg(360, 104, ic, 'Şiir dörtlükleri çizelgesi: Türkçem ile başlama 1, 4, 5 ve 7. dörtlüklerde; tırnak işareti kullanma 2 ve 4. dörtlüklerde; şehir adı Kırşehir geçme yalnız 7. dörtlükte.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = metin_plani()
    s[1]['gorsel'] = karagoz_karti()
    s[2]['gorsel'] = kabuk_kartlari()
    s[3]['gorsel'] = canli_karsilastirma()
    s[4]['gorsel'] = yazim_panosu()
    s[5]['gorsel'] = yazit_seridi()
    s[8]['gorsel'] = sozcuk_turetme()
    s[9]['gorsel'] = siir_tablosu()
