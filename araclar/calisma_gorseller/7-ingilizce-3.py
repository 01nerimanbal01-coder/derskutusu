"""7. sınıf İngilizce 3. hafta (Appearance and Personality: T/F/NI, sayısal karşılaştırma, because/so, with ile betimleme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–13 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def tuna_profil_svg():
    """Tuna tanıtım kartı ve I, II, III numaralı değerlendirme cümleleri."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(90, 19, 'STUDENT NOTE · Tuna', 11, '#fff')
    satirlar = [
        'Tuna is thirteen years old.',
        'He is short and slim with',
        '  straight brown hair.',
        'He studies every day and',
        '  always finishes his homework.',
    ]
    for i, m in enumerate(satirlar):
        ic += yazi(12, 39 + i * 13, m, 10.5, LAC, 'start', True)

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="22" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="10" fill="{TUR}"/>'
    ic += yazi(270, 19, 'STATEMENTS (T - F - NI)', 11, '#fff')
    ifadeler = [
        ('I.', 'Tuna is fourteen.'),
        ('II.', 'Tuna has blue eyes.'),
        ('III.', 'Tuna is hardworking.'),
    ]
    for i, (no, m) in enumerate(ifadeler):
        y = 33 + i * 20
        ic += kutu(192, y, 156, 17, '#fff', TUR, 4, 1.1)
        ic += yazi(200, y + 12.5, no, 10.5, TUR, 'start')
        ic += yazi(220, y + 12.5, m, 10.5, LAC, 'start', True)
    return svg(360, 100, ic, 'Tuna tanıtım kartı: 13 yaşında, kısa ve zayıf, düz kahverengi saçlı, her gün ders çalışır; ifadeler I Tuna is fourteen, II Tuna has blue eyes, III Tuna is hardworking.', 19)


def kilo_yas_grafigi_svg():
    """Üç kuzenin yaş ve kütle karşılaştırma kartları (Bora, Sude, Kaan)."""
    kisiler = [
        ('Bora', 'Age: 15', 'Weight: 62 kg', MAVI, MAVI_A, 92),
        ('Sude', 'Age: 13', 'Weight: 49 kg', YES, YES_A, 68),
        ('Kaan', 'Age: 11', 'Weight: 54 kg', TUR, TUR_A, 78),
    ]
    ic = kutu(4, 4, 352, 88, '#fff', GRI, 8, 1.2)
    ic += yazi(180, 19, 'COUSINS · Age & Weight Chart', 11.5, LAC)
    for i, (ad, yas, kilo, r, z, bar_w) in enumerate(kisiler):
        x = 12 + i * 114
        ic += kutu(x, 26, 108, 60, z, r, 7, 1.3)
        ic += yazi(x + 54, 41, ad, 11.5, r)
        ic += yazi(x + 54, 56, yas, 10.5, LAC, 'middle', True)
        ic += yazi(x + 54, 70, kilo, 10.5, LAC)
        ic += f'<rect x="{x + 8}" y="76" width="{bar_w}" height="5" rx="2.5" fill="{r}"/>'
    return svg(360, 96, ic, 'Yaş ve kütle çizelgesi: Bora 15 yaş 62 kg, Sude 13 yaş 49 kg, Kaan 11 yaş 54 kg.', 19)


def neden_sonuc_semasi_svg():
    """Neden ve sonuç kutuları şeması (Sinan dakiklik örneği)."""
    ic = '<defs><marker id="okIng3" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0b2257"/></marker></defs>'
    ic += kutu(4, 6, 160, 76, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="6" width="160" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="18" width="160" height="8" fill="{MAVI}"/>'
    ic += yazi(84, 20, 'REASON (Neden)', 10.5, '#fff')
    ic += yazi(84, 44, 'Sinan arrives at school', 10.5, LAC, 'middle', True)
    ic += yazi(84, 60, 'on time every morning.', 10.5, LAC, 'middle', True)

    ic += f'<line x1="168" y1="44" x2="192" y2="44" stroke="{LAC}" stroke-width="2" marker-end="url(#okIng3)"/>'

    ic += kutu(196, 6, 160, 76, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="196" y="6" width="160" height="20" rx="8" fill="{TUR}"/><rect x="196" y="18" width="160" height="8" fill="{TUR}"/>'
    ic += yazi(276, 20, 'RESULT (Sonuç)', 10.5, '#fff')
    ic += yazi(276, 44, 'Sinan is a very', 10.5, LAC, 'middle', True)
    ic += yazi(276, 60, 'punctual student.', 10.5, LAC, 'middle', True)
    return svg(360, 88, ic, 'Neden sonuç şeması: Neden Sinan arrives at school on time every morning, Sonuç Sinan is a very punctual student.', 18)


def davranis_kartlari_svg():
    """Dört davranış ipucu kartı (Emre, Melis, Ozan, Duru)."""
    kartlar = [
        ('1. Emre', 'studies every evening', MAVI, MAVI_A),
        ('2. Melis', 'speaks non-stop', TUR, TUR_A),
        ('3. Ozan', 'reads at the library', YES, YES_A),
        ('4. Duru', 'quiet in crowds', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ip, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 12, y + 15, bas, 11, r, 'start')
        ic += yazi(x + 12, y + 29, ip, 10.5, LAC, 'start', True)
    return svg(360, 88, ic, 'Dört davranış kartı: 1 Emre studies every evening, 2 Melis speaks non-stop, 3 Ozan reads at the library, 4 Duru quiet in crowds.', 18)


def zeynep_karti_svg():
    """Zeynep bilgi kartı (Age: 14, Weight: 46 kg, Height: 158 cm)."""
    ic = kutu(4, 4, 352, 74, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{CAM}"/><rect x="4" y="16" width="352" height="10" fill="{CAM}"/>'
    ic += yazi(180, 19, 'PROFILE CARD · Zeynep', 11.5, '#fff')
    kutular = [
        ('Age', '14 years old', 14, MAVI),
        ('Weight', '46 kg', 132, TUR),
        ('Height', '158 cm', 250, YES),
    ]
    for bas, deg, x, r in kutular:
        ic += kutu(x, 32, 96, 38, '#fff', r, 6, 1.2)
        ic += yazi(x + 48, 47, bas, 10.5, r)
        ic += yazi(x + 48, 63, deg, 11, LAC)
    return svg(360, 82, ic, 'Zeynep profil kartı: Age 14 years old, Weight 46 kg, Height 158 cm.', 18)


def dort_ogrenci_tablosu_svg():
    """Dört öğrencinin yaş, kütle ve arkadaş sayısı karşılaştırma tablosu."""
    ic = kutu(4, 4, 352, 98, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    basliklar = [('Name', 50), ('Age', 136), ('Weight', 220), ('Close Friends', 306)]
    for b, x in basliklar:
        ic += yazi(x, 19, b, 10.5, '#fff')
    satirlar = [
        ('Mert', '14', '56 kg', '8 friends'),
        ('Ece', '15', '50 kg', '14 friends'),
        ('Yaman', '12', '45 kg', '10 friends'),
        ('Nil', '13', '47 kg', '4 friends'),
    ]
    for i, (ad, yas, kilo, ark) in enumerate(satirlar):
        y = 28 + i * 18
        ic += f'<rect x="8" y="{y}" width="344" height="16" rx="3" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(50, y + 12, ad, 10.5, MAVI)
        ic += yazi(136, y + 12, yas, 10.5, LAC, 'middle', True)
        ic += yazi(220, y + 12, kilo, 10.5, LAC, 'middle', True)
        ic += yazi(306, y + 12, ark, 10.5, LAC, 'middle', True)
    return svg(360, 106, ic, 'Dört öğrenci tablosu: Mert 14 yaş 56 kg 8 arkadaş, Ece 15 yaş 50 kg 14 arkadaş, Yaman 12 yaş 45 kg 10 arkadaş, Nil 13 yaş 47 kg 4 arkadaş.', 20)


def cumle_fisleri_svg():
    """Dört numaralı cümle fişi (skin and bones, generous, honest, punctual)."""
    fisler = [
        ('I. fiş', 'The little cat was skin and bones.', MAVI, MAVI_A),
        ('II. fiş', 'My aunt is generous and helpful.', TUR, TUR_A),
        ('III. fiş', 'Kerem is honest; he never lies.', YES, YES_A),
        ('IV. fiş', 'Selin is punctual every morning.', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, m, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, no, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, m, 10, LAC, 'start', True)
    return svg(360, 88, ic, 'Dört cümle fişi: I. fiş skin and bones, II. fiş generous, III. fiş honest, IV. fiş punctual.', 18)


def leo_birlestirme_svg():
    """Leo hakkında iki ayrı dış görünüş cümlesini with ile birleştirme kartı."""
    ic = kutu(4, 4, 352, 76, KUM, GRI, 8, 1.3)
    ic += kutu(12, 10, 152, 30, MAVI_A, MAVI, 6, 1.2)
    ic += yazi(88, 29, 'Leo is tall and slim.', 10.5, LAC)
    ic += kutu(172, 10, 34, 30, TUR_A, TUR, 6, 1.2)
    ic += yazi(189, 29, 'with', 10.5, TUR)
    ic += kutu(214, 10, 134, 30, YES_A, YES, 6, 1.2)
    ic += yazi(281, 23, 'short straight brown', 10, LAC, 'middle', True)
    ic += yazi(281, 35, 'hair and hazel eyes', 10, LAC, 'middle', True)
    ic += kutu(12, 46, 336, 26, '#fff', MOR, 6, 1.2)
    ic += yazi(180, 63, 'Single sentence: Leo is ... with ...', 10.5, MOR)
    return svg(360, 84, ic, 'Leo iki cümle birleştirme şeması: Leo is tall and slim artı with artı short straight brown hair and hazel eyes.', 18)


def aylin_damla_karti_svg():
    """Aylin ve Damla karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 80, MAVI_A, MAVI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="172" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="8" fill="{MAVI}"/>'
    ic += yazi(90, 18, 'AYLİN', 11, '#fff')
    ic += yazi(16, 38, 'Age: 13 years old', 10.5, LAC, 'start', True)
    ic += yazi(16, 54, 'Weight: 50 kg', 10.5, LAC, 'start', True)
    ic += yazi(16, 70, '12 friends (outgoing)', 10.5, LAC, 'start', True)

    ic += kutu(184, 4, 172, 80, TUR_A, TUR, 8, 1.3)
    ic += f'<rect x="184" y="4" width="172" height="20" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="8" fill="{TUR}"/>'
    ic += yazi(270, 18, 'DAMLA', 11, '#fff')
    ic += yazi(196, 38, 'Age: 12 years old', 10.5, LAC, 'start', True)
    ic += yazi(196, 54, 'Weight: 44 kg', 10.5, LAC, 'start', True)
    ic += yazi(196, 70, '3 friends (shy)', 10.5, LAC, 'start', True)
    return svg(360, 88, ic, 'Aylin ve Damla kartları: Aylin 13 yaş 50 kg 12 arkadaş outgoing, Damla 12 yaş 44 kg 3 arkadaş shy.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tuna_profil_svg()
    s[2]['gorsel'] = kilo_yas_grafigi_svg()
    s[4]['gorsel'] = neden_sonuc_semasi_svg()
    s[5]['gorsel'] = davranis_kartlari_svg()
    s[6]['gorsel'] = zeynep_karti_svg()
    s[8]['gorsel'] = dort_ogrenci_tablosu_svg()
    s[9]['gorsel'] = cumle_fisleri_svg()
    s[10]['gorsel'] = leo_birlestirme_svg()
    s[12]['gorsel'] = aylin_damla_karti_svg()
