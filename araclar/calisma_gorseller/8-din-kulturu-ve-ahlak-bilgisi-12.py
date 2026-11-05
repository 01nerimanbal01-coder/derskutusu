"""8. sınıf Din Kültürü ve Ahlak Bilgisi 12. hafta (Maûn Suresi ve Anlamı, 2. Ünite Genel Değerlendirmesi) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def maun_1_3_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 24, 'Maûn Suresi 1–3. Ayetler Meali', TUR, kalin=True)
    ic += yazi(180, 48, '«1. Gördün mü, o hesap ve ceza gününü (dini) yalanlayanı!', LAC, kalin=True)
    ic += yazi(180, 72, '2. İşte o, yetimi itip kakan,', KIR, kalin=True)
    ic += yazi(180, 95, '3. Yoksulu doyurmaya teşvik etmeyen kimsedir.»', KIR, kalin=True)
    return svg(ic, 'Maûn suresi 1, 2 ve 3. ayetlerin meali kartı.')


def maun_cozumleme_tablosu():
    kartlar = [
        (6, 6, 'Ayet 2: Yetimi İtip Kakar', 'Erdem: Yetimi Korumak', MAVI, MAVI_A),
        (184, 6, 'Ayet 3: Yoksulu Gözetmez', 'Erdem: İnfaka Teşvik', YES, YES_A),
        (6, 60, 'Ayet 6: Gösteriş Yaparlar', 'Erdem: İhlas (Samimiyet)', TUR, TUR_A),
        (184, 60, 'Ayet 7: Yardımı Esirgerler', 'Erdem: Cömertlik / Maûn', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Maûn suresinde eleştirilen davranışlar ve istenen erdemler.')


def maun_4_7_karti():
    ic = kutu(6, 6, 348, 103, KIR_A, KIR)
    ic += yazi(180, 24, 'Maûn Suresi 4–7. Ayetler Meali', KIR, kalin=True)
    ic += yazi(180, 48, '«4–5. Yazıklar olsun o namaz kılanlara ki, onlar namazlarını ciddiye almazlar.', LAC)
    ic += yazi(180, 72, '6. Onlar (namazlarıyla) gösteriş (riya) yaparlar.', KIR, kalin=True)
    ic += yazi(180, 95, '7. Ufacık bir yardıma (zekâta / maûn’a) bile engel olurlar.»', LAC, kalin=True)
    return svg(ic, 'Maûn suresi 4, 5, 6 ve 7. ayetlerin meali kartı.')


def unite_degerlendirme_semasi():
    kartlar = [
        (6, 6, 'Altın ve Ticaret Malları', 'Zekât Oranı: 1/40 (%2,5)', YES, YES_A),
        (184, 6, 'Toprak Ürünleri (Öşür)', 'Yağmurla: 1/10 · Masraflı: 1/20', MAVI, MAVI_A),
        (6, 60, 'Fıtır Sadakası (Fitre) (?)', 'Kurban Bayramı’nda Zenginlere?', KIR, KIR_A),
        (184, 60, 'Tevbe Suresi 60. Ayet', 'Zekât Verilecek 8 Sınıf', TUR, TUR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'İkinci ünite zekât ve sadaka oranları genel değerlendirme şeması.')


def riya_ihlas_karsilastirma():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 26, 'RİYA (Gösterişçilik)', KIR, kalin=True)
    ic += yazi(92, 54, '• İnsanlar görsün ve övsün diye', LAC)
    ic += yazi(92, 76, '• İbadetin sevabını yok eder', LAC)
    ic += yazi(92, 96, '• Maûn 6. ayette kınanır', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'İHLAS (Samimiyet)', YES, kalin=True)
    ic += yazi(269, 54, '• Yalnız Allah (cc) rızası için', LAC)
    ic += yazi(269, 76, '• İbadeti anlamlı ve makbul kılar', LAC)
    ic += yazi(269, 96, '• Gizli ve incitmeden yardım', YES, kalin=True)
    return svg(ic, 'Riya ve ihlas kavramlarının karşılaştırma kartı.')


def maun_okunus_sirasi():
    adimlar = [
        (6, 'Ayet 1–2', 'Era’eytellezî...', MAVI, MAVI_A),
        (94, 'Ayet 3', 'Ve lâ yehuddu...', YES, YES_A),
        (182, 'Ayet 4–5', 'Feveylün li’l...', TUR, TUR_A),
        (270, 'Ayet 6–7', 'Ellezîne hüm...', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Maûn suresinin Arapça okunuş bölümlerinin sıralanması.')


def bakara_maun_ortak_mesaj():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'Bakara Suresi 264. Ayet', MAVI, kalin=True)
    ic += yazi(92, 54, '«Sadakalarınızı başa kakmak', LAC)
    ic += yazi(92, 76, 've gönül kırmak suretiyle', LAC)
    ic += yazi(92, 96, 'boşa çıkarmayın...»', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Maûn Suresi 6. Ayet', TUR, kalin=True)
    ic += yazi(269, 54, '«Onlar ibadetlerinde', LAC)
    ic += yazi(269, 76, 'gösteriş (riya) yaparlar', LAC)
    ic += yazi(269, 96, 've yardımı esirgerler.»', KIR, kalin=True)
    return svg(ic, 'Bakara 264 ve Maûn 6. ayetlerin ortak ihlas mesajı.')


def ibadet_ahlak_butunlugu():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Maûn Suresinin Temel Mesajı: İbadet ve Ahlak Bütünlüğü', CAM, kalin=True)
    ic += yazi(180, 56, 'Samimi İbadet (Namaz)  +  Sosyal Sorumluluk (Yetim/Yoksul/Maûn)', LAC, kalin=True)
    ic += yazi(180, 86, 'İbadet, insanı merhametli ve yardımsever kıldığı ölçüde amacına ulaşır.', YES, kalin=True)
    return svg(ic, 'Maûn suresinde ibadet ve sosyal yardımlaşma bütünlüğü panosu.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = maun_1_3_karti()
    s[2]['gorsel'] = maun_cozumleme_tablosu()
    s[5]['gorsel'] = maun_4_7_karti()
    s[6]['gorsel'] = unite_degerlendirme_semasi()
    s[7]['gorsel'] = riya_ihlas_karsilastirma()
    s[8]['gorsel'] = maun_okunus_sirasi()
    s[9]['gorsel'] = bakara_maun_ortak_mesaj()
    s[11]['gorsel'] = ibadet_ahlak_butunlugu()
