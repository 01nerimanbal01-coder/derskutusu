"""8. sınıf Türkçe 2. hafta (Öğrencilerin Dijital Okuma Kültürü: Düşünceyi Geliştirme Yolları, Makale, Güvenilir Kaynaklar ve Fiilimsiler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def fiilimsi_cozumleme_kartlari():
    kartlar = [
        ('İsim-fiil (Eylem adı)', 'zenginleştirmek · okuması', TUR, TUR_A),
        ('Sıfat-fiil (İsmi niteler)', 'olunan dergi · genişletecek fırsat', MAVI, MAVI_A),
        ('Zarf-fiil (Durum: Nasıl?)', 'göstererek · ara vermeksizin', YES, YES_A),
        ('Zarf-fiil (Zaman: Ne zaman?)', 'kütüphaneye girdiğinde', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Cümlede isim-fiil, sıfat-fiil ve zarf-fiil görev şeması.', 16)


def makale_olcut_tablosu():
    sat = [
        ('1. Öne sürülen düşünce kanıtlanmaya çalışılmıştır.', 'VAR (✓)', YES, YES_A),
        ('2. Olaya dayalı kurmaca bir anlatım yapılmıştır.', 'YOK (—)', GRI, GRI_A),
        ('3. Doğrulanabilir, nesnel ifadeler kullanılmıştır.', 'VAR (✓)', MAVI, MAVI_A),
        ('4. İçerik bilimsel bir yaklaşımla ele alınmıştır.', 'VAR (✓)', TUR, TUR_A),
    ]
    ic = ''
    for i, (m, d, r, z) in enumerate(sat):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 10, y + 23, m, 9.6, LAC, 'start', ince=True)
        ic += yazi(x + 276, y + 23, d, 10.2, r, 'end')
    return svg(600, 96, ic, 'Makale türünü ayırt eden bilimsel ve nesnel ölçütler tablosu.', 16)


def dijital_okuma_rehberi():
    ic = kutu(6, 6, 286, 74, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Dijital Okuma ve Materyal İlkeleri', 10.6, MAVI)
    ic += yazi(149, 45, '• Basılı ve dijital materyaller birlikte kullanılır', 10.0, LAC, ince=True)
    ic += yazi(149, 64, '• Sözcük tahminleri TDK sözlüğünden doğrulanır', 10.0, MAVI)

    ic += kutu(308, 6, 286, 74, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Güvenilir Ağ ve Dil Bilgisi', 10.6, YES)
    ic += yazi(451, 45, '• Araştırmada “edu” ve “gov” siteleri seçilir', 10.0, LAC, ince=True)
    ic += yazi(451, 64, '• Çekimli fiil (yaşayacak) fiilimsi değildir', 10.0, YES)
    return svg(600, 86, ic, 'Dijital okuma, sözlük kontrolü ve güvenilir kaynak ilkeleri.', 16)


def dort_cumle_fisi():
    fisler = [
        ('1. Fiş · eserler okuması', 'Yalnız isim-fiil var', MAVI, MAVI_A),
        ('2. Fiş · genişletecek fırsat', 'Yalnız sıfat-fiil var', TUR, TUR_A),
        ('3. Fiş · okumadan geçirdiği gün', 'Zarf-fiil + Sıfat-fiil birlikte!', YES, YES_A),
        ('4. Fiş · düşünmek, okuma', 'İki isim-fiil var', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(fisler):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Dört cümle fişinde bulunan fiilimsi türleri analizi.', 16)


def konusma_plani_adimlari():
    adimlar = [
        ('1. Araştır & Planla', 'edu, gov · içerik sırası', MAVI, MAVI_A),
        ('2. Hitapla Başla', 'Dinleyiciyi selamla', TUR, TUR_A),
        ('3. Materyal Kullan', 'Görsel-işitsel destek', MOR, MOR_A),
        ('4. Ses & Beden Dili', 'Anlama uygun tonlama', CAM, CAM_A),
        ('5. Uygun Bitir', 'Özet ve teşekkür', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 66, z, r, 8, 1.4)
        ic += yazi(x + 56, 26, bas, 10.0, r)
        ic += yazi(x + 56, 50, alt, 9.5, LAC, ince=True)
    return svg(600, 78, ic, 'Hazırlıklı konuşma planının beş uygulama adımı.', 15)


def basili_dijital_karti():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Geleneksel (Basılı) Metin', 10.8, MAVI)
    ic += yazi(149, 46, '• Kâğıt sayfa, yazı ve durağan resim', 10.0, LAC, ince=True)
    ic += yazi(149, 63, '• Çoğunlukla bireysel zihinsel süreç', 10.0, MAVI)

    ic += kutu(308, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Dijital ve Etkileşimli Metin', 10.8, TUR)
    ic += yazi(451, 46, '• Ekran, video, animasyon, film ve simge', 10.0, LAC, ince=True)
    ic += yazi(451, 63, '• Toplumla paylaşımlı sosyo-bilişsel etkinlik', 10.0, TUR)
    return svg(600, 84, ic, 'Geleneksel basılı metin ile etkileşimli dijital metin karşılaştırması.', 16)


def genel_ag_kaynak_kartlari():
    adresler = [
        ('I. Adres · okurgunlugu.blog', 'Kişisel blog (Öznel)', KIR, KIR_A),
        ('II. Adres · sohbetforumu.net', 'İmzasız yorumlar (Denetimsiz)', TUR, TUR_A),
        ('III. Adres · meb.gov.tr', 'Devlet kurumu (Güvenilir ✓)', YES, YES_A),
        ('IV. Adres · ankara.edu.tr', 'Üniversite (Güvenilir ✓)', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adresler):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Dört genel ağ adresinin bilimsel güvenilirlik karşılaştırması.', 16)


def sifat_fiil_cekimli_karti():
    ic = kutu(6, 6, 286, 70, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, '“Unutulmaz eserlerin sahibi...”', 10.6, MAVI)
    ic += yazi(149, 46, 'Görev: “eserler” ismini niteler (Nasıl eser?)', 10.0, LAC, ince=True)
    ic += yazi(149, 63, 'Tür: Sıfat-fiil (Eylemsi)', 10.1, MAVI)

    ic += kutu(308, 6, 286, 70, KIR_A, KIR, 8, 1.5)
    ic += yazi(451, 24, '“...kuşaklarda da yaşayacak.”', 10.6, KIR)
    ic += yazi(451, 46, 'Görev: Cümlenin temel yargısını kurar (Yüklem)', 10.0, LAC, ince=True)
    ic += yazi(451, 63, 'Tür: Gelecek zamanla çekimli fiil', 10.1, KIR)
    return svg(600, 82, ic, 'Sıfat-fiil ile gelecek zaman çekimli fiilin görev farkı kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = fiilimsi_cozumleme_kartlari()
    s[1]['gorsel'] = makale_olcut_tablosu()
    s[3]['gorsel'] = dijital_okuma_rehberi()
    s[5]['gorsel'] = dort_cumle_fisi()
    s[6]['gorsel'] = konusma_plani_adimlari()
    s[7]['gorsel'] = basili_dijital_karti()
    s[8]['gorsel'] = genel_ag_kaynak_kartlari()
    s[11]['gorsel'] = sifat_fiil_cekimli_karti()
