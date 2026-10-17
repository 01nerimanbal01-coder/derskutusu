from PIL import Image, ImageDraw
import os
from yardimci import (
    W, H, C_BG, C_WHITE, C_DARK, C_TEXT, C_MUTED, C_BORDER,
    C_BLUE, C_GREEN, C_ORANGE, C_RED, C_PURPLE, C_TEAL, C_YELLOW,
    C_LIGHT_BLUE, C_LIGHT_GREEN, C_LIGHT_ORANGE, C_LIGHT_RED, C_LIGHT_PURPLE, C_LIGHT_YELLOW,
    font, yeni_kart, kaydet, ciz_kutu, ciz_baslik_kutu, ciz_etiket, ortali_yazi,
    sarili_yazi, ciz_ok, ciz_tablo
)

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                       "img", "ozetler", "6-din-kulturu-ve-ahlak-bilgisi-7")

def gorsel_1():
    img, d = yeni_kart("BİR SURE ÖĞRENİYORUM: FELAK SURESİ VE ANLAMI",
                       "6. Sınıf Din Kültürü ve Ahlak Bilgisi • 1. Ünite • 7. Hafta", C_TEAL)

    ciz_baslik_kutu(d, 50, 120, 560, 420, "FELAK SURESİ KÜNYESİ VE OKUNUŞU", C_TEAL, C_LIGHT_GREEN)
    bilgiler = [
        ("İniş Yeri ve Ayet:", "Mekke'de inmiştir, 5 ayettir. 113. suredir."),
        ("Felak Kelimesi:", "'Sabah aydınlığı, karanlığı yarıp çıkan ışık' demektir."),
        ("Muavvizeteyn:", "Felak ve Nâs surelerine 'iki koruyucu' (Muavvizeteyn) denir.")
    ]
    y = 175
    for b, a in bilgiler:
        ciz_kutu(d, 70, y, 520, 44, C_WHITE, C_TEAL, r=8)
        d.text((85, y + 12), b, font=font(14, True), fill=C_TEAL)
        d.text((240, y + 12), a, font=font(13), fill=C_DARK)
        y += 52

    ciz_kutu(d, 70, 340, 520, 185, C_WHITE, C_GREEN, r=10)
    d.text((90, 352), "OKUNUŞU (Bismillâhirrahmânirrahîm):", font=font(14, True), fill=C_GREEN)
    ayetler = [
        "1. Kul eûzü birabbil-felak.",
        "2. Min şerri mâ halak.",
        "3. Ve min şerri gâsikın izâ vekab.",
        "4. Ve min şerrin-neffâsâti fil-ukad.",
        "5. Ve min şerri hâsidin izâ hased."
    ]
    ay_y = 378
    for ay in ayetler:
        d.text((95, ay_y), ay, font=font(14, True), fill=C_DARK)
        ay_y += 28

    ciz_baslik_kutu(d, 640, 120, 590, 420, "FELAK SURESİNDE ALLAH'A SIĞINILAN KÖTÜLÜKLER", C_PURPLE, C_LIGHT_PURPLE)
    anlamlar = [
        ("1. Ayet: Sabahın Rabbine Sığınma", "De ki: Yarattığı şeylerin kötülüğünden sabahın Rabbine sığınırım.", C_TEAL),
        ("2. Ayet: Yaratılmışların Şerri", "Görünür-görünmez tüm zararlı varlıkların kötülüğünden korunma.", C_BLUE),
        ("3. Ayet: Çöken Karanlığın Şerri", "Karanlığı çöktüğü zaman gecenin ve içindeki tehlikelerin şerri.", C_PURPLE),
        ("4. Ayet: Düğümlere Üfleyenler", "İnsanların arasını bozan, fitne ve büyü peşinde koşanların şerri.", C_ORANGE),
        ("5. Ayet: Kıskanç (Hasetçi) Şerri", "Başkasının nimetini çekemeyen hasetçinin kıskandığı zamanki şerri.", C_RED)
    ]
    y = 175
    for bas, acik, renk in anlamlar:
        ciz_kutu(d, 660, y, 550, 62, C_WHITE, renk, r=8)
        d.text((675, y + 10), bas, font=font(14, True), fill=renk)
        d.text((675, y + 34), acik, font=font(13), fill=C_DARK)
        y += 70

    ciz_kutu(d, 50, 560, 1180, 75, C_LIGHT_YELLOW, C_ORANGE, r=12)
    ortali_yazi(d, "Peygamberimiz (s.a.v.) her gece yatmadan önce İhlas, Felak ve Nâs surelerini okuyup ellerine üfler ve vücudunu mesh ederdi.", 597, font(15, True), C_DARK)

    kaydet(img, os.path.join(OUT_DIR, "gorsel_1.png"))

if __name__ == "__main__":
    gorsel_1()
