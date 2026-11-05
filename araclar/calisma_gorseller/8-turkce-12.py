"""8. sınıf Türkçe 12. hafta (Erdemler Metinleri, Cümlenin Ögeleri, Fiilde Çatı ve Yazım-Noktalama) görselleri.
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


def oge_ve_cati_cumlesi():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 24, 'Karma Cümle Çözümlemesi (Ögeler + Fiilde Çatı)', MAVI, kalin=True)
    ic += yazi(180, 52, '«Görevliler / kütüphanedeki yıpranmış kitapları / dün / özenle / onardı.»', LAC, kalin=True)
    ic += yazi(180, 82, 'Kim? → Görevliler   |   Neyi? → kütüphanedeki yıpranmış kitapları   |   onu onardı (+)', YES, kalin=True)
    return svg(ic, 'Cümlenin ögeleri ve fiilde çatı çözümleme kartı.')


def dort_cati_tablo_karti():
    kartlar = [
        (6, 6, '1. Öğrenciler şiiri okudu.', 'Kim? Öğrenciler · onu okudu', YES, YES_A),
        (184, 6, '2. Sokaklar temizlendi.', '-n eki (Sözde özne)', MAVI, MAVI_A),
        (6, 60, '3. Çocuk uyuyakaldı.', 'Gerçek özne · onu uyuyakaldı (X)', TUR, TUR_A),
        (184, 60, '4. Dedem fidan dikti.', 'Gerçek özne · onu dikti (+)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört farklı cümlenin özne ve nesne çatısı inceleme kartları.')


def ara_soz_ve_vurgu_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 24, 'Cümlede Ara Söz ve Vurgu İncelemesi', TUR, kalin=True)
    ic += yazi(180, 52, '«Annem —hayatımın en değerli insanı— dün akşam bize', LAC, kalin=True)
    ic += yazi(180, 74, '[ taze kurabiyeler ] pişirdi.»', KIR, kalin=True)
    ic += yazi(180, 96, 'İpucu: Fiil cümlesinde vurgu yüklemden (pişirdi) hemen önceki ögededir!', MAVI, kalin=True)
    return svg(ic, 'Ara söz ve cümle vurgusu içeren cümle inceleme kartı.')


def mese_ile_saz_karti():
    ic = kutu(6, 6, 172, 103, TUR_A, TUR)
    ic += yazi(92, 26, 'Ulu Meşe (Kibirli)', TUR, kalin=True)
    ic += yazi(92, 54, '• Gücüne güvenip böbürlenir', LAC)
    ic += yazi(92, 76, '• Rüzgâra karşı inatlaşır', LAC)
    ic += yazi(92, 96, '• Fırtınada kökünden sökülür!', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'İnce Saz (Alçak Gönüllü)', YES, kalin=True)
    ic += yazi(269, 54, '• Mütevazı ve esnek davranır', LAC)
    ic += yazi(269, 76, '• Fırtınada eğilerek uyum sağlar', LAC)
    ic += yazi(269, 96, '• Fırtına geçince ayakta kalır!', YES, kalin=True)
    return svg(ic, 'Meşe ile Saz fablında kibir ve tevazu karşılaştırması.')


def etkenden_edilgene_donusum():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Etken Cümleden Edilgen Cümleye Dönüşüm', CAM, kalin=True)
    ic += yazi(180, 54, 'Etken: «Belediye ekipleri (Özne) / mahallemizin parkını (Nesne) / dün / temizledi.»', LAC, kalin=True)
    ic += yazi(180, 84, 'Edilgen: İşi yapanı çıkarıp yükleme «-n» eki getiriniz → Sözde Özne = ?', MAVI, kalin=True)
    return svg(ic, 'Etken çatılı cümlenin edilgen çatılı cümleye dönüştürülmesi şeması.')


def oge_bulma_sirasi():
    adimlar = [
        (6, '1. Adım', 'Önce YÜKLEM', KIR, KIR_A),
        (94, '2. Adım', 'Sonra ÖZNE', MAVI, MAVI_A),
        (182, '3. Adım', 'Varsa NESNE', YES, YES_A),
        (270, '4. Adım', 'TÜMLEÇLER', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Cümlenin ögelerini bulurken izlenen dört temel adım (YÖNT).')


def yazim_noktalama_kartlari():
    kartlar = [
        (6, 6, '1. fark etmek de', 'Ayrı yazım + bağlaç (Doğru)', YES, YES_A),
        (184, 6, '2. sanatsal; makale,', 'Noktalı virgül kullanımı (Doğru)', MAVI, MAVI_A),
        (6, 60, '3. Ankara’dan, İzmir’den', 'Özel adlara gelen ekler (Doğru)', TUR, TUR_A),
        (184, 60, '4. nasıl farketmedin?', 'Yardımcı fiil bitişik? (Yanlış!)', KIR, KIR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört cümlede yazım ve noktalama kuralları denetim kartları.')


def iki_cumle_cati_analizi():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, '1. Cümle (anlatmış)', YES, kalin=True)
    ic += yazi(92, 52, '«Yazar ... çocukluk anılarını', LAC)
    ic += yazi(92, 74, 'samimi bir dille anlatmış.»', LAC)
    ic += yazi(92, 95, 'Özne: Yazar · Nesne: +', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, '2. Cümle (aç-ıl-dı)', MAVI, kalin=True)
    ic += yazi(269, 52, '«Sinema salonunun kapıları', LAC)
    ic += yazi(269, 74, 'saat onda açıldı.»', LAC)
    ic += yazi(269, 95, 'Sözde Özne · -l çatı eki', MAVI, kalin=True)
    return svg(ic, 'İki cümlenin özne ve nesne çatısı bakımından karşılaştırılması.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = oge_ve_cati_cumlesi()
    s[2]['gorsel'] = dort_cati_tablo_karti()
    s[5]['gorsel'] = ara_soz_ve_vurgu_karti()
    s[6]['gorsel'] = mese_ile_saz_karti()
    s[7]['gorsel'] = etkenden_edilgene_donusum()
    s[8]['gorsel'] = oge_bulma_sirasi()
    s[9]['gorsel'] = yazim_noktalama_kartlari()
    s[11]['gorsel'] = iki_cumle_cati_analizi()
