"""6. sınıf DKAB 3. hafta (Peygamberlerin İlettiği Mesaj: Vahiy — Vahyin Gönderiliş Amacı) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; ayet levhası yok K055; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def akil_vahiy_karsilastirma():
    ic = f'<rect x="8" y="8" width="280" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(148, 26, 'İnsana Verilen Akıl', 11.4, MAVI)
    ic += yazi(22, 48, 'İyi ile kötüyü, doğru ile yanlışı ayırt eder.', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 68, 'Ancak K alanındaki büyük sorularda', 10.5, LAC, 'start', ince=True)
    ic += yazi(32, 86, 'cevaplar kişiden kişiye değişebilir: K = ?', 10.6, MAVI, 'start')

    ic += f'<rect x="308" y="8" width="284" height="96" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(450, 26, 'Allah’ın Gönderdiği Vahiy', 11.4, TUR)
    ic += yazi(322, 48, 'K alanındaki sorularda doğru bilgiyi verir.', 10.5, LAC, 'start', ince=True)
    ic += yazi(322, 68, 'İnsanın yaratılış ve dünya-ahiret', 10.5, LAC, 'start', ince=True)
    ic += yazi(332, 86, 'hedefini açıklar: L = ?', 10.6, TUR, 'start')
    return svg(600, 112, ic, 'Akıl ve vahiy karşılaştırma şeması: K cevabı kişiden kişiye değişen büyük sorular, L vahyin kazandırdığı kavrayış.', 22)


def mesaj_alanlari_panosu():
    kartlar = [
        ('1. Kart: İnanç Alanı', 'Yaratıcının varlığı, birliği ve', 'temel iman esasları', MAVI, MAVI_A),
        ('2. Kart: İbadet Alanı', 'Namaz, oruç, hac, kurban ve', 'zekât gibi kulluk görevleri', YES, YES_A),
        ('3. Kart: Ahlak Alanı', 'Eski devletlerin coğrafi', 'sınır ve ölçek haritaları', KIR, '#fdeaea'),
        ('4. Kart: Toplumsal Konular', 'İnsanlar arası adalet, haklar', 've karşılıklı yardımlaşma', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 11, renk, 'start')
        ic += yazi(x + 18, y + 38, f'{s1} {s2}', 10.3, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Kur’an mesaj alanları panosu: 1. İnanç, 2. İbadet, 3. Ahlak (hatalı açıklama), 4. Toplumsal konular.', 23)


def peygamber_ozellik_kartlari():
    kartlar = [
        ('1. Kart', 'Hz. İbrahim', 'Öne çıkan yönü : ?', MAVI, MAVI_A),
        ('2. Kart', 'Hz. Eyyüb ve Hz. Yakub', 'Öne çıkan yönü : ?', YES, YES_A),
        ('3. Kart', 'Hz. Yusuf', 'Öne çıkan yönü : ?', TUR, TUR_A),
        ('4. Kart', 'Hz. Musa', 'Öne çıkan yönü : ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ad, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, ad, 10.6, LAC)
        ic += yazi(x + 68, 76, alt, 10.3, renk, ince=True)
    return svg(600, 102, ic, 'Dört peygamber kartı: 1. Hz. İbrahim, 2. Hz. Eyyüb ve Hz. Yakub, 3. Hz. Yusuf, 4. Hz. Musa.', 22)


def insan_peygamber_katkisi_sema():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Peygamberlerin İnsanlar Arasından Seçilmesinin Katkıları', 11.4, LAC)
    kutular = [
        ('1. Toplumu Tanıma', 'Yaşadığı halkın dilini ve', 'koşullarını yakından bilme', MAVI, MAVI_A),
        ('2. Sağlıklı İletişim', 'Mesajı anlaşılır biçimde', 've eksiksiz ulaştırma', TUR, TUR_A),
        ('3. Uygulamalı Örneklik', 'Namaz, oruç, hac, zekât ve', 'kurbanı bizzat gösterme', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.1, LAC, ince=True)
    return svg(600, 110, ic, 'Peygamberlerin insanlar arasından seçilmesinin üç katkısı: toplumu tanıma, sağlıklı iletişim ve ibadetleri uygulayarak gösterme.', 22)


def vahiy_ulasma_yolu_sema():
    adimlar = [
        ('İlahi Mesaj', 'Allah vahiy gönderir', MAVI, MAVI_A),
        ('Tebliğ ve Örneklik', 'Peygamberler iletir', TUR, TUR_A),
        ('Doğru Yola Yöneliş', 'İnsanlar rehber edinir', MOR, MOR_A),
        ('Temel Amaç', 'Dünya-ahiret mutluluğu', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11.2, renk)
        ic += yazi(x + 68, 62, alt, 10.4, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 137}" y1="48" x2="{x + 147}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Vahyin ulaşma zinciri: İlahi mesaj, peygamberlerin iletmesi, doğru yola yöneliş ve dünya-ahiret mutluluğu.', 22)


def kissa_amac_karti():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(300, 25, 'Kavram Bilgi Kartı: Kur’an-ı Kerim’de Kıssalar', 11.5, MOR)
    maddeler = [
        ('Konusu', 'Geçmiş peygamberler', 've milletler', MAVI),
        ('Anlatılış Nedeni', 'İnsanlara ibret ve', 'ders vermek', TUR),
        ('İçerik Katkısı', 'İnanç ve ahlak mesajlarını', 'somutlaştırmak', YES),
    ]
    for i, (bas, s1, s2, renk) in enumerate(maddeler):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="58" rx="7" fill="#fff" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.1, LAC, ince=True)
    return svg(600, 108, ic, 'Kıssa bilgi kartı: konusu geçmiş peygamber ve milletler, anlatılış nedeni ibret ve ders vermek, katkısı mesajları somutlaştırmak.', 22)


def hadis_kuran_niteleme_panosu():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 25, 'Hadis-i Şerifte Kur’an-ı Kerim İçin Yapılan Nitelemeler (Tirmizi)', 11.2, KAHVE)
    kutular = [
        ('1. Niteleme', '“Allah’ın sağlam ipidir.”', MAVI, MAVI_A),
        ('2. Niteleme', '“Hikmet dolu sözleridir.”', TUR, TUR_A),
        ('3. Niteleme', '“O, dosdoğru yoldur.”', YES, YES_A),
    ]
    for i, (bas, soz, renk, arka) in enumerate(kutular):
        x = 20 + i * 190
        ic += f'<rect x="{x}" y="36" width="180" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 54, bas, 10.8, renk)
        ic += yazi(x + 90, 75, soz, 10.6, LAC)
    return svg(600, 108, ic, 'Hadiste Kur’an-ı Kerim için yapılan üç niteleme: Allah’ın sağlam ipi, hikmet dolu sözler ve dosdoğru yol.', 22)


def bakara_21_analiz_karti():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 25, 'Bakara Suresi 21. Ayet Kavram Çözümleme Tablosu', 11.3, MAVI)
    sutunlar = [
        ('Hitap Bölümü', '“Ey insanlar!”', '(Bütün insanlığa çağrı)', MAVI),
        ('Hatırlatma Bölümü', '“Sizi ve öncekileri yaratan…”', '(Yaratıcının tanıtılması)', TUR),
        ('Görev ve Hedef', '“…rabbinize kulluk edin…”', '(Sorumluluk ve takvâ)', YES),
    ]
    for i, (bas, s1, s2, renk) in enumerate(sutunlar):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="58" rx="7" fill="#fff" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 90, 50, bas, 10.6, renk)
        ic += yazi(x + 90, 67, s1, 10.3, LAC)
        ic += yazi(x + 90, 83, s2, 10, LAC, ince=True)
    return svg(600, 108, ic, 'Bakara suresi 21. ayet çözümleme tablosu: hitap bölümü, yaratılış hatırlatması ve kulluk görevi.', 22)


def iki_ogrenci_tartisma_karti():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Görüş Kartı', 11.2, KIR)
    ic += yazi(149, 50, '“Vahiy yalnızca namaz ve oruç gibi', 10.6, LAC, ince=True)
    ic += yazi(149, 70, 'ibadet kurallarını bildiren metindir.”', 10.6, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Görüş Kartı', 11.2, YESIL_K)
    ic += yazi(451, 50, '“Vahiy; Allah’ı tanıtır, inanç, ibadet,', 10.6, LAC, ince=True)
    ic += yazi(451, 70, 'ahlak ve toplumda rehberlik eder.”', 10.6, LAC, ince=True)
    return svg(600, 104, ic, 'Vahyin kapsamı hakkında iki görüş kartı: 1. görüş ibadetle sınırlar, 2. görüş inanç, ibadet, ahlak ve toplumu kapsar.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = akil_vahiy_karsilastirma()
    s[4]['gorsel'] = mesaj_alanlari_panosu()
    s[5]['gorsel'] = peygamber_ozellik_kartlari()
    s[6]['gorsel'] = insan_peygamber_katkisi_sema()
    s[7]['gorsel'] = vahiy_ulasma_yolu_sema()
    s[8]['gorsel'] = kissa_amac_karti()
    s[9]['gorsel'] = hadis_kuran_niteleme_panosu()
    s[10]['gorsel'] = bakara_21_analiz_karti()
    s[12]['gorsel'] = iki_ogrenci_tartisma_karti()
