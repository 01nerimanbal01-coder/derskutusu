"""7. sınıf Temel Dinî Bilgiler (İslam 1) — 2. hafta konu özeti görselleri.
1. Ünite: Dinimiz İslam — Kur’an ve Sünnetin Hayatımdaki Yeri (çözümleme, sınıflandırma, yorumlama)."""

from ozet_gorsel import svg


def gorsel_kavram_cozumlemesi():
    """Kur’an ve sünnet kavramlarının sözlük ve terim anlamları."""
    W, H = 700, 290
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'İslam’ın İki Temel Kaynağı: Sözlük ve Terim Çözümlemesi</text>',

        '<rect x="24" y="42" width="314" height="186" rx="10" class="g-ma g-ms" stroke-width="1.5"/>',
        '<text x="181" y="66" text-anchor="middle" font-size="14" font-weight="700" class="g-mf">'
        '1. KUR’AN-I KERİM</text>',
        '<line x1="42" y1="78" x2="320" y2="78" class="g-c" stroke-width="1"/>',

        '<rect x="40" y="88" width="282" height="46" rx="6" class="g-z g-c" stroke-width="1"/>',
        '<text x="181" y="106" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">'
        'Sözlük Anlamı</text>',
        '<text x="181" y="124" text-anchor="middle" font-size="12" class="g-y">'
        'Okumak, toplamak, bir araya getirmek</text>',

        '<rect x="40" y="144" width="282" height="72" rx="6" class="g-z g-c" stroke-width="1"/>',
        '<text x="181" y="162" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">'
        'Terim Kapsamı ve Özelliği</text>',
        '<text x="181" y="180" text-anchor="middle" font-size="12" class="g-y">'
        'Cebrail (as) ile indirilen son ilahi kitap;</text>',
        '<text x="181" y="198" text-anchor="middle" font-size="12" class="g-y">'
        'okunarak ve ezberlenerek korunmuştur.</text>',

        '<rect x="362" y="42" width="314" height="186" rx="10" class="g-ta g-ts" stroke-width="1.5"/>',
        '<text x="519" y="66" text-anchor="middle" font-size="14" font-weight="700" class="g-tf">'
        '2. PEYGAMBERİMİZİN SÜNNETİ</text>',
        '<line x1="380" y1="78" x2="658" y2="78" class="g-c" stroke-width="1"/>',

        '<rect x="378" y="88" width="282" height="46" rx="6" class="g-z g-c" stroke-width="1"/>',
        '<text x="519" y="106" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">'
        'Sözlük Anlamı</text>',
        '<text x="519" y="124" text-anchor="middle" font-size="12" class="g-y">'
        'Yol, âdet, gidişat</text>',

        '<rect x="378" y="144" width="282" height="72" rx="6" class="g-z g-c" stroke-width="1"/>',
        '<text x="519" y="162" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">'
        'Terim Kapsamı ve Özelliği</text>',
        '<text x="519" y="180" text-anchor="middle" font-size="12" class="g-y">'
        'Hz. Peygamber’in sözleri, davranışları</text>',
        '<text x="519" y="198" text-anchor="middle" font-size="12" class="g-y">'
        've sahabenin güzel işlerini onaylamasıdır.</text>',

        '<rect x="24" y="240" width="652" height="38" rx="8" class="g-ya g-ys" stroke-width="1.5"/>',
        '<text x="350" y="264" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">'
        'Ortak İlke: “Allah’ın Kitabı ve Peygamberinin sünnetine sıkı sarılan yolunu şaşırmaz.”</text>',
    ]
    return svg(W, H, "".join(ic), "Kur’an ve sünnet kavramlarının sözlük ve terim anlamları")


def gorsel_sunnet_aciklama():
    """Sünnetin Kur’an’ı açıklama ve uygulamaya dönüştürme örnekleri."""
    W, H = 700, 294
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Sünnetin Kur’an-ı Kerim’i Açıklama ve Uygulama Örnekleri (Nahl 44)</text>',
    ]
    satirlar = [
        (
            44,
            "1. Namaz İbadeti Emri",
            "Kur’an’da namaz kılmak emredilir.",
            "Uygulamalı Öğretim (Buhari, Ezan, 18)",
            "“Beni nasıl namaz kılıyor gördüyseniz...”",
        ),
        (
            126,
            "2. Hac ve Zekât Emri",
            "Kur’an’da hac ve zekât farz kılınır.",
            "Uygulamalı Öğretim (Müslim, Hac, 310)",
            "“Hacda yapacağınız ibadetleri benden öğrenin.”",
        ),
        (
            208,
            "3. Kapalı İfade (Bakara 238)",
            "“Namazlara ve orta namaza devam edin.”",
            "Sözlü Açıklama (Tirmizi, Tefsir, 3)",
            "“Orta namaz, ikindi namazıdır.”",
        ),
    ]
    for y, sol_b, sol_m, sag_b, sag_m in satirlar:
        ok_y = y + 34
        ic.extend([
            f'<rect x="24" y="{y}" width="290" height="68" rx="8" class="g-ma g-ms" stroke-width="1.5"/>',
            f'<text x="169" y="{y+26}" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">{sol_b}</text>',
            f'<text x="169" y="{y+48}" text-anchor="middle" font-size="12" class="g-y">{sol_m}</text>',

            f'<line x1="322" y1="{ok_y}" x2="368" y2="{ok_y}" class="g-c" stroke-width="2"/>',
            f'<polygon points="376,{ok_y} 366,{ok_y-5} 366,{ok_y+5}" class="g-y"/>',

            f'<rect x="384" y="{y}" width="292" height="68" rx="8" class="g-ya g-ys" stroke-width="1.5"/>',
            f'<text x="530" y="{y+26}" text-anchor="middle" font-size="13" font-weight="700" class="g-yf">{sag_b}</text>',
            f'<text x="530" y="{y+48}" text-anchor="middle" font-size="12" class="g-y">{sag_m}</text>',
        ])
    return svg(W, H, "".join(ic), "Sünnetin Kur’an-ı Kerim’i açıklama ve uygulama örnekleri")


def gorsel_dort_alan():
    """Davranışların İnanç, İbadet, Ahlak ve Sosyal Hayat alanlarına göre sınıflandırılması."""
    W, H = 700, 282
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Kur’an ve Sünnetin Hayatımızdaki Yeri: Dört Temel Sınıflandırma Alanı</text>',
    ]
    kartlar = [
        (
            24, 42, "g-ma g-ms", "g-mf",
            "1. İNANÇ ALANI",
            "• Allah’ın (cc) varlığına ve birliğine iman",
            "• Verilen nimetler için gönülden şükür",
            "• Her durumda Allah’a (cc) güvenip sığınma",
        ),
        (
            362, 42, "g-ta g-ts", "g-tf",
            "2. İBADET ALANI",
            "• Beş vakit namaz kılmak ve Kur’an okumak",
            "• Oruç tutmak, zekât vermek, hacca gitmek",
            "• Samimiyetle Allah’a (cc) dua etmek",
        ),
        (
            24, 162, "g-ya g-ys", "g-yf",
            "3. AHLAK ALANI",
            "• Doğru sözlü olmak ve kırıcı konuşmamak",
            "• Suyu ve nimetleri israf etmemek",
            "• Küçüklere merhamet, büyüklere saygı",
        ),
        (
            362, 162, "g-ma g-ms", "g-mf",
            "4. SOSYAL HAYAT ALANI",
            "• Aileye ve çevreye güler yüzle selam vermek",
            "• Eşyasını paylaşmak ve görevde adil olmak",
            "• Kantinde sıraya girip kul hakkını gözetmek",
        ),
    ]
    for x, y, kutu_cls, bas_cls, baslik, s1, s2, s3 in kartlar:
        cx = x + 157
        ic.extend([
            f'<rect x="{x}" y="{y}" width="314" height="106" rx="9" class="{kutu_cls}" stroke-width="1.5"/>',
            f'<text x="{cx}" y="{y+24}" text-anchor="middle" font-size="13" font-weight="700" class="{bas_cls}">{baslik}</text>',
            f'<line x1="{x+18}" y1="{y+34}" x2="{x+296}" y2="{y+34}" class="g-c" stroke-width="1"/>',
            f'<text x="{cx}" y="{y+54}" text-anchor="middle" font-size="12" class="g-y">{s1}</text>',
            f'<text x="{cx}" y="{y+73}" text-anchor="middle" font-size="12" class="g-y">{s2}</text>',
            f'<text x="{cx}" y="{y+92}" text-anchor="middle" font-size="12" class="g-y">{s3}</text>',
        ])
    return svg(W, H, "".join(ic), "Kur’an ve sünnetin hayatımızdaki yeri: dört temel sınıflandırma alanı")


def gorsel_gunluk_akis():
    """Bir öğrencinin günlük davranışlarının zaman dilimlerine ve alanlara göre çözümlenmesi."""
    W, H = 700, 304
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Bir Günün Çözümlenmesi: Davranışlar ve İlgili Oldukları Alanlar</text>',
    ]
    adimlar = [
        (
            42, "1. Sabah Evde",
            "Uyanınca yeni güne şükreder; yüzünü yıkarken",
            "suyu israf etmez; ailesine güler yüzle selam verir.",
            "İnanç · Ahlak · Sosyal", "g-ma g-ms", "g-mf",
        ),
        (
            106, "2. Okulda / Derste",
            "Kalemini unutan arkadaşıyla yedek kalemini paylaşır;",
            "grup çalışmasında herkesi dinler ve adil görev dağıtır.",
            "Ahlak · Sosyal Hayat", "g-ta g-ts", "g-tf",
        ),
        (
            170, "3. Teneffüste",
            "Kantinde sıraya girerek başkasının hakkına engel olmaz;",
            "konuşurken doğru sözlü olur ve kimseyi incitmez.",
            "Ahlak · Sosyal Hayat", "g-ya g-ys", "g-yf",
        ),
        (
            234, "4. Akşam / Gece",
            "Ödevlerinden sonra ailesiyle namaz kılıp Kur’an okur;",
            "yatmadan önce gününü düşünür ve herkese dua eder.",
            "İbadet · İnanç", "g-ma g-ms", "g-mf",
        ),
    ]
    for y, vakit, s1, s2, alan, r_kutu, r_yazi in adimlar:
        ic.extend([
            f'<rect x="24" y="{y}" width="652" height="54" rx="8" class="g-z g-c" stroke-width="1.2"/>',
            f'<rect x="34" y="{y+10}" width="132" height="34" rx="6" class="{r_kutu}" stroke-width="1.2"/>',
            f'<text x="100" y="{y+32}" text-anchor="middle" font-size="12" font-weight="700" class="{r_yazi}">{vakit}</text>',

            f'<text x="336" y="{y+22}" text-anchor="middle" font-size="12" class="g-y">{s1}</text>',
            f'<text x="336" y="{y+41}" text-anchor="middle" font-size="12" class="g-y">{s2}</text>',

            f'<rect x="508" y="{y+10}" width="156" height="34" rx="6" class="{r_kutu}" stroke-width="1.2"/>',
            f'<text x="586" y="{y+32}" text-anchor="middle" font-size="12" font-weight="700" class="{r_yazi}">{alan}</text>',
        ])
    return svg(W, H, "".join(ic), "Bir günün çözümlenmesi: davranışlar ve ilgili oldukları alanlar")


GORSELLER = {
    "Kur’an ve Sünnet Kavramlarının Sözlük ve Terim Anlamları": gorsel_kavram_cozumlemesi,
    "Sünnetin Kur’an’ı Açıklama ve Uygulamaya Dönüştürme Görevi": gorsel_sunnet_aciklama,
    "Davranışların Dört Temel Alana Göre Sınıflandırılması": gorsel_dort_alan,
    "Bir Günün Çözümlenmesi ve Kur’an-Sünnet Rehberliğini Yorumlama": gorsel_gunluk_akis,
}


def uygula(o):
    for b in o.get("bolumler", []):
        fn = GORSELLER.get(b.get("baslik"))
        if fn:
            b["gorsel"] = fn()
