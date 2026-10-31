"""5. sınıf DKAB 3. hafta (Allah’ın Varlığı ve Birliği: gökteki ahenk, mevsimler, akıl ve sorumluluk, yaşam koşulları, tevhit) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = ' style="max-height:16mm"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10.5, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="1.8"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def gokteki_uyum_sema():
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    # Sol üst: Dünya'nın hareketleri -> K
    ic += f'<rect x="18" y="16" width="210" height="42" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<circle cx="42" cy="37" r="12" fill="{MAVI}"/><path d="M35 37 a7 7 0 1 0 14 0" fill="none" stroke="#fff" stroke-width="1.5"/>'
    ic += yazi(132, 34, 'Dünya’nın', 11.5, MAVI)
    ic += yazi(132, 49, 'Hareketleri', 11.5, MAVI)
    ic += f'<line x1="234" y1="37" x2="270" y2="37" stroke="{MAVI}" stroke-width="2"/><path d="M265 32 l6 5 l-6 5" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<rect x="278" y="16" width="302" height="42" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.6" stroke-dasharray="5 3"/>'
    ic += rozet(302, 37, 'K', MAVI)
    ic += yazi(438, 41, 'Sonuç: ?', 12, MAVI)

    # Sol alt: Dünya'nın Güneş'e uzaklığı -> L
    ic += f'<rect x="18" y="66" width="210" height="42" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += f'<circle cx="38" cy="87" r="10" fill="{TUR}"/><circle cx="56" cy="87" r="5" fill="{MAVI}"/>'
    ic += yazi(136, 84, 'Dünya’nın Güneş’e', 11.5, TUR)
    ic += yazi(136, 99, 'Uygun Uzaklığı', 11.5, TUR)
    ic += f'<line x1="234" y1="87" x2="270" y2="87" stroke="{TUR}" stroke-width="2"/><path d="M265 82 l6 5 l-6 5" fill="none" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<rect x="278" y="66" width="302" height="42" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.6" stroke-dasharray="5 3"/>'
    ic += rozet(302, 87, 'L', TUR)
    ic += yazi(438, 91, 'Sonuç: ?', 12, TUR)
    return svg(600, 126, ic, 'Gökteki ahenk neden-sonuç şeması: Dünya’nın hareketleri K sonucuna, Dünya’nın Güneş’e uygun uzaklığı L sonucuna bağlanır.', 24)


def mevsim_zinciri():
    ic = ''
    veriler = [
        ('1. Kış Mevsimi', 'Kar toprağı korur;', 'yer altı suları çoğalır.', MAVI, MAVI_A),
        ('2. Bahar Mevsimi', '?', '(Bitkiler ve su ihtiyacı)', YES, YES_A),
        ('3. Yaz Mevsimi', 'Sıcaklık artar; ekinler', 've bitkiler olgunlaşır.', TUR, TUR_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(veriler):
        x = 8 + i * 200
        ic += f'<rect x="{x}" y="8" width="184" height="96" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="8" width="184" height="26" rx="10" fill="{renk}"/><rect x="{x}" y="24" width="184" height="10" fill="{renk}"/>'
        ic += yazi(x + 92, 26, bas, 11.5, '#fff')
        ic += yazi(x + 92, 58, s1, 12 if s1 == '?' else 11, renk if s1 == '?' else LAC)
        ic += yazi(x + 92, 78, s2, 10.8, LAC, ince=True)
        if i < 2:
            ic += f'<line x1="{x + 186}" y1="56" x2="{x + 198}" y2="56" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 194} 51 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 112, ic, 'Mevsimler arası bağlantı şeması: 1. Kış (kar ve yer altı suları), 2. Bahar (soru işareti), 3. Yaz (sıcaklık artışı ve olgunlaşma).', 23)


def canli_ortam_kartlari():
    kartlar = [
        ('1. Kart: Tohum', 'Toprağa düşen çekirdek', 'Meyve ağacına dönüşüm', YES, YES_A),
        ('2. Kart: Bal Arısı', 'Çiçek özleri ve petek', 'Bal yapma becerisi', TUR, TUR_A),
        ('3. Kart: Fidan', 'Toprak, su ve güneş', 'Büyüyüp ağaca dönüşme', MAVI, MAVI_A),
        ('4. Kart: Anne Hayvan', 'Kuş yuvası ve yavrular', 'Yavrusunu koruma bilgisi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 35, s1 + ' → ' + s2, 10.8, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört varlık ve yaşam ortamı kartı: 1. Tohum, 2. Bal arısı, 3. Fidan, 4. Anne hayvan.', 23)


def insan_ustunluk_karti():
    ic = f'<rect x="6" y="6" width="588" height="102" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'İsra suresi 70. ayet: “… ve onları yarattıklarımızın çoğundan üstün kıldık.”', 11.5, KAHVE)
    ic += f'<rect x="24" y="36" width="246" height="58" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += rozet(46, 65, 'K', MAVI)
    ic += yazi(158, 58, 'İnsanı Diğer Canlılardan', 11, MAVI)
    ic += yazi(158, 76, 'Ayıran Özellik: ?', 11.5, LAC)
    ic += f'<line x1="278" y1="65" x2="322" y2="65" stroke="{LAC}" stroke-width="2"/><path d="M317 60 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="330" y="36" width="246" height="58" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.6"/>'
    ic += rozet(352, 65, 'L', YES)
    ic += yazi(464, 58, 'Yeryüzündeki Davranışlarda', 11, YESIL_K)
    ic += yazi(464, 76, 'Beklenen Tutum: ?', 11.5, LAC)
    return svg(600, 114, ic, 'İsra suresi 70. ayet şeması: K insanı diğer canlılardan ayıran özellik, L yeryüzündeki davranışlarda beklenen tutum.', 23)


def fidan_yasam_sema():
    adimlar = [
        ('Kış: Kar Örtüsü', '#d8e8ff', MAVI),
        ('Yer Altı Suları', '#e0f4f8', '#0e8fa8'),
        ('Bahar: Filizlenme', YES_A, YES),
        ('Yaz: Olgun Başak', TUR_A, TUR),
    ]
    ic = ''
    for i, (etiket, arka, renk) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="82" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        cx = x + 68
        if i == 0:
            ic += f'<path d="M{cx - 36} 54 Q{cx} 42 {cx + 36} 54" fill="none" stroke="{MAVI}" stroke-width="3"/>'
            ic += f'<circle cx="{cx - 18}" cy="32" r="3" fill="{MAVI}"/><circle cx="{cx}" cy="26" r="3" fill="{MAVI}"/><circle cx="{cx + 18}" cy="34" r="3" fill="{MAVI}"/>'
        elif i == 1:
            ic += f'<path d="M{cx - 34} 34 H{cx + 34}" stroke="{KAHVE}" stroke-width="2.5"/>'
            ic += f'<path d="M{cx - 28} 48 Q{cx - 14} 42 {cx} 48 T{cx + 28} 48" fill="none" stroke="{MAVI}" stroke-width="2.5"/>'
        elif i == 2:
            ic += f'<line x1="{cx}" y1="56" x2="{cx}" y2="28" stroke="{YES}" stroke-width="2.8"/>'
            ic += f'<ellipse cx="{cx - 9}" cy="38" rx="8" ry="4" fill="{YES}"/><ellipse cx="{cx + 9}" cy="34" rx="8" ry="4" fill="{YES}"/>'
        else:
            ic += f'<circle cx="{cx - 22}" cy="26" r="9" fill="{TUR}"/>'
            ic += f'<line x1="{cx + 8}" y1="56" x2="{cx + 8}" y2="24" stroke="{ALTIN}" stroke-width="3"/>'
            ic += f'<ellipse cx="{cx + 8}" cy="28" rx="6" ry="10" fill="{ALTIN}"/>'
        ic += yazi(cx, 76, etiket, 11, LAC)
    return svg(600, 98, ic, 'Kıştan yaza ekinin yetişme basamakları: kar örtüsü, yer altı suları, baharda filizlenme, yazın olgun başak.', 22)


def tevhit_dort_ilke():
    ic = f'<rect x="228" y="42" width="144" height="36" rx="18" fill="{YESIL_K}"/>'
    ic += yazi(300, 65, 'TEVHİT İNANCI', 12, '#fff')
    kutular = [
        (10, 6, '1. Bir ve ibadete layık', 'tek ilahtır.', MAVI, MAVI_A),
        (370, 6, '2. Eşi, benzeri ve', 'ortağı yoktur.', MAVI, MAVI_A),
        (10, 78, '3. Her şeyi yoktan yaratan,', 'varlıkların sahibidir.', MAVI, MAVI_A),
        (370, 78, '4. ?', '(Varlıklarla kıyas ve ihtiyaç)', TUR, TUR_A),
    ]
    ic += f'<line x1="220" y1="42" x2="238" y2="48" stroke="{YESIL_K}" stroke-width="1.8"/>'
    ic += f'<line x1="380" y1="42" x2="362" y2="48" stroke="{YESIL_K}" stroke-width="1.8"/>'
    ic += f'<line x1="220" y1="78" x2="238" y2="72" stroke="{YESIL_K}" stroke-width="1.8"/>'
    ic += f'<line x1="380" y1="78" x2="362" y2="72" stroke="{YESIL_K}" stroke-width="1.8"/>'
    for x, y, s1, s2, renk, arka in kutular:
        ic += f'<rect x="{x}" y="{y}" width="220" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 110, y + 16, s1, 10.8, renk if '?' in s1 else LAC)
        ic += yazi(x + 110, y + 31, s2, 10.5, LAC, ince=True)
    return svg(600, 122, ic, 'Tevhit inancının dört ilkesi şeması: 1, 2 ve 3. ilkeler yazılı, 4. kutu soru işaretli.', 23)


def nimet_hizmet_panosu():
    satirlar = [
        ('Güneş ve Ay', 'Gündüzü aydınlatır, geceleri ışık verir.', TUR, TUR_A),
        ('Yağmur ve Pınarlar', 'Bahçeleri sular, içimizi serinletir.', MAVI, MAVI_A),
        ('Dağlar ve Ormanlar', 'Yeryüzünü sağlamlaştırır, havayı temizler.', YES, YES_A),
        ('İnek, Arı ve Tavuk', 'İnsanlara süt, bal ve yumurta verir.', MOR, MOR_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    for i, (bas, acik, renk, arka) in enumerate(satirlar):
        x = 16 + (i % 2) * 288
        y = 14 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="276" height="42" rx="7" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 12, y + 17, bas, 11.2, renk, 'start')
        ic += yazi(x + 12, y + 34, acik, 10.5, LAC, 'start', ince=True)
    return svg(600, 126, ic, 'Evrendeki varlıkların (Güneş, Ay, yağmur, pınarlar, dağlar, ormanlar, hayvanlar) insana sağladığı faydalar panosu.', 24)


def iki_dusunce_karti():
    ic = f'<rect x="8" y="8" width="282" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Enbiya suresi 22. ayet', 11.5, MAVI)
    ic += yazi(149, 48, '“… Allah’tan başka tanrılar', 11, LAC, ince=True)
    ic += yazi(149, 66, 'bulunsaydı kesinlikle yerin', 11, LAC, ince=True)
    ic += yazi(149, 84, 'göğün düzeni bozulurdu. …”', 11, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Fatır suresi 3. ayet', 11.5, YESIL_K)
    ic += yazi(451, 48, '“Allah’tan başka gökten ve', 11, LAC, ince=True)
    ic += yazi(451, 66, 'yerden size rızık veren', 11, LAC, ince=True)
    ic += yazi(451, 84, 'yaratıcı var mı? …”', 11, LAC, ince=True)
    return svg(600, 112, ic, 'Enbiya suresi 22. ayet ve Fatır suresi 3. ayet kartları.', 22)


def tevhit_hayat_karti():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'İslam’ın Özü: Tevhit İnancının Hayatımıza Yansımaları', 11.5, KAHVE)
    alanlar = [
        ('1. Allah’a Bağlılık', 'Yalnız O’na güvenmek', MAVI, MAVI_A),
        ('2. İbadet Anlayışı', 'Yalnız O’na kulluk etmek', YES, YES_A),
        ('3. Yaşayış Biçimi', 'Emirlerine uygun yaşamak', TUR, TUR_A),
    ]
    for i, (bas, alt, renk, arka) in enumerate(alanlar):
        x = 18 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="58" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 54, bas, 11.2, renk)
        ic += yazi(x + 90, 76, alt, 10.8, LAC, ince=True)
    return svg(600, 110, ic, 'Tevhit inancının Müslümanın Allah’a bağlılığını, ibadet anlayışını ve yaşayış biçimini şekillendirmesi şeması.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gokteki_uyum_sema()
    s[4]['gorsel'] = mevsim_zinciri()
    s[5]['gorsel'] = canli_ortam_kartlari()
    s[6]['gorsel'] = insan_ustunluk_karti()
    s[7]['gorsel'] = fidan_yasam_sema()
    s[8]['gorsel'] = tevhit_dort_ilke()
    s[9]['gorsel'] = nimet_hizmet_panosu()
    s[10]['gorsel'] = iki_dusunce_karti()
    s[12]['gorsel'] = tevhit_hayat_karti()
