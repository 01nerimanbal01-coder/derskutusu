"""6. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta (Oruç ve Kur'an Ayı Ramazan) çalışma kâğıdı görselleri.
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


def bakara_185_panosu():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'BAKARA SURESİ · 185. AYET MEALİ', 10.4, MAVI)
    ic += yazi(180, 42, '“İnsanlar için bir hidayet rehberi ve hak ile batılı ayıran', 9.7, LAC, ince=True)
    ic += yazi(180, 57, 'apaçık deliller olarak Kur’an, Ramazan ayında indirilmiştir.', 9.7, LAC, ince=True)
    ic += yazi(180, 72, 'İçinizden kim bu aya ulaşırsa onu oruçla geçirsin...”', 9.9, LAC)
    return svg(360, 88, ic, 'Bakara Suresi 185. ayet meali bilgi kartı.', 15)


def bursa_imsakiye_karti():
    vakitler = [
        ('1. 05.10', 'Sahur Vakti', MAVI, MAVI_A),
        ('2. 05.42', 'Oruç Başlangıcı (?)', KIR, KIR_A),
        ('3. 18.15', 'Oruç Açma (?)', YES, YES_A),
        ('4. 19.35', 'Yatsı Sonrası (?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (saat, aciklama, r, z) in enumerate(vakitler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, saat, 10.3, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, aciklama, 9.3, LAC, ince=True)
    return svg(360, 84, ic, 'Ramazan gününde dört temel vakti gösteren imsakiye çizelgesi.', 15)


def dort_kavram_kontrol_karti():
    kartlar = [
        ('1. Sahur', 'İmsak öncesi bereket yemeği', YES, YES_A),
        ('2. Hatim', 'Kur’an’ı baştan sona okumak', MAVI, MAVI_A),
        ('3. İftar', 'Akşam ezanıyla orucu açmak', TUR, TUR_A),
        ('4. Teravih (!)', 'Kurban Bayramı sabah namazı (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, icerik, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Sahur, hatim, iftar ve teravih kavram kartları.', 16)


def arza_mukabele_semasi():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'Asr-ı Saadet (Arza)', 10.3, CAM)
    ic += yazi(91, 44, 'Cebrail (a.s.) ve Peygamberimiz', 9.6, LAC, ince=True)
    ic += yazi(91, 64, 'Karşılıklı Kur’an tilaveti', 9.8, CAM)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Günümüzdeki Geleneğimiz', 10.3, YESIL_K)
    ic += yazi(269, 44, 'Hafız okur · Cemaat takip eder', 9.6, LAC, ince=True)
    ic += yazi(269, 64, 'Kavram Adı = ?', 10.0, YESIL_K)
    return svg(360, 88, ic, 'Arza uygulamasından mukabele geleneğine geçiş şeması.', 15)


def kadir_gecesi_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'KADİR SURESİ (1-5. AYETLER) BİLGİ KARTI', 10.4, MOR)
    ic += yazi(180, 43, '• Kur’an-ı Kerim Kadir Gecesi’nde indirilmeye başlanmıştır.', 9.7, LAC, ince=True)
    ic += yazi(180, 58, '• “Kadir Gecesi bin aydan (yaklaşık 83 yıldan) daha hayırlıdır.”', 9.8, MOR)
    ic += yazi(180, 73, '• Melekler ve Ruh (Cebrail) o gece esenlik için yeryüzüne iner.', 9.6, LAC, ince=True)
    return svg(360, 88, ic, 'Kadir Gecesi ve Kadir Suresi temel mesajları kartı.', 15)


def ramazan_gunu_adimlari():
    adimlar = [
        ('Gece', 'Sahur ve Niyet', MAVI, MAVI_A),
        ('Şafak', 'İmsak (Başlangıç)', KIR, KIR_A),
        ('Akşam', 'İftar (Oruç Açma)', YES, YES_A),
        ('Yatsı', 'Teravih Namazı', MOR, MOR_A),
    ]
    ic = ''
    for i, (vakit, eylem, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, vakit, 10.3, r)
        ic += yazi(x + 41, 54, eylem, 9.3, LAC, ince=True)
    return svg(360, 84, ic, 'Ramazan gününde sahur, imsak, iftar ve teravih sıralaması.', 15)


def oruc_ahlaki_hadis_karti():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 22, 'HADİS-İ ŞERİF · ORUÇ VE GÜZEL AHLAK', 10.4, TUR)
    ic += yazi(180, 44, '“Kim yalan konuşmayı ve yalanla iş yapmayı bırakmazsa,', 9.8, LAC, ince=True)
    ic += yazi(180, 62, 'Allah’ın o kimsenin yemesini ve içmesini bırakmasına ihtiyacı yoktur.”', 9.8, LAC)
    return svg(360, 88, ic, 'Orucun ahlaki boyutunu vurgulayan hadis-i şerif kartı.', 15)


def ramazan_dayanisma_panosu():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Empati ve Sabır', 10.3, YESIL_K)
    ic += yazi(91, 44, 'Aç ve susuz kalarak yoksulun', 9.6, LAC, ince=True)
    ic += yazi(91, 64, 'hâlini bizzat anlamak', 9.8, YESIL_K)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, '2. Paylaşma ve Fitre', 10.3, MAVI)
    ic += yazi(269, 44, 'İftar sofrası, zekât ve fitre ile', 9.6, LAC, ince=True)
    ic += yazi(269, 64, 'bayram sevincini çoğaltmak', 9.8, MAVI)
    return svg(360, 88, ic, 'Ramazan ayında empati ve fitre ile toplumsal dayanışma panosu.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bakara_185_panosu()
    s[2]['gorsel'] = bursa_imsakiye_karti()
    s[5]['gorsel'] = dort_kavram_kontrol_karti()
    s[6]['gorsel'] = arza_mukabele_semasi()
    s[7]['gorsel'] = kadir_gecesi_karti()
    s[8]['gorsel'] = ramazan_gunu_adimlari()
    s[9]['gorsel'] = oruc_ahlaki_hadis_karti()
    s[11]['gorsel'] = ramazan_dayanisma_panosu()
