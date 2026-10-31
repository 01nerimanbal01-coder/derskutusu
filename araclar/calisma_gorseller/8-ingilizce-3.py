"""8. sınıf İngilizce 3. hafta (Friendship: Davet metinleri, kabul-ret ve özür dileyerek gerekçe bildirme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

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


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 10.5, '#fff')


def davranis_ozellik_kartlari():
    """Dört arkadaşlık davranışı kanıt kartı."""
    kartlar = [
        ('1. Kart', 'tells me', 'the truth', MAVI, MAVI_A, 4),
        ('2. Kart', 'keeps my', 'secrets', MOR, MOR_A, 92),
        ('3. Kart', 'cheers me up', 'when I feel sad', TUR, TUR_A, 180),
        ('4. Kart', 'we never', 'argue', YES, YES_A, 268),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 44
        ic += kutu(x, 4, 86, 78, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 10.5, r)
        ic += f'<line x1="{x + 10}" y1="28" x2="{x + 76}" y2="28" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 48, s1, 10.5, LAC, 'middle', True)
        ic += yazi(cx, 64, s2, 10.5, LAC, 'middle', True)
    return svg(358, 86, ic, 'Dört davranış kanıt kartı: 1. tells me the truth, 2. keeps my secrets, 3. cheers me up when I feel sad, 4. we never argue.', 18)


def dort_konusma_ozeti():
    """Dört kısa telefon konuşması özet kartı."""
    kartlar = [
        ('1) David → Bob · Dinner', 'Bob: “Yes, why not?” (Accepts)', YES, YES_A),
        ('2) Jamie → Tanya · Cinema', 'Tanya: Refuses (has homework)', TUR, TUR_A),
        ('3) Angel → Jenny · Fruit juice', 'Jenny: Refuses (helps sister)', KIR, KIR_A),
        ('4) Thomas → John · Concert', 'John: Accepts · Meet at 7 p.m.', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += yazi(x + 8, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 8, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 96, ic, 'Dört konuşma özeti: David-Bob akşam yemeği kabul, Jamie-Tanya sinema ödev nedeniyle ret, Angel-Jenny meyve suyu ret, Thomas-John konser kabul saat 7.', 19)


def eposta_analiz_karti():
    """Betty'nin Megan'a gönderdiği doğum günü davet e-postası."""
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="14" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 18, 'INVITATION E-MAIL · From: Betty   To: Megan', 10.5, '#fff')
    ic += yazi(14, 38, 'Dear Megan,', 10.8, MAVI, 'start')
    ic += yazi(14, 53, 'Sarah and I are organizing a birthday party for Linda on Saturday.', 10.5, LAC, 'start', True)
    ic += yazi(14, 68, 'It starts at 6 p.m. at Sarah’s house. Would you like to join us?', 10.5, LAC, 'start', True)
    ic += yazi(14, 84, 'Love, Betty', 10.8, MOR, 'start')
    return svg(360, 100, ic, 'Betty nin Megan a yazdığı davet e-postası: Linda nın doğum günü partisi cumartesi saat 6 da.', 19)


def durum_oneri_fisleri():
    """Dört durum ve öneri fişi."""
    fisler = [
        ('1. fiş · Hungry', 'What about eating something?', YES, YES_A),
        ('2. fiş · Bored', 'How about watching a film?', MAVI, MAVI_A),
        ('3. fiş · Very tired', 'Let’s having a rest at home!', KIR, KIR_A),
        ('4. fiş · Free afternoon', 'Shall we play tennis in the park?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 8, y + 15, bas, 10.5, r, 'start')
        ic += yazi(x + 8, y + 30, cum, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört durum ve öneri fişi: 1. What about eating, 2. How about watching a film, 3. Let s having a rest, 4. Shall we play tennis.', 18)


def debbie_sally_eposta():
    """Debbie'nin Sally'ye gönderdiği film e-postası."""
    ic = kutu(4, 4, 352, 84, CAM_A, CAM, 8, 1.3)
    ic += yazi(14, 22, 'Hi Sally,', 11, CAM, 'start')
    ic += yazi(14, 40, 'There is a new sci-fi film at the Star Cinema this Sunday.', 10.5, LAC, 'start', True)
    ic += yazi(14, 56, 'How about watching [ it ] together at four o’clock?', 10.8, LAC, 'start')
    ic += yazi(14, 74, 'Best wishes, Debbie', 10.8, MOR, 'start')
    return svg(360, 92, ic, 'Debbie nin Sally ye e-postası: yeni bilim kurgu filmi ve watching it together daveti.', 18)


def mandy_davet_karti():
    """Mandy'nin doğum günü davet kartı."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MOR}"/><rect x="4" y="16" width="352" height="10" fill="{MOR}"/>'
    ic += yazi(180, 19, 'MANDY’S BIRTHDAY PARTY INVITATION CARD', 10.8, '#fff')
    ic += yazi(18, 42, 'Date: Sunday, 21st May', 10.8, LAC, 'start')
    ic += yazi(18, 60, 'Time: 7:30 p.m.', 10.8, LAC, 'start')
    ic += yazi(180, 42, 'Place: Daisy Café', 10.8, LAC, 'start')
    ic += yazi(180, 60, 'Dress code: Casual (günlük)', 10.5, LAC, 'start', True)
    ic += yazi(180, 79, 'Please send your reply e-mail to mandy@mail.com', 10.5, MOR, 'middle', True)
    return svg(360, 94, ic, 'Mandy doğum günü davet kartı: 21st May, 7:30 p.m., Daisy Cafe, casual giyim.', 19)


def teklif_cevap_uyumu():
    """Dört konuşma balonunda teklif ve cevap eşleştirmesi."""
    satirlar = [
        ('1) Why don’t we study together?', '→ Sure, it sounds good.', MAVI, MAVI_A),
        ('2) Would you like some orange juice?', '→ No, thanks. I’m full.', YES, YES_A),
        ('3) How about going for a walk?', '→ Cool. See you at five.', CAM, CAM_A),
        ('4) Shall we ride our bikes after school?', '→ No, thanks. I’m full.', KIR, KIR_A),
    ]
    ic = ''
    for i, (sol, sag, r, z) in enumerate(satirlar):
        y = 4 + i * 24
        ic += kutu(4, y, 352, 20, z, r, 5, 1.2)
        ic += yazi(10, y + 14, sol, 10.5, LAC, 'start')
        ic += yazi(216, y + 14, sag, 10.5, r, 'start')
    return svg(360, 100, ic, 'Dört teklif-cevap satırı: 1, 2, 3 uyumlu; 4. satırda bisiklet teklifine I m full cevabı verilmiş.', 19)


def carol_lily_notlari():
    """Carol'ın en yakın arkadaşı Lily hakkındaki okuma metni kartı."""
    ic = kutu(4, 4, 352, 86, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 20, 'Title:  ?  (Choose the best title)', 11, TUR)
    ic += yazi(14, 39, 'Lily is my closest friend at school. She backs me up when I need', 10.5, LAC, 'start', True)
    ic += yazi(14, 54, 'help and listens to my problems. She always tells me the truth and', 10.5, LAC, 'start', True)
    ic += yazi(14, 69, 'keeps my secrets. We get on well and never argue. — Carol', 10.5, LAC, 'start', True)
    return svg(360, 94, ic, 'Carol ın Lily hakkındaki okuma metni: backs me up, listens to my problems, tells the truth, keeps secrets.', 18)


def ret_eposta_sablonu():
    """Açık uçlu yazma sorusu için konser davet kartı ve cevap ipuçları."""
    ic = kutu(4, 4, 352, 80, YES_A, YES, 8, 1.3)
    ic += yazi(180, 20, 'CONCERT INVITATION · Sunday, 14th June · 8:00 p.m.', 11, YES)
    ic += yazi(16, 40, 'Write a refusal message with 3 parts:', 10.5, LAC, 'start')
    ic += yazi(16, 56, '1) Apology (I’m sorry, …)   2) Refusal + date/time (I can’t come on …)', 10.5, LAC, 'start', True)
    ic += yazi(16, 72, '3) Reason (because I have an exam / must help my parents …)', 10.5, LAC, 'start', True)
    return svg(360, 88, ic, 'Konser davet kartı: 14th June, 8:00 p.m. ve 3 parçalı ret cevabı yazma ipucu.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = davranis_ozellik_kartlari()
    s[1]['gorsel'] = dort_konusma_ozeti()
    s[3]['gorsel'] = eposta_analiz_karti()
    s[5]['gorsel'] = durum_oneri_fisleri()
    s[7]['gorsel'] = debbie_sally_eposta()
    s[8]['gorsel'] = mandy_davet_karti()
    s[9]['gorsel'] = teklif_cevap_uyumu()
    s[10]['gorsel'] = carol_lily_notlari()
    s[12]['gorsel'] = ret_eposta_sablonu()
