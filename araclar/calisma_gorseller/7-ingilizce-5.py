"""7. sınıf İngilizce 5. hafta (Unit 2: Sports — Günlük Rutinler, Geniş Zaman ve Do/Does Soruları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def defne_sporcu_karti():
    """Soru 1: Yüzücü Defne'nin günlük rutin kimlik kartı."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Swimmer Profile Card · Defne (She)', MOR)
    ic += kutu(14, 28, 158, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Morning Routine (06:00)', MAVI)
    ic += yazi(93, 66, 'get up early every day', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Afternoon Routine (16:00)', YESIL_K)
    ic += yazi(267, 66, 'train at the indoor pool', LAC, 'middle', True)
    return svg(360, 94, ic, 'Yüzücü Defne’nin sabah ve öğleden sonra rutinlerini gösteren kart.', 16)


def fiil_ekleri_kurallari():
    """Soru 2: He/She/It -s/-es/-ies ve has yazım kuralları."""
    kurallar = [
        ('1. -o / -ch / -sh / -x', 'go → goes · watch → watches', MAVI, MAVI_A),
        ('2. Consonant + y', 'study → studies · try → tries', MOR, MOR_A),
        ('3. Irregular Verb', 'have → has (has breakfast)', TUR, TUR_A),
        ('4. Time Prepositions', 'in morning · on Saturday · at 7', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kurallar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Geniş zamanda üçüncü tekil kişi fiil ekleri ve zaman edatları özeti.', 16)


def olumsuz_cumle_panosu():
    """Soru 4: 4 öğrencinin olumsuz geniş zaman cümleleri."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Negative Sentences Checkboard (don’t / doesn’t + V1)', KAHVE)
    ogrenciler = [
        ('1. Arda', '«...doesn’t eats...»', KIR, KIR_A, 10, 28),
        ('2. Beren', '«...doesn’t never...»', KIR, KIR_A, 184, 28),
        ('3. Cenk', '«...doesn’t go...»', YES, YES_A, 10, 58),
        ('4. Duru', '«...don’t trains...»', KIR, KIR_A, 184, 58),
    ]
    for ad, cumle, r, z, x, y in ogrenciler:
        ic += kutu(x, y, 166, 26, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 17, f'{ad}: {cumle}', LAC, 'middle', True)
    return svg(360, 96, ic, 'Dört öğrencinin geniş zaman olumsuz cümle örnekleri panosu.', 16)


def in_on_at_zaman_kartlari():
    """Soru 5: in / on / at zaman edatları kartları."""
    kartlar = [
        ('IN (Parts of Day)', '___ the afternoon', MAVI, MAVI_A, 6),
        ('ON (Days)', '___ Fridays', TUR, TUR_A, 126),
        ('AT (Clock Times)', '___ ten o’clock', YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, '#f8fafc', GRI, 8, 1.3)
    for bas, alt, r, z, x in kartlar:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.4)
        ic += yazi(x + 54, 34, bas, r)
        ic += yazi(x + 54, 60, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Günün bölümleri, günler ve saatlerle kullanılan edat kartları.', 16)


def sinan_etkinlik_tablosu():
    """Soru 7: Sinan'ın Find Someone Who yanıt tablosu."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Interview Notes · Sinan’s Sports Habits', MAVI)
    satirlar = [
        ('wake up early: Always (✓)', 'warm up: Always (✓)', YES, '#fff', 12),
        ('energy drinks: Never (✗)', 'skateboarding: Never (✗)', KIR, '#fff', 186),
    ]
    for s1, s2, r, z, x in satirlar:
        ic += kutu(x, 28, 162, 54, z, r, 6, 1.3)
        ic += yazi(x + 81, 46, s1, LAC, 'middle', True)
        ic += yazi(x + 81, 68, s2, r)
    return svg(360, 96, ic, 'Sinan’ın spor alışkanlıkları anket sonuçları kartı.', 16)


def tuna_cumartesi_cizelgesi():
    """Soru 8: Okçu Tuna'nın cumartesi günü 4 adımlı zaman çizelgesi."""
    adimlar = [
        ('1. 07:00 AM', 'Wake up & breakfast', MAVI, MAVI_A, 6),
        ('2. 09:00 AM', 'Archery & warm up', TUR, TUR_A, 94),
        ('3. 12:00 PM', 'Have lunch & rest', YES, YES_A, 182),
        ('4. 08:00 PM', 'Homework & sleep', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Okçu Tuna’nın cumartesi günü sabahtan akşama zaman çizelgesi.', 15)


def roportaj_soru_cevap_karti():
    """Soru 9: Muhabir ve sporcu Do/Does soru-cevap kartı."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Sports Magazine Interview · Subject: «your teammates (they)»', YESIL_K)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Question Form', MAVI)
    ic += yazi(93, 66, '___ + they + often + go...?', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Positive Short Answer', YESIL_K)
    ic += yazi(267, 66, 'Yes, they ___. (Healthy diet)', LAC, 'middle', True)
    return svg(360, 94, ic, 'Çoğul özne ile geniş zaman sorusu ve olumlu kısa cevap kartı.', 16)


def ozne_donusum_not_karti():
    """Soru 12: I -> He (Selim) özne dönüşüm kartı."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Reporting a Friend’s Routine: «I» → «Selim (He)»', MOR)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, '1st Person (I)', MAVI)
    ic += yazi(93, 66, 'I wake up · I never eat', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(267, 46, '3rd Person (Selim / He)', TUR)
    ic += yazi(267, 66, 'He ___ up · He never ___', LAC, 'middle', True)
    return svg(360, 94, ic, 'Birinci tekil kişiden üçüncü tekil kişiye geniş zaman aktarma kartı.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = defne_sporcu_karti()
    s[1]['gorsel'] = fiil_ekleri_kurallari()
    s[3]['gorsel'] = olumsuz_cumle_panosu()
    s[4]['gorsel'] = in_on_at_zaman_kartlari()
    s[6]['gorsel'] = sinan_etkinlik_tablosu()
    s[7]['gorsel'] = tuna_cumartesi_cizelgesi()
    s[8]['gorsel'] = roportaj_soru_cevap_karti()
    s[11]['gorsel'] = ozne_donusum_not_karti()
