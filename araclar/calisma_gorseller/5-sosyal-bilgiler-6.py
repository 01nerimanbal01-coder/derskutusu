"""5. sınıf Sosyal Bilgiler 6. hafta (Yardımlaşma ve Dayanışmanın Toplumsal Birliğe Etkisi & Yaşadığımız İlin Göreceli Konumu) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#8a5a2b', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def pusula_gulu_sema():
    ic = kutu(6, 6, 588, 96, KUM, GRI, 9, 1.4)
    cx, cy = 155, 54
    ic += f'<circle cx="{cx}" cy="{cy}" r="36" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<line x1="{cx}" y1="14" x2="{cx}" y2="94" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="115" y1="{cy}" x2="195" y2="{cy}" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="127" y1="26" x2="183" y2="82" stroke="{TUR}" stroke-width="1.5" stroke-dasharray="3,2"/>'
    ic += f'<line x1="183" y1="26" x2="127" y2="82" stroke="{TUR}" stroke-width="1.5" stroke-dasharray="3,2"/>'
    ic += yazi(cx, 13, 'Kuzey', KIR, kalin=True)
    ic += yazi(cx, 100, 'Güney', LAC, kalin=True)
    ic += yazi(85, cy + 4, 'Batı', LAC, kalin=True)
    ic += yazi(225, cy + 4, 'Doğu', LAC, kalin=True)
    ic += yazi(115, 25, 'K (?)', TUR, kalin=True)
    ic += yazi(196, 25, 'L', TUR, kalin=True)
    ic += yazi(115, 88, 'M', TUR, kalin=True)
    ic += yazi(196, 88, 'N', TUR, kalin=True)

    ic += kutu(280, 16, 300, 76, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(430, 36, 'Ana ve Ara Yönler Kuralı', MAVI, kalin=True)
    ic += yazi(430, 58, 'Ara yönler iki ana yönün tam ortasındadır.', LAC)
    ic += yazi(430, 78, 'Önce Kuzey veya Güney kelimesi söylenir.', LAC, kalin=True)
    return svg(600, 108, ic, 'Ana yönler ve K, L, M, N ara yönlerini gösteren pusula gülü.', 21)


def komsu_iller_sema():
    ic = kutu(6, 6, 588, 92, KUM, GRI, 9, 1.4)
    ic += kutu(216, 32, 168, 38, YES_A, YES, 8, 1.8)
    ic += yazi(300, 55, 'ESKİŞEHİR (Merkez)', YESIL_K, kalin=True)

    ic += kutu(24, 32, 148, 38, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(98, 55, 'Batı: KÜTAHYA', MAVI, kalin=True)
    ic += f'<line x1="172" y1="51" x2="216" y2="51" stroke="{TUR}" stroke-width="2.2"/>'

    ic += kutu(428, 32, 148, 38, TUR_A, TUR, 8, 1.4)
    ic += yazi(502, 55, 'Doğu: ANKARA', TUR, kalin=True)
    ic += f'<line x1="384" y1="51" x2="428" y2="51" stroke="{TUR}" stroke-width="2.2"/>'

    ic += yazi(300, 22, 'Kuzeybatı: Bilecik · Güney: Afyonkarahisar', LAC)
    ic += yazi(300, 88, 'Rota: Kütahya → Eskişehir → Ankara (Yön oku: ↑ Kuzey)', KIR, kalin=True)
    return svg(600, 104, ic, 'Kütahya, Eskişehir ve Ankara komşuluk ve yön şeması.', 21)


def dort_il_ekonomi_kartlari():
    kartlar = [
        ('1. Antalya', 'Akdeniz kıyısı · Yaz turizmi', MAVI, MAVI_A),
        ('2. Adana', 'Verimli Çukurova · Tarım sanayisi', YES, YES_A),
        ('3. Zonguldak', 'Taş kömürü · Madencilik', TUR, TUR_A),
        ('4. Erzurum', 'Yüksek plato · Kış turizmi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Antalya, Adana, Zonguldak ve Erzurum göreceli konum ve ekonomi kartları.', 21)


def fiziki_harita_renk_karti():
    kutular = [
        ('Yeşil (0 - 500 m)', 'Çukurova (Adana)', 'Deniz kıyısı alçak ova', YES, YES_A),
        ('Sarı (500 - 1000 m)', 'Konya Ovası', 'Orta yükseltide iç ova', TUR, TUR_A),
        ('Kahverengi (1500 m+)', 'Ağrı Dağı Çevresi', 'Yüksek dağlık alan', KAHVE, '#f7eee6'),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 86, arka, renk, 8, 1.5)
        ic += yazi(x + 96, 26, bas, renk, kalin=True)
        ic += yazi(x + 96, 52, s1, LAC, kalin=True)
        ic += yazi(x + 96, 75, s2, LAC)
    return svg(600, 98, ic, 'Fiziki haritada yeşil, sarı ve kahverengi yükselti basamakları kartı.', 21)


def yukselti_siralama_kartlari():
    kartlar = [
        ('İzmir Kıyısı', '0 - 200 m (Koyu yeşil)', YES, YES_A),
        ('İnegöl Ovası', '300 - 500 m (Açık yeşil)', CAM, CAM_A),
        ('Konya Platosu', '~1000 m (Sarı)', TUR, TUR_A),
        ('Erzurum Dağları', '2000 m+ (Kahverengi)', KAHVE, '#f7eee6'),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Batıdan doğuya yükseltisi artan dört yer şekli kartı.', 21)


def dayanisma_kultur_panosu():
    kartlar = [
        ('Sadaka Taşı & Zimem', 'İncitmeden gizli yardımlaşma', YES, YES_A),
        ('İmece Geleneği', 'Köy işlerinde gönüllü el birliği', MAVI, MAVI_A),
        ('AFAD & Türk Kızılayı', 'Afetlerde arama-kurtarma ve yardım', KIR, KIR_A),
        ('Toplumsal Birlik', 'Sevgi, güven ve kardeşliği pekiştirir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Tarihî ve güncel yardımlaşma-dayanışma örnekleri panosu.', 21)


def bursa_kimlik_karti():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'İL KİMLİK KARTI · BURSA’NIN GÖRECELİ KONUMU', '#fff', kalin=True)
    ic += yazi(300, 50, '• Kuzeyinde Marmara Denizi kıyısı ve verimli Bursa Ovası yer alır.', LAC, kalin=True)
    ic += yazi(300, 74, '• Güneyinde Uludağ yükselir; gelişmiş kara ve deniz ulaşım ağlarına sahiptir.', LAC)
    return svg(600, 98, ic, 'Bursa ilinin deniz, ova, dağ ve ulaşım özelliklerini gösteren kimlik kartı.', 21)


def rize_kayseri_karsilastirma():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(149, 25, 'Rize (Karadeniz Kıyısı)', YESIL_K, kalin=True)
    ic += yazi(149, 50, 'Denize kıyısı var · Her mevsim yağışlı', LAC, kalin=True)
    ic += yazi(149, 74, 'Çay tarımı ve balıkçılık yaygın', LAC)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(451, 25, 'Kayseri (İç Anadolu)', TUR, kalin=True)
    ic += yazi(451, 50, 'Denize kıyısı yok · Yükseltisi fazla', LAC, kalin=True)
    ic += yazi(451, 74, 'Tahıl tarımı, sanayi ve Erciyes kış turizmi', LAC)
    return svg(600, 98, ic, 'Rize ve Kayseri illerinin göreceli konum karşılaştırma kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = pusula_gulu_sema()
    s[4]['gorsel'] = komsu_iller_sema()
    s[5]['gorsel'] = dort_il_ekonomi_kartlari()
    s[6]['gorsel'] = fiziki_harita_renk_karti()
    s[7]['gorsel'] = yukselti_siralama_kartlari()
    s[8]['gorsel'] = dayanisma_kultur_panosu()
    s[10]['gorsel'] = bursa_kimlik_karti()
    s[11]['gorsel'] = rize_kayseri_karsilastirma()
