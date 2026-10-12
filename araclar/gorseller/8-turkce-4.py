"""8. sınıf Türkçe, 4. hafta: Atatürk Bizimle (dinleme süreci), fiilimsi kurma, cümleleri fiilimsiyle birleştirme.

Görseller yalnız MEB 8. sınıf Türkçe ders kitabındaki etkinliklerin yönergelerine dayanır (PDF sayfaları s28-s31); örnek cümleler kurgusaldır
ve özet metnindeki cümlelerle aynıdır.
Renk anlamı:
- Dinleme süreci: mavi = dinlemeden önce, turuncu = dinlerken, yeşil = dinledikten sonra.
- Fiilimsi kurma ve birleştirme: turuncu = isim-fiil, mavi = sıfat-fiil, yeşil = zarf-fiil (3. hafta görselleriyle aynı).
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _cip(x, y, w, h, metin, renk, boyut=12):
    s = RENK[renk][1]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{s}" stroke-width="1.6"/>'
            + _yazi(x + 12, y + h / 2 + 4.3, metin, boyut))


def dinleme_sureci():
    """Dinleme metni çalışmasının basamakları: önce, dinlerken, sonra (s28-s29)."""
    ic = ''
    asamalar = [
        ('mavi', ['Dinlemeden', 'önce'], 8, 48, ['1. Araştırmanı arkadaşlarınla paylaş']),
        ('turuncu', ['Dinlerken'], 64, 82, ['2. Dikkatini dağıtacak hareketlerden uzak dur', '3. Bilmediğin sözcükleri not al']),
        ('yesil', ['Dinledikten', 'sonra'], 154, 148, ['4. Sözcüklerin anlamını sözlükten bul', '5. Metni özetle', '6. Metne başlık öner',
                                                        '7. Sorulara sözlü cevap ver, görüş bildir']),
    ]
    for renk, ad, y, h, maddeler in asamalar:
        _, _, f = RENK[renk]
        ic += _kutu(8, y, 456, h, renk)
        by = y + (h - 40) / 2
        ic += f'<rect x="16" y="{by:g}" width="92" height="40" rx="10" class="{f}"/>'
        if len(ad) == 2:
            ic += _yazi(62, by + 17, ad[0], 12, 'g-b', True, 'middle') + _yazi(62, by + 32, ad[1], 12, 'g-b', True, 'middle')
        else:
            ic += _yazi(62, by + 25, ad[0], 12.5, 'g-b', True, 'middle')
        for k, m in enumerate(maddeler):
            ic += _cip(120, y + 10 + k * 34, 336, 26, m, renk)
    return svg(472, 310, ic, 'Dinleme çalışmasının basamakları. Dinlemeden önce, mavi: araştırmanı arkadaşlarınla paylaş. Dinlerken, turuncu: dikkatini dağıtacak hareketlerden uzak dur; bilmediğin sözcükleri not al. '
               'Dinledikten sonra, yeşil: sözcüklerin anlamını sözlükten bul, metni özetle, metne başlık öner, sorulara sözlü cevap ver, görüş bildir.')


def fiilimsi_kur():
    """Aynı fiil kökünden boşluğun görevine göre üç farklı fiilimsi: dinle- kökü (s30)."""
    ic = '<defs>' + ok_isareti('okT4k', 'g-s') + '</defs>'
    ic += '<rect x="186" y="6" width="100" height="30" rx="15" class="g-z"/><rect x="186" y="6" width="100" height="30" rx="15" class="g-c" stroke-width="2"/>'
    ic += _yazi(236, 26, 'dinle-', 14.5, 'g-y', True, 'middle')
    kartlar = [
        ('turuncu', 'İsim-fiil', 'Metni ___ için', 'dinlemek', 8),
        ('mavi', 'Sıfat-fiil', '___ metinde', 'dinlenen', 163),
        ('yesil', 'Zarf-fiil', 'Metni ___ not aldı', 'dinleyerek', 318),
    ]
    for renk, tur, boslk, sonuc, x in kartlar:
        _, s, f = RENK[renk]
        cx = x + 73
        ic += f'<line x1="236" y1="40" x2="{cx}" y2="64" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4k)"/>'
        ic += _kutu(x, 70, 146, 118, renk)
        ic += _yazi(cx, 94, tur, 13.5, f, True, 'middle')
        ic += f'<rect x="{x + 8}" y="104" width="130" height="28" rx="8" class="g-z"/><rect x="{x + 8}" y="104" width="130" height="28" rx="8" class="{s}" stroke-width="1.6"/>'
        ic += _yazi(cx, 122.4, boslk, 11, 'g-y', False, 'middle')
        ic += f'<rect x="{x + 8}" y="144" width="130" height="30" rx="8" class="{f}"/>'
        ic += _yazi(cx, 164, sonuc, 13.5, 'g-b', True, 'middle')
    return svg(472, 196, ic, 'Aynı fiil kökünden üç fiilimsi: dinle- kökü. Turuncu kart, isim-fiil: Metni boşluk için cümlesinde dinlemek gelir. Mavi kart, sıfat-fiil: boşluk metinde cümlesinde dinlenen gelir. '
               'Yeşil kart, zarf-fiil: Metni boşluk not aldı cümlesinde dinleyerek gelir.')


def birlestir():
    """İki cümleyi fiilimsiyle birleştirme: zaman, nasıl, amaç, niteleme (s31)."""
    satirlar = [
        ('yesil', 'Zaman', 'zarf-fiil', 'Ödevini bitirdi. Kitaplığa gitti.', [('Ödevini ', 0), ('bitirince', 1), (' kitaplığa gitti.', 0)]),
        ('yesil', 'Nasıl', 'zarf-fiil', 'Notlarına baktı. Başlığı buldu.', [('Notlarına ', 0), ('bakarak', 1), (' başlığı buldu.', 0)]),
        ('turuncu', 'Amaç', 'isim-fiil', 'Kitap alacaktı. Kütüphaneye gitti.', [('Kitap ', 0), ('almak', 1), (' için kütüphaneye gitti.', 0)]),
        ('mavi', 'Niteleme', 'sıfat-fiil', 'Metin yeni sözcük içeriyor. Metni dinledik.', [('Yeni sözcük ', 0), ('içeren', 1), (' metni dinledik.', 0)]),
    ]
    ic = ''
    for k, (renk, iliski, tur, iki, parcalar) in enumerate(satirlar):
        y = 8 + k * 70
        _, _, f = RENK[renk]
        ic += _kutu(8, y, 456, 62, renk)
        ic += f'<rect x="16" y="{y + 8}" width="96" height="46" rx="10" class="{f}"/>'
        ic += _yazi(64, y + 28, iliski, 13.5, 'g-b', True, 'middle')
        ic += _yazi(64, y + 44, tur, 11.5, 'g-b', False, 'middle')
        ic += _yazi(124, y + 26, iki, 12.5, 'g-y')
        tek = ''.join((f'<tspan font-weight="800" class="{f}">{m}</tspan>' if v else f'<tspan>{m}</tspan>') for m, v in parcalar)
        ic += f'<text x="124" y="{y + 48}" font-size="12.5" class="g-y"><tspan class="g-s">→ </tspan>{tek}</text>'
    return svg(472, 288, ic, 'İki cümleyi fiilimsiyle birleştirme. Yeşil satır, zaman: Ödevini bitirdi ve Kitaplığa gitti cümleleri, zarf-fiil bitirince ile Ödevini bitirince kitaplığa gitti olur. '
               'Yeşil satır, nasıl: Notlarına baktı ve Başlığı buldu cümleleri, zarf-fiil bakarak ile tek cümle olur. Turuncu satır, amaç: Kitap alacaktı ve Kütüphaneye gitti cümleleri, isim-fiil almak ile Kitap almak için kütüphaneye gitti olur. '
               'Mavi satır, niteleme: Metin yeni sözcük içeriyor ve Metni dinledik cümleleri, sıfat-fiil içeren ile Yeni sözcük içeren metni dinledik olur.')


def uygula(o):
    g = {'Dinlemeye hazırlan': dinleme_sureci(),
         'Fiilimsi kur': fiilimsi_kur(),
         'Cümleleri fiilimsiyle birleştir': birlestir()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
