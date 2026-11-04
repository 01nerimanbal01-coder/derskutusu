"""7. sınıf İngilizce 6. hafta (Unit 2: Sports — Rutin Metinleri ve Karşılaştırma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, GRI, KUM = '#c9a227', '#8a5a2b', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kaan_blog_karti():
    """Soru 1: Genç okçu Kaan'ın blog yazısı kartı."""
    ic = kutu(4, 4, 352, 92, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 21, 'Kaan’s Sports Blog · My Archery Routine', MOR)
    ic += kutu(12, 28, 336, 60, '#fff', MOR, 6, 1.2)
    ic += yazi(180, 45, '«I always get up at 6:30 on weekdays. After school,', LAC, 'middle', True)
    ic += yazi(180, 63, 'I practice archery on Mondays, Wednesdays and Fridays.', LAC, 'middle', True)
    ic += yazi(180, 81, 'I go cycling at the weekend and I never eat fast food.»', MAVI)
    return svg(360, 100, ic, 'Okçu Kaan’ın haftalık antrenman ve beslenme blog yazısı.', 14)


def lara_rutin_notlari():
    """Soru 2: Yüzücü Lara'nın rutin bilgi aktarım fişleri."""
    kartlar = [
        ('Wake Up', 'Every day · 06:45', MAVI, MAVI_A),
        ('Swimming', 'Mon · Wed · Fri', YES, YES_A),
        ('Table Tennis', 'Tue · Thu (Twice)', TUR, TUR_A),
        ('Junk Food', '0% · In the evenings', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Yüzücü Lara’nın dört adet rutin bilgi fişi.', 14)


def uc_soru_cevap_karti():
    """Soru 4: How often, When, What time soru-cevap kartları."""
    kartlar = [
        ('1. ___ do you train?', 'Three times a week.', MAVI, MAVI_A, 6),
        ('2. ___ do you train?', 'On Mondays and Fridays.', YES, YES_A, 124),
        ('3. ___ do you get up?', 'At half past six.', TUR, TUR_A, 242),
    ]
    ic = ''
    for bas, cvp, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 26, bas, r)
        ic += yazi(x + 56, 54, 'Answer:', LAC, 'middle', True)
        ic += yazi(x + 56, 74, cvp, LAC)
    return svg(360, 94, ic, 'Üç rutin sorusu ve cevap eşleştirme kartları.', 14)


def podcast_duzeltme_notu():
    """Soru 5: Spor podcast'i dinleme ve düzeltme notu."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Sports Podcast Transcript · Guest: Mert (Tennis)', KAHVE)
    ic += kutu(12, 28, 336, 56, '#fff', TUR, 6, 1.2)
    ic += yazi(180, 47, 'Host: How often do you train at the tennis court, Mert?', MAVI)
    ic += yazi(180, 67, 'Mert: «I train twice — oh no, four times a week now.»', LAC, 'middle', True)
    ic += yazi(180, 81, 'Not: Düzeltmede son söylenen sıklık geçerlidir!', TUR)
    return svg(360, 96, ic, 'Tenisçi Mert’in podcast röportajında antrenman sıklığını düzeltmesi.', 14)


def ege_sude_karsilastirma():
    """Soru 7: Ege ve Sude'nin haftalık rutin karşılaştırma tablosu."""
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Routine Comparison: Ege vs. Sude', MAVI)
    ic += kutu(12, 28, 162, 60, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 44, 'Ege’s Routine', MAVI)
    ic += yazi(93, 62, 'Get up: 07:30 · Swim: Twice', LAC, 'middle', True)
    ic += yazi(93, 79, 'Train: 3 times · Chocolate: Never', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 60, '#fff', MOR, 6, 1.2)
    ic += yazi(267, 44, 'Sude’s Routine', MOR)
    ic += yazi(267, 62, 'Get up: 06:30 · Swim: Never', LAC, 'middle', True)
    ic += yazi(267, 79, 'Train: Every day · Chocolate: Sometimes', LAC, 'middle', True)
    return svg(360, 100, ic, 'Ege ve Sude’nin rutin karşılaştırma kartları.', 14)


def gunluk_siralama_akisi():
    """Soru 8: First, Then, After that, Finally günlük akış şeması."""
    adimlar = [
        ('1. First', '07:00 Breakfast', MAVI, MAVI_A, 6),
        ('2. Then', '08:00 School', YES, YES_A, 94),
        ('3. After that', '16:00 Training', TUR, TUR_A, 182),
        ('4. Finally', '22:00 Sleep', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Dört aşamalı sporcu günlük yazısı sıralama şeması.', 18)


def sozcuk_dizilisi_kartlari():
    """Soru 9: Sıklık zarfı ve sıklık ifadesi diziliş kartları."""
    kartlar = [
        ('1. Kart · Zarf Yeri', 'Subject + Adverb + Verb', MAVI, MAVI_A),
        ('2. Kart · İfade Yeri', 'Verb + Place + Frequency', YES, YES_A),
        ('3. Kart · Never Kuralı', 'He + never + eats...', MOR, MOR_A),
        ('4. Kart · Hatalı Sıra', 'Verb + Frequency + Place (X)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Sıklık zarfları ve ifadelerinin cümledeki yeri kartları.', 14)


def nehir_doruk_karti():
    """Soru 12: Nehir ve Doruk karşılaştırma kartı."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 8, 1.4)
    ic += yazi(180, 21, 'Athletes Profile Card: Nehir & Doruk', YES)
    ic += kutu(14, 28, 160, 54, '#fff', MAVI, 6, 1.2)
    ic += yazi(94, 46, 'Nehir (Volleyball)', MAVI)
    ic += yazi(94, 68, 'Train: 3 times a week · Junk food: Never', LAC, 'middle', True)
    ic += kutu(186, 28, 160, 54, '#fff', TUR, 6, 1.2)
    ic += yazi(266, 46, 'Doruk (Basketball)', TUR)
    ic += yazi(266, 68, 'Train: Every day · Junk food: Never', LAC, 'middle', True)
    return svg(360, 96, ic, 'Voleybolcu Nehir ve basketbolcu Doruk antrenman karşılaştırma kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kaan_blog_karti()
    s[1]['gorsel'] = lara_rutin_notlari()
    s[3]['gorsel'] = uc_soru_cevap_karti()
    s[4]['gorsel'] = podcast_duzeltme_notu()
    s[6]['gorsel'] = ege_sude_karsilastirma()
    s[7]['gorsel'] = gunluk_siralama_akisi()
    s[8]['gorsel'] = sozcuk_dizilisi_kartlari()
    s[11]['gorsel'] = nehir_doruk_karti()
