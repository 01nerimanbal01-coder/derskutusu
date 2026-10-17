"""5. sınıf DKAB 4. hafta (Allah’ın güzel isimleri, Rahman, Rahîm, besmele, merhamet) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=12, boy=14):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def kitaplik():
    kitap = [('Kur’an-ı', 'Kerim', YESIL_K, ALTIN), ('Dünya', 'Atlası', MAVI, '#fff'),
             ('Hadis', 'Kitabı', '#8a2d3b', ALTIN), ('Masal', 'Kitabı', TUR, '#fff')]
    ic = f'<rect x="4" y="160" width="592" height="12" rx="3" fill="#a0703c"/><rect x="10" y="172" width="580" height="5" fill="#d9c3a5"/>'
    for i, (s1, s2, renk, yrenk) in enumerate(kitap):
        x = 18 + i * 146
        ic += f'<rect x="{x}" y="14" width="122" height="146" rx="5" fill="{renk}"/><rect x="{x}" y="14" width="12" height="146" rx="4" fill="#000" opacity="0.18"/>'
        if i == 0:
            ic += f'<rect x="{x + 20}" y="22" width="94" height="130" rx="3" fill="none" stroke="{ALTIN}" stroke-width="2"/>'
            ic += f'<rect x="{x + 56}" y="44" width="22" height="22" fill="{ALTIN}"/><rect x="{x + 56}" y="44" width="22" height="22" fill="{ALTIN}" transform="rotate(45 {x + 67} 55)"/>'
        elif i == 1:
            cx = x + 67
            ic += f'<circle cx="{cx}" cy="56" r="22" fill="none" stroke="#fff" stroke-width="2"/><ellipse cx="{cx}" cy="56" rx="10" ry="22" fill="none" stroke="#fff" stroke-width="1.5"/>'
            ic += f'<line x1="{cx - 22}" y1="56" x2="{cx + 22}" y2="56" stroke="#fff" stroke-width="1.5"/><path d="M{cx - 19} 45 h38 M{cx - 19} 67 h38" stroke="#fff" stroke-width="1.2"/>'
        elif i == 2:
            ic += f'<rect x="{x + 20}" y="22" width="94" height="130" rx="3" fill="none" stroke="{ALTIN}" stroke-width="1.6"/>'
            ic += f'<circle cx="{x + 67}" cy="55" r="12" fill="none" stroke="{ALTIN}" stroke-width="2"/><circle cx="{x + 67}" cy="55" r="4" fill="{ALTIN}"/>'
        else:
            cx = x + 67
            ic += f'<path d="M{cx} 36 l5 11 l12 1 l-9 8 l3 12 l-11 -6 l-11 6 l3 -12 l-9 -8 l12 -1 z" fill="#fff4c2"/>'
            ic += f'<circle cx="{cx + 30}" cy="40" r="3" fill="#fff4c2"/><circle cx="{cx - 30}" cy="66" r="2.5" fill="#fff4c2"/>'
        ic += yazi(x + 67, 104, s1, 16, yrenk) + yazi(x + 67, 124, s2, 16, yrenk)
        ic += rozet(x + 14, 14, str(i + 1), LAC, 12, 14)
    return svg(600, 180, ic, 'Kitap rafı: 1. Kur’an-ı Kerim, 2. Dünya Atlası, 3. Hadis Kitabı, 4. Masal Kitabı.', 32)


def isim_kartlari():
    adlar = ['Âlim', 'Rahman', 'Kadir', 'Rahîm', 'Semi', 'Basir']
    ic = f'<rect x="4" y="4" width="592" height="46" rx="10" fill="{YESIL_K}"/>'
    ic += f'<rect x="10" y="10" width="580" height="34" rx="7" fill="none" stroke="{ALTIN}" stroke-width="1.4"/>'
    ic += yazi(300, 35, 'Bismillâhirrahmânirrahîm', 22, '#f4d27a')
    for i, ad in enumerate(adlar):
        x = 4 + i * 100
        ic += f'<rect x="{x}" y="62" width="92" height="70" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
        ic += rozet(x + 16, 78, str(i + 1), MAVI, 10, 13) + yazi(x + 46, 114, ad, 18, LAC)
    return svg(600, 136, ic, 'Besmele: Bismillâhirrahmânirrahîm. Altında numaralı isim kartları: 1. Âlim, 2. Rahman, 3. Kadir, 4. Rahîm, 5. Semi, 6. Basir.', 28)


def is_kartlari():
    ic = ''
    adlar = ['Kahvaltı sofrası', 'Ders çalışma', 'Fidan dikme']
    for i, ad in enumerate(adlar):
        x = 4 + i * 198
        cx = x + 93
        ic += f'<rect x="{x}" y="4" width="186" height="150" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.6"/>'
        if i == 0:
            ic += f'<rect x="{x + 16}" y="100" width="154" height="8" rx="3" fill="{TUR_A}" stroke="{TUR}" stroke-width="1"/>'
            ic += f'<ellipse cx="{cx - 8}" cy="90" rx="46" ry="12" fill="#fff" stroke="{GRI}" stroke-width="1.6"/>'
            ic += f'<path d="M{cx - 34} 76 a26 18 0 0 0 52 0 z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
            ic += ''.join(f'<path d="M{cx - 16 + k * 10} 64 q-5 -7 0 -14 q5 -7 0 -14" fill="none" stroke="{GRI}" stroke-width="1.6" stroke-linecap="round"/>' for k in range(3))
            ic += f'<rect x="{cx + 32}" y="70" width="34" height="18" rx="9" fill="#e3b06b" stroke="{KAHVE}" stroke-width="1.4"/><path d="M{cx + 40} 74 l4 10 M{cx + 50} 74 l4 10" stroke="{KAHVE}" stroke-width="1.2"/>'
        elif i == 1:
            ic += f'<path d="M{cx} 50 Q{cx - 30} 38 {cx - 64} 44 V100 Q{cx - 30} 94 {cx} 106 Z" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
            ic += f'<path d="M{cx} 50 Q{cx + 30} 38 {cx + 64} 44 V100 Q{cx + 30} 94 {cx} 106 Z" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
            ic += ''.join(f'<path d="M{cx - 54} {56 + k * 10} Q{cx - 30} {51 + k * 10} {cx - 8} {60 + k * 10}" fill="none" stroke="{MAVI_A}" stroke-width="2.4"/>' for k in range(4))
            ic += ''.join(f'<path d="M{cx + 8} {60 + k * 10} Q{cx + 30} {51 + k * 10} {cx + 54} {56 + k * 10}" fill="none" stroke="{MAVI_A}" stroke-width="2.4"/>' for k in range(4))
            ic += f'<g transform="rotate(-35 {cx + 40} 70)"><rect x="{cx + 10}" y="66" width="56" height="9" rx="2" fill="#f2c94c" stroke="{KAHVE}" stroke-width="1"/><path d="M{cx + 66} 66 l12 4.5 l-12 4.5 z" fill="#f5deb3" stroke="{KAHVE}" stroke-width="1"/><path d="M{cx + 74} 69 l4 1.5 l-4 1.5 z" fill="{LAC}"/><rect x="{cx + 4}" y="66" width="8" height="9" rx="2" fill="{KIR}"/></g>'
        else:
            sx = cx - 26
            ic += f'<ellipse cx="{sx}" cy="104" rx="38" ry="9" fill="#a0703c"/><path d="M{sx} 104 V62" stroke="{YES}" stroke-width="3"/>'
            ic += f'<path d="M{sx} 82 q-18 -2 -22 -16 q16 1 22 16 M{sx} 72 q18 -2 22 -16 q-16 1 -22 16 M{sx} 62 q-8 -10 0 -18 q8 8 0 18" fill="{YES}"/>'
            wx = cx + 26
            ic += f'<rect x="{wx}" y="68" width="40" height="32" rx="5" fill="{MAVI}"/><path d="M{wx + 40} 74 q14 0 14 12 q0 12 -14 12" fill="none" stroke="{MAVI}" stroke-width="4"/>'
            ic += f'<path d="M{wx + 2} 76 L{wx - 20} 58" stroke="{MAVI}" stroke-width="5" stroke-linecap="round"/><ellipse cx="{wx - 22}" cy="56" rx="5" ry="3" fill="{MAVI}" transform="rotate(-40 {wx - 22} 56)"/>'
            ic += ''.join(f'<path d="M{wx - 26 - k * 7} {64 + k * 8} q-3 5 0 7 q3 -2 0 -7" fill="#5aa9e6"/>' for k in range(3))
        ic += rozet(x + 18, 20, str(i + 1), LAC, 11, 13) + yazi(cx, 138, ad, 15, LAC)
    return svg(590, 158, ic, 'Üç iş kartı: 1. Kahvaltı sofrası, 2. Ders çalışma, 3. Fidan dikme.', 30)


def kuyu():
    ic = f'<polygon points="22,38 100,8 178,38" fill="#b4532a"/><rect x="40" y="36" width="10" height="58" fill="{KAHVE}"/><rect x="150" y="36" width="10" height="58" fill="{KAHVE}"/>'
    ic += f'<line x1="50" y1="50" x2="150" y2="50" stroke="{KAHVE}" stroke-width="6"/><line x1="100" y1="50" x2="100" y2="68" stroke="#6b5844" stroke-width="2"/>'
    ic += f'<path d="M88 68 h24 l-4 20 h-16 z" fill="{GRI}" stroke="#5f6b80" stroke-width="1.6"/><path d="M88 68 q12 -10 24 0" fill="none" stroke="#5f6b80" stroke-width="1.6"/>'
    ic += f'<rect x="26" y="94" width="148" height="58" rx="4" fill="#d8c7ab" stroke="#8a7458" stroke-width="2"/>'
    ic += ''.join(f'<line x1="26" y1="{94 + k * 14.5}" x2="174" y2="{94 + k * 14.5}" stroke="#8a7458" stroke-width="1.2"/>' for k in range(1, 4))
    ic += ''.join(f'<line x1="{26 + (k % 5) * 30 + (15 if (k // 5) % 2 else 0)}" y1="{94 + (k // 5) * 14.5}" x2="{26 + (k % 5) * 30 + (15 if (k // 5) % 2 else 0)}" y2="{108.5 + (k // 5) * 14.5}" stroke="#8a7458" stroke-width="1.2"/>' for k in range(20) if 26 < 26 + (k % 5) * 30 + (15 if (k // 5) % 2 else 0) < 174)
    ic += f'<path d="M196 112 H262" stroke="{LAC}" stroke-width="2.4"/><path d="M256 105 l10 7 l-10 7" fill="none" stroke="{LAC}" stroke-width="2.4"/>'
    ic += f'<path d="M286 140 H436 Q446 140 444 128 L436 118 Q404 108 374 106 L352 84 L302 84 Q288 84 286 100 Z" fill="{KAHVE}" stroke="#5c3a1a" stroke-width="2"/>'
    ic += f'<path d="M286 140 H436" stroke="#3b2410" stroke-width="5"/><ellipse cx="327" cy="86" rx="24" ry="5" fill="#5aa9e6" stroke="#2f7fc0" stroke-width="1.2"/>'
    ic += ''.join(f'<path d="M{306 + k * 20} {62 - (k % 2) * 8} q-4 7 0 10 q4 -3 0 -10" fill="#5aa9e6"/>' for k in range(3))
    ic += yazi(100, 172, 'Kuyu', 14, LAC) + yazi(365, 172, 'Ayakkabıyla taşınan su', 14, LAC)
    return svg(460, 180, ic, 'Hikâyedeki kuyu ve ayakkabıyla taşınan su.', 30)


def hadis_karti():
    ic = f'<rect x="4" y="4" width="592" height="100" rx="10" fill="#fbf7ee" stroke="#c9a86a" stroke-width="2"/>'
    ic += f'<rect x="4" y="4" width="10" height="100" rx="5" fill="#c9a86a"/>'
    ic += yazi(30, 32, 'Hz. Peygamber (sav) buyurdu:', 14, '#8a6d12', 'start')
    ic += yazi(30, 62, '“İşte Allah’ın kullarına merhameti bu annenin', 17, LAC, 'start', ' font-style="italic"', ince=True)
    ic += yazi(30, 88, 'yavrusuna duyduğundan çok daha fazladır.”', 17, LAC, 'start', ' font-style="italic"', ince=True)
    return svg(600, 108, ic, 'Hz. Peygamber (sav) buyurdu: İşte Allah’ın kullarına merhameti bu annenin yavrusuna duyduğundan çok daha fazladır.', 22)


def davranis_kartlari():
    kart = [('I', 'Kışın kuşlar için', 'pencereye yem koymak'), ('II', 'Arkadaşının hatasını', 'sınıfa duyurmak'),
            ('III', 'Yaşlı komşunun pazar', 'çantasını taşımak'), ('IV', 'Beslenmesini', 'arkadaşıyla paylaşmak')]
    ic = ''
    for i, (no, s1, s2) in enumerate(kart):
        x, y = 4 + (i % 2) * 300, 4 + (i // 2) * 92
        cx, cy = x + 50, y + 46
        ic += f'<rect x="{x}" y="{y}" width="292" height="84" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
        ic += f'<rect x="{x + 12}" y="{y + 10}" width="76" height="64" rx="8" fill="#fff"/>'
        if i == 0:
            ic += f'<polygon points="{cx - 22},{cy - 8} {cx - 8},{cy - 22} {cx + 6},{cy - 8}" fill="{KIR}"/><rect x="{cx - 19}" y="{cy - 8}" width="22" height="22" fill="#e3b06b" stroke="{KAHVE}" stroke-width="1.2"/>'
            ic += f'<circle cx="{cx - 8}" cy="{cy + 2}" r="5" fill="{KAHVE}"/><rect x="{cx - 24}" y="{cy + 14}" width="32" height="4" rx="2" fill="{KAHVE}"/>'
            ic += ''.join(f'<circle cx="{cx - 18 + k * 6}" cy="{cy + 12}" r="1.6" fill="#b8860b"/>' for k in range(4))
            ic += f'<ellipse cx="{cx + 20}" cy="{cy + 6}" rx="11" ry="7" fill="{MAVI}"/><circle cx="{cx + 28}" cy="{cy - 3}" r="5.5" fill="{MAVI}"/>'
            ic += f'<path d="M{cx + 33} {cy - 4} l6 2 l-6 2 z" fill="{TUR}"/><circle cx="{cx + 29}" cy="{cy - 4}" r="1.2" fill="#fff"/><path d="M{cx + 10} {cy + 4} l-8 -5 l2 9 z" fill="{MAVI}"/>'
            ic += f'<path d="M{cx + 18} {cy + 12} v6 M{cx + 23} {cy + 12} v6" stroke="{TUR}" stroke-width="1.4"/>'
        elif i == 1:
            ic += f'<path d="M{cx - 26} {cy - 20} h52 a8 8 0 0 1 8 8 v22 a8 8 0 0 1 -8 8 h-30 l-12 10 v-10 h-10 a8 8 0 0 1 -8 -8 v-22 a8 8 0 0 1 8 -8 z" fill="#fde8e8" stroke="{KIR}" stroke-width="2"/>'
            ic += yazi(cx, cy + 8, '!', 24, KIR)
        elif i == 2:
            ic += f'<path d="M{cx - 6} {cy - 12} q-4 -14 4 -18 M{cx + 2} {cy - 12} q2 -16 10 -18" fill="none" stroke="{YES}" stroke-width="3" stroke-linecap="round"/>'
            ic += f'<path d="M{cx - 22} {cy - 12} h44 l-5 34 h-34 z" fill="{TUR_A}" stroke="{TUR}" stroke-width="2"/><path d="M{cx - 12} {cy - 12} q12 -12 24 0" fill="none" stroke="{TUR}" stroke-width="2"/>'
            ic += f'<circle cx="{cx + 14}" cy="{cy - 15}" r="6" fill="{KIR}"/>'
        else:
            ic += f'<rect x="{cx - 26}" y="{cy - 10}" width="52" height="32" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="2"/><line x1="{cx}" y1="{cy - 10}" x2="{cx}" y2="{cy + 22}" stroke="{YES}" stroke-width="1.6"/>'
            ic += f'<path d="M{cx - 22} {cy + 16} l10 -20 l10 20 z" fill="#f2d39b" stroke="{KAHVE}" stroke-width="1.2"/><circle cx="{cx + 13}" cy="{cy + 6}" r="8" fill="{KIR}"/><path d="M{cx + 13} {cy - 2} v-4" stroke="{KAHVE}" stroke-width="1.6"/>'
            ic += f'<rect x="{cx - 28}" y="{cy - 16}" width="56" height="6" rx="3" fill="{YES}"/>'
        ic += rozet(x + 14, y + 12, no, MOR, 12, 12 if len(no) < 3 else 10)
        ic += yazi(x + 102, y + 38, s1, 15, LAC, 'start', ince=True) + yazi(x + 102, y + 60, s2, 15, LAC, 'start', ince=True)
    return svg(600, 184, ic, 'Davranış kartları: I. Kışın kuşlar için pencereye yem koymak, II. Arkadaşının hatasını sınıfa duyurmak, III. Yaşlı komşunun pazar çantasını taşımak, IV. Beslenmesini arkadaşıyla paylaşmak.', 38)


def not_karti():
    ic = f'<rect x="4" y="8" width="512" height="100" rx="8" fill="#fffbe6" stroke="#d9b84a" stroke-width="1.8"/>'
    ic += f'<rect x="200" y="2" width="120" height="16" rx="3" fill="#f3e3a6" opacity="0.9"/>'
    ic += yazi(24, 40, 'Mert’in notu', 14, '#8a6d12', 'start')
    ic += yazi(24, 68, 'Rahman ve Rahîm aynı isimdir; ikisi de yalnızca', 16, LAC, 'start', ince=True)
    ic += yazi(24, 92, 'iyilik yapanlara gösterilen merhameti anlatır.', 16, LAC, 'start', ince=True)
    return svg(520, 112, ic, 'Mert’in notu: Rahman ve Rahîm aynı isimdir; ikisi de yalnızca iyilik yapanlara gösterilen merhameti anlatır.', 24)


def soru_cevap():
    ic = f'<path d="M14 4 H494 a10 10 0 0 1 10 10 V52 a10 10 0 0 1 -10 10 H60 l-18 12 v-12 H14 a10 10 0 0 1 -10 -10 V14 a10 10 0 0 1 10 -10 z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(20, 26, 'Sahabilerin sorusu:', 13, MAVI, 'start') + yazi(20, 50, 'Hayvanlara iyilik edince de sevap kazanır mıyız?', 15, LAC, 'start', ince=True)
    ic += f'<path d="M106 84 H586 a10 10 0 0 1 10 10 V132 a10 10 0 0 1 -10 10 H572 v12 l-18 -12 H106 a10 10 0 0 1 -10 -10 V94 a10 10 0 0 1 10 -10 z" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(112, 106, 'Hz. Peygamber’in (sav) cevabı:', 13, '#0d7a3e', 'start') + yazi(112, 130, 'Canlı olan her varlığa yapılan iyiliğin karşılığı vardır.', 15, LAC, 'start', ince=True)
    return svg(600, 158, ic, 'Konuşma. Sahabilerin sorusu: Hayvanlara iyilik edince de sevap kazanır mıyız? Hz. Peygamber’in (sav) cevabı: Canlı olan her varlığa yapılan iyiliğin karşılığı vardır.', 30)


def sema():
    kutu = [('Kaynak', MAVI, MAVI_A), ('Öğrenme', YES, YES_A), ('Kullanma', TUR, TUR_A)]
    ic = ''
    for i, (b, renk, acik) in enumerate(kutu):
        x = 4 + i * 208
        ic += f'<rect x="{x}" y="4" width="176" height="92" rx="10" fill="{acik}" stroke="{renk}" stroke-width="2"/>'
        ic += f'<rect x="{x}" y="4" width="176" height="28" rx="10" fill="{renk}"/><rect x="{x}" y="22" width="176" height="10" fill="{renk}"/>'
        ic += yazi(x + 88, 23, b, 14, '#fff')
        if i == 0:
            ic += yazi(x + 88, 58, 'Kur’an-ı Kerim', 15, LAC) + yazi(x + 88, 80, 've hadisler', 15, LAC)
        else:
            ic += f'<rect x="{x + 38}" y="46" width="100" height="36" rx="6" fill="#fff" stroke="{renk}" stroke-width="1.4" stroke-dasharray="5 4"/>' + yazi(x + 88, 70, '?', 18, renk)
        if i < 2:
            ic += f'<path d="M{x + 182} 58 h20 m-6 -5 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 100, ic, 'Şema: Kaynak (Kur’an-ı Kerim ve hadisler) → Öğrenme (?) → Kullanma (?).', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kitaplik()
    s[4]['gorsel'] = isim_kartlari()
    s[6]['gorsel'] = is_kartlari()
    s[7]['gorsel'] = kuyu()
    s[8]['gorsel'] = hadis_karti()
    s[9]['gorsel'] = davranis_kartlari()
    s[10]['gorsel'] = not_karti()
    s[11]['gorsel'] = soru_cevap()
    s[12]['gorsel'] = sema()
