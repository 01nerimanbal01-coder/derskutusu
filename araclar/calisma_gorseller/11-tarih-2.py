"""11. sınıf Tarih 2. hafta görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def antlasma_kartlari():
    kartlar = [
        ('1. 1711 Prut', 'Azak Geri Alındı', YES, YES_A),
        ('2. 1718 Pasarofça', 'Belgrad Kaybı &amp; Lale Devri', TUR, TUR_A),
        ('3. 1739 Belgrad', 'Son Kazançlı Barış', MAVI, MAVI_A),
        ('4. 1774 Kaynarca', 'Kırım Bağımsız Oldu', KIR, KIR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'XVIII. yüzyıl Osmanlı antlaşmaları kartı.', 34)

def kirim_bagimsizligi_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, '1774 KÜÇÜK KAYNARCA VE KIRIM\'IN KAYBI', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Kırım Hanlığı Bağımsız', 9.4, KIR)
    ic += yazi(92, 76, 'İlk kez Müslüman toprak kaybı', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Dini bakımdan Halifeye bağlı', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Karadeniz Hâkimiyeti', 9.4, TUR)
    ic += yazi(267, 76, 'Rus donanması Karadeniz\'de', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Türk gölü özelliği sona erdi', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Küçük Kaynarca ve Kırım analizi şeması.', 34)

def prut_kusatmasi_harita_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, '1711 PRUT ZAFERİ VE AZAK KALESİ\'NİN GERİ ALINIŞI', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Baltacı Mehmed Paşa', 9.6, YESIL_K)
    ic += yazi(92, 76, 'Çar I. Petro Prut\'ta kuşatıldı', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Diplomatik barış imzalandı', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, MAVI_A, MAVI)
    ic += yazi(267, 56, 'Stratejik Kazanım', 9.6, MAVI)
    ic += yazi(267, 76, 'Azak Kalesi geri alındı', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Kayıpları telafi umudu doğdu', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Prut zaferi ve Azak Kalesi modeli.', 34)

def xviii_yy_savas_dengesi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'XVIII. YÜZYIL ASKERÎ MÜCADELE VE ISLAHAT EKSENİ', 10.3, CAM)
    ic += kutu(20, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(67, 58, '1718 Pasarofça', 9.4, TUR)
    ic += yazi(67, 78, 'Batı Üstünlüğü', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Lale Devri Barışı', 8.8, TUR, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', YES)
    ic += yazi(179, 58, '1739 Belgrad', 9.4, YESIL_K)
    ic += yazi(179, 78, 'Askerî Toparlanma', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'I. Mahmud Islahatı', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', KIR)
    ic += yazi(292, 58, '1774 Kaynarca', 9.4, KIR)
    ic += yazi(292, 78, 'Ağır Bozgun', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Tazminat &amp; Kırım', 8.8, KIR, ince=True)
    return svg(360, 125, ic, 'XVIII. yüzyıl askerî denge şeması.', 34)

def antlasma_kronoloji_seridi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, '1711-1774 BARIŞ ANTLAŞMALARI SIRALAMASI', 10.2, MOR)
    adımlar = [
        ('1711', 'Prut Barışı', 16),
        ('1718', 'Pasarofça', 102),
        ('1739', 'Belgrad', 188),
        ('1774', 'Küçük Kaynarca', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.4, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Barış antlaşmaları zaman çizelgesi.', 34)

def halifelik_bag_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'KÜÇÜK KAYNARCA\'DA HALİFELİK MADDESİ', 10.3, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Siyasi Açıdan Kayıp', 9.4, KIR)
    ic += yazi(92, 76, 'Kırım Hanlığı bağımsız oldu', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Osmanlı idaresinden çıktı', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Manevi Bağın Korunması', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Dini açıdan Halifeye bağlılık', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Halkla kültürel bağ sürdürüldü', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Halifelik maddesi ve kültürel bağ modeli.', 34)

def savas_sonuc_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'TARİHSEL ASKERÎ OLAY VE DOĞURDUĞU SONUÇ', 10.1, YESIL_K)
    kartlar = [
        ('1770 Çeşme', 'Donanma Yakıldı', 16),
        ('I. Mahmud', 'Batı Tarzı Islahat', 102),
        ('Kırım Kaybı', 'Karadeniz Açıldı', 188),
        ('Lale Devri', 'Geçici Elçilikler', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'XVIII. yüzyıl askerî olay ve sonuç kartı.', 34)

def prut_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, TUR)
    harfler = ['P', 'R', 'U', 'T']
    for i, h in enumerate(harfler):
        x = 75 + i * 56
        ic += kutu(x, 42, 48, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 24, 74, h, 16.0, TUR)
        ic += yazi(x + 24, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Prut kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = antlasma_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = kirim_bagimsizligi_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = prut_kusatmasi_harita_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = xviii_yy_savas_dengesi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = antlasma_kronoloji_seridi()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = halifelik_bag_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = savas_sonuc_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = prut_sifre_kutulari()
    s[10]['en_fazla'] = 34
