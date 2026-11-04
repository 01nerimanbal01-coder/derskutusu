"""5. sınıf Din Kültürü ve Ahlak Bilgisi 6. hafta (Bir Sure Öğreniyorum: İhlas Suresi ve Anlamı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı Noto Sans 12 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ihlas_kimlik_karti():
    satirlar = [
        ('1 · Mushaf Sırası: Kur’an’ın 112. suresi', MAVI, MAVI_A),
        ('2 · İniş Yeri ve Ayet: Medine - 7 ayet', KIR, '#fdeaea'),
        ('3 · Ana Konu: Tevhid (Allah’ın birliği)', YES, YES_A),
        ('4 · Fazileti: Kur’an’ın üçte birine denk', MOR, MOR_A),
    ]
    ic = ''
    for i, (m, renk, arka) in enumerate(satirlar):
        y = 4 + i * 26
        ic += f'<rect x="6" y="{y}" width="348" height="23" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(16, y + 16, m, LAC, 'start', kalin=(i == 1))
    return svg(360, 110, ic, 'İhlas Suresi kimlik kartı numaralı satırları.', 20)


def okunus_anlam_tablosu():
    satirlar = [
        ('1. Ayet: K', 'De ki: O, Allah’tır, bir tektir.', MAVI, MAVI_A),
        ('2. Ayet: Allâhü’s-samed', 'Her şey O’na muhtaçtır.', YES, YES_A),
        ('3. Ayet: Lem yelid ve lem yûled', 'O doğurmamış ve doğmamıştır.', TUR, TUR_A),
        ('4. Ayet: Ve lem yekün lehû küfüven ehad', 'L', MOR, MOR_A),
    ]
    ic = ''
    for i, (sol, sag, renk, arka) in enumerate(satirlar):
        y = 4 + i * 26
        ic += f'<rect x="6" y="{y}" width="348" height="23" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(14, y + 16, f'{sol}  -  {sag}', LAC, 'start', kalin=(i in (0, 3)))
    return svg(360, 110, ic, 'İhlas Suresi okunuş ve anlam eşleştirme tablosu.', 20)


def dort_ayet_kartlari():
    kartlar = [
        ('1. Ayet', 'Kul hüvallâhü ehad', MAVI, MAVI_A),
        ('2. Ayet', 'Allâhü’s-samed', YES, YES_A),
        ('3. Ayet', 'Lem yelid ve lem yûled', TUR, TUR_A),
        ('4. Ayet', 'Ve lem yekün lehû...', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, okunus, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 36, okunus, LAC)
    return svg(360, 108, ic, 'İhlas Suresi dört ayetinin okunuş kartları.', 20)


def ihlas_davranis_panosu():
    ic = f'<rect x="6" y="6" width="170" height="92" rx="9" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(91, 24, 'A Kartı · Gösteriş', KIR, kalin=True)
    ic += yazi(91, 50, 'Herkes görsün ve', LAC)
    ic += yazi(91, 70, 'övsün diye yardım', LAC)
    ic += yazi(91, 88, 'yapmak (Riya)', KIR)

    ic += f'<rect x="184" y="6" width="170" height="92" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(269, 24, 'B Kartı · Samimiyet', YESIL_K, kalin=True)
    ic += yazi(269, 50, 'Yalnızca Allah rızası', LAC)
    ic += yazi(269, 70, 'için gizlice iyilik', LAC)
    ic += yazi(269, 88, 'yapmak (İhlas)', YESIL_K)
    return svg(360, 104, ic, 'Gösteriş ve ihlas davranış karşılaştırma kartları.', 20)


def karisik_ayet_sirasi():
    kartlar = [
        ('K Kartı', 'Lem yelid ve lem yûled.', TUR, TUR_A),
        ('L Kartı', 'Kul hüvallâhü ehad.', MAVI, MAVI_A),
        ('M Kartı', 'Ve lem yekün lehû küfüven ehad.', MOR, MOR_A),
        ('N Kartı', 'Allâhü’s-samed.', YES, YES_A),
    ]
    ic = ''
    for i, (kod, metin, renk, arka) in enumerate(kartlar):
        y = 4 + i * 26
        ic += f'<rect x="6" y="{y}" width="348" height="23" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(14, y + 16, f'{kod} · {metin}', LAC, 'start', kalin=True)
    return svg(360, 110, ic, 'Karışık sırada verilen İhlas Suresi ayet kartları.', 20)


def ehad_samed_panosu():
    ic = f'<rect x="6" y="6" width="170" height="92" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 24, 'el-Ehad', MAVI, kalin=True)
    ic += yazi(91, 48, 'Bir ve tek olan,', LAC)
    ic += yazi(91, 68, 'ortağı ve bölünmesi', LAC)
    ic += yazi(91, 88, 'olmayan Allah', MAVI)

    ic += f'<rect x="184" y="6" width="170" height="92" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(269, 24, 'es-Samed', TUR, kalin=True)
    ic += yazi(269, 48, 'Her şeyin muhtaç', LAC)
    ic += yazi(269, 68, 'olduğu, hiçbir şeye', LAC)
    ic += yazi(269, 88, 'muhtaç olmayan', TUR)
    return svg(360, 104, ic, 'el-Ehad ve es-Samed güzel isimlerinin anlam panosu.', 20)


def ayet_3_4_inceleme():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(180, 22, '3. Ayet · Lem yelid ve lem yûled', YESIL_K, kalin=True)
    ic += yazi(180, 40, 'O doğurmamış ve doğmamıştır (Ezelî ve ebedîdir).', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(180, 72, '4. Ayet · Ve lem yekün lehû küfüven ehad', MOR, kalin=True)
    ic += yazi(180, 90, 'O’nun hiçbir dengi, eşi ve benzeri yoktur.', LAC)
    return svg(360, 106, ic, 'İhlas Suresi 3 ve 4. ayetlerinin mesaj inceleme kartı.', 20)


def kuran_ucte_bir_semasi():
    kutular = [
        ('1. Bölüm', 'Tevhid (İnanç)', 'İhlas Suresi Özeti', YES, YES_A),
        ('2. Bölüm', 'İbadet ve Hüküm', 'Namaz, Oruç, Zekât', MAVI, MAVI_A),
        ('3. Bölüm', 'Ahlak ve Kıssalar', 'Güzel Davranışlar', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="90" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 24, bas, renk, kalin=True)
        ic += yazi(x + 56, 52, s1, LAC, kalin=True)
        ic += yazi(x + 56, 76, s2, LAC)
    return svg(360, 102, ic, 'Kur’an-ı Kerim’in üç ana konusu ve İhlas Suresi’nin yeri şeması.', 20)


def ibadet_kullanim_semasi():
    kartlar = [
        ('Beş Vakit Namazda', 'Fâtiha’dan sonra okunur', MAVI, MAVI_A),
        ('Hatim ve Mevlitlerde', '3 İhlas 1 Fâtiha okunur', YES, YES_A),
        ('Gece Yatmadan Önce', 'Felak ve Nâs ile okunur', TUR, TUR_A),
        ('Dua ve Zikirlerde', 'Tevhid bilinciyle okunur', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 36, alt, LAC)
    return svg(360, 108, ic, 'İhlas Suresi’nin günlük ibadet hayatında okunduğu yerler şeması.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ihlas_kimlik_karti()
    s[4]['gorsel'] = okunus_anlam_tablosu()
    s[5]['gorsel'] = dort_ayet_kartlari()
    s[6]['gorsel'] = ihlas_davranis_panosu()
    s[7]['gorsel'] = karisik_ayet_sirasi()
    s[8]['gorsel'] = ehad_samed_panosu()
    s[9]['gorsel'] = ayet_3_4_inceleme()
    s[11]['gorsel'] = kuran_ucte_bir_semasi()
    s[12]['gorsel'] = ibadet_kullanim_semasi()
