"""8. sınıf DKAB 3. hafta (İnsanın İradesi ve Kader: ilim, cüzi ve külli irade, sorumluluk, hesap verme, kaderi bahane etmeme) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10.5, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def ilim_irade_sema():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#f7f9fd" stroke="{MAVI}" stroke-width="1.6"/>'
    # Başlık sütunları
    ic += f'<rect x="116" y="14" width="224" height="24" rx="7" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(228, 30, 'İnsan (Akıllı ve Sorumlu Varlık)', 11.5, TUR)
    ic += f'<rect x="352" y="14" width="230" height="24" rx="7" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(467, 30, 'Allah (Yüce Yaratıcı)', 11.5, MAVI)

    # 1. satır: İlim
    ic += f'<rect x="16" y="44" width="90" height="36" rx="7" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(61, 66, 'İlim (Bilgi)', 11.5, LAC)
    ic += f'<rect x="116" y="44" width="224" height="36" rx="7" fill="#fff" stroke="{TUR}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += rozet(136, 62, 'K', TUR)
    ic += yazi(238, 66, 'K = ?', 11.5, TUR)
    ic += f'<rect x="352" y="44" width="230" height="36" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(467, 59, 'Sonsuzdur; görünen ve görünmeyen', 10.8, LAC, ince=True)
    ic += yazi(467, 74, 'âlemi (gayb) içine alır.', 10.8, MAVI)

    # 2. satır: İrade
    ic += f'<rect x="16" y="86" width="90" height="36" rx="7" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(61, 108, 'İrade', 11.5, LAC)
    ic += f'<rect x="116" y="86" width="224" height="36" rx="7" fill="#fff" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(228, 101, 'Sınırlıdır (Cüzi irade);', 10.8, TUR)
    ic += yazi(228, 116, 'her istediğini yapamaz.', 10.8, LAC, ince=True)
    ic += f'<rect x="352" y="86" width="230" height="36" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += rozet(372, 104, 'L', MAVI)
    ic += yazi(476, 108, 'L = ? (Külli irade)', 11.5, MAVI)
    return svg(600, 134, ic, 'İnsan ile Allah karşılaştırma şeması: İlim satırında K boşluğu, İrade satırında L boşluğu.', 18)


def irade_sinir_kartlari():
    kartlar = [
        ('1. Durum', 'Saç renginin kumral, göz', 'renginin kahverengi olması', MOR, MOR_A),
        ('2. Durum', 'Hangi şehirde ve hangi anne', 'babadan dünyaya geldiği', MAVI, MAVI_A),
        ('3. Durum', 'Kütüphaneden okumak için', 'tarih romanı seçip alması', YES, YES_A),
        ('4. Durum', 'Sınıf arkadaşına hafta sonu', 'çalışmak için söz vermesi', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="52" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="52" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 47, s2, 10.8, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Bir öğrencinin hayatına dair dört durum kartı: 1. saç ve göz rengi, 2. doğduğu şehir ve aile, 3. seçtiği roman, 4. arkadaşına verdiği söz.', 18)


def ayet_mesaj_kartlari():
    kartlar = [
        ('1. Kart · İnsan suresi 3. ayet', '“… artık o isterse şükreden olur,', 'isterse nankör.”', MAVI, MAVI_A),
        ('2. Kart · Fussilet suresi 46. ayet', '“Kim yararlı iş yaparsa kendi iyiliği için;', 'kötülük işlerse kendi aleyhinedir.”', YES, YES_A),
        ('3. Kart · Bakara suresi 286. ayet', '“Allah hiçbir kimseyi, gücünün', 'yetmediği bir şeyle yükümlü kılmaz…”', TUR, TUR_A),
        ('4. Kart · İsra suresi 15. ayet', '“… Hiç kimse başkasının günah', 'yükünü üstüne almaz. …”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 62
        ic += f'<rect x="{x}" y="{y}" width="286" height="56" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 14, y + 35, s1, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 14, y + 49, s2, 10.8, LAC, 'start', ince=True)
    return svg(600, 130, ic, 'Dört ayet kartı: İnsan 3, Fussilet 46, Bakara 286 ve İsra 15.', 18)


def bilgi_tercih_akisi():
    ic = f'<rect x="6" y="6" width="588" height="108" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    # Üst kutu: Allah önceden bilir
    ic += f'<rect x="150" y="14" width="300" height="36" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(300, 29, 'Allah Sonsuz İlmiyle Önceden Bilir', 11.5, MAVI)
    ic += yazi(300, 44, '(Bilmek, seçimi zorlayan bir etki değildir)', 10.5, LAC, ince=True)
    # Kesikli engel çizgisi
    ic += f'<line x1="300" y1="50" x2="300" y2="62" stroke="{KIR}" stroke-width="1.8" stroke-dasharray="3 2"/>'
    ic += f'<line x1="286" y1="62" x2="314" y2="62" stroke="{KIR}" stroke-width="2.6"/>'

    # Alt üç kutu: İnsan -> Tercih -> Yaratma
    kutular = [
        (18, 'Akıl ve İrade Sahibi İnsan', 'Doğru ile yanlışı ayırt eder', TUR, TUR_A),
        (214, 'Özgür Tercih (Cüzi İrade)', 'Kendi isteğiyle yolu seçer', YES, YES_A),
        (410, 'Fiilin Yaratılması (Allah)', 'Seçilen davranışı yaratır', MOR, MOR_A),
    ]
    for x, b1, b2, renk, arka in kutular:
        ic += f'<rect x="{x}" y="68" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 86, 84, b1, 10.8, renk)
        ic += yazi(x + 86, 99, b2, 10.5, LAC, ince=True)
    ic += f'<line x1="192" y1="87" x2="212" y2="87" stroke="{LAC}" stroke-width="2"/><path d="M208 83 l5 4 l-5 4" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="388" y1="87" x2="408" y2="87" stroke="{LAC}" stroke-width="2"/><path d="M404 83 l5 4 l-5 4" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 120, ic, 'Allah’ın önceden bilmesi insanın tercihini zorlamaz; insan cüzi iradesiyle seçer, Allah seçilen fiili yaratır.', 18)


def sorumluluk_zinciri():
    adlar = [
        ('1. Halka', 'Akıl ve İrade', MAVI, MAVI_A),
        ('2. Halka', 'Yol Gösterme', MOR, MOR_A),
        ('3. Halka', 'İradeli Seçim', TUR, TUR_A),
        ('4. Halka', 'Fiili Yaratma', ALTIN, '#fffbe6'),
        ('5. Halka', 'Hesap Verme', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += f'<rect x="{x}" y="10" width="102" height="68" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.7"/>'
        ic += yazi(x + 51, 35, ust, 11.5, renk)
        ic += yazi(x + 51, 58, alt, 11, LAC)
        if i < 4:
            ic += f'<line x1="{x + 104}" y1="44" x2="{x + 117}" y2="44" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 113} 39 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 88, ic, 'Sorumluluk ve hesap verme sürecinin 5 halkalı akış şeması.', 17)


def kader_bahane_panosu():
    kartlar = [
        ('Arda', 'Sınav için planlı çalıştım; eksik konularımı', 'tamamlayıp sonucun sorumluluğunu üstlendim.', YES, YES_A),
        ('Mert', 'Arkadaşımın defterini izinsiz alıp kaybettim;', 'kaderim böyleymiş, benim suçum yok.', KIR, '#fdeaea'),
        ('Zeynep', 'İyi ile kötüyü ayırt edebildiğim için yaptığım', 'her tercihin hesabını vereceğimi biliyorum.', MAVI, MAVI_A),
        ('Elif', 'Ödevimi zamanında yapmadım ama talihim kötü', 'olduğu için düşük puan aldım.', TUR, TUR_A),
    ]
    ic = ''
    for i, (isim, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 60
        ic += f'<rect x="{x}" y="{y}" width="286" height="52" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 19, isim + ':', 11.5, renk, 'start')
        ic += yazi(x + 14, y + 34, s1, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 14, y + 47, s2, 10.6, LAC, 'start', ince=True)
    return svg(600, 128, ic, 'Dört öğrencinin (Arda, Mert, Zeynep, Elif) davranış ve kader konusundaki tutum kartları.', 18)


def gorev_ihmal_karti():
    ic = f'<rect x="6" y="6" width="290" height="98" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(151, 24, 'Vaka: Nöbetçi Öğrencinin Görevi', 11.5, TUR)
    ic += yazi(20, 44, 'Görev: Sınıftaki çiçekleri sulamak ve', 10.8, LAC, 'start', ince=True)
    ic += yazi(28, 59, 'pencereleri ders sonunda kapatmak.', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 77, 'Durum: Görev yapılmadı, çiçekler soldu.', 10.8, KIR, 'start')
    ic += yazi(20, 93, 'Savunma: “Ben çiçeklere zarar vermedim ki!”', 10.6, LAC, 'start', ince=True)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Sorumluluk ve Nahl Suresi 93. Ayet', 11.5, MAVI)
    ic += yazi(451, 46, '“… Yapmakta olduklarınızdan dolayı', 10.8, LAC, ince=True)
    ic += yazi(451, 61, 'kesinlikle sorgulanacaksınız.”', 10.8, LAC, ince=True)
    ic += f'<rect x="322" y="70" width="258" height="24" rx="6" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += yazi(451, 86, 'Yapılanlar ve yapılması gereken görevler', 10.8, MAVI)
    return svg(600, 110, ic, 'Nöbetçi öğrenci vakası ve Nahl suresi 93. ayet: yapılan işler ve yapılması gerekirken ihmal edilen görevler.', 18)


def iki_yol_sema():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Beled Suresi 10. Ayet: “Ve ona iki yolu göstermedik mi?”', 11.5, KAHVE)
    ic += f'<rect x="20" y="34" width="264" height="66" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(152, 52, '1. Yol: Şükreden ve Doğru Olmak', 11.2, YESIL_K)
    ic += yazi(152, 70, 'Hak yolu seçmek → Mükâfat', 10.8, LAC, ince=True)
    ic += yazi(152, 88, '(İnsan suresi 3: “… artık o isterse…”)', 10.5, YESIL_K, ince=True)

    ic += f'<rect x="316" y="34" width="264" height="66" rx="8" fill="{TUR_A}" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(448, 52, '2. Yol: Nankör ve Yanlış Olmak', 11.2, KIR)
    ic += yazi(448, 70, 'Batıl yolu seçmek → Ceza ve Sorumluluk', 10.8, LAC, ince=True)
    ic += yazi(448, 88, '(Seçmek insana, yaratmak Allah’a aittir)', 10.5, KIR, ince=True)
    return svg(600, 116, ic, 'Beled suresi 10 ve İnsan suresi 3 ayetlerine göre insana gösterilen iki yol şeması.', 18)


def akil_irade_kalkan():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Sorumluluğun İki Temel Şartı', 11.5, MAVI)
    ic += yazi(22, 46, '1. Akıl: Düşünme, öğrenme ve iyiyi', 10.8, LAC, 'start', ince=True)
    ic += yazi(34, 61, 'kötüden ayırt etme yeteneği', 10.8, MAVI, 'start')
    ic += yazi(22, 79, '2. Cüzi İrade: Gösterilen yollardan', 10.8, LAC, 'start', ince=True)
    ic += yazi(34, 94, 'birini özgürce tercih etme gücü', 10.8, MAVI, 'start')

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Sorumluluğun Sınırı (Bakara 286)', 11.5, YESIL_K)
    ic += yazi(324, 46, 'Sınır: İnsanın gücü ve tercih alanı', 10.8, YESIL_K, 'start')
    ic += yazi(324, 66, 'Gücü dahilinde: Seçtiği her davranış', 10.8, LAC, 'start', ince=True)
    ic += yazi(324, 86, 'İrade dışı: Doğum yeri, fiziki özellikler', 10.8, LAC, 'start', ince=True)
    return svg(600, 110, ic, 'Sorumluluğun temel şartları (akıl ve cüzi irade) ile sorumluluğun sınırı (güç ve tercih alanı).', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ilim_irade_sema()
    s[4]['gorsel'] = irade_sinir_kartlari()
    s[5]['gorsel'] = ayet_mesaj_kartlari()
    s[6]['gorsel'] = bilgi_tercih_akisi()
    s[7]['gorsel'] = sorumluluk_zinciri()
    s[8]['gorsel'] = kader_bahane_panosu()
    s[9]['gorsel'] = gorev_ihmal_karti()
    s[10]['gorsel'] = iki_yol_sema()
    s[12]['gorsel'] = akil_irade_kalkan()
