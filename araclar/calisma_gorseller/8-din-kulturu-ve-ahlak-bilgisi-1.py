"""8. sınıf DKAB 1. hafta (Kader, kaza, Allah'ın sıfatları ve sünnetullah: fiziksel, biyolojik, toplumsal yasalar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:calc(16mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def kader_kaza_sema():
    kartlar = [
        ('Genel Ölçü ve Düzen', 'Evrendeki kütle çekimi yasası ve', 'suyun 100 °C’de kaynama kuralı', 'K', MAVI, MAVI_A),
        ('Gerçekleşen Belirli Olay', 'Dalından kopan elmanın o anda', 'yere düşmesi ve suyun kaynaması', 'L', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 298
        ic += f'<rect x="{x}" y="6" width="286" height="114" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="6" width="286" height="26" rx="10" fill="{renk}"/><rect x="{x}" y="20" width="286" height="12" fill="{renk}"/>'
        ic += yazi(x + 143, 23, bas, 12, '#fff')
        ic += yazi(x + 143, 52, s1, 11.2, LAC, ince=True)
        ic += yazi(x + 143, 70, s2, 11.2, LAC, ince=True)
        ic += f'<rect x="{x + 68}" y="84" width="150" height="26" rx="7" fill="#fff" stroke="{renk}" stroke-width="1.5" stroke-dasharray="4 3"/>'
        ic += yazi(x + 143, 101, f'Kavram: {harf} ?', 11.8, renk)
    ic += f'<line x1="294" y1="63" x2="302" y2="63" stroke="{LAC}" stroke-width="2.2"/><path d="M298 58 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 126, ic, 'Genel ölçü ve düzen (K) ile belirli olayın zamanı gelince gerçekleşmesi (L) şeması.', 23)


def yasa_turleri_pano():
    kartlar = [
        ('1', 'Fiziksel Yasa', 'Dünya’nın eksen eğikliği ve Güneş', 'çevresinde dolanmasıyla mevsimlerin oluşması', MAVI, MAVI_A),
        ('2', 'Biyolojik Yasa', 'Bir toplumda adaletin korunmasıyla', 'güven ve barış ortamının güçlenmesi', YES, YES_A),
        ('3', 'Toplumsal Yasa', 'Balıkların suda solungaçlarıyla', 'solunum yaparak yaşamını sürdürmesi', TUR, TUR_A),
        ('4', 'Fiziksel Yasa', 'Denizlerden buharlaşan suyun', 'yoğuşarak yağmur hâlinde yeryüzüne inmesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 64
        ic += f'<rect x="{x}" y="{y}" width="286" height="56" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += rozet(x + 20, y + 28, no, renk, 10, 11.5)
        ic += yazi(x + 38, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 38, y + 35, s1, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 38, y + 49, s2, 10.8, LAC, 'start', ince=True)
    return svg(600, 132, ic, 'Dört gözlem kartı ve yasa sınıflandırması: 1. Mevsimler, 2. Adalet ve güven, 3. Balıkların solunumu, 4. Su döngüsü.', 23)


def ayet_yasa_kartlari():
    kart = [
        ('1. Kart · Enbiya 33', '“Geceyi, gündüzü, Güneş’i ve Ay’ı yaratan', 'O’dur; her biri bir yörüngede yüzmektedir.”', MAVI, MAVI_A),
        ('2. Kart · Enam 99', '“Gökten su indiren O’dur... Onunla her türlü', 'bitkiyi, yeşilliği ve daneleri çıkarırız.”', YES, YES_A),
        ('3. Kart · Nisa 135', '“Kendinizin veya yakınlarınızın aleyhine', 'olsa bile adaleti titizlikle ayakta tutun.”', TUR, TUR_A),
        ('4. Kart · Enam 96', '“Güneş ve Ay bir hesaba göre hareket', 'eder. Bu, üstün ve bilgin Allah’ın takdiridir.”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 62
        ic += f'<rect x="{x}" y="{y}" width="286" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="54" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.2, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 48, s2, 10.6, LAC, 'start', ince=True)
    return svg(600, 128, ic, 'Dört ayet kartı: Enbiya 33, Enam 99, Nisa 135 ve Enam 96.', 22)


def bahce_uc_bakis():
    kutular = [
        ('1. İnceleme', 'Sulama suyunun eğimli', 'borularda akış hızı', MAVI, MAVI_A),
        ('2. İnceleme', 'Fidanın kök ve yaprak', 'geliştirerek büyümesi', YES, YES_A),
        ('3. İnceleme', 'Ortak sulama suyunun', 'bahçelere adil dağıtımı', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="6" width="192" height="96" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 96, 26, bas, 12, renk)
        ic += f'<line x1="{x + 18}" y1="34" x2="{x + 174}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 96, 56, s1, 11, LAC, ince=True)
        ic += yazi(x + 96, 76, s2, 11, LAC, ince=True)
    return svg(600, 108, ic, 'Aynı bahçede üç farklı inceleme: 1. suyun boruda akışı, 2. fidanın büyümesi, 3. ortak suyun adil dağıtımı.', 22)


def ayet_analiz_zinciri():
    adlar = [
        ('1. Adım', 'Meali Oku', MAVI, MAVI_A),
        ('2. Adım', 'Mesajı Belirle', YES, YES_A),
        ('3. Adım', 'Ölçütle Sınıflandır', TUR, TUR_A),
        ('4. Adım', 'Gerekçeyi Açıkla', MOR, MOR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="10" width="132" height="68" rx="12" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 66, 34, ust, 11.5, renk)
        ic += yazi(x + 66, 56, alt, 11, LAC)
        if i < 3:
            ic += f'<line x1="{x + 134}" y1="44" x2="{x + 146}" y2="44" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 141} 39 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 88, ic, 'Ayeti konuyla ilişkilendirme adımları: Meali oku, Mesajı belirle, Ölçütle sınıflandır, Gerekçeyi açıkla.', 20)


def sifatlar_sema():
    kutular = [
        ('İLİM Sıfatı', 'Allah’ın olmuş ve olacak', 'her şeyi eksiksiz bilmesi', MAVI, MAVI_A),
        ('İRADE Sıfatı', 'Allah’ın varlıkları ve', 'özelliklerini dileyip seçmesi', YES, YES_A),
        ('KUDRET Sıfatı', 'Allah’ın dilediği düzeni', 'sınırsız gücüyle yaratması', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="6" width="192" height="96" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 96, 26, bas, 12, renk)
        ic += yazi(x + 96, 52, s1, 11, LAC, ince=True)
        ic += yazi(x + 96, 72, s2, 11, LAC, ince=True)
    return svg(600, 108, ic, 'Kaderle ilişkili üç ilahi sıfat: İlim (bilme), İrade (dileme), Kudret (güç yetirme).', 21)


def gunluk_dil_karti():
    ic = f'<rect x="6" y="6" width="286" height="96" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(149, 25, 'Günlük Dilde “Kaza” Kullanımı', 11.8, TUR)
    ic += yazi(149, 50, 'Yalnızca trafik kazası veya', 11, LAC, ince=True)
    ic += yazi(149, 68, 'beklenmedik üzücü olayları', 11, LAC, ince=True)
    ic += yazi(149, 86, 'anlatmak için dar anlamda kullanılır.', 11, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(451, 25, 'Dinî Terim Olarak “Kaza”', 11.8, MAVI)
    ic += yazi(451, 50, 'Allah’ın ezelde takdir ettiği', 11, LAC, ince=True)
    ic += yazi(451, 68, 'bütün olayların yeri ve zamanı', 11, LAC, ince=True)
    ic += yazi(451, 86, 'geldiğinde meydana gelmesidir.', 11, MAVI)
    return svg(600, 108, ic, 'Günlük dildeki kaza kullanımı ile dinî terim olan kaza kavramının karşılaştırılması.', 21)


def gozlem_arastirma_karti():
    ic = f'<rect x="6" y="6" width="286" height="96" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.8"/>'
    ic += yazi(149, 25, 'Kaan’ın Hatalı Çıkarımı', 11.8, KIR)
    ic += yazi(149, 50, '“Evrendeki her olay kaderle', 11, LAC, ince=True)
    ic += yazi(149, 68, 'belirlendiği için doğa olaylarını', 11, LAC, ince=True)
    ic += yazi(149, 86, 'araştırmaya ve deneye gerek yoktur.”', 11, KIR)

    ic += f'<rect x="308" y="6" width="286" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(451, 25, 'Kur’an’ın Yönlendirmesi', 11.8, YESIL_K)
    ic += yazi(451, 50, 'Göklerin, suyun ve bitkilerin', 11, LAC, ince=True)
    ic += yazi(451, 68, '  düzeni üzerinde düşünmeye çağırır.', 11, LAC, ince=True)
    ic += yazi(451, 86, 'Sabit ölçü araştırmayı mümkün kılar.', 11, YESIL_K)
    return svg(600, 108, ic, 'Kaan’ın hatalı çıkarımı ve Kur’an’ın evrendeki ölçü üzerinde düşünmeye/araştırmaya yönlendirmesi.', 21)


def nisa135_adalet_karti():
    ic = f'<rect x="6" y="6" width="588" height="94" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += f'<rect x="6" y="6" width="10" height="94" rx="4" fill="{ALTIN}"/>'
    ic += yazi(26, 26, 'Nisa suresi 135. ayet mesajı:', 11.8, KAHVE, 'start')
    ic += yazi(26, 48, '“Ey iman edenler! Kendinizin, anne babanızın ve yakınlarınızın aleyhine bile olsa adaleti titizlikle koruyun.”', 11.2, LAC, 'start', ince=True)
    ic += f'<rect x="26" y="62" width="260" height="26" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(156, 79, 'Adalet → Güven, barış ve dayanışma', 11, YESIL_K)
    ic += f'<rect x="310" y="62" width="268" height="26" rx="6" fill="{TUR_A}" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(444, 79, 'Ayrıcalık / Haksızlık → Güvensizlik ve kargaşa', 11, KIR)
    return svg(600, 106, ic, 'Nisa suresi 135. ayet mesajı: adaletin toplumsal güvene etkisi ve haksızlığın sonuçları.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kader_kaza_sema()
    s[4]['gorsel'] = yasa_turleri_pano()
    s[5]['gorsel'] = ayet_yasa_kartlari()
    s[6]['gorsel'] = bahce_uc_bakis()
    s[7]['gorsel'] = ayet_analiz_zinciri()
    s[8]['gorsel'] = sifatlar_sema()
    s[9]['gorsel'] = gunluk_dil_karti()
    s[10]['gorsel'] = gozlem_arastirma_karti()
    s[12]['gorsel'] = nisa135_adalet_karti()
