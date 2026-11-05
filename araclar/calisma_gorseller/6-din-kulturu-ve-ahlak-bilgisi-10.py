"""6. sınıf Din Kültürü ve Ahlak Bilgisi 10. hafta (Oruç İbadeti: Şartları, Bozan-Bozmayan Durumlar, Kazâ-Kefaret-Fidye ve Oruç Çeşitleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def orucu_bozan_bozmayan_kartlari():
    kartlar = [
        ('1. Kart (!)', 'Abdestte hata ile su yutmak', KIR, KIR_A),
        ('2. Kart', 'Unutarak bir şey yemek', YES, YES_A),
        ('3. Kart', 'Su yutmadan duş almak', MAVI, MAVI_A),
        ('4. Kart', 'Hastaya kan bağışı yapmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Orucu bozan ve bozmayan dört farklı durum kartı.', 16)


def dini_kolayliklar_panosu():
    kartlar = [
        ('1. Seferî (Yolcu)', 'Kazâ (1’e 1)', MAVI, MAVI_A),
        ('2. Kalıcı Yaşlı/Hasta', 'Fidye (?)', YES, YES_A),
        ('3. Kasten Bozan', 'Kefaret 60+1 (?)', KIR, KIR_A),
        ('4. Geçici Hasta', 'Kazâ (?)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Kazâ, kefaret ve fidye hükümlerini özetleyen pano.', 15)


def oruc_cesitleri_sema():
    kartlar = [
        ('K Kutusu', 'Ramazan Ayı Orucu', MAVI, MAVI_A),
        ('L Kutusu', 'Adak (Nezir) Orucu', YES, YES_A),
        ('M Kutusu', 'Aşure ve Şevval Orucu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 10}" y1="32" x2="{x + 102}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 56, 52, alt, 9.3, LAC, ince=True)
        ic += yazi(x + 56, 68, 'Hükmü = ?', 9.3, r)
    return svg(360, 86, ic, 'K, L ve M kutularında oruç çeşitlerinin sınıflandırılması.', 15)


def yukumluluk_durum_kartlari():
    kartlar = [
        ('A · Zeynep (9 yaş)', 'Ergenlik çağına gelmemiş', TUR, TUR_A),
        ('B · Mehmet Bey', 'Uzun yolda (Seferî)', MAVI, MAVI_A),
        ('C · Ali Bey (25 yaş)', 'Akıllı, sağlıklı, mukim', YES, YES_A),
        ('D · Ayşe Hanım', 'Ağır hasta (Ruhsatlı)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Oruçla yükümlü olma şartlarını inceleyen dört kişi kartı.', 16)


def unutarak_yeme_hadis_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'HADİS-İ ŞERİF · UNUTARAK YEME VE İÇMENİN HÜKMÜ', 10.1, CAM)
    ic += yazi(180, 44, '“Kim oruçlu iken unutarak yer veya içerse orucunu tamamlasın;', 9.4, LAC, ince=True)
    ic += yazi(180, 64, 'çünkü ona Allah yedirmiş ve içirmiştir.” (Buhârî, Savm, 26)', 9.4, CAM)
    return svg(360, 88, ic, 'Unutarak yiyip içenin orucunun bozulmayacağını bildiren hadis kartı.', 15)


def gunluk_oruc_akisi():
    adimlar = [
        ('1. Sahur', 'İmsaktan önce', MAVI, MAVI_A),
        ('2. Niyet', 'Kalben ve dille', YES, YES_A),
        ('3. İmsak', 'Sakınma süreci', TUR, TUR_A),
        ('4. İftar', 'Akşam duası', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Sahurdan iftara bir günlük oruç ibadeti akış şeması.', 15)


def oruc_kazanimlari_panosu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Bireysel Kazanımlar', 10.2, MAVI)
    ic += yazi(91, 44, '• Sabır ve irade eğitimi', 9.4, LAC, ince=True)
    ic += yazi(91, 64, '• Nimetlere şükür ve öz denetim', 9.4, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Toplumsal Kazanımlar', 10.2, YESIL_K)
    ic += yazi(269, 44, '• Yoksullarla empati ve merhamet', 9.4, LAC, ince=True)
    ic += yazi(269, 64, '• İftar ve yardımlaşma kardeşliği', 9.4, YESIL_K)
    return svg(360, 88, ic, 'Oruç ibadetinin bireysel ve toplumsal faydaları şeması.', 15)


def bakara_kolaylik_ayeti_karti():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 22, 'KUR’AN-I KERİM’DE ORUÇ KOLAYLIĞI (RUHSAT)', 10.2, TUR)
    ic += yazi(180, 44, '“...Sizden kim hasta ya da yolculukta olursa, tutamadığı günler', 9.4, LAC, ince=True)
    ic += yazi(180, 64, 'sayısınca başka günlerde tutar. Allah sizin için kolaylık ister...” (Bakara, 185)', 9.2, TUR)
    return svg(360, 88, ic, 'Bakara suresi 185. ayette yolcu ve hastalara tanınan kolaylık kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = orucu_bozan_bozmayan_kartlari()
    s[2]['gorsel'] = dini_kolayliklar_panosu()
    s[5]['gorsel'] = oruc_cesitleri_sema()
    s[6]['gorsel'] = yukumluluk_durum_kartlari()
    s[7]['gorsel'] = unutarak_yeme_hadis_karti()
    s[8]['gorsel'] = gunluk_oruc_akisi()
    s[9]['gorsel'] = oruc_kazanimlari_panosu()
    s[11]['gorsel'] = bakara_kolaylik_ayeti_karti()
