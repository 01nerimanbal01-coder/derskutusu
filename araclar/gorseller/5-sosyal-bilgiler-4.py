"""5. sınıf Sosyal Bilgiler, 4. hafta: yardımlaşma ve dayanışma faaliyetlerinin toplumsal birliğe etkisi.

Görseller yalnız MEB 5. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (kitap s. 34-37).
Renk anlamı: sadaka taşı akışında mavi = yardım eden, turuncu = taş, yeşil = ihtiyaç sahibi;
kamu kurumları mavi, sivil toplum kuruluşları turuncu, ortak hedef yeşil;
Millî Eğitim Bakanlığı çalışmalarında mavi = barınma, turuncu = arama kurtarma, yeşil = üretim;
proje süreci adımlarında mavi = fikir üretme, turuncu = geliştirme ve değerlendirme, yeşil = karar.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def sadaka_tasi():
    """Sadaka taşında yardımın yolu (kitap s. 34)."""
    ic = '<defs>' + ok_isareti('okS4a', 'g-s') + '</defs>'
    kutu = [(8, 'mavi', 'Yardım eden', ('taşın içine', 'para bırakır')),
            (166, 'turuncu', 'Sadaka taşı', ('meydan, cami ve', 'çeşme çevresinde', 'bulunur')),
            (324, 'yesil', 'İhtiyaç sahibi', ('gece geç saatte,', 'kimseye', 'görünmeden alır'))]
    for x, renk, ad, satir in kutu:
        ic += _kutu(x, 8, 140, 104, renk)
        ic += f'<text x="{x + 12}" y="32" font-size="13" font-weight="800" class="{RENK[renk][2]}">{ad}</text>'
        for k, t in enumerate(satir):
            ic += f'<text x="{x + 12}" y="{54 + k * 17}" font-size="12" class="g-y">{t}</text>'
    for x in (150, 308):
        ic += f'<line x1="{x}" y1="60" x2="{x + 10}" y2="60" class="g-c" stroke-width="2" marker-end="url(#okS4a)"/>'
    ic += '<rect x="8" y="124" width="456" height="36" rx="8" class="g-z"/>'
    ic += '<rect x="8" y="124" width="456" height="36" rx="8" class="g-c" stroke-width="1.5"/>'
    ic += '<text x="236" y="147" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Sonuç: ihtiyaç sahibi incinmez, yardım amacına ulaşır.</text>'
    ic += '<text x="236" y="180" text-anchor="middle" font-size="12" class="g-s">Selçuklu ve Osmanlı dönemlerinde kullanılırdı.</text>'
    return svg(472, 190, ic, 'Sadaka taşında yardımın yolu: yardım eden kişi taşın içine para bırakır; taş meydan, cami ve çeşme çevresinde bulunur; '
               'ihtiyaç sahibi gece geç saatte kimseye görünmeden parayı alır. Sonuç: ihtiyaç sahibi incinmez, yardım amacına ulaşır.')


def kamu_stk():
    """Kamu kurumları ve sivil toplum kuruluşları: faaliyet alanı ve ortak hedef (kitap s. 35)."""
    ic = ''
    sol = ('mavi', 'Kamu kurumları', ('Ülkenin her yerinde', 'faaliyet gösterir.', 'Örnek: Aile ve Sosyal', 'Hizmetler Bakanlığı’nın', 'Ulusal Vefa Programı'))
    sag = ('turuncu', 'Sivil toplum kuruluşları', ('Kurulduğu bölgede sosyal', 'yardım faaliyeti düzenler;', 'ülke genelinde de', 'çalışma yürütür.', '(kısaca STK)'))
    for x, (renk, ad, satir) in ((8, sol), (240, sag)):
        ic += _kutu(x, 8, 224, 122, renk)
        ic += f'<text x="{x + 12}" y="32" font-size="13" font-weight="800" class="{RENK[renk][2]}">{ad}</text>'
        for k, t in enumerate(satir):
            ic += f'<text x="{x + 12}" y="{54 + k * 16}" font-size="12" class="g-y">{t}</text>'
    ic += _kutu(8, 140, 456, 62, 'yesil')
    ic += '<text x="236" y="161" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">Ortak hedef</text>'
    ic += '<text x="236" y="180" text-anchor="middle" font-size="12" class="g-y">Yoksulluğun azalması ve insanların daha iyi</text>'
    ic += '<text x="236" y="195" text-anchor="middle" font-size="12" class="g-y">şartlarda yaşaması; toplumsal birliğin güçlenmesi</text>'
    return svg(472, 212, ic, 'Kamu kurumları ülkenin her yerinde faaliyet gösterir; örnek: Aile ve Sosyal Hizmetler Bakanlığı’nın Ulusal Vefa Programı. '
               'Sivil toplum kuruluşları (STK) kurulduğu bölgede sosyal yardım faaliyeti düzenler, ülke genelinde de çalışma yürütür. '
               'Ortak hedef: yoksulluğun azalması, insanların daha iyi şartlarda yaşaması, toplumsal birliğin güçlenmesi.')


def meb_calismalari():
    """Millî Eğitim Bakanlığının deprem bölgesindeki çalışmaları (kitap s. 37)."""
    satir = [('mavi', 'Barınma', 44, ('Uygulama otelleri, öğretmenevleri,', 'pansiyonlar ve okullar hizmete açıldı')),
             ('turuncu', 'Arama kurtarma', 44, ('Arama kurtarma birimi MEB AKUB’da', 'görevli öğretmenler destek verdi')),
             ('yesil', 'Üretim', 84, ('Battaniye, uyku tulumu ve çadır:', 'olgunlaşma enstitüleri, halk eğitim', 'merkezleri ve meslek liseleri.', 'Soba, yatak, atkı, bere: meslek liseleri.'))]
    ic = ''
    y = 8
    for renk, ad, h, metin in satir:
        a, s, f = RENK[renk]
        ic += f'<rect x="8" y="{y}" width="132" height="{h}" rx="10" class="{f}"/>'
        ic += f'<text x="74" y="{y + h / 2 + 4:g}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{ad}</text>'
        ic += f'<rect x="146" y="{y}" width="318" height="{h}" rx="10" class="{a}"/>'
        ic += f'<rect x="146" y="{y}" width="318" height="{h}" rx="10" class="{s}" stroke-width="2"/>'
        n = len(metin)
        ty0 = y + h / 2 - (n - 1) * 8 + 4
        for k, t in enumerate(metin):
            ic += f'<text x="158" y="{ty0 + k * 16:g}" font-size="12" class="g-y">{t}</text>'
        y += h + 8
    ic += '<text x="236" y="214" text-anchor="middle" font-size="12" class="g-s">Bakanlık, depremin ilk gününden itibaren çalıştı.</text>'
    return svg(472, 224, ic, 'Millî Eğitim Bakanlığının deprem bölgesindeki çalışmaları: barınma: uygulama otelleri, öğretmenevleri, pansiyonlar ve okullar hizmete açıldı; '
               'arama kurtarma: MEB AKUB’da görevli öğretmenler destek verdi; üretim: battaniye, uyku tulumu ve çadır olgunlaşma enstitüleri, '
               'halk eğitim merkezleri ve meslek liselerinde; soba, yatak, atkı ve bere meslek liselerinde üretildi.')


def proje_sureci():
    """Fikir üretmeden karara: sınıfın izlediği yol (kitap s. 37)."""
    ic = '<defs>' + ok_isareti('okS4d', 'g-s') + '</defs>'
    adim = [('mavi', ('Fikir', 'üret')), ('mavi', ('Güçlü, zayıf', 'yönleri yaz')), ('turuncu', ('Zayıf yönlere', 'çözüm bul')),
            ('turuncu', ('Anekdot kaydıyla', 'değerlendir')), ('yesil', ('Sınıfça', 'karar ver'))]
    yer = [(8, 8), (166, 8), (324, 8), (324, 100), (166, 100)]
    for i, ((renk, (s1, s2)), (x, y)) in enumerate(zip(adim, yer)):
        cx = x + 70
        ic += _kutu(x, y, 140, 74, renk, rx=10)
        ic += f'<circle cx="{cx}" cy="{y + 18}" r="11" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{cx}" y="{y + 23}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="{cx}" y="{y + 46}" text-anchor="middle" font-size="12" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="{y + 63}" text-anchor="middle" font-size="12" font-weight="700" class="g-y">{s2}</text>'
    for x in (150, 308):
        ic += f'<line x1="{x}" y1="45" x2="{x + 10}" y2="45" class="g-c" stroke-width="2" marker-end="url(#okS4d)"/>'
    ic += '<line x1="394" y1="84" x2="394" y2="94" class="g-c" stroke-width="2" marker-end="url(#okS4d)"/>'
    ic += '<line x1="322" y1="137" x2="312" y2="137" class="g-c" stroke-width="2" marker-end="url(#okS4d)"/>'
    for k, (renk, t) in enumerate([('mavi', 'Fikir üretme'), ('turuncu', 'Geliştirme'), ('yesil', 'Karar')]):
        ic += f'<circle cx="16" cy="{116 + k * 22}" r="6" class="{RENK[renk][2]}"/>'
        ic += f'<text x="28" y="{120 + k * 22}" font-size="12" class="g-y">{t}</text>'
    ic += '<text x="236" y="204" text-anchor="middle" font-size="12" class="g-s">Sınıfın kararı: depremden etkilenen bölgedeki bir okula</text>'
    ic += '<text x="236" y="220" text-anchor="middle" font-size="12" class="g-s">yönelik “El Ele, Gönül Gönüle” projesi.</text>'
    return svg(472, 230, ic, 'Proje süreci: 1 fikir üret, 2 güçlü ve zayıf yönleri yaz, 3 zayıf yönlere çözüm bul, 4 anekdot kaydıyla değerlendir, 5 sınıfça karar ver. '
               'Sınıfın kararı: depremden etkilenen bölgedeki bir okula yönelik El Ele, Gönül Gönüle projesi.')


def uygula(o):
    g = {'Geçmişten bir örnek: sadaka taşı': sadaka_tasi(),
         'Yardımlaşma çalışmalarını kimler yürütür?': kamu_stk(),
         'Proje öncesi hazırlık: gruplar ve inceleme': meb_calismalari(),
         'Fikir üret, değerlendir, karar ver': proje_sureci()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
