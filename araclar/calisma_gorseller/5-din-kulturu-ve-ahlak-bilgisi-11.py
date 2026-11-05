"""5. sınıf Din Kültürü ve Ahlak Bilgisi 11. hafta (Namazı Bozan Durumlar, Sehiv Secdesi, Cemaatle Namaz ve Namazın Kazandırdıkları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_namaz_durum_karti():
    kartlar = [
        ('1. Kart · Unutma', 'İlk oturuş (vacip) unutuldu', YES, YES_A),
        ('2. Kart · Konuşma', 'Kapıdakine sesli yanıt verildi', KIR, KIR_A),
        ('3. Kart · Farz Terki', 'Rükû ve secde yapılmadı', TUR, TUR_A),
        ('4. Kart · Abdest', 'Namaz içinde abdest bozuldu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, aciklama, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, aciklama, 9.5, LAC, ince=True)
    return svg(360, 94, ic, 'Namazda karşılaşılan dört farklı durum kartı.', 15)


def cemaat_namazlari_kartlari():
    kartlar = [
        ('1. Cuma', '10 Rekât · Hutbeli', YES, YES_A),
        ('2. Bayram', '2 Rekât · Tekbirli', MAVI, MAVI_A),
        ('3. Teravih', '20 Rekât · Ramazan', TUR, TUR_A),
        ('4. Cenaze', 'Ayakta · 4 Tekbir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Cuma, bayram, teravih ve cenaze namazı kartları.', 15)


def cuma_bayram_karsilastirma_panosu():
    satirlar = [
        ('I. Rekât Sayısı', 'Cuma farzı: 2 · Bayram: 2', MAVI, MAVI_A),
        ('II. Hutbe Zamanı', 'Cuma: Sonra · Bayram: Önce', KIR, KIR_A),
        ('III. Kılınış Şekli', 'Her ikisi de cemaatle kılınır', YES, YES_A),
        ('IV. İlave Tekbir', 'Bayramda her rekâtta 3 tekbir', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, bilgi, r, z) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, bilgi, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Cuma ve bayram namazı özelliklerini karşılaştırma panosu.', 15)


def ramazan_namazi_tanitim_karti():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 23, 'Ramazan Ayına Özgü Namaz Bilgi Kartı', 10.5, TUR)
    ic += yazi(180, 45, 'Vakti: Yatsı namazının son sünnetinden sonra, vitirden önce', 9.7, LAC)
    ic += yazi(180, 66, 'Hükmü: Sünnet  |  Rekât Sayısı: 20 Rekât (2 veya 4 rekâtta selamla)', 9.5, TUR, ince=True)
    return svg(360, 88, ic, 'Ramazan ayında yatsıdan sonra kılınan 20 rekâtlık namaz kartı.', 15)


def ankebut_ayet_panosu():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 23, 'Kur’an-ı Kerim Mesajı · Ankebût Suresi, 45. Ayet', 10.4, YESIL_K)
    ic += yazi(180, 46, '«Şüphesiz namaz, insanı hayasızlıktan ve kötülükten alıkoyar.»', 10.0, LAC)
    ic += yazi(180, 67, 'Günde 5 vakit İlahi huzura çıkma bilinci → Güzel ahlak ve dürüstlük', 9.4, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Ankebût suresi 45. ayet ve ahlaki etkisi kartı.', 15)


def sehiv_secdesi_adimlari():
    adimlar = [
        ('A Adımı', 'Sağa selam ver', MAVI, MAVI_A),
        ('B Adımı', 'Peş peşe 2 secde', TUR, TUR_A),
        ('C Adımı', 'Duaları oku', YES, YES_A),
        ('D Adımı', 'İki yana selam', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 55, met, 9.3, LAC, ince=True)
    return svg(360, 84, ic, 'Sehiv secdesi uygulama basamakları.', 15)


def namazin_kazandirdiklari_semasi():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Bireysel Kazanımlar', 10.3, MAVI)
    ic += yazi(91, 44, '• İç huzuru ve güzel ahlak', 9.6, LAC, ince=True)
    ic += yazi(91, 64, '• Zaman ve temizlik disiplini', 9.6, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Toplumsal Kazanımlar', 10.3, YESIL_K)
    ic += yazi(269, 44, '• Aynı safta eşitlik ve birlik', 9.6, LAC, ince=True)
    ic += yazi(269, 64, '• Komşuluk ve yardımlaşma', 9.6, LAC, ince=True)
    return svg(360, 88, ic, 'Namazın bireysel ve toplumsal kazanımları şeması.', 15)


def farz_vacip_terki_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, '1. Durum · Farzın Terki', 10.2, KIR)
    ic += yazi(91, 44, 'Rükû veya secde hiç yapılmadı', 9.6, LAC, ince=True)
    ic += yazi(91, 65, 'Sonuç: Namaz bozulur (İade)', 9.6, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Durum · Vacibin Unutulması', 10.2, YESIL_K)
    ic += yazi(269, 44, 'Zamm-ı sure unutularak atlandı', 9.6, LAC, ince=True)
    ic += yazi(269, 65, 'Sonuç: Sehiv secdesi yeterlidir', 9.6, YESIL_K)
    return svg(360, 88, ic, 'Farzın terk edilmesi ile vacibin unutulması farkı kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_namaz_durum_karti()
    s[2]['gorsel'] = cemaat_namazlari_kartlari()
    s[5]['gorsel'] = cuma_bayram_karsilastirma_panosu()
    s[6]['gorsel'] = ramazan_namazi_tanitim_karti()
    s[7]['gorsel'] = ankebut_ayet_panosu()
    s[8]['gorsel'] = sehiv_secdesi_adimlari()
    s[9]['gorsel'] = namazin_kazandirdiklari_semasi()
    s[11]['gorsel'] = farz_vacip_terki_karti()
