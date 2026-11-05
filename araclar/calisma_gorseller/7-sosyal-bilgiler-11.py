"""7. sınıf Sosyal Bilgiler 11. hafta (İstanbul’un Fethi ve Yükselme Dönemi) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def bogazkesen_hazirlik():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Rumeli (Boğazkesen) Hisarı', MAVI, kalin=True)
    ic += yazi(91, 52, 'Anadolu Hisarı karşısına', LAC)
    ic += yazi(91, 76, 'Karadeniz yardımlarını', KIR, kalin=True)
    ic += yazi(91, 96, 'kesmek için inşa edildi', LAC)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Diğer Fetih Hazırlıkları', TUR, kalin=True)
    ic += yazi(269, 52, '• Dev Şahi topları dökümü', LAC)
    ic += yazi(269, 76, '• 400 parçalık donanma', LAC)
    ic += yazi(269, 96, '• 72 gemi karadan Haliç’e', YES, kalin=True)
    return svg(ic, 'İstanbul kuşatması öncesi Rumeli Hisarı ve askerî hazırlık şeması.')


def fetih_sonuclari_panosu():
    kartlar = [
        (6, 6, '1. Toprak Bütünlüğü', 'Anadolu ve Rumeli birleşti', MAVI, MAVI_A),
        (184, 6, '2. Şahi Topları Etkisi', 'Derebeylik şatoları yıkıldı', KIR, KIR_A),
        (6, 60, '3. Bilginlerin Göçü', 'İtalya’da Rönesans doğdu', YES, YES_A),
        (184, 60, '4. Yeni Başkent', 'Cihan devleti dönemi', TUR, TUR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'İstanbul’un Fethi’nin Türk ve dünya tarihi açısından dört temel sonucu.')


def fatih_ahidnamesi():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 26, 'Fatih Sultan Mehmed’in Fermanı (Ahidname)', YES, kalin=True)
    ic += yazi(180, 52, '«Kimsenin canına, malına ve kilisesine dokunulmayacak;', LAC)
    ic += yazi(180, 74, 'herkes inancını ve ticaretini özgürce sürdürecektir.»', LAC)
    ic += yazi(180, 98, 'Temel İlke: İstimalet (Hoşgörü) ve Millet Sistemi', MAVI, kalin=True)
    return svg(ic, 'Fatih Sultan Mehmed’in din ve vicdan özgürlüğü tanıyan Ahidname fermanı.')


def ticaret_yollari_haritasi():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'İpek Yolu Denetimi', MAVI, kalin=True)
    ic += yazi(91, 52, 'İstanbul (1453) ve', LAC)
    ic += yazi(91, 74, 'Kırım’ın Fethi (1475)', MAVI, kalin=True)
    ic += yazi(91, 96, 'Karadeniz = Türk Gölü', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Baharat Yolu Denetimi', TUR, kalin=True)
    ic += yazi(269, 52, 'Mercidabık ve Ridaniye', LAC)
    ic += yazi(269, 74, 'Mısır Seferi (1516-1517)', TUR, kalin=True)
    ic += yazi(269, 96, 'Doğu Akdeniz - Kızıldeniz', KIR, kalin=True)
    return svg(ic, 'İpek Yolu ve Baharat Yolu’nun Osmanlı denetimine geçişini gösteren pano.')


def avrupa_etkisi_sema():
    ic = kutu(6, 6, 170, 103, KIR_A, KIR)
    ic += yazi(91, 26, 'Surların Topla Yıkılması', KIR, kalin=True)
    ic += yazi(91, 56, 'Derebeylik şatoları yıkıldı', LAC)
    ic += yazi(91, 84, '→ Feodalite Zayıfladı', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 26, 'Ticaret Yolu Kontrolü', CAM, kalin=True)
    ic += yazi(269, 56, 'Avrupa yeni yol aradı', LAC)
    ic += yazi(269, 84, '→ Coğrafi Keşifler', CAM, kalin=True)
    return svg(ic, 'İstanbul’un Fethi’nin Avrupa’da feodalite ve Coğrafi Keşiflere etkisi.')


def yukselme_kronoloji():
    adimlar = [
        (6, '1453', 'İstanbul Fethi', MAVI, MAVI_A),
        (94, '1475', 'Kırım Fethi', CAM, CAM_A),
        (182, '1517', 'Mısır Seferi', TUR, TUR_A),
        (270, '1538', 'Preveze Zaferi', YES, YES_A),
    ]
    ic = ''
    for x, yil, olay, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, yil, r, kalin=True)
        ic += yazi(x + 42, 72, olay, LAC, kalin=True)
    return svg(ic, 'Yükselme Dönemi dört temel gelişmesinin kronolojik şeridi.')


def misir_seferi_kazanim():
    ic = kutu(6, 6, 170, 103, MOR_A, MOR)
    ic += yazi(91, 26, 'Dinî Kazanım (1517)', MOR, kalin=True)
    ic += yazi(91, 54, 'Memlûk Devleti yıkıldı', LAC)
    ic += yazi(91, 82, 'Halifelik Osmanlı’ya geçti', MOR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Ekonomik Kazanım', YES, kalin=True)
    ic += yazi(269, 54, 'Mısır ve Suriye alındı', LAC)
    ic += yazi(269, 82, 'Baharat Yolu denetlendi', YES, kalin=True)
    return svg(ic, 'Yavuz Sultan Selim’in Mısır Seferi’nin dinî ve ekonomik sonuçları.')


def sahni_seman_bilim():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Sahn-ı Seman Medresesi', MAVI, kalin=True)
    ic += yazi(91, 54, 'Dönemin yükseköğretim', LAC)
    ic += yazi(91, 78, 've bilim merkezi kuruldu', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'İmar ve Bilim İnsanı', TUR, kalin=True)
    ic += yazi(269, 54, 'Ali Kuşçu davet edildi;', LAC)
    ic += yazi(269, 78, 'Kapalıçarşı ve vakıflar', TUR, kalin=True)
    return svg(ic, 'Fatih Sultan Mehmed’in Sahn-ı Seman Medreseleri ve bilim-kültür yatırımları.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bogazkesen_hazirlik()
    s[2]['gorsel'] = fetih_sonuclari_panosu()
    s[5]['gorsel'] = fatih_ahidnamesi()
    s[6]['gorsel'] = ticaret_yollari_haritasi()
    s[7]['gorsel'] = avrupa_etkisi_sema()
    s[8]['gorsel'] = yukselme_kronoloji()
    s[9]['gorsel'] = misir_seferi_kazanim()
    s[11]['gorsel'] = sahni_seman_bilim()
