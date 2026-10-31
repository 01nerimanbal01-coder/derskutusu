"""7. sınıf Sosyal Bilgiler 4. hafta (özel gereksinimli bireyler için fırsat eşitliği) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=10.5, renk=LAC, hiza='start', ara=13):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, no, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="8.5" fill="{renk}"/>' + yazi(x, y + 4, str(no), 10.5, '#fff')


def bakim_merkez_semasi():
    """Aile ve Sosyal Hizmetler Bakanlığının dört bakım hizmeti şeması (3 numaralı kart soru işaretli)."""
    ic = kutu(66, 4, 228, 22, LAC, LAC, 11, 1) + yazi(180, 19, 'Aile ve Sosyal Hizmetler Bakanlığı', 11.5, '#fff')
    kartlar = [
        (1, 'Umut Evleri', ['Günlük yaşam becerileri,', 'bağımsız yaşam ve katılım'], MAVI, MAVI_A),
        (2, 'Gündüz Bakım Merkezleri', ['Aileye zaman; bireye öz bakım,', 'kültür ve spor etkinlikleri'], TUR, TUR_A),
        (3, 'Geçici ve Misafir Bakım', ['?', '(İşlevi nedir?)'], YES, YES_A),
        (4, 'Özel Bakım Merkezleri', ['Devamlı bakıma gereksinimi', 'olanlara profesyonel destek'], MOR, MOR_A),
    ]
    for i, (no, bas, sat, c, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 32 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, c, 7, 1.3) + rozet(x + 14, y + 14, no, c)
        ic += yazi(x + 28, y + 17, bas, 10.5, c, 'start')
        ic += duz(x + 12, y + 29, [sat[0]], 10.5, LAC, 'start', 11)
    return svg(360, 118, ic, 'Aile ve Sosyal Hizmetler Bakanlığı dört hizmet şeması: 1 Umut Evleri, 2 Gündüz Bakım Merkezleri, 3 Geçici ve Misafir Bakım soru işaretli, 4 Özel Bakım Merkezleri.', 22)


def erisim_araclari():
    """Üç erişilebilirlik düzenlemesi: Braille kabartma yazı, işaret dili, araç içi rampa."""
    ic = ''
    kartlar = [('Braille kabartma yazı', MAVI, MAVI_A), ('İşaret dili alfabesi', TUR, TUR_A), ('Araç içi rampa', YES, YES_A)]
    for i, (bas, c, z) in enumerate(kartlar):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 76, z, c, 8, 1.4)
        ic += yazi(x + 57, 22, bas, 10.5, c)
        if i == 0:
            ic += kutu(x + 22, 30, 70, 42, '#fff', c, 5, 1.1)
            for r in range(3):
                for k in range(4):
                    dolu = (r + k) % 2 == 0
                    ic += f'<circle cx="{x + 34 + k * 15}" cy="{40 + r * 11}" r="3.2" fill="{c if dolu else GRI_A}" stroke="{c}" stroke-width="1"/>'
        elif i == 1:
            ic += kutu(x + 22, 30, 70, 42, '#fff', c, 5, 1.1)
            ic += f'<rect x="{x + 34}" y="38" width="20" height="24" rx="4" fill="{TUR_A}" stroke="{c}" stroke-width="1.2"/>'
            ic += yazi(x + 44, 54, 'A', 12, c)
            ic += f'<rect x="{x + 60}" y="38" width="20" height="24" rx="4" fill="{TUR_A}" stroke="{c}" stroke-width="1.2"/>'
            ic += yazi(x + 70, 54, 'B', 12, c)
        else:
            ic += kutu(x + 16, 32, 46, 28, '#fff', c, 4, 1.2)
            ic += f'<circle cx="{x + 28}" cy="62" r="5" fill="{LAC}"/><circle cx="{x + 50}" cy="62" r="5" fill="{LAC}"/>'
            ic += f'<path d="M{x + 62} 56 L{x + 98} 68 L{x + 62} 68 Z" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.2"/>'
    return svg(360, 88, ic, 'Üç erişilebilirlik düzenlemesi kartı: Braille kabartma nokta levhası, işaret dili harf kartları ve toplu taşıma araç içi rampa.', 19)


def il_uygulamalari_harita():
    """Kastamonu, Fethiye ve Karabük fırsat eşitliği uygulama panosu."""
    veri = [
        ('Kastamonu', '“Sen de Gel” Projesi', ['Uzman eğitmenle atlı terapi', 'Kas, denge ve yürüme gelişimi'], MAVI, MAVI_A),
        ('Fethiye', 'Engelsiz Plaj ve Kısa Mola', ['Denizden kolay yararlanma', 'Ailelere günlük işler için vakit'], TUR, TUR_A),
        ('Karabük', 'Evde Bakım Hizmeti', ['Haftada veya ayda bir ziyaret', 'Yaşlılar dâhil temizlik desteği'], YES, YES_A),
    ]
    ic = ''
    for i, (il, bas, sat, c, z) in enumerate(veri):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 88, z, c, 8, 1.4)
        ic += f'<rect x="{x}" y="6" width="114" height="22" rx="8" fill="{c}"/><rect x="{x}" y="18" width="114" height="10" fill="{c}"/>'
        ic += yazi(x + 57, 21, il, 11.5, '#fff')
        ic += yazi(x + 57, 42, bas, 10.5, c)
        ic += duz(x + 57, 60, sat, 10.5, LAC, 'middle', 14)
    return svg(360, 100, ic, 'Üç yerleşim yeri uygulama panosu: Kastamonu Sen de Gel atlı terapi projesi, Fethiye engelsiz plaj ve kısa mola merkezi, Karabük evde bakım hizmeti.', 20)


def atli_terapi_etki():
    """Kastamonu Sen de Gel atlı terapi projesinin iki yönlü etkisi diyagramı."""
    ic = kutu(84, 4, 192, 24, MAVI, MAVI, 12, 1) + yazi(180, 20, 'Kastamonu · “Sen de Gel” Atlı Terapi', 11, '#fff')
    ic += f'<path d="M140 28 L90 42 M220 28 L270 42" stroke="{LAC}" stroke-width="1.6"/>'
    ic += kutu(8, 42, 166, 52, TUR_A, TUR, 8, 1.4)
    ic += yazi(91, 58, '1. Çocuk üzerindeki etkisi', 11, TUR)
    ic += duz(91, 74, ['Fiziksel ve ruhsal gelişim', '(Kas, denge ve yürüme: ?)'], 10.5, LAC, 'middle', 13)
    ic += kutu(186, 42, 166, 52, YES_A, YES, 8, 1.4)
    ic += yazi(269, 58, '2. Aile üzerindeki etkisi', 11, YES)
    ic += duz(269, 74, ['Sosyal hayata daha çok katılım,', 'çocuğun gelişimine etkin destek'], 10.5, LAC, 'middle', 13)
    return svg(360, 100, ic, 'Kastamonu Sen de Gel atlı terapi diyagramı: 1 çocuk üzerindeki fiziksel ve ruhsal gelişim etkisi, 2 aile üzerindeki sosyal hayata katılım ve destek etkisi.', 20)


def beyin_eseri_masa():
    """Beyin eseri tekniğinde beş alan kâğıdı ve öğretmen masası şeması."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.3)
    ic += yazi(180, 20, 'Beyin Eseri Tekniği · Fikir Üretilen Beş Alan Kâğıdı', 11.5, LAC)
    alanlar = [('Eğitim', MAVI, MAVI_A), ('Sağlık', YES, YES_A), ('Ulaşım', TUR, TUR_A), ('İstihdam', MOR, MOR_A), ('Sosyal yaşam', CAM, CAM_A)]
    for i, (ad, c, z) in enumerate(alanlar):
        x = 10 + i * 68
        ic += kutu(x, 28, 64, 34, z, c, 6, 1.3)
        ic += yazi(x + 32, 49, ad, 10.5, c)
    ic += kutu(24, 68, 312, 22, '#fff', KAHVE, 6, 1.2)
    ic += yazi(180, 83, 'Kâğıtlar ters çevrilir → Sesli okunur → Gruplandırılır → En özgün seçilir', 10.5, KAHVE)
    return svg(360, 102, ic, 'Beyin eseri tekniği beş alan kâğıdı: Eğitim, Sağlık, Ulaşım, İstihdam, Sosyal yaşam. Altta süreç akışı.', 20)


def deger_kartlari():
    """Sevgi, şefkat ve merhamet değer kartları ile ortak toplumsal sonuç."""
    ic = ''
    degerler = [('Sevgi', 'Olduğu gibi kabul', MAVI, MAVI_A), ('Şefkat', 'Anında destek', TUR, TUR_A), ('Merhamet', 'Zorluğu anlama', YES, YES_A)]
    for i, (ad, ip, c, z) in enumerate(degerler):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 44, z, c, 8, 1.4)
        ic += yazi(x + 56, 24, ad, 12, c)
        ic += yazi(x + 56, 40, ip, 10.5, SOLUK)
    ic += kutu(18, 58, 324, 26, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 75, 'Ortak sonuç: Saygı, dayanışma, yardımlaşma ve kapsayıcı toplum', 10.5, MOR)
    return svg(360, 90, ic, 'Üç değer kartı: Sevgi, Şefkat, Merhamet. Altta ortak sonuç: saygı, dayanışma, yardımlaşma ve kapsayıcı toplum.', 19)


def proje_taslak_panosu():
    """Üç bölümlü proje taslağı panosu: Ekip, Projenin Kimliği, Uygulama."""
    bolumler = [
        ('1. Ekip', ['Grubun adı', 'Görevli öğrenciler', 'Proje yürütücüsü'], MAVI, MAVI_A),
        ('2. Projenin Kimliği', ['Adı ve amacı', 'Yeri, tarihi ve süresi', 'Yararlanacak kişiler'], TUR, TUR_A),
        ('3. Uygulama', ['İzlenecek adımlar', 'Yararlanılan kaynaklar', 'Sonuç ve değerlendirme'], YES, YES_A),
    ]
    ic = ''
    for i, (bas, maddeler, c, z) in enumerate(bolumler):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 86, z, c, 8, 1.4)
        ic += f'<rect x="{x}" y="6" width="114" height="22" rx="8" fill="{c}"/><rect x="{x}" y="18" width="114" height="10" fill="{c}"/>'
        ic += yazi(x + 57, 21, bas, 11, '#fff')
        ic += duz(x + 8, 42, maddeler, 10.5, LAC, 'start', 15)
    return svg(360, 98, ic, 'Üç sütunlu proje taslağı panosu. 1 Ekip: grubun adı, görevli öğrenciler, proje yürütücüsü. 2 Projenin Kimliği: adı ve amacı, yeri tarihi ve süresi, yararlanacak kişiler. 3 Uygulama: izlenecek adımlar, yararlanılan kaynaklar, sonuç ve değerlendirme.', 17)


def fethiye_karabuk_karsilastirma():
    """Evde ve hastanede eğitim ile evde bakım hizmeti karşılaştırma kartları."""
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(91, 22, 'Evde ve Hastanede Eğitim', 11, MAVI)
    ic += duz(91, 40, ['Millî Eğitim Bakanlığı sunar;', 'okula gidemeyen öğrencinin', 'eğitim hakkı kesintisiz sürer.'], 10.5, LAC, 'middle', 13)
    ic += kutu(184, 6, 170, 76, YES_A, YES, 8, 1.4)
    ic += yazi(269, 22, 'Evde Bakım Hizmeti (Karabük)', 11, YES)
    ic += duz(269, 40, ['Haftada veya ayda bir ziyaret;', 'temel temizlik ihtiyaçları görülür,', 'güvenli ve huzurlu yaşam sağlanır.'], 10.5, LAC, 'middle', 13)
    return svg(360, 88, ic, 'İki kart: solda Millî Eğitim Bakanlığı Evde ve Hastanede Eğitim, sağda Karabük Evde Bakım Hizmeti.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bakim_merkez_semasi()
    s[1]['gorsel'] = erisim_araclari()
    s[2]['gorsel'] = il_uygulamalari_harita()
    s[3]['gorsel'] = atli_terapi_etki()
    s[5]['gorsel'] = beyin_eseri_masa()
    s[7]['gorsel'] = deger_kartlari()
    s[8]['gorsel'] = proje_taslak_panosu()
    s[10]['gorsel'] = fethiye_karabuk_karsilastirma()
