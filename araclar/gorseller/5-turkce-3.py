"""5. sınıf Türkçe, 3. hafta: Topsuz Basketbol Oyunu (tahmin, anlam, nokta, ses kullanımı).

Görseller yalnız MEB 5. sınıf Türkçe ders kitabındaki bilgilerle çizilir (kitap s. 18-33; PDF sayfaları s19-s33).
Renk anlamı:
- Tahmin akışı: mavi = okumadan önce, turuncu = 1 numaralı yer, yeşil = 2 numaralı yer, mor = okuma bitince.
- Gerçek ve hayal: mavi = gerçekte yaşanan, turuncu = gerçekte yaşanmayan.
- Noktanın görevleri: mavi = cümle sonu, turuncu = kısaltma, yeşil = sıra bildiren sayı, mor = tarih.
- Ses kullanımı: turuncu = ok yukarı (ses yükselir), mavi = ok aşağı (ses alçalır).
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _hap(x, y, w, h, metin, renk, boyut=13):
    """Başlık hapı: açık zemin, renkli çerçeve; yazı ortalanır."""
    return (_kutu(x, y, w, h, renk, rx=h // 2)
            + f'<text x="{x + w / 2:g}" y="{y + h / 2 + 4.5:g}" text-anchor="middle" font-size="{boyut}" '
              f'font-weight="800" class="{RENK[renk][2]}">{metin}</text>')


def tahmin_akisi():
    """Okurken tahmin: okumadan önce, 1 ve 2 numaralı yerler, okuma bitince (kitap s. 19-27)."""
    ic = '<defs>' + ok_isareti('okT53', 'g-s') + '</defs>'
    kutular = [
        (12, 12, 'mavi', 'Okumadan önce', ['Başlıktan ilk tahmini', 'gerekçesiyle birlikte', 'yaz.']),
        (256, 12, 'turuncu', '1 numaralı yer', ['Moni’nin fikir bulduğu', 'cümleden sonra dur,', 'sonrasını tahmin et.']),
        (256, 156, 'yesil', '2 numaralı yer', ['İnci’nin yardım', 'çağrısından sonra dur,', 'yeni tahmin yaz.']),
        (12, 156, 'mor', 'Okuma bitince', ['Tahminlerin gerekçesini', 've doğruluğunu', 'değerlendir.']),
    ]
    for x, y, renk, baslik, satirlar in kutular:
        ic += _kutu(x, y, 204, 104, renk)
        ic += f'<text x="{x + 14}" y="{y + 28}" font-size="14.5" font-weight="800" class="{RENK[renk][2]}">{baslik}</text>'
        for i, s in enumerate(satirlar):
            ic += f'<text x="{x + 14}" y="{y + 54 + i * 20}" font-size="12.5" class="g-y">{s}</text>'
    ic += '<line x1="222" y1="64" x2="250" y2="64" class="g-c" stroke-width="2.5" marker-end="url(#okT53)"/>'
    ic += '<line x1="358" y1="122" x2="358" y2="150" class="g-c" stroke-width="2.5" marker-end="url(#okT53)"/>'
    ic += '<line x1="250" y1="208" x2="222" y2="208" class="g-c" stroke-width="2.5" marker-end="url(#okT53)"/>'
    ic += '<text x="236" y="292" text-anchor="middle" font-size="12.5" class="g-s">Her durakta tahmin ve gerekçe birlikte yazılır.</text>'
    return svg(472, 302, ic, 'Okurken tahmin akışı: okumadan önce başlıktan ilk tahmini gerekçesiyle yaz; 1 numaralı yerde, '
               'Moni’nin fikir bulduğu cümleden sonra dur ve sonrasını tahmin et; 2 numaralı yerde, İnci’nin yardım çağrısından '
               'sonra dur ve yeni tahmin yaz; okuma bitince tahminlerin gerekçesini ve doğruluğunu değerlendir.')


def gercek_hayal():
    """Gerçekte yaşananlar ve yaşanmayanlar (kitap s. 28-29, 31)."""
    ic = _hap(8, 8, 222, 32, 'Gerçekte yaşanan', 'mavi')
    ic += _hap(242, 8, 222, 32, 'Gerçekte yaşanmayan', 'turuncu')
    sol = ['Neşeli koşuşturma', 'Moni’nin siren sesi']
    sag = ['Ambulans', 'Sedye', 'Buz ve sargı bezi', 'Satürn’deki hastane']
    for k, t in enumerate(sol):
        y = 50 + k * 40
        ic += _kutu(8, y, 222, 32, 'mavi', rx=10)
        ic += f'<text x="22" y="{y + 21}" font-size="12.5" class="g-y">{t}</text>'
    for k, t in enumerate(sag):
        y = 50 + k * 40
        ic += _kutu(242, y, 222, 32, 'turuncu', rx=10)
        ic += f'<text x="256" y="{y + 21}" font-size="12.5" class="g-y">{t}</text>'
    ic += '<text x="236" y="228" text-anchor="middle" font-size="13" font-weight="800" class="g-y">Altın kural: olmayanı varmış gibi yapmak.</text>'
    return svg(472, 242, ic, 'Gerçekte yaşanan: neşeli koşuşturma ve Moni’nin çıkardığı siren sesi. Gerçekte yaşanmayan: ambulans, sedye, '
               'buz ve sargı bezi, Satürn’deki hastane. Oyunun altın kuralı olmayanı varmış gibi yapmaktır.')


def nokta_gorevleri():
    """Noktanın dört görevi: cümle sonu, kısaltma, sıra bildiren sayı, tarih (kitap s. 30-31)."""
    satir = [
        ('mavi', ['Cümle sonu'], 'Çocuklar topsuz bir maç oynadı.'),
        ('turuncu', ['Kısaltmanın sonu'], 'vb., Cad., dk.'),
        ('yesil', ['Sıra bildiren', 'sayıdan sonra'], '1. olan takım, 2. sırada'),
        ('mor', ['Gün, ay ve yıl arası'], '03.10.2026'),
    ]
    ic = ''
    for k, (renk, etiket, ornek) in enumerate(satir):
        y = 8 + k * 54
        ic += _kutu(8, y, 176, 44, renk, rx=10)
        if len(etiket) == 1:
            ic += f'<text x="20" y="{y + 27}" font-size="13" font-weight="800" class="{RENK[renk][2]}">{etiket[0]}</text>'
        else:
            ic += f'<text x="20" y="{y + 19}" font-size="13" font-weight="800" class="{RENK[renk][2]}">{etiket[0]}</text>'
            ic += f'<text x="20" y="{y + 36}" font-size="13" font-weight="800" class="{RENK[renk][2]}">{etiket[1]}</text>'
        ic += f'<rect x="192" y="{y}" width="272" height="44" rx="10" class="g-z"/>'
        ic += f'<rect x="192" y="{y}" width="272" height="44" rx="10" class="g-c" stroke-width="1.5"/>'
        nokta = f'<tspan font-size="19" font-weight="800" class="{RENK[renk][2]}">.</tspan>'
        ic += f'<text x="206" y="{y + 28}" font-size="13.5" class="g-y">{ornek.replace(".", nokta)}</text>'
    return svg(472, 226, ic, 'Noktanın dört görevi: cümle sonunda cümlenin bittiğini gösterir, örnek Çocuklar topsuz bir maç oynadı; '
               'kısaltmanın sonuna gelir, örnekler vb., Cad., dk.; sıra bildiren sayıdan sonra gelir, örnekler 1. olan takım ve 2. sırada; '
               'gün, ay ve yılı ayırır, örnek 03.10.2026.')


def ses_kullanimi():
    """Cümle sonundaki okun yönü: yukarı ok sesi yükseltir, aşağı ok sesi alçaltır (kitap s. 32)."""
    ic = '<defs>' + ok_isareti('okS53', 'g-s') + '</defs>'
    ic += _hap(8, 8, 224, 34, 'Ok yukarı: sesi yükselt', 'turuncu')
    ic += _hap(240, 8, 224, 34, 'Ok aşağı: sesi alçalt', 'mavi')
    for k, t in enumerate(['Maç başlıyor!', 'Top nerede kaldı?']):
        y = 54 + k * 50
        ic += _kutu(48, y, 184, 40, 'turuncu', rx=10)
        ic += f'<text x="60" y="{y + 25}" font-size="13" class="g-y">{t}</text>'
    for k, t in enumerate(['Kapıyı kapattım.', 'Yarın görüşürüz.']):
        y = 54 + k * 50
        ic += _kutu(280, y, 184, 40, 'mavi', rx=10)
        ic += f'<text x="292" y="{y + 25}" font-size="13" class="g-y">{t}</text>'
    ic += '<line x1="26" y1="144" x2="26" y2="62" class="g-ts" stroke-width="3" marker-end="url(#okS53)"/>'
    ic += '<line x1="258" y1="62" x2="258" y2="144" class="g-ms" stroke-width="3" marker-end="url(#okS53)"/>'
    ic += '<text x="236" y="176" text-anchor="middle" font-size="12.5" class="g-s">Ses, cümle sonundaki okun yönünü izler.</text>'
    return svg(472, 188, ic, 'Cümle sonundaki okun yönü: ok yukarıyı gösteriyorsa sesi yükselt; örnekler Maç başlıyor ve Top nerede kaldı. '
               'Ok aşağıyı gösteriyorsa sesi alçalt; örnekler Kapıyı kapattım ve Yarın görüşürüz.')


def uygula(o):
    g = {'Okurken tahmin et: öğren, uygula, kaydet': tahmin_akisi(),
         'Topsuz Basketbol Oyunu: açık bilgi, yorum, gerçek ve hayal': gercek_hayal(),
         'Noktanın ilk dört görevi': nokta_gorevleri(),
         'Sesini kullan: diyafram nefesi ve ok yönü': ses_kullanimi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
