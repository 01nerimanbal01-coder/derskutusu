"""7. sınıf DKAB 8. hafta (Hac ve Umre İbadetinin Tanımı, Yapılışı ve Farkları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def hac_yukumluluk_panosu():
    kartlar = [
        ('1. Kart', 'Akıllı ve ergenlik', 'çağına ulaşmış olmak', YES, YES_A),
        ('2. Kart', 'Yolculuk masrafına', 'yetecek maddi güç', MAVI, MAVI_A),
        ('3. Kart', 'Yalnızca Ramazan ayında', 'oruçlu iken gitmek', KIR, KIR_A),
        ('4. Kart', 'Sağlıklı olmak ve', 'yol güvenliği bulunmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="52" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 48, y + 30, bas, 12, renk)
        ic += f'<line x1="{x + 92}" y1="{y + 8}" x2="{x + 92}" y2="{y + 44}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 188, y + 22, s1, 12, LAC, ince=True)
        ic += yazi(x + 188, y + 40, s2, 12, LAC, ince=True)
    return svg(600, 122, ic, 'Haccın yükümlülük şartları dört kartı.', 21)


def kutsal_mekan_kartlari():
    kartlar = [
        ('Mîkat', 'İhram Sınırı', YES, YES_A),
        ('Arafat', 'Arefe Vakfesi', TUR, TUR_A),
        ('Safa - Merve', '7 Kez Sa’y', MAVI, MAVI_A),
        ('Mina', 'Taşlama - Kurban', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, gorev, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="8" width="140" height="78" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 70, 34, ad, 12, renk)
        ic += f'<line x1="{x + 14}" y1="44" x2="{x + 126}" y2="44" stroke="{renk}" stroke-width="1.1"/>'
        ic += yazi(x + 70, 68, gorev, 12, LAC, ince=True)
    return svg(600, 94, ic, 'Kutsal mekânlar Mîkat, Arafat, Safa-Merve ve Mina kartları.', 20)


def haccin_uc_farzi_sema():
    kutular = [
        ('K : 1. Farz', 'Mîkat sınırında', 'ihrama girmek', YES, YES_A, 10),
        ('L : 2. Farz', 'Arefe günü Arafat’ta', 'vakfe yapmak', TUR, TUR_A, 206),
        ('M : 3. Farz', '?', '(Kâbe’deki farz görev)', MAVI, MAVI_A, 402),
    ]
    ic = ''
    for bas, s1, s2, renk, arka, x in kutular:
        ic += f'<rect x="{x}" y="8" width="188" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 94, 30, bas, 12, renk)
        ic += f'<line x1="{x + 16}" y1="38" x2="{x + 172}" y2="38" stroke="{renk}" stroke-width="1.1"/>'
        ic += yazi(x + 94, 60, s1, 12, LAC, ince=True)
        ic += yazi(x + 94, 80, s2, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Haccın üç farzı K, L ve M şeması.', 21)


def say_ibadeti_levhasi():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += f'<rect x="20" y="18" width="140" height="68" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(90, 44, 'SAFA TEPESİ', 12, YESIL_K)
    ic += yazi(90, 66, '(Başlangıç)', 12, LAC, ince=True)
    ic += f'<line x1="168" y1="42" x2="432" y2="42" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<line x1="432" y1="64" x2="168" y2="64" stroke="{MAVI}" stroke-width="2" stroke-dasharray="5 3"/>'
    ic += yazi(300, 32, '4 Gidiş - 3 Geliş = Toplam 7 Yürüyüş (Sa’y)', 12, KAHVE)
    ic += yazi(300, 84, 'Su Arayışı Hatırası · Yeşil Direkler Arası Hervele', 12, LAC, ince=True)
    ic += f'<rect x="440" y="18" width="140" height="68" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(510, 44, 'MERVE TEPESİ', 12, MAVI)
    ic += yazi(510, 66, '(Bitiş)', 12, LAC, ince=True)
    return svg(600, 104, ic, 'Safa ve Merve tepeleri arasında 7 gidiş-geliş sa’y şeması.', 21)


def hac_umre_karsilastirma():
    ic = f'<rect x="6" y="6" width="190" height="96" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(101, 26, 'YALNIZ HAC (Farz)', 12, TUR)
    ic += yazi(101, 48, 'Zilhicce ayı · Yılda 1 kez', 12, LAC, ince=True)
    ic += yazi(101, 68, 'Arafat-Müzdelife vakfesi', 12, LAC, ince=True)
    ic += yazi(101, 88, 'Şeytan taşlama · Kurban', 12, LAC, ince=True)

    ic += f'<rect x="205" y="6" width="190" height="96" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'ORTAK UNSURLAR', 12, YESIL_K)
    ic += yazi(300, 50, 'Mîkatta ihrama girmek', 12, LAC, ince=True)
    ic += yazi(300, 70, 'Kâbe’yi 7 şavt tavaf etmek', 12, LAC, ince=True)
    ic += yazi(300, 90, 'Safa-Merve sa’yi ve tıraş', 12, LAC, ince=True)

    ic += f'<rect x="404" y="6" width="190" height="96" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(499, 26, 'YALNIZ UMRE (Sünnet)', 12, MAVI)
    ic += yazi(499, 50, 'Hac günleri dışında', 12, LAC, ince=True)
    ic += yazi(499, 70, 'yılın her vaktinde yapılır', 12, LAC, ince=True)
    ic += yazi(499, 90, 'Vakfe ve taşlama yoktur', 12, LAC, ince=True)
    return svg(600, 108, ic, 'Hac ve umre ibadetlerinin ortak ve farklı yönleri şeması.', 21)


def hac_yolculuk_seridi():
    adimlar = [
        ('1. Durak', 'Mîkat ve İhram', YES, YES_A),
        ('2. Durak', 'Arafat Vakfesi', TUR, TUR_A),
        ('3. Durak', 'Müzdelife Gece', MOR, MOR_A),
        ('4. Durak', 'Mina ve Kâbe', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="10" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 34, ust, 12, renk)
        ic += yazi(x + 68, 58, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="44" x2="{x + 148}" y2="44" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 88, ic, 'Hac ibadetinin dört duraklı uygulama sırası.', 20)


def ihram_yasaklari_panosu():
    ic = f'<rect x="8" y="6" width="584" height="90" rx="10" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'İHRAM YASAKLARI VE ADABI PANOSU', 12, KIR)
    ic += yazi(150, 52, 'Yasak: Saç-sakal tıraşı ve tırnak kesmek', 12, LAC, ince=True)
    ic += yazi(450, 52, 'Yasak: Koku sürünmek ve avlanmak', 12, LAC, ince=True)
    ic += yazi(150, 76, 'Yasak: Bitki koparmak ve kavga etmek', 12, LAC, ince=True)
    ic += yazi(450, 76, 'Serbest: Telbiye, dua, namaz, zemzem', 12, YESIL_K)
    return svg(600, 102, ic, 'İhram yasakları ve serbest ibadetler panosu.', 20)


def ihram_esitlik_karti():
    ic = f'<rect x="8" y="6" width="282" height="86" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 28, '1. Kart · Sade İhram Örtüsü', 12, MAVI)
    ic += yazi(149, 52, 'Makam, zenginlik ve ırk farkı', 12, LAC, ince=True)
    ic += yazi(149, 72, 'olmadan aynı kıyafette buluşma', 12, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="86" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 28, '2. Kart · Toplumsal Mesaj', 12, YESIL_K)
    ic += yazi(451, 52, 'Allah katında eşitlik, tevazu,', 12, LAC, ince=True)
    ic += yazi(451, 72, 'birlik ve evrensel kardeşlik', 12, LAC, ince=True)
    return svg(600, 98, ic, 'İhram örtüsü ve toplumsal eşitlik-kardeşlik kartları.', 20)


def dort_uygulama_kartlari():
    kartlar = [
        ('Zeynep', 'Müzdelife’de taş topladı', MOR, MOR_A),
        ('Kerem', 'Mina’da şeytan taşladı', TUR, TUR_A),
        ('Ahmet', 'Arafat’ta vakfe yaptı', YES, YES_A),
        ('Elif', 'Veda tavafı yaptı', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, islem, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 48
        ic += f'<rect x="{x}" y="{y}" width="286" height="42" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 48, y + 26, ad, 12, renk)
        ic += f'<line x1="{x + 92}" y1="{y + 6}" x2="{x + 92}" y2="{y + 36}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 188, y + 26, islem, 12, LAC, ince=True)
    return svg(600, 102, ic, 'Dört hacı adayının yaptığı uygulamalar kartları.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = hac_yukumluluk_panosu()
    s[1]['gorsel'] = kutsal_mekan_kartlari()
    s[3]['gorsel'] = haccin_uc_farzi_sema()
    s[4]['gorsel'] = say_ibadeti_levhasi()
    s[6]['gorsel'] = hac_umre_karsilastirma()
    s[7]['gorsel'] = hac_yolculuk_seridi()
    s[8]['gorsel'] = ihram_yasaklari_panosu()
    s[11]['gorsel'] = ihram_esitlik_karti()
    s[12]['gorsel'] = dort_uygulama_kartlari()
