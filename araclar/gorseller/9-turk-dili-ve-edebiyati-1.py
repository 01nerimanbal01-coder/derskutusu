"""9. sınıf Türk Dili ve Edebiyatı, 1. hafta (Sözün İnceliği: San’at şiiri, Picasso’nun Hatları denemesi).

Görseller yalnız MEB 9. sınıf TDE ders kitabındaki bilgilerle kurulur:
- okuma_sureci(): okuma öncesi / sırası / sonrası (kitap PDF s17–19, s40–44; tahmin ↔ içerik karşılaştırması s17 d–e, s40 2a–b)
- sen_biz(): San’at şiirinde “sen” ve “biz” sanat anlayışları (kitap s18, s20)
Renk sınıfları stil.css "Özet görselleri": g-m* mavi, g-y* yeşil, g-t* turuncu, g-o* mor, g-c çizgi, g-y metin, g-s soluk, g-z yüzey.
"""
from ozet_gorsel import svg


def okuma_sureci():
    ic = ''
    kart = [
        (8, 'Okuma öncesi', ('Başlığa ve', 'görsellere bak.', 'İçerik hakkında', 'tahminde bulun.'), ('g-ma', 'g-ms', 'g-mf')),
        (168, 'Okuma sırası', ('Türüne uygun oku.', 'Şiir: söz korosu', 'Deneme: düzyazıya', 'özgü vurgu ve', 'tonlamayla'), ('g-ya', 'g-ys', 'g-yf')),
        (328, 'Okuma sonrası', ('Tahmini içerikle', 'karşılaştır.', 'Söz varlığını', 've yazımı incele.'), ('g-ta', 'g-ts', 'g-tf')),
    ]
    for i, (x, bas, satirlar, (a, s, f)) in enumerate(kart):
        ic += f'<rect x="{x}" y="10" width="136" height="160" rx="14" class="{a}"/><rect x="{x}" y="10" width="136" height="160" rx="14" class="{s}" stroke-width="2"/>'
        ic += f'<circle cx="{x + 68}" cy="34" r="13" class="{f}"/><text x="{x + 68}" y="39" text-anchor="middle" font-size="13" font-weight="800" class="g-z">{i + 1}</text>'
        ic += f'<text x="{x + 68}" y="66" text-anchor="middle" font-size="13.5" font-weight="800" class="{f}">{bas}</text>'
        for k, t in enumerate(satirlar):
            ic += f'<text x="{x + 68}" y="{90 + (5 - len(satirlar)) * 8 + k * 16}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
    for x in (144, 304):   # kartlar arası ok (dolgulu, kartlara değmez: 4 px boşluk)
        a, b = x + 5, x + 19
        ic += f'<path d="M{a} 88.6H{b - 7}V84.5L{b} 90L{b - 7} 95.5V91.4H{a}Z" class="g-s"/>'
    # 1 ile 3 arasındaki bağ: okuma öncesindeki tahmin, okuma sonrasında içerikle karşılaştırılır (kitap PDF s17 d–e, s40 2a–b).
    # Kartların altından geçen, iki ucu oklu dirsekli çizgi; ok uçları kartlara 5 px uzak; ortadaki yazı için çizgide ≥ 8 px boşluk.
    yazi = 'Tahmin ile içerik karşılaştırılır.'
    yari = len(yazi) * 12 * 0.55 / 2 + 8
    ic += (f'<path d="M76 176V196H{236 - yari:.0f}M{236 + yari:.0f} 196H396V176M71 181L76 176L81 181M391 181L396 176L401 181" '
           'class="g-c" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    ic += f'<text x="236" y="200" text-anchor="middle" font-size="12" class="g-s">{yazi}</text>'
    return svg(472, 210, ic, 'Okumayı yönetmek: 1. Okuma öncesi: başlığa ve görsellere bakıp içerik hakkında tahminde bulunma. '
               '2. Okuma sırası: türüne uygun okuma; şiir söz korosuyla, deneme düzyazıya özgü vurgu ve tonlamayla. '
               '3. Okuma sonrası: tahmini içerikle karşılaştırma, söz varlığını ve yazımı inceleme. Okuma öncesindeki tahmin, okuma sonrasında içerikle karşılaştırılır.')


def sen_biz():
    ic = ''
    # başlıklar
    ic += '<rect x="10" y="8" width="162" height="46" rx="12" class="g-ma"/><rect x="10" y="8" width="162" height="46" rx="12" class="g-ms" stroke-width="2"/>'
    ic += '<text x="91" y="28" text-anchor="middle" font-size="14" font-weight="800" class="g-mf">“SEN”</text>'
    ic += '<text x="91" y="45" text-anchor="middle" font-size="11.5" class="g-s">şairin seslendiği kişi</text>'
    ic += '<rect x="300" y="8" width="162" height="46" rx="12" class="g-ta"/><rect x="300" y="8" width="162" height="46" rx="12" class="g-ts" stroke-width="2"/>'
    ic += '<text x="381" y="28" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">“BİZ”</text>'
    ic += '<text x="381" y="45" text-anchor="middle" font-size="11.5" class="g-s">şairin benimsediği</text>'
    ic += '<text x="236" y="36" text-anchor="middle" font-size="11.5" class="g-s">karşılaştırma</text>'
    satir = [
        ('Süsleme', ('mabette ince', 'bir mozayik'), ('duvarda sülüs yazı,', 'yeşil çini')),
        ('Dans', ('sahnede raks eden', 'beyaz kelebek'), ('zeybeğin toprağa', 'diz vuruşu')),
        ('Müzik', ('fırtınayı andıran', 'orkestra sesleri'), ('acı çekenlerin', 'nefesleri')),
        ('Heykel / insan', ('yabancı bir şehirde', 'kadın heykeli'), ('köylünün', 'kıvrılmayan beli')),
    ]
    for i, (orta, sol, sag) in enumerate(satir):
        y = 64 + i * 48
        ic += f'<rect x="10" y="{y}" width="162" height="40" rx="10" class="g-ma"/><rect x="10" y="{y}" width="162" height="40" rx="10" class="g-ms" stroke-width="1.5"/>'
        ic += f'<rect x="300" y="{y}" width="162" height="40" rx="10" class="g-ta"/><rect x="300" y="{y}" width="162" height="40" rx="10" class="g-ts" stroke-width="1.5"/>'
        for k, t in enumerate(sol):
            ic += f'<text x="91" y="{y + 17 + k * 15}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
        for k, t in enumerate(sag):
            ic += f'<text x="381" y="{y + 17 + k * 15}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
        # orta etiket: mor hap 180–292 (kartlara 8 px boşluk); en uzun etiket "Heykel / insan" iki yanda ≥ 7 px boşlukla sığar
        ic += f'<rect x="180" y="{y + 7}" width="112" height="26" rx="13" class="g-oa"/><rect x="180" y="{y + 7}" width="112" height="26" rx="13" class="g-os" stroke-width="1.5"/>'
        ic += f'<text x="236" y="{y + 24}" text-anchor="middle" font-size="11.5" font-weight="800" class="g-of">{orta}</text>'
    ic += '<rect x="10" y="262" width="452" height="50" rx="12" class="g-ta"/><rect x="10" y="262" width="452" height="50" rx="12" class="g-ts" stroke-width="2"/>'
    ic += '<text x="236" y="282" text-anchor="middle" font-size="12.5" class="g-y">Son dörtlükte Anadolu “yazılmamış bir destan” gibidir.</text>'
    ic += '<text x="236" y="301" text-anchor="middle" font-size="12.5" class="g-y">Şair yolunu “sen”den ayırır, <tspan font-weight="800" class="g-tf">“biz”in sanatını seçer.</tspan></text>'
    return svg(472, 320, ic, 'San’at şiirinde iki sanat anlayışı. Sen: mabette ince mozayik, sahnede raks eden beyaz kelebek, fırtınayı andıran orkestra sesleri, '
               'yabancı bir şehirde kadın heykeli. Biz: duvarda sülüs yazı ve yeşil çini, zeybeğin toprağa diz vuruşu, acı çekenlerin nefesleri, '
               'köylünün kıvrılmayan beli. Son dörtlükte Anadolu yazılmamış bir destan gibidir; şair yolunu ayırır ve biz anlayışını seçer.')


def uygula(o):
    g = {'Okumayı yönetmek: öncesi, sırası, sonrası': okuma_sureci(),
         'San’at şiiri: “sen” ve “biz”in sanatı': sen_biz()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
