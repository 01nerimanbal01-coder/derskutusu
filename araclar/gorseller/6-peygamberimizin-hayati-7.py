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
                       "img", "ozetler", "6-peygamberimizin-hayati-7")

def gorsel_1():
    img, d = yeni_kart("VAHYİN GELİŞİ: HİRA MAĞARASI VE İLK VAHİY (610)",
                       "6. Sınıf Peygamberimizin Hayatı • 1. Ünite • 7. Hafta", C_PURPLE)

    ciz_baslik_kutu(d, 50, 120, 560, 420, "İLK VAHİY SÜRECİ (MİLADİ 610 - RAMAZAN)", C_PURPLE, C_LIGHT_PURPLE)
    adimlar = [
        ("1. Hira'da İnziva (Tahannüs)", "40 yaşına yaklaşan Hz. Muhammed (s.a.v.), Nur Dağı'ndaki Hira Mağarası'nda tefekkür ederdi.", C_PURPLE),
        ("2. Vahiy Meleği Cebrail (a.s.)", "610 yılı Ramazan ayında Kadir Gecesi'nde Cebrail (a.s.) gelerek 'İkra!' (Oku!) buyurdu.", C_BLUE),
        ("3. Alak Suresi 1-5. Ayetler", "'Yaratan Rabbinin adıyla oku! O, insanı alaktan yarattı... Kalemle yazmayı öğretti.'", C_GREEN),
        ("4. Hz. Hatice ve Varaka Desteği", "İlk Müslüman Hz. Hatice onu teskin etti; bilgin Varaka bin Nevfel peygamberliği müjdeledi.", C_ORANGE)
    ]
    y = 175
    for bas, acik, renk in adimlar:
        ciz_kutu(d, 70, y, 520, 78, C_WHITE, renk, r=10)
        d.text((88, y + 10), bas, font=font(14, True), fill=renk)
        sarili_yazi(d, acik, 88, y + 34, 490, font(13), C_DARK)
        y += 88

    ciz_baslik_kutu(d, 640, 120, 590, 420, "İLK İMAN EDENLER (SÂBİKÛN-İ EVVELÛN)", C_TEAL, C_LIGHT_GREEN)
    ilkler = [
        ("Hz. Hatice (r.a.)", "Peygamberimizin vefakâr eşi — İlk Müslüman (Kadınlardan ilk)", C_TEAL),
        ("Hz. Ali (r.a.)", "Peygamberimizin yanında büyüyen kuzeni — Çocuklardan ilk", C_BLUE),
        ("Hz. Zeyd bin Hârise (r.a.)", "Peygamberimizin azatlısı ve manevi evladı — Azatlılardan ilk", C_GREEN),
        ("Hz. Ebû Bekir (r.a.)", "Peygamberimizin en yakın dostu (es-Sıddîk) — Hür erkeklerden ilk", C_ORANGE)
    ]
    y = 180
    for isim, unvan, renk in ilkler:
        ciz_kutu(d, 660, y, 550, 74, C_WHITE, renk, r=10)
        d.text((680, y + 12), isim, font=font(16, True), fill=renk)
        d.text((680, y + 40), unvan, font=font(13, True), fill=C_DARK)
        y += 86

    ciz_kutu(d, 50, 560, 1180, 75, C_LIGHT_YELLOW, C_ORANGE, r=12)
    ortali_yazi(d, "İlk vahiy 'Oku!' (İkra) emriyle başlamış; İslam dini ilme, okumaya, kaleme ve düşünmeye en üstün değeri vermiştir.", 597, font(15, True), C_DARK)

    kaydet(img, os.path.join(OUT_DIR, "gorsel_1.png"))

if __name__ == "__main__":
    gorsel_1()
