"""7. sınıf Din Kültürü ve Ahlak Bilgisi 11. hafta (Hz. İsmail, Zemzem, Kâbe’nin İnşası ve Kurban Kültürü) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px, max-height 21-22mm."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def mekke_hatira_semasi():
    kartlar = [
        (6, 'Safa — Merve', '7 Gidiş-Geliş', 'Sa’y İbadeti', YES, YES_A),
        (144, 'Kâbe İnşası', 'Beytullah', 'Tavaf Merkezi', TUR, TUR_A),
        (282, 'Mina Yolu', 'Vesvese Reddi', 'Şeytan Taşlama', MAVI, MAVI_A),
    ]
    ic = ''
    for x, b1, b2, b3, r, z in kartlar:
        ic += kutu(x, 6, 132, 84, z, r)
        ic += yazi(x + 66, 26, b1, r, kalin=True)
        ic += f'<line x1="{x + 12}" y1="35" x2="{x + 120}" y2="35" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 66, 56, b2, LAC)
        ic += yazi(x + 66, 78, b3, r, kalin=True)
    return svg(420, 96, ic, 'Mekke kıssası olayları ile hac ibadetleri bağlantı şeması.', 21)


def ayet_mesaj_kartlari():
    kartlar = [
        (6, 6, '1. Sâffât, 100', 'Salih evlat duası', MAVI, MAVI_A),
        (214, 6, '2. Bakara, 127', 'Beytullah temelleri', TUR, TUR_A),
        (6, 54, '3. Sâffât, 102', 'Rüya ve sabır sözü', YES, YES_A),
        (214, 54, '4. Meryem, 54-55', 'Sadıkü’l-va’d sıfatı', MOR, MOR_A),
    ]
    ic = ''
    for x, y, ayet, konu, r, z in kartlar:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi(x + 100, y + 18, ayet, r, kalin=True)
        ic += yazi(x + 100, y + 36, konu, LAC)
    return svg(420, 102, ic, 'Hz. İsmail kıssasıyla ilgili dört Kur’an ayeti kartı.', 22)


def saffat_istisare_panosu():
    ic = kutu(6, 6, 200, 84, MAVI_A, MAVI)
    ic += yazi(106, 26, 'Hz. İbrahim’in Sorusu', MAVI, kalin=True)
    ic += yazi(106, 52, '«Düşün bakalım,', LAC)
    ic += yazi(106, 74, 'sen bu işe ne dersin?»', LAC)

    ic += kutu(214, 6, 200, 84, YES_A, YES)
    ic += yazi(314, 26, 'Hz. İsmail’in Cevabı', YES, kalin=True)
    ic += yazi(314, 52, '«Emredileni yap,', LAC)
    ic += yazi(314, 74, 'sabredenlerden olacağım.»', YES, kalin=True)
    return svg(420, 96, ic, 'Sâffât suresi 102. ayet baba-oğul istişare ve teslimiyet panosu.', 21)


def kultur_yansima_haritasi():
    kartlar = [
        (6, 6, 'Edebiyat ve Dil', 'Koçyiğit deyimi', MOR, MOR_A),
        (214, 6, 'Hacı İkramı', 'Zemzem ve hurma', CAM, CAM_A),
        (6, 54, 'Cami Sanatı', 'Hat ve çini süsü', MAVI, MAVI_A),
        (214, 54, 'Üçlü Paylaşım', 'Aile · Komşu · Yoksul', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi(x + 100, y + 18, bas, r, kalin=True)
        ic += yazi(x + 100, y + 36, alt, LAC)
    return svg(420, 102, ic, 'Hac ve kurban ibadetinin kültürümüzdeki dört farklı yansıması.', 22)


def meryem_54_erdem_karti():
    ic = kutu(6, 6, 408, 84, MOR_A, MOR)
    ic += f'<rect x="18" y="18" width="54" height="60" rx="6" fill="#ddd6fe" stroke="{MOR}" stroke-width="1.2"/>'
    ic += f'<line x1="28" y1="34" x2="62" y2="34" stroke="{MOR}" stroke-width="1.2"/>'
    ic += f'<line x1="28" y1="48" x2="62" y2="48" stroke="{MOR}" stroke-width="1.2"/>'
    ic += f'<line x1="28" y1="62" x2="54" y2="62" stroke="{MOR}" stroke-width="1.2"/>'
    ic += yazi(246, 28, 'Meryem Suresi 54 ve 55. Ayetler', MOR, kalin=True)
    ic += yazi(246, 53, '1) Sözünde duran elçi (Sadıkü’l-va’d)', LAC)
    ic += yazi(246, 76, '2) Ailesine namazı ve zekâtı emretmesi', YES, kalin=True)
    return svg(420, 96, ic, 'Meryem suresi 54 ve 55. ayetlerde Hz. İsmail’in övülen erdemleri.', 21)


def mekke_tarih_seridi():
    adimlar = [
        (6, '1. Adım', 'Mekke Vadisi', MAVI, MAVI_A),
        (110, '2. Adım', 'Sa’y ve Zemzem', CAM, CAM_A),
        (214, '3. Adım', 'Cürhüm İskânı', YES, YES_A),
        (318, '4. Adım', 'Kâbe İnşası', TUR, TUR_A),
    ]
    ic = ''
    for x, ust, alt, r, z in adimlar:
        ic += kutu(x, 6, 96, 84, z, r)
        ic += yazi(x + 48, 30, ust, r, kalin=True)
        ic += f'<circle cx="{x + 48}" cy="48" r="4" fill="{r}"/>'
        ic += yazi(x + 48, 72, alt, LAC)
    return svg(420, 96, ic, 'Mekke vadisinde yerleşimden Kâbe inşasına dört aşamalı zaman şeridi.', 21)


def uc_kina_kultur_karti():
    ic = kutu(6, 6, 200, 84, KIR_A, KIR)
    ic += f'<circle cx="38" cy="48" r="18" fill="#fecaca" stroke="{KIR}" stroke-width="1.2"/>'
    ic += yazi(38, 53, '1', KIR, kalin=True)
    ic += yazi(128, 34, 'Kurbanlık Koç', KIR, kalin=True)
    ic += yazi(128, 62, 'Allah’a adanmışlık', LAC)

    ic += kutu(214, 6, 200, 84, YES_A, YES)
    ic += f'<circle cx="246" cy="48" r="18" fill="#bbf7d0" stroke="{YES}" stroke-width="1.2"/>'
    ic += yazi(246, 53, '2', YES, kalin=True)
    ic += yazi(336, 34, 'Mehmetçiğe Kına', YES, kalin=True)
    ic += yazi(336, 62, 'Vatana adanmışlık', LAC)
    return svg(420, 96, ic, 'Anadolu kültüründe kına geleneğinin sembolik anlam kartları.', 21)


def hac_37_takva_karti():
    ic = kutu(6, 6, 408, 84, TUR_A, TUR)
    ic += yazi(210, 26, 'Hac Suresi, 37. Ayet Mesajı', TUR, kalin=True)
    ic += yazi(210, 52, '«Allah’a ulaşacak olan ne etleri ne kanlarıdır;', LAC)
    ic += yazi(210, 75, 'O’na ulaşacak olan yalnızca sizin takvanızdır.»', YES, kalin=True)
    return svg(420, 96, ic, 'Hac suresi 37. ayette kurban ibadetinin takva mesajı kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = mekke_hatira_semasi()
    s[2]['gorsel'] = ayet_mesaj_kartlari()
    s[5]['gorsel'] = saffat_istisare_panosu()
    s[6]['gorsel'] = kultur_yansima_haritasi()
    s[7]['gorsel'] = meryem_54_erdem_karti()
    s[8]['gorsel'] = mekke_tarih_seridi()
    s[9]['gorsel'] = uc_kina_kultur_karti()
    s[11]['gorsel'] = hac_37_takva_karti()
