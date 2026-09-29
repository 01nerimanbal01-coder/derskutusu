"""9. sınıf Kimya, 1. hafta görselleri (MEB Kimya 9 ders kitabı, basılı s. 20–27).

- Mutfakta kimya: marinasyon ve pişirme sıcaklığına göre yiyecekte biriken alüminyum (kitap s. 24 tablosu)
  Renk anlamı: 150 °C mavi, 200 °C mor, 250 °C turuncu (sıcaklık arttıkça sıcak renk).
- Kimyanın alt disiplinleri: altı disiplin, ne inceler + kitaptaki örnek (kitap s. 25–26)
- Kariyer: ön lisans (turuncu) ve lisans (mavi) programları → unvanlar (kitap s. 26)
"""
from ozet_gorsel import svg, ok_isareti


def _sayi(v):
    return f'{v:.3f}'.replace('.', ',')


def marinasyon_grafigi():
    veri = [('A', '6,12', (0.051, 0.055, 0.062)),
            ('B', '5,23', (0.128, 0.130, 0.134)),
            ('C', '6,07', (0.061, 0.063, 0.066))]
    renk = ('g-mf', 'g-of', 'g-tf')
    x0, x1, y0, yst, ust = 64, 462, 200, 50, 0.14
    olc = (y0 - yst) / ust
    ic = '<text x="12" y="20" font-size="11.5" class="g-s">Yiyecekte biriken alüminyum (mg Al/100 g)</text>'
    for v, et in ((0.05, '0,05'), (0.10, '0,10')):
        y = y0 - v * olc
        ic += f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" class="g-c" stroke-width="1" stroke-dasharray="3 4"/>'
        ic += f'<text x="{x0 - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" class="g-s">{et}</text>'
    ic += f'<text x="{x0 - 8}" y="{y0 + 4}" text-anchor="end" font-size="11" class="g-s">0</text>'
    gw = (x1 - x0) / 3
    for i, (ad, ph, degerler) in enumerate(veri):
        cx = x0 + gw * (i + 0.5)
        for k, v in enumerate(degerler):
            bx = cx + (k - 1) * 38
            h = v * olc
            ic += f'<rect x="{bx - 15:.1f}" y="{y0 - h:.1f}" width="30" height="{h:.1f}" rx="3" class="{renk[k]}"/>'
            ic += f'<text x="{bx:.1f}" y="{y0 - h - 5:.1f}" text-anchor="middle" font-size="11" class="g-y">{_sayi(v)}</text>'
        ic += f'<text x="{cx:.1f}" y="{y0 + 19}" text-anchor="middle" font-size="12" font-weight="800" class="g-y">Marinasyon {ad}</text>'
        ic += f'<text x="{cx:.1f}" y="{y0 + 35}" text-anchor="middle" font-size="11.5" class="g-s">sosun pH değeri {ph}</text>'
    ic += f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" class="g-c" stroke-width="1.5"/>'
    ic += f'<text x="{x0}" y="{y0 + 63}" font-size="12" font-weight="700" class="g-s">Pişirme sıcaklığı:</text>'
    for k, (et, x) in enumerate((('150 °C', 190), ('200 °C', 268), ('250 °C', 346))):
        ic += f'<rect x="{x}" y="{y0 + 52}" width="13" height="13" rx="3" class="{renk[k]}"/>'
        ic += f'<text x="{x + 19}" y="{y0 + 63}" font-size="12" class="g-y">{et}</text>'
    return svg(472, 272, ic, 'Pişirme sıcaklığına göre yiyecekte biriken alüminyum (mg Al/100 g): Marinasyon A (sos pH 6,12) 150 °C 0,051, 200 °C 0,055, 250 °C 0,062; '
               'Marinasyon B (sos pH 5,23) 0,128, 0,130, 0,134; Marinasyon C (sos pH 6,07) 0,061, 0,063, 0,066. Üç sosta da sıcaklık arttıkça biriken alüminyum artar; en çok alüminyum pH değeri en küçük olan B sosunda birikir.')


def alt_disiplinler():
    kart = [('Analitik kimya', 'bileşenler ve miktarları', 'ör. suyun sertlik derecesi', ('g-ma', 'g-ms', 'g-mf')),
            ('Biyokimya', 'canlı kimyası', 'ör. protein, vitamin, hormon', ('g-ya', 'g-ys', 'g-yf')),
            ('Organik kimya', 'karbon kimyası, en geniş alan', 'ör. ilaç, boya, deterjan', ('g-ta', 'g-ts', 'g-tf')),
            ('Anorganik kimya', 'organik olmayan bileşikler', 'ör. metal, mineral, asit', ('g-oa', 'g-os', 'g-of')),
            ('Fizikokimya', 'tepkime ve enerji dönüşümü', 'ör. buzun erimesi', ('g-ma', 'g-ms', 'g-mf')),
            ('Polimer kimyası', 'büyük moleküller', 'ör. kauçuk, fiber, yapıştırıcı', ('g-ya', 'g-ys', 'g-yf'))]
    ic = ''
    for i, (ad, konu, ornek, (a, st, f)) in enumerate(kart):
        x, y = 10 + (i % 2) * 230, 10 + (i // 2) * 82
        ic += f'<rect x="{x}" y="{y}" width="222" height="72" rx="12" class="{a}"/><rect x="{x}" y="{y}" width="222" height="72" rx="12" class="{st}" stroke-width="2"/>'
        ic += f'<circle cx="{x + 20}" cy="{y + 21}" r="5" class="{f}"/>'
        ic += f'<text x="{x + 32}" y="{y + 26}" font-size="13.5" font-weight="800" class="{f}">{ad}</text>'
        ic += f'<text x="{x + 14}" y="{y + 46}" font-size="11.5" class="g-y">{konu}</text>'
        ic += f'<text x="{x + 14}" y="{y + 63}" font-size="11.5" class="g-s">{ornek}</text>'
    return svg(472, 256, ic, 'Kimyanın alt disiplinleri: analitik kimya (bileşenler ve miktarları), biyokimya (canlı kimyası), organik kimya (karbon kimyası), '
               'anorganik kimya (organik olmayan bileşikler), fizikokimya (tepkime ve enerji dönüşümü), polimer kimyası (büyük moleküller)')


def kariyer_yollari():
    ic = '<defs>' + ok_isareti('okKM', 'g-c') + '</defs>'
    ic += '<text x="122" y="18" text-anchor="middle" font-size="11.5" font-weight="700" class="g-s">Program</text>'
    ic += '<text x="357" y="18" text-anchor="middle" font-size="11.5" font-weight="700" class="g-s">Unvan</text>'
    # Ön lisans (turuncu)
    ic += '<rect x="8" y="28" width="456" height="118" rx="14" class="g-ta"/><rect x="8" y="28" width="456" height="118" rx="14" class="g-ts" stroke-width="2"/>'
    ic += '<text x="22" y="50" font-size="12.5" font-weight="800" class="g-tf">ÖN LİSANS</text>'
    ic += '<rect x="22" y="60" width="200" height="30" rx="15" class="g-tf"/>'
    ic += '<text x="122" y="80" text-anchor="middle" font-size="12" font-weight="700" class="g-b">Kimya teknolojisi</text>'
    ic += '<line x1="228" y1="75" x2="252" y2="75" class="g-c" stroke-width="2" marker-end="url(#okKM)"/>'
    ic += '<rect x="262" y="60" width="190" height="30" rx="15" class="g-z"/><rect x="262" y="60" width="190" height="30" rx="15" class="g-ts" stroke-width="2"/>'
    ic += '<text x="357" y="80" text-anchor="middle" font-size="12" font-weight="800" class="g-tf">Kimya teknikeri</text>'
    ic += '<text x="22" y="114" font-size="11.5" class="g-y"><tspan font-weight="700">Çalışabileceği pozisyonlar:</tspan> laboratuvar teknikeri,</text>'
    ic += '<text x="22" y="132" font-size="11.5" class="g-y">kalite kontrol analisti, araştırma asistanı</text>'
    # Lisans (mavi)
    ic += '<rect x="8" y="158" width="456" height="176" rx="14" class="g-ma"/><rect x="8" y="158" width="456" height="176" rx="14" class="g-ms" stroke-width="2"/>'
    ic += '<text x="22" y="180" font-size="12.5" font-weight="800" class="g-mf">LİSANS</text>'
    cift = [('Kimya', 'Kimyager'), ('Kimya öğretmenliği', 'Kimya öğretmeni'),
            ('Kimya mühendisliği', 'Kimya mühendisi'), ('Polimer malzeme mühendisliği', 'Polimer malzeme mühendisi')]
    for k, (p, u) in enumerate(cift):
        y = 190 + k * 35
        ic += f'<rect x="22" y="{y}" width="200" height="28" rx="14" class="g-mf"/>'
        ic += f'<text x="122" y="{y + 18.5}" text-anchor="middle" font-size="11.5" font-weight="700" class="g-b">{p}</text>'
        ic += f'<line x1="228" y1="{y + 14}" x2="252" y2="{y + 14}" class="g-c" stroke-width="2" marker-end="url(#okKM)"/>'
        ic += f'<rect x="262" y="{y}" width="190" height="28" rx="14" class="g-z"/><rect x="262" y="{y}" width="190" height="28" rx="14" class="g-ms" stroke-width="2"/>'
        ic += f'<text x="357" y="{y + 18.5}" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mf">{u}</text>'
    return svg(472, 342, ic, 'Kimya alanında eğitim ve unvanlar: ön lisans kimya teknolojisi programı → kimya teknikeri (laboratuvar teknikeri, kalite kontrol analisti, araştırma asistanı); '
               'lisans programları kimya → kimyager, kimya öğretmenliği → kimya öğretmeni, kimya mühendisliği → kimya mühendisi, polimer malzeme mühendisliği → polimer malzeme mühendisi')


def uygula(o):
    g = {'Mutfakta kimya ve verilerden çıkarım': marinasyon_grafigi(),
         'Kimyanın alt disiplinleri': alt_disiplinler(),
         'Kimya alanında kariyer olanakları': kariyer_yollari()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
