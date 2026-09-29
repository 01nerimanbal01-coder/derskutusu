"""10. sınıf Biyoloji, 1. hafta görselleri (MEB Biyoloji 10 ders kitabı, basılı s. 14–20; PDF s. 15–21).

- Canlılarda enerji dönüşümü (kitap s. 18, Görsel 1.2; s. 15 tema girişi; s. 20 Kontrol Noktası):
  ışık enerjisi → fotosentez → besinlerde kimyasal enerji → hücresel solunum → ATP → biyolojik iş.
  Renk anlamı: süreçler koyu dolgulu (fotosentez yeşil, hücresel solunum mavi), enerji biçimleri açık dolgulu
  (ışık turuncu, besin yeşil, ATP mavi, iş mor).
- Koyu dolgulu şekillerdeki yazılar g-z (yüzey rengi): açık temada beyaz, koyu temada koyu; iki temada da okunur.
- ATP’nin yapısı (kitap s. 18–19, Görsel 1.3): adenin (mavi), riboz (yeşil), üç fosfat (turuncu); glikozit, ester ve
  fosfat bağları; adenozin → AMP → ADP → ATP ayraçları.
- ATP döngüsü (kitap s. 19–20, Görsel 1.4): defosforilasyon = enerji çıkışı (turuncu),
  fosforilasyon = enerji girişi (yeşil).
"""
from ozet_gorsel import svg, ok_isareti


def _cizgi_ok(kimlik):
    # gri çizgiler için açık uçlu (çizgi rengiyle aynı) ok başı
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M1.5 1.5L8.5 5L1.5 8.5" class="g-c" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></marker>')


def _kutu(x, y, w, h, baslik, satirlar, renk, dolu):
    a, st, f = renk
    if dolu:
        ic = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="{f}"/>'
        yb, ys = 'g-z', 'g-z'
    else:
        ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="{a}"/>'
              f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="{st}" stroke-width="2"/>')
        yb, ys = f, 'g-y'
    cx = x + w / 2
    bas_y = y + (30 if len(satirlar) < 2 else 25)
    boy = 18 if baslik == 'ATP' else 12.5   # 'Hücresel solunum' 136 px kutuya iç boşlukla sığsın
    ic += f'<text x="{cx}" y="{bas_y}" text-anchor="middle" font-size="{boy}" font-weight="800" class="{yb}">{baslik}</text>'
    for k, s in enumerate(satirlar):
        ic += f'<text x="{cx}" y="{bas_y + 20 + k * 16}" text-anchor="middle" font-size="11.5" class="{ys}">{s}</text>'
    return ic


def enerji_donusumu():
    TUR, YES, MAV, MOR = ('g-ta', 'g-ts', 'g-tf'), ('g-ya', 'g-ys', 'g-yf'), ('g-ma', 'g-ms', 'g-mf'), ('g-oa', 'g-os', 'g-of')
    w, h = 136, 70
    x1, x2, x3 = 6, 168, 330
    y1, y2 = 10, 124
    ic = '<defs>' + _cizgi_ok('b10okA') + '</defs>'
    # 1. satır (soldan sağa): güneşten besine
    ic += _kutu(x1, y1, w, h, 'Işık enerjisi', ['güneşten gelir'], TUR, False)
    ic += _kutu(x2, y1, w, h, 'Fotosentez', ['yeşil bitkide'], YES, True)
    ic += _kutu(x3, y1, w, h, 'Kimyasal enerji', ['organik besinlerin', 'bağlarında'], YES, False)
    # 2. satır (sağdan sola): besinden işe
    ic += _kutu(x3, y2, w, h, 'Hücresel solunum', ['hücre içinde'], MAV, True)
    ic += _kutu(x2, y2, w, h, 'ATP', ['ortak enerji', 'molekülü'], MAV, False)
    ic += _kutu(x1, y2, w, h, 'Biyolojik iş', ['yaşamsal', 'faaliyetler'], MOR, False)
    ok = ' class="g-c" stroke-width="2.5" stroke-linecap="round" marker-end="url(#b10okA)"'
    yo = y1 + h / 2
    ic += f'<line x1="{x1 + w + 4}" y1="{yo}" x2="{x2 - 6}" y2="{yo}"{ok}/>'
    ic += f'<line x1="{x2 + w + 4}" y1="{yo}" x2="{x3 - 6}" y2="{yo}"{ok}/>'
    ya = y2 + h / 2
    ic += f'<line x1="{x3 - 4}" y1="{ya}" x2="{x2 + w + 6}" y2="{ya}"{ok}/>'
    ic += f'<line x1="{x2 - 4}" y1="{ya}" x2="{x1 + w + 6}" y2="{ya}"{ok}/>'
    xd = x3 + w / 2
    ic += f'<line x1="{xd}" y1="{y1 + h + 4}" x2="{xd}" y2="{y2 - 6}"{ok}/>'
    ic += f'<text x="{xd - 10}" y="{y1 + h + 20}" text-anchor="end" font-size="11.5" class="g-s">besin zinciriyle</text>'
    ic += f'<text x="{xd - 10}" y="{y1 + h + 36}" text-anchor="end" font-size="11.5" class="g-s">bütün canlılara</text>'
    # biyolojik iş örnekleri (kitap s. 18 ve s. 20)
    xb = x1 + w / 2
    py = 222
    ic += f'<line x1="{xb}" y1="{y2 + h + 4}" x2="{xb}" y2="{py - 6}"{ok}/>'
    ic += (f'<rect x="{x1}" y="{py}" width="460" height="110" rx="14" class="g-oa"/>'
           f'<rect x="{x1}" y="{py}" width="460" height="110" rx="14" class="g-os" stroke-width="2"/>')
    ic += f'<text x="{x1 + 16}" y="{py + 23}" font-size="12.5" font-weight="800" class="g-of">ATP’deki enerjiyle yürüyen yaşamsal faaliyetler</text>'
    ornek = [['hareket', 'üreme', 'büyüme', 'doku ve organların onarımı'],
             ['vücut ısısının korunması', 'kas kasılması', 'sinirsel iletim', 'aktif taşıma']]
    for s, sutun in enumerate(ornek):
        for k, t in enumerate(sutun):
            xx, yy = x1 + 22 + s * 230, py + 45 + k * 18
            ic += f'<circle cx="{xx}" cy="{yy - 4}" r="3.5" class="g-of"/><text x="{xx + 11}" y="{yy}" font-size="12" class="g-y">{t}</text>'
    return svg(472, 340, ic, 'Canlılarda enerji dönüşümü: güneşten gelen ışık enerjisi yeşil bitkide fotosentezle organik besinlerin bağlarında '
               'kimyasal enerjiye dönüşür; besinler besin zinciriyle bütün canlılara ulaşır; hücre içinde hücresel solunumla ATP oluşur; '
               'ATP’deki enerji biyolojik işte kullanılır: hareket, üreme, büyüme, doku ve organların onarımı, vücut ısısının korunması, '
               'kas kasılması, sinirsel iletim, aktif taşıma')


def atp_yapisi():
    cy = 92
    ic = ''
    # bağlar (şekillerin arkasında)
    for xa, xb in [(97, 127), (193, 225), (275, 293), (343, 361)]:
        ic += f'<line x1="{xa}" y1="{cy}" x2="{xb}" y2="{cy}" class="g-c" stroke-width="3" stroke-linecap="round"/>'
    # adenin: altıgen (mavi)
    r = 36
    alti = ' '.join(f'{56 + dx:.1f},{cy + dy:.1f}' for dx, dy in [(-r, 0), (-r / 2, -r * 0.866), (r / 2, -r * 0.866), (r, 0), (r / 2, r * 0.866), (-r / 2, r * 0.866)])
    ic += f'<polygon points="{alti}" class="g-mf"/>'
    ic += f'<text x="56" y="{cy + 5}" text-anchor="middle" font-size="13" font-weight="800" class="g-z">Adenin</text>'
    # riboz: beşgen (yeşil)
    import math
    bes = ' '.join(f'{160 + 34 * math.cos(math.radians(-90 + k * 72)):.1f},{cy + 34 * math.sin(math.radians(-90 + k * 72)):.1f}' for k in range(5))
    ic += f'<polygon points="{bes}" class="g-yf"/>'
    ic += f'<text x="160" y="{cy + 8}" text-anchor="middle" font-size="13" font-weight="800" class="g-z">Riboz</text>'
    # üç fosfat (turuncu)
    for x in (250, 318, 386):
        ic += f'<circle cx="{x}" cy="{cy}" r="21" class="g-tf"/><text x="{x}" y="{cy + 6}" text-anchor="middle" font-size="17" font-weight="800" class="g-z">P</text>'
    # bağ adları
    for x, ad in [(112, 'glikozit bağı'), (209, 'ester bağı')]:
        ic += f'<text x="{x}" y="32" text-anchor="middle" font-size="11.5" font-weight="700" class="g-s">{ad}</text>'
        ic += f'<line x1="{x}" y1="40" x2="{x}" y2="84" class="g-c" stroke-width="1.5" stroke-dasharray="3 3"/>'
    ic += '<text x="318" y="32" text-anchor="middle" font-size="11.5" font-weight="700" class="g-s">fosfat bağları</text>'
    for x in (284, 352):
        ic += f'<line x1="{x}" y1="40" x2="{x}" y2="84" class="g-c" stroke-width="1.5" stroke-dasharray="3 3"/>'
    # ayraçlar: adenozin → AMP → ADP → ATP
    ayrac = [(192, 140, 'Adenozin', False), (271, 174, 'Adenozin monofosfat (AMP)', False),
             (339, 208, 'Adenozin difosfat (ADP)', False), (407, 242, 'Adenozin trifosfat (ATP)', True)]
    for x2, y, ad, vurgu in ayrac:
        cz = 'g-ts' if vurgu else 'g-c'
        ic += f'<path d="M20 {y - 7}V{y}H{x2}V{y - 7}" class="{cz}" stroke-width="2" stroke-linejoin="round"/>'
        yz = ' font-size="12.5" font-weight="800" class="g-tf"' if vurgu else ' font-size="11.5" font-weight="600" class="g-y"'
        ic += f'<text x="{(20 + x2) / 2}" y="{y + 17}" text-anchor="middle"{yz}>{ad}</text>'
    return svg(472, 272, ic, 'ATP molekülünün yapısı: adenin bazı glikozit bağıyla riboz şekerine, riboz ester bağıyla fosfat grubuna bağlıdır; '
               'üç fosfat grubu arasında fosfat bağları vardır. Adenin ve riboz adenozini; adenozin ve bir fosfat AMP’yi; '
               'iki fosfat ADP’yi; üç fosfat ATP’yi oluşturur')


def atp_dongusu():
    ic = '<defs>' + ok_isareti('b10okT', 'g-tf') + ok_isareti('b10okY', 'g-yf') + '</defs>'
    # enerjiyi kullanan faaliyetler (üst, turuncu)
    ic += ('<rect x="66" y="6" width="340" height="52" rx="16" class="g-ta"/>'
           '<rect x="66" y="6" width="340" height="52" rx="16" class="g-ts" stroke-width="2"/>')
    ic += '<text x="236" y="27" text-anchor="middle" font-size="12.5" font-weight="800" class="g-tf">ATP’nin enerjisini kullanan faaliyetler</text>'
    ic += '<text x="236" y="47" text-anchor="middle" font-size="11.5" class="g-y">kas kasılması · sinirsel iletim · aktif taşıma</text>'
    # ATP ve ADP + Pi
    ic += '<rect x="16" y="134" width="130" height="52" rx="26" class="g-mf"/>'
    ic += '<text x="81" y="167" text-anchor="middle" font-size="20" font-weight="800" class="g-z">ATP</text>'
    ic += ('<rect x="326" y="134" width="130" height="52" rx="26" class="g-ma"/>'
           '<rect x="326" y="134" width="130" height="52" rx="26" class="g-ms" stroke-width="2"/>')
    ic += '<text x="391" y="166" text-anchor="middle" font-size="18" font-weight="800" class="g-mf">ADP + P<tspan dy="4" font-size="12">i</tspan></text>'
    ic += '<text x="236" y="165" text-anchor="middle" font-size="14" font-weight="800" class="g-s">ATP döngüsü</text>'
    # defosforilasyon (üst yay): enerji çıkışı
    ic += '<path d="M102 126Q236 40 370 126" class="g-ts" stroke-width="3" stroke-linecap="round" marker-end="url(#b10okT)"/>'
    ic += '<text x="236" y="110" text-anchor="middle" font-size="12.5" font-weight="800" class="g-tf">Defosforilasyon</text>'
    ic += '<text x="236" y="127" text-anchor="middle" font-size="11.5" class="g-s">H₂O kullanılır</text>'
    ic += '<line x1="236" y1="80" x2="236" y2="66" class="g-ts" stroke-width="2.5" stroke-linecap="round" marker-end="url(#b10okT)"/>'
    ic += '<text x="246" y="73" font-size="11.5" font-weight="700" class="g-tf">enerji çıkışı</text>'
    # fosforilasyon (alt yay): enerji girişi
    ic += '<path d="M370 194Q236 280 102 194" class="g-ys" stroke-width="3" stroke-linecap="round" marker-end="url(#b10okY)"/>'
    ic += '<text x="236" y="201" text-anchor="middle" font-size="11.5" class="g-s">H₂O açığa çıkar</text>'
    ic += '<text x="236" y="219" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">Fosforilasyon</text>'
    ic += '<line x1="236" y1="264" x2="236" y2="248" class="g-ys" stroke-width="2.5" stroke-linecap="round" marker-end="url(#b10okY)"/>'
    ic += '<text x="246" y="257" font-size="11.5" font-weight="700" class="g-yf">enerji girişi</text>'
    # besinlerdeki kimyasal enerji (alt, yeşil)
    ic += ('<rect x="66" y="268" width="340" height="36" rx="16" class="g-ya"/>'
           '<rect x="66" y="268" width="340" height="36" rx="16" class="g-ys" stroke-width="2"/>')
    ic += '<text x="236" y="291" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">Besinlerdeki kimyasal enerji</text>'
    return svg(472, 310, ic, 'ATP döngüsü: ATP defosforilasyonla su kullanılarak ADP ve inorganik fosfata (Pᵢ) ayrılır, açığa çıkan enerji kas kasılması, '
               'sinirsel iletim ve aktif taşımada kullanılır (enerji çıkışı); ADP ve Pᵢ, besinlerdeki kimyasal enerjiyle fosforilasyonla '
               'yeniden ATP’ye dönüşür, su açığa çıkar (enerji girişi)')


def uygula(o):
    g = {'Enerji ve canlılarda enerji dönüşümü': enerji_donusumu(),
         'ATP’nin yapısı': atp_yapisi(),
         'ATP döngüsü': atp_dongusu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
