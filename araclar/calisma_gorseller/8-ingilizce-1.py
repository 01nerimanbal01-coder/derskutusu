"""8. sınıf İngilizce 1. hafta (Friendship: Arkadaşlık, davet ve gerekçeli cevaplar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:calc(16mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def davet_kalip_kartlari():
    """Dört davet kalıbı ve fiil biçimi kartı."""
    kartlar = [
        ('Would you like to …?', '+ V1 (yalın)', MAVI, MAVI_A, 6),
        ('How about …?', '+ V-ing', TUR, TUR_A, 134),
        ('Why don’t we …?', '+ V1 (yalın)', YES, YES_A, 262),
        ('Let’s …', '+ V1 (yalın)', MOR, MOR_A, 390),
    ]
    ic = ''
    for bas, alt, r, z, x in kartlar:
        cx = x + 61
        ic += kutu(x, 4, 122, 76, z, r, 8, 1.3)
        ic += yazi(cx, 24, bas, 10.5, r)
        ic += f'<line x1="{x + 12}" y1="34" x2="{x + 110}" y2="34" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 56, alt, 11, LAC)
    return svg(518, 84, ic, 'Dört davet kalıbı kartı: Would you like to + V1, How about + V-ing, Why don t we + V1, Let s + V1.', 16)


def cevap_kartlari():
    """Dört arkadaşın come over davetine verdiği cevap kartları."""
    kartlar = [
        ('Mert', 'I’m sorry, I can’t. I have a math test.', KIR, KIR_A),
        ('Selin', 'Sure, it sounds good. What time?', YES, YES_A),
        ('Arda', 'I’d love to, but my cousin is coming.', TUR, TUR_A),
        ('Duru', 'I’m afraid I can’t. I have homework.', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, cum, r, z) in enumerate(kartlar):
        x, y = 6 + (i % 2) * 256, 4 + (i // 2) * 44
        ic += kutu(x, y, 248, 38, z, r, 7, 1.3)
        ic += yazi(x + 12, y + 15, ad, 10.8, r, 'start')
        ic += yazi(x + 12, y + 30, cum, 10.5, LAC, 'start', True)
    return svg(516, 92, ic, 'Dört arkadaşın davet cevabı kartları: Mert, Arda ve Duru reddediyor; Selin kabul ediyor.', 16)


def arkadaslik_panosu():
    """Arkadaşlık özellikleri ve kabul/ret kuralları panosu."""
    ic = kutu(6, 4, 210, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(111, 20, 'True Friend Qualities', 11, MAVI)
    ic += yazi(16, 38, 'keeps secrets → trustworthy', 10.5, LAC, 'start', True)
    ic += yazi(16, 54, 'tells the truth → honest', 10.5, LAC, 'start', True)
    ic += yazi(16, 70, 'backs me up → supportive', 10.5, LAC, 'start', True)

    ic += kutu(224, 4, 210, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(329, 20, 'Accepting & Refusing', 11, TUR)
    ic += yazi(234, 38, 'Yes, I’d love to. → Accept', 10.5, YES, 'start')
    ic += yazi(234, 54, 'I’d love to, but I can’t. → Refuse', 10.5, KIR, 'start')
    ic += yazi(234, 70, 'What about + V-ing? → Offer', 10.5, LAC, 'start', True)
    return svg(440, 90, ic, 'Arkadaşlık özellikleri ve kabul-ret kuralları bilgi panosu.', 16)


def oneri_fisleri():
    """Dört öneri fişi (3. fişte How about watch hatası)."""
    fisler = [
        ('1. fiş · Picnic', 'Would you like to have a picnic?', YES, YES_A),
        ('2. fiş · Music', 'Let’s listen to some music.', MAVI, MAVI_A),
        ('3. fiş · Film', 'How about watch a film at home?', KIR, KIR_A),
        ('4. fiş · Drink', 'What about drinking fruit juice?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(fisler):
        x, y = 6 + (i % 2) * 218, 4 + (i // 2) * 44
        ic += kutu(x, y, 210, 38, z, r, 7, 1.3)
        ic += yazi(x + 12, y + 15, bas, 10.5, r, 'start')
        ic += yazi(x + 12, y + 30, cum, 10.5, LAC, 'start', True)
    return svg(440, 92, ic, 'Dört öneri fişi: 1. Would you like to have, 2. Let s go, 3. How about watch, 4. What about drinking.', 16)


def bora_kaan_mesaji():
    """Bora'nın Kaan'a gönderdiği kısa yürüyüş daveti mesajı."""
    ic = kutu(6, 4, 428, 80, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="6" y="4" width="428" height="20" rx="8" fill="{CAM}"/><rect x="6" y="14" width="428" height="10" fill="{CAM}"/>'
    ic += yazi(220, 18, 'MESSAGE CARD · From: Bora   To: Kaan', 10.8, '#fff')
    ic += yazi(18, 42, '“Hi Kaan! Let’s go for a walk tomorrow.”', 11.2, LAC, 'start')
    ic += yazi(18, 64, 'Check: Event ✓   |   Day ✓   |   Place (Where?) ?   |   Time (What time?) ?', 10.5, CAM, 'start', True)
    return svg(440, 88, ic, 'Bora nın Kaan a gönderdiği Let s go for a walk tomorrow mesaj kartı.', 16)


def arkadas_ozellik_tablosu():
    """Dört arkadaşın davranış ve özellik tablosu."""
    ic = kutu(6, 4, 448, 94, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="6" y="4" width="448" height="20" rx="8" fill="{LAC}"/><rect x="6" y="14" width="448" height="10" fill="{LAC}"/>'
    ic += yazi(230, 18, 'Friends & Their Behaviours', 10.8, '#fff')
    satirlar = [
        ('Tuna', 'keeps secrets & never lies', 'trustworthy / honest', YES),
        ('Ela', 'backs her friends up in trouble', 'supportive', MAVI),
        ('Can', 'always tells the truth', 'honest / reliable', TUR),
        ('Zeynep', 'shares books & helps mates', 'supportive / gets on well', MOR),
    ]
    for i, (ad, dav, oz, r) in enumerate(satirlar):
        y = 30 + i * 16
        ic += yazi(18, y + 10, ad, 10.8, r, 'start')
        ic += yazi(84, y + 10, dav, 10.5, LAC, 'start', True)
        ic += yazi(292, y + 10, oz, 10.5, r, 'start')
    return svg(460, 102, ic, 'Tuna, Ela, Can ve Zeynep in arkadaşlık davranışları ve özellikleri tablosu.', 16)


def ret_mesaji_bolumleri():
    """Özür, ret ve gerekçe bölümlerini gösteren şema."""
    ic = kutu(6, 4, 468, 78, KUM, GRI, 8, 1.2)
    ic += yazi(240, 19, 'Parts of a Refusal Sentence', 11, LAC)
    parcalar = [
        ('1. Bölüm', '“I’m sorry,”', MAVI, MAVI_A, 14, 114),
        ('2. Bölüm', '“I can’t go to the cinema”', KIR, KIR_A, 136, 162),
        ('3. Bölüm', '“because I have a math test.”', TUR, TUR_A, 306, 160),
    ]
    for bas, met, r, z, x, w in parcalar:
        ic += kutu(x, 28, w, 46, z, r, 6, 1.3)
        ic += yazi(x + w / 2, 44, bas, 10.5, r)
        ic += yazi(x + w / 2, 62, met, 10.2, LAC, 'middle', True)
    return svg(480, 86, ic, 'Ret cümlesinin üç bölümü: I m sorry, I can t go to the cinema, because I have a math test.', 16)


def nil_haftasonu_plani():
    """Nil'in hafta sonu planı ve Sude'nin sinema daveti kartı."""
    ic = kutu(6, 4, 210, 80, MOR_A, MOR, 8, 1.3)
    ic += yazi(111, 20, 'Nil’s Saturday Plan', 11, MOR)
    ic += yazi(16, 40, 'Morning: finish homework', 10.5, LAC, 'start', True)
    ic += yazi(16, 56, 'Afternoon: cousin is coming', 10.5, KIR, 'start')
    ic += yazi(16, 72, 'Evening: listen to music', 10.5, LAC, 'start', True)

    ic += kutu(224, 4, 210, 80, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(329, 20, 'Sude’s Invitation', 11, MAVI)
    ic += yazi(234, 42, '“Would you like to go to the', 10.5, LAC, 'start', True)
    ic += yazi(234, 57, 'cinema on Saturday afternoon?”', 10.5, LAC, 'start', True)
    ic += yazi(234, 73, '→ Nil’s reply + because …', 10.5, MAVI, 'start')
    return svg(440, 88, ic, 'Nil in cumartesi planı (öğleden sonra kuzeni geliyor) ve Sude nin cumartesi öğleden sonra sinema daveti.', 16)


def diyalog_ipucu_karti():
    """Açık uçlu soru için davet ve özürlü ret ipucu kartı."""
    ic = kutu(6, 4, 428, 74, YES_A, YES, 8, 1.3)
    ic += yazi(220, 20, 'Dialogue Writing Prompts (Invitation + Refusal with Excuse)', 11, YES)
    ic += yazi(18, 40, 'Friend A (Invite): Would you like to … / How about … this evening?', 10.5, LAC, 'start', True)
    ic += yazi(18, 56, 'Friend B (Apology + Refusal): I’m sorry, I can’t. / I’d love to, but I can’t.', 10.5, LAC, 'start', True)
    ic += yazi(18, 70, 'Friend B (Excuse): … because I have an exam tomorrow.', 10.5, YES, 'start')
    return svg(440, 82, ic, 'Davet ve sınav gerekçeli ret diyaloğu yazma ipucu kartı.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = davet_kalip_kartlari()
    s[1]['gorsel'] = cevap_kartlari()
    s[3]['gorsel'] = arkadaslik_panosu()
    s[5]['gorsel'] = oneri_fisleri()
    s[7]['gorsel'] = bora_kaan_mesaji()
    s[8]['gorsel'] = arkadas_ozellik_tablosu()
    s[9]['gorsel'] = ret_mesaji_bolumleri()
    s[10]['gorsel'] = nil_haftasonu_plani()
    s[13]['gorsel'] = diyalog_ipucu_karti()
