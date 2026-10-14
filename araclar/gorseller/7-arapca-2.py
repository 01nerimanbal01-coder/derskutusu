"""7. sınıf Arapça, 2. hafta: okuma metni, «مَنْ / ماذا» soruları, fiilin baş harfi, şeddeli meslek adları.

Görseller yalnız MEB 7. sınıf Arapça ders kitabındaki bilgilerle çizilir (kitap s. 16-20).
Renk anlamı: mavi = erkek, turuncu = kadın, yeşil = konuşanın kendisi / yapılan iş.
Arapça yazılar ortalanır (sağdan sola okunuş bozulmaz); cümle sonu noktaları görselde yazılmaz.
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


def _tr(x, y, metin, boy=12, sinif='g-y', kalin=False, orta=False):
    k = ' font-weight="700"' if kalin else ''
    a = ' text-anchor="middle"' if orta else ''
    return f'<text x="{x}" y="{y}"{a} font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def aile_tablosu():
    """Okuma metni (s. 16): Muhammed ve ailesindeki altı kişi; kişi + meslek ve yaptığı iş."""
    ic = _ar(236, 26, 'أَنا وَأُسْرَتي', 17, kalin=True)
    ic += _tr(236, 44, 'Ben ve ailem', 12, 'g-s', orta=True)
    satir = [('yesil', 'أَنا مُهَنْدِس مِعْمارِيّ', 'Ben (Muhammed): ev tasarlarım'),
             ('turuncu', 'أُمّي مُمَرِّضَة', 'Annem: hastalara hizmet eder'),
             ('mavi', 'أَبي شُرْطِيّ', 'Babam: vatandaşları korur'),
             ('mavi', 'أَخي الكَبير مُدَرِّس', 'Ağabeyim: ortaokulda öğretmen'),
             ('mavi', 'أَخي الصَّغير طَيّار', 'Küçük kardeşim: özel şirkette'),
             ('turuncu', 'أُخْتي الكَبيرَة خَيّاطَة', 'Ablam: güzel giysiler diker'),
             ('turuncu', 'أُخْتي الصَّغيرَة طَبّاخَة', 'Küçük kız kardeşim: yemek pişirir')]
    for k, (renk, ar, tr) in enumerate(satir):
        y = 56 + k * 40
        ic += _kutu(8, y, 456, 34, renk)
        ic += _ar(364, y + 23, ar, 15)
        ic += _tr(20, y + 22, tr)
    return svg(472, 340, ic, 'Muhammed ailesini tanıtıyor. Ben mimar mühendisim, ev tasarlarım. Annem hemşire, hastalara hizmet eder. '
               'Babam polis, vatandaşları korur. Ağabeyim ortaokulda öğretmen. Küçük erkek kardeşim pilot, özel şirkette çalışır. '
               'Ablam terzi, güzel giysiler diker. Küçük kız kardeşim aşçı, yemek pişirir. Erkekler mavi, kadınlar turuncu.')


def soru_cevap():
    """Diyalog ve anlama soruları (s. 17-18): مَنْ sorusu meslekle, ماذا sorusu yapılan işle cevaplanır."""
    ic = '<defs>' + ok_isareti('okA72s', 'g-s') + '</defs>'
    ic += _tr(356, 22, 'Soru', 12.5, 'g-s', kalin=True, orta=True)
    ic += _tr(164, 22, 'Cevap', 12.5, 'g-s', kalin=True, orta=True)
    ic += _tr(48, 22, 'Cevap türü', 12.5, 'g-s', kalin=True, orta=True)
    satir = [('مَنْ يَبيعُ اللَّحْمَ؟', 'الجَزّار', 'meslek', 'mavi'),
             ('مَنْ يُصَلِّحُ السَّيّاراتِ؟', 'المُصَلِّح', 'meslek', 'mavi'),
             ('ماذا يَفْعَلُ الجَزّارُ؟', 'يَبيعُ اللَّحْمَ', 'iş', 'yesil'),
             ('ماذا تَفْعَلُ المُذيعَةُ؟', 'تُقَدِّمُ الأَخْبارَ', 'iş', 'turuncu')]
    for k, (soru, cevap, tur, renk) in enumerate(satir):
        y = 34 + k * 50
        ic += _kutu(254, y, 210, 40, renk)
        ic += _ar(359, y + 26, soru, 15)
        ic += f'<line x1="250" y1="{y + 20}" x2="238" y2="{y + 20}" class="g-c" stroke-width="2" marker-end="url(#okA72s)"/>'
        ic += f'<rect x="96" y="{y}" width="136" height="40" rx="12" class="g-z"/>'
        ic += f'<rect x="96" y="{y}" width="136" height="40" rx="12" class="g-c" stroke-width="1.5"/>'
        ic += _ar(164, y + 26, cevap, 15, kalin=True)
        ic += _tr(48, y + 25, tur, 12.5, kalin=True, orta=True)
    ic += '<rect x="8" y="236" width="456" height="30" rx="8" class="g-z"/>'
    ic += _tr(236, 256, 'مَنْ (kim?) → kişi ya da meslek  ·  ماذا (ne?) → yapılan iş', 14, kalin=True, orta=True)
    return svg(472, 274, ic, 'Soru kelimesi cevabı belirler. Eti kim satar? Kasap. Arabaları kim tamir eder? Tamirci. '
               'Kasap ne yapar? Et satar. Spiker ne yapar? Haberleri sunar. Kim sorusu meslekle, ne sorusu yapılan işle cevaplanır.')


def fiil_basi():
    """Alıştırma (s. 19): fiilin baş harfi kimi anlattığını gösterir; ما مِهْنَتُهُ / ما مِهْنَتُها."""
    sutun = [(316, 'yesil', 'أَـ', 'ben', 'أَفْحَصُ', 'أُصَمِّمُ'),
             (164, 'mavi', 'يَـ / يُـ', 'o (erkek)', 'يُطْفِئُ', 'يَعْمَلُ'),
             (12, 'turuncu', 'تَـ / تُـ', 'o (kadın)', 'تَخْدِمُ', 'تَطْبُخُ')]
    ic = ''
    for x, renk, harf, kim, f1, f2 in sutun:
        yazi = RENK[renk][2]
        ic += _kutu(x, 8, 144, 136, renk)
        ic += _ar(x + 72, 40, harf, 22, yazi, kalin=True)
        ic += _tr(x + 72, 62, kim, 13, kalin=True, orta=True)
        ic += f'<rect x="{x + 14}" y="74" width="116" height="58" rx="8" class="g-z"/>'
        ic += _ar(x + 72, 98, f1, 16)
        ic += _ar(x + 72, 122, f2, 16)
    ic += _kutu(240, 156, 224, 66, 'mavi')
    ic += _ar(352, 182, 'ما مِهْنَتُهُ؟', 16, kalin=True)
    ic += _ar(352, 208, 'هُوَ رَجُلُ الإِطْفاء', 15)
    ic += _kutu(8, 156, 224, 66, 'turuncu')
    ic += _ar(120, 182, 'ما مِهْنَتُها؟', 16, kalin=True)
    ic += _ar(120, 208, 'هِيَ مُضيفَة', 15)
    return svg(472, 230, ic, 'Fiilin baş harfi: elif ile başlayan fiil ben, ye ile başlayan fiil o erkek, te ile başlayan fiil o kadın. '
               'Örnekler: muayene ederim, tasarlarım; söndürür, çalışır; hizmet eder, pişirir. '
               'Onun mesleği ne? O itfaiyeci. Onun (kadının) mesleği ne? O hostes.')


def bulmaca_kutulari():
    """Bulmaca (s. 20): şeddeli harf tek kutuya bir kez yazılır; sondaki ة bir kutu sayılır."""
    satir = [('طَيّار', ['ط', 'ي', 'ا', 'ر'], 1, '4 kutu'),
             ('نَجّار', ['ن', 'ج', 'ا', 'ر'], 1, '4 kutu'),
             ('مُذيعَة', ['م', 'ذ', 'ي', 'ع', 'ة'], None, '5 kutu')]
    ic = ''
    for k, (soz, harfler, sedde, sayi) in enumerate(satir):
        y = 10 + k * 56
        ic += f'<rect x="372" y="{y}" width="92" height="44" rx="10" class="g-z"/>'
        ic += f'<rect x="372" y="{y}" width="92" height="44" rx="10" class="g-c" stroke-width="1.5"/>'
        ic += _ar(418, y + 29, soz, 18, kalin=True)
        for j, h in enumerate(harfler):  # sağdan sola dizilir
            x = 310 - j * 48
            renk = 'turuncu' if j == sedde else ('yesil' if h == 'ة' else 'mavi')
            ic += _kutu(x, y + 2, 40, 40, renk, rx=6)
            ic += _ar(x + 20, y + 29, h, 19, RENK[renk][2], kalin=True)
        ic += _tr(48, y + 27, sayi, 13, kalin=True, orta=True)
    ic += '<rect x="8" y="178" width="456" height="30" rx="8" class="g-z"/>'
    ic += _tr(236, 198, 'Şeddeli harf (turuncu) bir kez yazılır; sondaki ة (yeşil) bir kutudur', 12.5, kalin=True, orta=True)
    return svg(472, 216, ic, 'Bulmaca kutuları: tayyar dört kutu, ta ye elif ra; neccar dört kutu, nun cim elif ra; '
               'müzia beş kutu, mim zel ye ayn te. Şeddeli harf bir kez yazılır, sondaki yuvarlak te bir kutudur.')


def uygula(o):
    g = {'Okuma metni: Muhammed ailesini tanıtıyor': aile_tablosu(),
         'Soru kelimesi cevabı belirler: {ar:مَنْ} ve {ar:ماذا}': soru_cevap(),
         'Yapılan işten mesleği bulma': fiil_basi(),
         'Şeddeli meslek adları ve bulmaca': bulmaca_kutulari()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
