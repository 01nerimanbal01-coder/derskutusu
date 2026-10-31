"""5. sınıf DKAB 7. hafta (İhlas Suresi’nin Mesajları, Tevhid İlkesi ve 1. Ünite Genel Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.0, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def ihlas_ayet_eslestirme_sema():
    satirlar = [
        ('1. Ayet: Kul hüvallâhü ehad', 'K = ? (Bir ve tek olma ilkesi)', MAVI, MAVI_A),
        ('2. Ayet: Allâhü’s-samed', 'L = ? (Hiçbir şeye muhtaç olmama)', TUR, TUR_A),
        ('3. Ayet: Lem yelid ve lem yûled', 'Ezelî ve ebedî olma (Doğurmama / doğmama)', YES, YES_A),
        ('4. Ayet: Ve lem yekün lehû küfüven ehad', 'M = ? (Hiçbir varlığın O’na denk olmaması)', MOR, MOR_A),
    ]
    ic = ''
    for i, (sol, sag, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 54
        ic += f'<rect x="{x}" y="{y}" width="286" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="7" height="46" rx="3.5" fill="{renk}"/>'
        ic += yazi(x + 16, y + 18, sol, 10.6, renk, 'start')
        ic += yazi(x + 16, y + 36, sag, 10.1, LAC, 'start', ince=True)
    return svg(600, 116, ic, 'İhlas suresinin dört ayetinin okunuşu ve K, L, M temel mesaj kutuları.', 22)


def unite_kavram_panosu():
    satirlar = [
        ('1. Satır · El-Hâlık', 'Evreni ve tüm varlıkları yoktan, ölçüyle yaratan', YES, YES_A),
        ('2. Satır · El-Alîm', 'Gizli ve açık, geçmiş ve gelecek her şeyi bilen', MAVI, MAVI_A),
        ('3. Satır · Es-Samed', 'Yalnızca bulutlardan yağmur yağdıran (Hatalı)', KIR, '#fdeaea'),
        ('4. Satır · El-Kâdir', 'İstediği her şeyi yaratmaya sonsuz gücü yeten', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 54
        ic += f'<rect x="{x}" y="{y}" width="286" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="7" height="46" rx="3.5" fill="{renk}"/>'
        ic += yazi(x + 16, y + 18, bas, 10.7, renk, 'start')
        ic += yazi(x + 16, y + 36, acik, 10.1, LAC, 'start', ince=True)
    return svg(600, 116, ic, '1. Ünite güzel isimler panosu: 1. El-Hâlık, 2. El-Alîm, 3. Es-Samed (hatalı), 4. El-Kâdir.', 22)


def dort_ayet_esma_karti():
    kartlar = [
        ('1. Kart · En’âm 59', '“O’nun bilgisi dışında bir', 'yaprak bile düşmez.”', MAVI, MAVI_A),
        ('2. Kart · İhlas 2', '“Allah Samed’dir (Her şey', 'O’na muhtaçtır).”', TUR, TUR_A),
        ('3. Kart · Bakara 117', '“Bir işin olmasını dilerse', 'sadece ‘Ol!’ der, oluverir.”', MOR, MOR_A),
        ('4. Kart · İhlas 1', '“De ki: O, Allah’tır,', 'bir tektir.”', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="6" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 23, bas, 10.6, renk)
        ic += f'<line x1="{x + 12}" y1="31" x2="{x + 124}" y2="31" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 68, 70, s2, 10.0, LAC, ince=True)
    return svg(600, 98, ic, 'Dört ayet kartı: 1. En’âm 59, 2. İhlas 2, 3. Bakara 117, 4. İhlas 1.', 22)


def enbiya_duzen_semasi():
    ic = f'<rect x="8" y="6" width="276" height="88" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(146, 24, 'İki Farklı Yönetici Olsaydı', 10.8, KIR)
    ic += yazi(146, 46, 'Birbiriyle çelişen zıt kurallar konurdu.', 10.1, LAC, ince=True)
    ic += yazi(146, 64, 'Okulda ve evrende kargaşa çıkardı;', 10.1, LAC, ince=True)
    ic += yazi(146, 80, 'mevcut düzen tamamen bozulurdu.', 10.1, KIR)

    ic += f'<line x1="288" y1="50" x2="312" y2="50" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="316" y="6" width="276" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(454, 24, 'Enbiyâ Suresi 22. Ayet Delili', 10.8, YESIL_K)
    ic += yazi(454, 46, 'Evrende milyarlarca yıldır kusursuz', 10.1, LAC, ince=True)
    ic += yazi(454, 64, 'bir uyum ve ölçü devam etmektedir.', 10.1, LAC, ince=True)
    ic += yazi(454, 80, 'Yaratıcı bir ve tektir (Tevhid).', 10.2, YESIL_K)
    return svg(600, 100, ic, 'İki yönetici örneği ve Enbiyâ suresi 22. ayet tevhid delili karşılaştırma şeması.', 22)


def ihlas_okunus_zinciri():
    kartlar = [
        ('1. Ayet', 'Allah bir ve tektir', MAVI, MAVI_A),
        ('2. Ayet', 'Her şey O’na muhtaçtır', TUR, TUR_A),
        ('3. Ayet', 'Doğurmamış, doğmamıştır', MOR, MOR_A),
        ('4. Ayet', 'Hiçbir dengi yoktur', YES, YES_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="24" rx="6" fill="{YESIL_K}"/>'
    ic += yazi(300, 22, 'Besmele: Bismillâhirrahmânirrahîm', 10.8, '#fff')
    for i, (ust, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="36" width="136" height="58" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 55, ust, 10.6, renk)
        ic += yazi(x + 68, 76, alt, 9.2, LAC, ince=True)
    return svg(600, 100, ic, 'Besmele ve İhlas suresinin dört ayetinin anlam sırası zinciri.', 22)


def esma_davranis_kartlari():
    kutular = [
        ('El-Alîm Bilinci', 'Allah’ın her şeyi bildiğini', 'düşünerek dürüst yaşar.', MAVI, MAVI_A),
        ('Es-Semî Bilinci', 'Her sözün işitildiğini bilir;', 'kırıcı sözden uzak durur.', TUR, TUR_A),
        ('El-Basîr Bilinci', 'Kimse yokken bile Allah’ın', 'gördüğünü bilip iyilik yapar.', YES, YES_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 23, 'Allah’ın Güzel İsimlerini İçselleştiren Öğrencinin Davranış İlkeleri', 11.0, LAC)
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, bas, 10.6, renk)
        ic += yazi(x + 90, 65, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 90, 80, s2, 10.0, LAC, ince=True)
    return svg(600, 108, ic, 'El-Alîm, Es-Semî ve El-Basîr bilincinin davranış ilkeleri şeması.', 22)


def evren_duzen_gorseli():
    kutular = [
        ('İdeal Mesafe', 'Dünya’nın Güneş’e uzaklığı', 'canlı yaşamına tam uygundur.', TUR, TUR_A),
        ('Su Döngüsü', 'Buharlaşan su yağış olarak', 'yeryüzüne ölçüyle döner.', MAVI, MAVI_A),
        ('Mevsim Düzeni', 'Gece-gündüz ve mevsimler', 'şaşmadan birbirini izler.', YES, YES_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 23, 'Evrendeki Mükemmel Ölçü ve Düzen (El-Hâlık)', 11.0, LAC)
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, bas, 10.6, renk)
        ic += yazi(x + 90, 65, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 90, 80, s2, 10.0, LAC, ince=True)
    return svg(600, 108, ic, 'Evrendeki düzen örnekleri: ideal mesafe, su döngüsü ve mevsim düzeni.', 22)


def ihlas_riya_karti():
    ic = f'<rect x="8" y="6" width="282" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(149, 24, 'Zeynep’in Tutumu (İhlas)', 10.8, YESIL_K)
    ic += yazi(149, 46, 'Harçlığından ayırdığı yardımı kimseye', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'söylemeden ihtiyaç sahibine ulaştırır.', 10.1, LAC, ince=True)
    ic += yazi(149, 80, 'Yalnız Allah’ın rızasını gözetir.', 10.2, YESIL_K)

    ic += f'<rect x="310" y="6" width="282" height="86" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(451, 24, 'Kaan’ın Tutumu (Gösteriş / Riya)', 10.8, KIR)
    ic += yazi(451, 46, 'Yaptığı yardımı herkesin duyması ve', 10.1, LAC, ince=True)
    ic += yazi(451, 63, 'kendisini övmesi için sınıfta anlatır.', 10.1, LAC, ince=True)
    ic += yazi(451, 80, 'Başkalarının beğenisini ön planda tutar.', 10.2, KIR)
    return svg(600, 98, ic, 'Zeynep’in samimi (ihlaslı) tutumu ile Kaan’ın gösterişçi tutumunun karşılaştırma kartları.', 22)


def rahman_rahim_karti():
    ic = f'<rect x="8" y="6" width="584" height="24" rx="6" fill="{ALTIN}"/>'
    ic += yazi(300, 22, 'Besmelede Geçen İki Güzel İsim: Er-Rahmân ve Er-Rahîm', 10.8, '#fff')

    ic += f'<rect x="8" y="36" width="282" height="60" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(149, 53, 'Er-Rahmân', 10.8, MAVI)
    ic += yazi(149, 70, 'Dünyada inanan-inanmayan bütün', 10.0, LAC, ince=True)
    ic += yazi(149, 85, 'canlılara ayrım yapmadan rızık verir.', 10.0, LAC, ince=True)

    ic += f'<rect x="310" y="36" width="282" height="60" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(451, 53, 'Er-Rahîm', 10.8, YESIL_K)
    ic += yazi(451, 70, 'Ahirette yalnızca iman edip güzel', 10.0, LAC, ince=True)
    ic += yazi(451, 85, 'davranış yapan kullarını ödüllendirir.', 10.0, LAC, ince=True)
    return svg(600, 102, ic, 'Besmelede geçen Er-Rahmân ve Er-Rahîm isimlerinin kapsam karşılaştırma kartları.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ihlas_ayet_eslestirme_sema()
    s[4]['gorsel'] = unite_kavram_panosu()
    s[5]['gorsel'] = dort_ayet_esma_karti()
    s[6]['gorsel'] = enbiya_duzen_semasi()
    s[7]['gorsel'] = ihlas_okunus_zinciri()
    s[8]['gorsel'] = esma_davranis_kartlari()
    s[9]['gorsel'] = evren_duzen_gorseli()
    s[10]['gorsel'] = ihlas_riya_karti()
    s[12]['gorsel'] = rahman_rahim_karti()
