"""6. sınıf Arapça, 2. hafta: dinleme metni, anlama soruları, kameri ve şemsi kelime listeleri.

Görseller yalnız MEB 6. sınıf Arapça ders kitabındaki bilgilerle çizilir (kitap s. 12-22).
Renk anlamı: mavi = erkek aile bireyleri / kameri harfler (ay), turuncu = kadın aile bireyleri /
şemsi harfler (güneş), yeşil = doğru biçim. Arapça yazılar ortalanır (sağdan sola okunuş bozulmaz);
cümle sonu noktaları görselde yazılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _ar(x, y, metin, boy=16, sinif='g-y', kalin=False):
    k = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def aile_tanitimi():
    """Yasemin'in dinleme metni (s. 14): dört cümle, aynı kalıp; erkek mavi, kadın turuncu."""
    ic = _ar(236, 26, 'مَرْحَبًا أَنا ياسَمين، هَذِهِ عائِلَتي', 16, kalin=True)
    ic += '<text x="236" y="44" text-anchor="middle" font-size="12" class="g-s">Merhaba, ben Yasemin; bu benim ailem</text>'
    satir = [('mavi', 'هَذا جَدّي وَهُوَ طَبّاخ', 'Bu dedem, o aşçıdır'),
             ('turuncu', 'وَهَذِهِ جَدَّتي زَهْرَة وَهِيَ مُتَقاعِدَة', 'Bu ninem Zehra, o emeklidir'),
             ('mavi', 'هَذا والِدي أَحْمَد وَهُوَ مُحامٍ', 'Bu babam Ahmet, o avukattır'),
             ('turuncu', 'هَذِهِ والِدَتي فاطِمَة وَهِيَ مُعَلِّمَة', 'Bu annem Fatma, o öğretmendir')]
    for k, (renk, ar, tr) in enumerate(satir):
        y = 56 + k * 42
        ic += _kutu(8, y, 456, 36, renk)
        ic += _ar(330, y + 24, ar, 16)
        ic += f'<text x="20" y="{y + 23}" font-size="12" class="g-y">{tr}</text>'
    ic += '<rect x="8" y="228" width="456" height="30" rx="8" class="g-z"/>'
    ic += '<text x="236" y="248" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">Kalıp: işaret zamiri + akraba (+ ad) + وَهُوَ / وَهِيَ + meslek</text>'
    return svg(472, 266, ic, 'Yasemin ailesini tanıtıyor: Merhaba, ben Yasemin, bu benim ailem. Bu dedem, o aşçıdır. '
               'Bu ninem Zehra, o emeklidir. Bu babam Ahmet, o avukattır. Bu annem Fatma, o öğretmendir. '
               'Kalıp: işaret zamiri, akraba adı, ve o zamiri, meslek.')


def soru_cevap():
    """Dinlediğini anlama soruları (s. 15): soru kelimesi, soru ve cevap."""
    ic = '<text x="350" y="24" text-anchor="middle" font-size="12.5" font-weight="800" class="g-s">Soru</text>'
    ic += '<text x="164" y="24" text-anchor="middle" font-size="12.5" font-weight="800" class="g-s">Cevap</text>'
    ic += '<text x="50" y="24" text-anchor="middle" font-size="12.5" font-weight="800" class="g-s">Soru türü</text>'
    satir = [('مَنِ الْمُتَقاعِدَة؟', 'الْجَدَّة زَهْرَة', 'مَن', 'kişi', 'mavi'),
             ('ما اسْمُ الْوالِد؟', 'أَحْمَد', 'ما اسْم', 'ad', 'yesil'),
             ('هَلِ الْوالِدَة مُحامِيَة؟', 'لا، هِيَ مُعَلِّمَة', 'هَل', 'evet / hayır', 'turuncu')]
    for k, (soru, cevap, sk, tur, renk) in enumerate(satir):
        y = 36 + k * 50
        ic += _kutu(236, y, 228, 40, renk)
        ic += _ar(350, y + 26, soru, 16)
        ic += f'<rect x="100" y="{y}" width="128" height="40" rx="12" class="g-z"/>'
        ic += _ar(164, y + 26, cevap, 16)
        ic += f'<rect x="8" y="{y}" width="84" height="40" rx="12" class="{RENK[renk][2]}"/>'
        ic += _ar(50, y + 18, sk, 14, 'g-b', kalin=True)
        ic += f'<text x="50" y="{y + 33}" text-anchor="middle" font-size="11.5" class="g-b">{tur}</text>'
    ic += '<text x="236" y="200" text-anchor="middle" font-size="12" class="g-s">هَل sorusuna “hayır” deniyorsa doğru bilgi eklenir</text>'
    return svg(472, 210, ic, 'Soru ve cevap: Emekli olan kim? Nine Zehra. Babanın adı ne? Ahmet. Anne avukat mı? '
               'Hayır, o öğretmendir. Soru türleri: men kişi, ma ism ad, hel evet-hayır.')


def _liste(ic, y0, kelimeler, renk):
    """İki sütun, yedi satır: kelime ← ال'lı biçim (sağdan sola okunur)."""
    for i, (yalin, elli) in enumerate(kelimeler):
        x = 8 + (i // 7) * 232
        y = y0 + (i % 7) * 30
        ic += _kutu(x, y, 224, 26, renk, rx=8)
        ic += _ar(x + 112, y + 18, f'{yalin} ← {elli}', 15)
    return ic


def kameri_listesi():
    """Belirli isim (s. 17) ve kameri harfli on dört kelime (s. 18)."""
    ic = _kutu(8, 8, 224, 50, 'mavi')
    ic += _ar(120, 28, 'بَيْت', 16, kalin=True)
    ic += '<text x="120" y="48" text-anchor="middle" font-size="12" class="g-y">herhangi bir ev</text>'
    ic += _kutu(240, 8, 224, 50, 'mavi')
    ic += _ar(352, 28, 'الْبَيْت', 16, kalin=True)
    ic += '<text x="352" y="48" text-anchor="middle" font-size="12" class="g-y">o bilinen ev (belirli)</text>'
    ic += '<text x="236" y="80" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">☾ Kameri harfler: lam sükûnlu okunur (el-…)</text>'
    kelime = [('أَرْنَب', 'الْأَرْنَب'), ('بُرْتُقال', 'الْبُرْتُقال'), ('جَمَل', 'الْجَمَل'), ('حِصان', 'الْحِصان'),
              ('خُبْز', 'الْخُبْز'), ('عِنَب', 'الْعِنَب'), ('غُرْفَة', 'الْغُرْفَة'), ('فُرْشاة', 'الْفُرْشاة'),
              ('قِطَّة', 'الْقِطَّة'), ('كُرَة', 'الْكُرَة'), ('مِرْآة', 'الْمِرْآة'), ('وَرْدَة', 'الْوَرْدَة'),
              ('هاتِف', 'الْهاتِف'), ('يَخْت', 'الْيَخْت')]
    ic = _liste(ic, 90, kelime, 'mavi')
    ic += '<text x="236" y="314" text-anchor="middle" font-size="12" class="g-s">Kameri harf dizisi: ا ب ج ح خ ع غ ف ق ك م ه و ي</text>'
    return svg(472, 324, ic, 'Belirli isim: beyt herhangi bir ev, el-beyt o bilinen ev. Kameri harfli on dört kelime: '
               'el-arnab, el-burtukal, el-cemel, el-hisan, el-hubz, el-ineb, el-gurfe, el-furşat, el-kıtta, el-kura, '
               'el-mirat, el-verde, el-hatif, el-yaht. Kameri harf dizisi: elif be cim ha hı ayn gayn fe kaf kef mim he vav ye.')


def semsi_listesi():
    """Tilmiz tabelası (s. 19) ve şemsi harfli on dört kelime (s. 20)."""
    ic = '<defs>' + ok_isareti('okA62s', 'g-s') + '</defs>'
    ic += '<rect x="196" y="8" width="80" height="34" rx="10" class="g-z"/>'
    ic += '<rect x="196" y="8" width="80" height="34" rx="10" class="g-c" stroke-width="1.5"/>'
    ic += _ar(236, 31, 'تِلْميذ', 16, kalin=True)
    ic += '<line x1="190" y1="25" x2="150" y2="25" class="g-c" stroke-width="2" marker-end="url(#okA62s)"/>'
    ic += '<line x1="282" y1="25" x2="322" y2="25" class="g-c" stroke-width="2" marker-end="url(#okA62s)"/>'
    ic += '<rect x="8" y="8" width="136" height="34" rx="10" class="g-s"/>'
    ic += _ar(84, 31, 'اَلْتِلْميذ', 16, 'g-b')
    ic += '<text x="22" y="31" font-size="16" font-weight="800" class="g-b">✗</text>'
    ic += _kutu(328, 8, 136, 34, 'yesil', rx=10)
    ic += _ar(390, 31, 'اَلتِّلْميذ', 16, 'g-yf', kalin=True)
    ic += '<text x="448" y="31" text-anchor="middle" font-size="16" font-weight="800" class="g-yf">✓</text>'
    ic += '<text x="76" y="60" text-anchor="middle" font-size="12" class="g-s">lam okunarak: yanlış</text>'
    ic += '<text x="396" y="60" text-anchor="middle" font-size="12" class="g-yf">lam okunmaz, ت şeddeli: et-tilmîz</text>'
    ic += '<text x="236" y="84" text-anchor="middle" font-size="12.5" font-weight="800" class="g-tf">☀ Şemsi harfler: lam yazılır, okunmaz; sonraki harf şeddeli</text>'
    kelime = [('تَنّورَة', 'التَّنّورَة'), ('ثَوْب', 'الثَّوْب'), ('دَفْتَر', 'الدَّفْتَر'), ('ذُرَة', 'الذُّرَة'),
              ('رُمّان', 'الرُّمّان'), ('زَرافَة', 'الزَّرافَة'), ('سَفينَة', 'السَّفينَة'), ('شَجَرَة', 'الشَّجَرَة'),
              ('صَفّ', 'الصَّفّ'), ('ضِفْدَع', 'الضِّفْدَع'), ('طائِرَة', 'الطّائِرَة'), ('ظَرْف', 'الظَّرْف'),
              ('لَوْز', 'اللَّوْز'), ('نَظّارَة', 'النَّظّارَة')]
    ic = _liste(ic, 94, kelime, 'turuncu')
    ic += '<text x="236" y="318" text-anchor="middle" font-size="12" class="g-s">Şemsi harf dizisi: ت ث د ذ ر ز س ش ص ض ط ظ ل ن</text>'
    return svg(472, 328, ic, 'Tilmiz kelimesine el takısı: el-tilmiz lam okunarak yanlış, et-tilmiz lam okunmadan ve te şeddeli doğru. '
               'Şemsi harfli on dört kelime: et-tennura, es-sevb, ed-defter, ez-zura, er-rumman, ez-zerafe, es-sefine, '
               'eş-şecere, es-saff, ed-dıfda, et-taire, ez-zarf, el-levz, en-nezzara. '
               'Şemsi harf dizisi: te se dal zel ra ze sin şın sad dad tı zı lam nun.')


def uygula(o):
    g = {'Dinleme metni: Yasemin ailesini tanıtıyor': aile_tanitimi(),
         'Dinlediğini anlama: {ar:مَن}, {ar:ما}, {ar:هَل} soruları': soru_cevap(),
         'Telaffuz: {ar:ال} ile belirli isim ve kameri harfler': kameri_listesi(),
         'Telaffuz: şemsi harfte lam yazılır, okunmaz': semsi_listesi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
