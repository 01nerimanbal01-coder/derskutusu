"""7. sınıf Sosyal Bilgiler 1. hafta (gruplarda ve sosyal hayatta iletişim) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def harf(x, y, h, renk):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{renk}"/>' + yazi(x, y + 4.5, h, 12, '#fff')


# --- küçük simgeler (40 × 34 alan, sol üst köşe x, y)
def s_pano(x, y, c):
    return (f'<rect x="{x + 2}" y="{y + 2}" width="36" height="26" rx="3" fill="#c9a27a" stroke="#8a5a2b" stroke-width="1.2"/>'
            f'<rect x="{x + 9}" y="{y + 6}" width="22" height="18" fill="#fff" stroke="{c}"/>'
            + ''.join(f'<line x1="{x + 12}" y1="{y + 11 + k * 5}" x2="{x + 28}" y2="{y + 11 + k * 5}" stroke="{c}" stroke-width="1.4"/>' for k in range(3))
            + f'<circle cx="{x + 20}" cy="{y + 6}" r="2" fill="{KIR}"/>')


def s_radyo(x, y, c):
    return (f'<rect x="{x + 3}" y="{y + 9}" width="34" height="20" rx="4" fill="{c}"/><circle cx="{x + 13}" cy="{y + 19}" r="6" fill="#fff"/>'
            f'<circle cx="{x + 13}" cy="{y + 19}" r="3" fill="{c}"/><rect x="{x + 23}" y="{y + 14}" width="10" height="3" rx="1" fill="#fff"/>'
            f'<rect x="{x + 23}" y="{y + 20}" width="10" height="3" rx="1" fill="#fff"/><line x1="{x + 30}" y1="{y + 9}" x2="{x + 36}" y2="{y + 1}" stroke="{c}" stroke-width="2"/>')


def s_forma(x, y, c):
    return (f'<path d="M{x + 12} {y + 3} L{x + 4} {y + 8} L{x + 7} {y + 15} L{x + 11} {y + 13} V{y + 31} H{x + 29} V{y + 13} L{x + 33} {y + 15} '
            f'L{x + 36} {y + 8} L{x + 28} {y + 3} Q{x + 20} {y + 9} {x + 12} {y + 3} Z" fill="{c}"/>' + yazi(x + 20, y + 26, '7', 11, '#fff'))


def s_kart(x, y, c):
    return (f'<rect x="{x + 4}" y="{y + 4}" width="32" height="24" rx="3" fill="#fff" stroke="{c}" stroke-width="1.6"/>'
            f'<path d="M{x + 20} {y + 22} c-5 -4 -9 -7 -6 -11 c2 -3 5 -2 6 0 c1 -2 4 -3 6 0 c3 4 -1 7 -6 11 z" fill="{KIR}"/>')


def s_telefon(x, y, c):
    return (f'<rect x="{x + 12}" y="{y + 2}" width="16" height="29" rx="3" fill="{c}"/><rect x="{x + 14}" y="{y + 6}" width="12" height="18" rx="1" fill="#fff"/>'
            f'<path d="M{x + 31} {y + 10} q4 5 0 10 M{x + 34} {y + 7} q7 8 0 16" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>')


def turler():
    """A-E durum listesi (iletişim türü tabloda yazılır); tek sütun, yazı satıra sığar."""
    kart = [('A', 'Okul panosuna gezi duyurusu asmak', s_pano, MAVI, MAVI_A), ('B', 'Radyoda hava durumunu sunmak', s_radyo, TUR, TUR_A),
            ('C', 'Takımını forma giyerek desteklemek', s_forma, KIR, KIR_A), ('D', 'Arkadaşına tebrik kartı yazmak', s_kart, MOR, MOR_A),
            ('E', 'Dedesiyle telefonda konuşmak', s_telefon, YES, YES_A)]
    ic = ''
    for i, (h, metin, simge, c, d) in enumerate(kart):
        y = 3 + i * 38
        ic += kutu(4, y, 352, 34, d, c) + harf(20, y + 17, h, c) + simge(38, y, c) + yazi(90, y + 21.5, metin, 12.5, LAC, 'start', True)
    return svg(360, 194, ic, 'Durumlar: A okul panosuna gezi duyurusu asmak, B radyoda hava durumunu sunmak, C takımını forma giyerek desteklemek, D arkadaşına tebrik kartı yazmak, E dedesiyle telefonda konuşmak', 40)


def balonlar():
    """A-D konuşma balonları."""
    soz = [('A', ['Sen hiç beni', 'dinlemiyorsun!']), ('B', ['Ders çalışırken ses olunca', 'dikkatimi toplayamıyorum.']),
           ('C', ['Hep sen haklısın', 'zaten!']), ('D', ['Sen çok', 'dağınıksın!'])]
    renk = [MAVI, TUR, YES, MOR]
    acik = [MAVI_A, TUR_A, YES_A, MOR_A]
    ic = ''
    for i, (h, satirlar) in enumerate(soz):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 60
        c, d = renk[i], acik[i]
        ic += f'<path d="M{x + 8} {y} H{x + 164} a8 8 0 0 1 8 8 V{y + 38} a8 8 0 0 1 -8 8 H{x + 40} L{x + 26} {y + 55} L{x + 28} {y + 46} H{x + 8} a8 8 0 0 1 -8 -8 V{y + 8} a8 8 0 0 1 8 -8 Z" fill="{d}" stroke="{c}" stroke-width="1.5"/>'
        ic += harf(x + 16, y + 23, h, c) + ''.join(yazi(x + 32, y + 20 + j * 14, s, 10.5, LAC, 'start', True) for j, s in enumerate(satirlar))
    return svg(360, 124, ic, 'Konuşma balonları: A Sen hiç beni dinlemiyorsun! B Ders çalışırken ses olunca dikkatimi toplayamıyorum. C Hep sen haklısın zaten! D Sen çok dağınıksın!', 28)


def araclar():
    """Dört kitle iletişim aracı."""
    ic = ''
    ogeler = [('Televizyon', MAVI), ('Radyo', TUR), ('Gazete', SOLUK), ('Genel ağ', YES)]
    for i, (ad, c) in enumerate(ogeler):
        x = 4 + i * 90
        ic += kutu(x, 4, 84, 82, GRI_A, GRI, 8, 1.2)
        cx = x + 42
        if ad == 'Televizyon':
            ic += f'<rect x="{cx - 24}" y="16" width="48" height="32" rx="4" fill="{c}"/><rect x="{cx - 20}" y="20" width="40" height="24" rx="2" fill="#dbe6ff"/><path d="M{cx - 8} 54 h16 l-4 -6 h-8 z" fill="{c}"/>'
        elif ad == 'Radyo':
            ic += s_radyo(cx - 20, 16, c)
        elif ad == 'Gazete':
            ic += f'<rect x="{cx - 22}" y="14" width="44" height="40" rx="2" fill="#fff" stroke="{c}" stroke-width="1.4"/><rect x="{cx - 17}" y="19" width="34" height="7" fill="{c}"/>'
            ic += ''.join(f'<line x1="{cx - 17}" y1="{31 + k * 5}" x2="{cx + (2 if k % 2 else 17)}" y2="{31 + k * 5}" stroke="{GRI}" stroke-width="1.4"/>' for k in range(4))
        else:
            ic += f'<rect x="{cx - 22}" y="16" width="44" height="30" rx="3" fill="{c}"/><rect x="{cx - 19}" y="19" width="38" height="24" fill="#e3f6ea"/><path d="M{cx - 27} 49 h54 l-4 5 h-46 z" fill="{c}"/>'
            ic += f'<circle cx="{cx}" cy="31" r="9" fill="none" stroke="{c}" stroke-width="1.5"/><ellipse cx="{cx}" cy="31" rx="4" ry="9" fill="none" stroke="{c}" stroke-width="1.2"/><line x1="{cx - 9}" y1="31" x2="{cx + 9}" y2="31" stroke="{c}" stroke-width="1.2"/>'
        ic += yazi(cx, 76, ad, 11.5, LAC)
    return svg(364, 90, ic, 'Araçlar: televizyon, radyo, gazete, genel ağ', 22)


def sohbet():
    """Proje grubunun mesajlaşma ekranı."""
    ic = kutu(4, 4, 352, 168, '#f5f7fc', LAC, 12, 2) + f'<path d="M4 16 a12 12 0 0 1 12 -12 H344 a12 12 0 0 1 12 12 V26 H4 Z" fill="{LAC}"/>'
    ic += yazi(180, 20, '7-C Proje grubu', 12, '#fff')
    mesaj = [('Ece', 'Sunumu kim hazırlayacak?', MAVI, MAVI_A, 'sol'), ('Can', 'Bilmem.', TUR, TUR_A, 'sag'),
             ('Ece', 'Mesaj gönderilemedi: bağlantı yok', KIR, KIR_A, 'uyari'), ('Can', 'Hep son dakikada soruyorsun zaten!', MOR, MOR_A, 'sag')]
    for i, (ad, m, c, d, yer) in enumerate(mesaj):
        y = 34 + i * 34
        w = 26 + len(m) * 6.3
        x = 14 if yer == 'sol' else (356 - 10 - w if yer == 'sag' else 180 - w / 2)
        ic += kutu(x, y, w, 28, d, c, 8, 1.2)
        if yer == 'uyari':
            ic += yazi(x + w / 2, y + 18.5, f'⚠ {m}', 10.5, KIR, 'middle', True)
        else:
            ic += yazi(x + 9, y + 12, ad, 9.5, c, 'start') + yazi(x + 9, y + 24, m, 10.5, LAC, 'start', True)
    return svg(360, 176, ic, 'Mesajlaşma: Ece: Sunumu kim hazırlayacak? Can: Bilmem. Ece: Mesaj gönderilemedi, bağlantı yok. Can: Hep son dakikada soruyorsun zaten!', 38)


def notlar():
    """Öğretmenin sunum gözlem notları (yarım sütunda okunur punto)."""
    satir = ['Kelimeleri doğru söyledi.', 'Konuşurken hep yere baktı.', 'Çok hızlı ve alçak sesle konuştu.', 'Soruları içtenlikle cevapladı.']
    ic = f'<rect x="10" y="6" width="340" height="120" rx="4" fill="#fffbea" stroke="#d9b24c" stroke-width="1.4"/><rect x="150" y="0" width="60" height="12" rx="2" fill="#f5d77a"/>'
    ic += yazi(180, 29, 'Sunum notlarım: Mert', 14, LAC)
    for i, s in enumerate(satir):
        y = 52 + i * 21
        ic += f'<line x1="24" y1="{y + 6}" x2="336" y2="{y + 6}" stroke="#e8d9a8" stroke-width="1"/><circle cx="32" cy="{y - 4.5}" r="3" fill="{SOLUK}"/>'
        ic += yazi(44, y, s, 13.5, LAC, 'start', True)
    return svg(360, 130, ic, 'Sunum notları, Mert: Kelimeleri doğru söyledi. Konuşurken hep yere baktı. Çok hızlı ve alçak sesle konuştu. Soruları içtenlikle cevapladı.', 27)


def afis():
    """Okulun kültür günü afişi."""
    ic = kutu(40, 4, 280, 134, YES_A, YES, 8, 2)
    ic += yazi(180, 32, 'KÜLTÜR GÜNÜ', 18, '#0c7a3c')
    ic += yazi(180, 56, 'Farklı ülkelerden gelen arkadaşlarımız', 11.5, LAC, 'middle', True)
    ic += yazi(180, 72, 'yemeklerini, oyunlarını ve dillerini tanıtıyor.', 11.5, LAC, 'middle', True)
    for i, (c1, c2) in enumerate([(KIR, '#fff'), (MAVI, TUR), (YES, '#fff'), (MOR, '#f5d77a'), (TUR, MAVI)]):   # süs değil: çok kültürlülüğü anlatan bayrakçıklar
        x = 96 + i * 36
        ic += f'<line x1="{x}" y1="86" x2="{x}" y2="110" stroke="{SOLUK}" stroke-width="1.4"/><rect x="{x}" y="86" width="22" height="14" fill="{c1}"/><rect x="{x}" y="91" width="22" height="4" fill="{c2}"/>'
    ic += yazi(180, 128, 'Cuma 13.30 · Okul bahçesi', 11.5, SOLUK)
    return svg(360, 142, ic, 'Afiş: Kültür günü. Farklı ülkelerden gelen arkadaşlarımız yemeklerini, oyunlarını ve dillerini tanıtıyor. Cuma 13.30, okul bahçesi.', 27)


def uygula(o):
    s = o['sorular']
    s[2]['gorsel'] = turler()
    s[4]['gorsel'] = balonlar()
    s[7]['gorsel'] = araclar()
    s[8]['gorsel'] = sohbet()
    s[9]['gorsel'] = notlar()
    s[11]['gorsel'] = afis()
