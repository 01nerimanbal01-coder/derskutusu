"""7. sınıf Türkçe 7. hafta (Bayrağımızın Altında: Şiirde Ana Duygu, Söz Sanatları ile Fiillerde Kip, Kişi ve Anlam Kayması) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def duz(x, y, satirlar, boy=10.5, renk=LAC, hiza='start', ara=14):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def siir_yapragi_svg():
    """Soru 1: Bayrak sevgisi temalı dörtlük ve kişileştirme içeren şiir yaprağı."""
    ic = kutu(4, 4, 352, 88, KIR_A, KIR, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{KIR}"/><rect x="4" y="16" width="352" height="10" fill="{KIR}"/>'
    ic += yazi(180, 19, 'ŞİİR YAPRAĞI · Bayrağımızın Altında', 11, '#fff')
    dizeler = [
        'Gökyüzünde gururla gülümser al bayrağım,',
        'Özgürlük türküsünü fısıldar her şafağım,',
        'Gölgesinde huzurla nefes alır toprağım,',
        'Sonsuza dek sönmeyen ışıktır bu ocağım.',
    ]
    ic += duz(180, 39, dizeler, 10.5, LAC, 'middle', 13.5)
    return svg(360, 96, ic, 'Şiir yaprağı: Gökyüzünde gururla gülümser al bayrağım, Özgürlük türküsünü fısıldar her şafağım dörtlüğü.', 14)


def cekimli_fiil_fisleri_svg():
    """Soru 2: Tablo sorusu için dört çekimli fiil fişi."""
    fisler = [
        ('1. Fiş', 'dalgalan-ıyor', MAVI, MAVI_A),
        ('2. Fiş', 'koru-malı-yız', TUR, TUR_A),
        ('3. Fiş', 'kutla-dı-nız', YES, YES_A),
        ('4. Fiş', 'çalış-a-lım', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, fiil, c, z) in enumerate(fisler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 62, z, c, 8, 1.4)
        ic += yazi(x + 41, 22, no, 10.5, c)
        ic += kutu(x + 6, 30, 70, 28, '#fff', c, 5, 1.1)
        ic += yazi(x + 41, 48, fiil, 10.5, LAC)
    return svg(360, 74, ic, 'Dört çekimli fiil fişi: 1 dalgalanıyor, 2 korumalıyız, 3 kutladınız, 4 çalışalım.', 14)


def dort_cumle_kip_karti_svg():
    """Soru 4: Dört çekimli fiil ve kip-kişi analiz kartı (3. kartta dinlesin hatası)."""
    kartlar = [
        ('1. Kart', 'okumuşlar (3. çoğul)', MAVI, MAVI_A),
        ('2. Kart', 'bilmezsin (2. tekil)', YES, YES_A),
        ('3. Kart', 'dinlesin (İstek · 2. tekil)', KIR, KIR_A),
        ('4. Kart', 'hazırlayacağız (1. çoğul)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, c, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, c, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 10.5, c)
        ic += yazi(x + 86, y + 29, alt, 10.5, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört çekimli fiil kartı: 1 okumuşlar, 2 bilmezsin, 3 dinlesin, 4 hazırlayacağız.', 14)


def teshis_intak_kartlari_svg():
    """Soru 5: Teşhis ve intak karşılaştırma dize kartları."""
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(91, 22, '1. Dize Kartı', 11, MAVI)
    ic += duz(91, 40, ['“Akşam rüzgârı tepelerin', 'ardından hüzünle iç çekti.”', '(Ağızdan çıkan cümle yok)'], 10.5, LAC, 'middle', 13.5)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR, 8, 1.4)
    ic += yazi(269, 22, '2. Dize Kartı', 11, TUR)
    ic += duz(269, 40, ['“Rüzgâr: ‘Ben dağların', 'özgür bekçisiyim!’ dedi.”', '(Doğrudan konuşma cümlesi)'], 10.5, LAC, 'middle', 13.5)
    return svg(360, 88, ic, 'İki dize kartı: 1. kartta rüzgâr hüzünle iç çekti, 2. kartta rüzgâr ben dağların özgür bekçisiyim dedi.', 14)


def anlam_kaymasi_cizelgesi_svg():
    """Soru 7: Dört cümlelik zaman ve kip çizelgesi."""
    satirlar = [
        ('I.', 'Haftaya → katılıyor', MAVI, MAVI_A),
        ('II.', '1919’da → çıkar', TUR, TUR_A),
        ('III.', 'Her sabah → sular', YES, YES_A),
        ('IV.', 'Sabahları → içiyorum', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    for i, (no, m, c, z) in enumerate(satirlar):
        x, y = 10 + (i % 2) * 172, 10 + (i // 2) * 38
        ic += kutu(x, y, 166, 32, z, c, 6, 1.2)
        ic += yazi(x + 8, y + 20, no, 10.5, c, 'start')
        ic += yazi(x + 26, y + 20, m, 10.5, LAC, 'start', True)
    return svg(360, 94, ic, 'Zaman çizelgesi kartları: I önümüzdeki hafta katılıyor, II 19 Mayıs 1919 da çıkar, III her sabah sular, IV sabahları içiyorum.', 14)


def dort_pano_kip_svg():
    """Soru 9: A, B, C, D cümle panoları (haber ve dilek kipleri)."""
    panolar = [
        ('A Panosu', ['düzenleyeceğiz', '(-ecek)'], MAVI, MAVI_A),
        ('B Panosu', ['astık', '(-tı)'], TUR, TUR_A),
        ('C Panosu', ['koruruz', '(-r)'], YES, YES_A),
        ('D Panosu', ['alsın', '(emir kipi)'], MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, satir, c, z) in enumerate(panolar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 62, z, c, 8, 1.4)
        ic += yazi(x + 41, 21, ad, 10.5, c)
        ic += duz(x + 41, 38, satir, 10.5, LAC, 'middle', 13)
    return svg(360, 74, ic, 'Dört cümle panosu: A düzenleyeceğiz, B astık, C koruruz, D alsın.', 14)


def fiil_cozumleme_semasi_svg():
    """Soru 10: kutla-ya-lım ve sev-meli-sin çekimli fiil çözümleme şeması."""
    ic = kutu(6, 6, 170, 72, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(91, 22, '1. Çekimli Fiil Yapısı', 11, MAVI)
    ic += kutu(16, 30, 150, 24, '#fff', MAVI, 5, 1.1)
    ic += yazi(91, 46, 'kutla  +  ya  +  lım', 11.5, LAC)
    ic += yazi(91, 68, 'Gövde + Kip + Kişi', 10.5, SOLUK, 'middle', True)

    ic += kutu(184, 6, 170, 72, YES_A, YES, 8, 1.4)
    ic += yazi(269, 22, '2. Çekimli Fiil Yapısı', 11, YES)
    ic += kutu(194, 30, 150, 24, '#fff', YES, 5, 1.1)
    ic += yazi(269, 46, 'sev  +  meli  +  sin', 11.5, LAC)
    ic += yazi(269, 68, 'Kök + Kip + Kişi', 10.5, SOLUK, 'middle', True)
    return svg(360, 84, ic, 'Çekimli fiil çözümleme şeması: 1 kutla artı ya artı lım, 2 sev artı meli artı sin.', 14)


def soz_sanatlari_fisleri_svg():
    """Soru 11: Dört söz sanatı sözlük fişi (Abartma fişinde örnek dize soru işaretli)."""
    fisler = [
        ('Benzetme (Teşbih)', 'Zayıfı güçlüye benzetme', MAVI, MAVI_A),
        ('Kişileştirme (Teşhis)', 'İnsan özelliğini doğaya verme', YES, YES_A),
        ('Abartma (Mübalağa)', 'Örnek dize: ?', KIR, KIR_A),
        ('Karşıtlık (Tezat)', 'Zıt kavramları kullanma', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, c, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, c, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 10.5, c)
        ic += yazi(x + 86, y + 29, alt, 10.5, LAC, 'middle', True)
    return svg(360, 88, ic, 'Dört söz sanatı fişi: Benzetme, Kişileştirme, Abartma örnek dize soru işaretli ve Karşıtlık.', 14)


def nasreddin_hoca_karti_svg():
    """Soru 14: Nasreddin Hoca fıkra cümlesinde anlam kayması inceleme kartı."""
    ic = kutu(4, 4, 352, 76, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{TUR}"/><rect x="4" y="16" width="352" height="10" fill="{TUR}"/>'
    ic += yazi(180, 19, 'ANLAM (ZAMAN) KAYMASI İNCELEME KARTI', 11, '#fff')
    ic += yazi(180, 44, '“Nasreddin Hoca bir gün göl kıyısına gider ve suya maya çalar.”', 10.5, LAC)
    ic += yazi(180, 66, 'Yazılan fiiller: gid-er, çal-ar   →   Kastedilen zaman: ?', 10.5, TUR, 'middle', True)
    return svg(360, 84, ic, 'Anlam kayması inceleme kartı: Nasreddin Hoca bir gün göl kıyısına gider ve suya maya çalar.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = siir_yapragi_svg()
    s[1]['gorsel'] = cekimli_fiil_fisleri_svg()
    s[3]['gorsel'] = dort_cumle_kip_karti_svg()
    s[4]['gorsel'] = teshis_intak_kartlari_svg()
    s[6]['gorsel'] = anlam_kaymasi_cizelgesi_svg()
    s[8]['gorsel'] = dort_pano_kip_svg()
    s[9]['gorsel'] = fiil_cozumleme_semasi_svg()
    s[10]['gorsel'] = soz_sanatlari_fisleri_svg()
    s[13]['gorsel'] = nasreddin_hoca_karti_svg()
