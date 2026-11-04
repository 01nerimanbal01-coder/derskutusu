"""8. sınıf İngilizce 6. hafta (Unit 2: Teen Life — Likes, Dislikes, Preferences & Opinions) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def muzik_tercih_kartlari():
    """Soru 1: Dört gencin müzik görüşleri kartı."""
    kartlar = [
        ('Leo · Rock & Opera', 'Rock: Terrific (+) · Opera: Unbearable (−)', MAVI, MAVI_A),
        ('Maya · Heavy Metal', 'Heavy metal: Too loud and boring (−)', KIR, KIR_A),
        ('Bora · Rap Music', 'Rap: Energetic and impressive (+)', YES, YES_A),
        ('Ada · Folk Music', 'Folk: Harmonic and traditional (+)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Dört gencin müzik türleri hakkındaki görüş kartları.', 15)


def sifat_ve_kalip_panosu():
    """Soru 2: Olumlu ve olumsuz sıfatlar panosu."""
    ic = kutu(4, 4, 172, 86, YES_A, YES, 8, 1.4)
    ic += yazi(90, 22, 'Positive (+) Expressions', YESIL_K)
    ic += yazi(90, 44, 'terrific · impressive · trendy', LAC, 'middle', True)
    ic += yazi(90, 64, 'fond of · keen on · crazy about', LAC, 'middle', True)
    ic += yazi(90, 81, '(Sevilen ve beğenilenler)', YESIL_K)

    ic += kutu(184, 4, 172, 86, KIR_A, KIR, 8, 1.4)
    ic += yazi(270, 22, 'Negative (−) Expressions', KIR)
    ic += yazi(270, 44, 'unbearable · ridiculous · boring', LAC, 'middle', True)
    ic += yazi(270, 64, 'can’t stand · hate · dislike', LAC, 'middle', True)
    ic += yazi(270, 81, '(Katlanılamayanlar)', KIR)
    return svg(360, 94, ic, 'Teen Life ünitesi olumlu ve olumsuz sıfatlar panosu.', 15)


def selin_hafta_sonu_tercihi():
    """Soru 4: Selin'in kamp (+) ve alışveriş (-) tercih kartı."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Selin’s Weekend Preference Card (prefer ... to ...)', KAHVE)
    ic += kutu(12, 28, 162, 54, YES_A, YES, 6, 1.3)
    ic += yazi(93, 46, '(+) Likes / Prefers', YESIL_K)
    ic += yazi(93, 68, 'Camping · Pitching a tent', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 54, KIR_A, KIR, 6, 1.3)
    ic += yazi(267, 46, '(−) Dislikes / Hates', KIR)
    ic += yazi(267, 68, 'Shopping at crowded malls', LAC, 'middle', True)
    return svg(360, 96, ic, 'Selin’in hafta sonu kamp ve alışveriş tercih kartı.', 15)


def arda_kitap_tercihi():
    """Soru 5: Arda'nın kitap kulübü tercih kartı."""
    ic = kutu(4, 4, 352, 84, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Book Club Member Card · Arda', MAVI)
    ic += kutu(14, 28, 158, 48, '#fff', YES, 6, 1.2)
    ic += yazi(93, 46, 'Detective Books (+)', YESIL_K)
    ic += yazi(93, 66, 'Exciting and impressive', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 48, '#fff', KIR, 6, 1.2)
    ic += yazi(267, 46, 'Gothic Books (−)', KIR)
    ic += yazi(267, 66, 'Dark and boring', LAC, 'middle', True)
    return svg(360, 92, ic, 'Arda’nın polisiye ve gotik kitap tercih kartı.', 15)


def kamp_malzemeleri_karti():
    """Soru 7: Kamp malzemeleri ve kullanım amaçları kartları."""
    esya = [
        ('1. Tent & Bag', 'For sleeping safely', MAVI, MAVI_A, 6),
        ('2. Torch', 'To see in the dark', TUR, TUR_A, 94),
        ('3. Compass', 'To find the direction', YES, YES_A, 182),
        ('4. Matches', 'To make a campfire', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in esya:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Dört kamp malzemesi ve kullanım amacı kartları.', 18)


def muzik_diyalog_akisi():
    """Soru 8: Tina ve Kerem müzik diyaloğu akış şeması."""
    adimlar = [
        ('1. Soru', 'What kind of music?', MAVI, MAVI_A, 6),
        ('2. Kerem', 'Keen on jazz (+)', YES, YES_A, 94),
        ('3. Tina', 'Prefers pop (+)', TUR, TUR_A, 182),
        ('4. Uzlaşma', 'Music festival!', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'İki arkadaşın müzik tercihleri konuşma akışı.', 18)


def mina_siklik_grafigi():
    """Soru 9: Mina'nın akşam etkinlikleri sıklık yüzdeleri panosu."""
    ic = kutu(4, 4, 352, 90, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Mina’s Evening Activities & Frequency Rates', LAC)
    barlar = [
        ('Doing homework', '100% (Always)', YES, YES_A, 10),
        ('Reading sci-fi', '80% (Usually)', MAVI, MAVI_A, 98),
        ('Chatting online', '40% (Sometimes)', TUR, TUR_A, 186),
        ('Playing games', '0% (Never)', KIR, KIR_A, 274),
    ]
    for bas, oran, r, z, x in barlar:
        ic += kutu(x, 28, 78, 56, z, r, 6, 1.3)
        ic += yazi(x + 39, 48, bas, r)
        ic += yazi(x + 39, 70, oran, LAC, 'middle', True)
    return svg(360, 98, ic, 'Mina’nın akşam etkinlikleri sıklık oranları tablosu.', 15)


def teen_opinion_cue_card():
    """Soru 12: Teen Life Opinion ipucu kartı."""
    ic = kutu(4, 4, 352, 84, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Teen Life Opinion Cue Card (Music Preferences)', MOR)
    ic += kutu(14, 28, 158, 48, '#fff', YES, 6, 1.2)
    ic += yazi(93, 46, 'Favorite Music (+)', YESIL_K)
    ic += yazi(93, 66, 'fond of · terrific / energetic', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 48, '#fff', KIR, 6, 1.2)
    ic += yazi(267, 46, 'Disliked Music (−)', KIR)
    ic += yazi(267, 66, 'can’t stand · unbearable', LAC, 'middle', True)
    return svg(360, 92, ic, 'Sevilen ve katlanılamayan müzik türleri yazma ipucu kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = muzik_tercih_kartlari()
    s[1]['gorsel'] = sifat_ve_kalip_panosu()
    s[3]['gorsel'] = selin_hafta_sonu_tercihi()
    s[4]['gorsel'] = arda_kitap_tercihi()
    s[6]['gorsel'] = kamp_malzemeleri_karti()
    s[7]['gorsel'] = muzik_diyalog_akisi()
    s[8]['gorsel'] = mina_siklik_grafigi()
    s[11]['gorsel'] = teen_opinion_cue_card()
