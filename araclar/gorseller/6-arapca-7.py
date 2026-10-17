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
                       "img", "ozetler", "6-arapca-7")

def gorsel_1():
    img, d = yeni_kart("HARF-İ TARİF (el-) İLE AKRABA VE MESLEK DİYALOGLARI",
                       "6. Sınıf Arapça • 1. Ünite: Akrabalarım • 7. Hafta", C_ORANGE)

    ciz_baslik_kutu(d, 50, 120, 560, 420, "ŞEMSÎ VE KAMERÎ HARFLER (Harf-i Tarif: el-)", C_ORANGE, C_LIGHT_ORANGE)
    ciz_kutu(d, 70, 175, 520, 165, C_WHITE, C_BLUE, r=10)
    d.text((88, 188), "1. KAMERÎ HARFLER (el- Takısındaki 'L' Okunur)", font=font(14, True), fill=C_BLUE)
    d.text((88, 216), "Kural: Kelime başına gelen 'el-' (ال) takısının Lam harfi", font=font(13), fill=C_DARK)
    d.text((88, 236), "cezimli olarak açıkça okunur, sonraki harf şeddelenmez.", font=font(13), fill=C_DARK)
    d.text((88, 266), "Örnekler: el-Ebü (Baba), el-Ümmü (Anne), el-Ceddu (Dede),", font=font(13, True), fill=C_BLUE)
    d.text((88, 290), "el-Ammu (Amca), el-Hâlü (Dayı), el-Mühendisu (Mühendis)", font=font(13, True), fill=C_BLUE)

    ciz_kutu(d, 70, 355, 520, 165, C_WHITE, C_RED, r=10)
    d.text((88, 368), "2. ŞEMSÎ HARFLER (el- Takısındaki 'L' Okunmaz, Şeddelenir)", font=font(14, True), fill=C_RED)
    d.text((88, 396), "Kural: 'el-' takısındaki Lam okunmaz; kelimenin ilk harfi", font=font(13), fill=C_DARK)
    d.text((88, 416), "şeddeli (çift sesli) olarak okunur.", font=font(13), fill=C_DARK)
    d.text((88, 446), "Örnekler: et-Tabîbu (Doktor), et-Tâciru (Tüccar),", font=font(13, True), fill=C_RED)
    d.text((88, 470), "eş-Şurtiyyu (Polis), es-Sâiku (Şoför), en-Neccâru (Marangoz)", font=font(13, True), fill=C_RED)

    ciz_baslik_kutu(d, 640, 120, 590, 420, "AKRABALARIM VE MESLEKLERİ DİYALOG KALIPLARI", C_TEAL, C_LIGHT_GREEN)
    kaliplar = [
        ("Men hâzâ? / Men hâzihî?", "Bu kimdir? (Erkek / Kadın için)", C_TEAL),
        ("Hâzâ ammî. Hüve mühendisün.", "Bu benim amcamdır. O bir mühendistir.", C_BLUE),
        ("Hâzihî ammetî. Hiye tabîbetün.", "Bu benim halamdır. O bir kadın doktordur.", C_PURPLE),
        ("Mâ mihnetü hâlike?", "Senin dayının mesleği nedir?", C_ORANGE),
        ("Hâlî muallimün fî'l-medreseti.", "Dayım okulda bir öğretmendir.", C_GREEN)
    ]
    y = 175
    for ar, tr, renk in kaliplar:
        ciz_kutu(d, 660, y, 550, 62, C_WHITE, renk, r=8)
        d.text((678, y + 10), ar, font=font(14, True), fill=renk)
        d.text((678, y + 34), tr, font=font(13), fill=C_DARK)
        y += 70

    ciz_kutu(d, 50, 560, 1180, 75, C_LIGHT_YELLOW, C_ORANGE, r=12)
    ortali_yazi(d, "Ünite Özeti: Erkek akraba/meslek için 'Hâzâ - Hüve', kadın akraba/meslek (sonunda -tün/-etün olan) için 'Hâzihî - Hiye' kullanılır.", 597, font(14, True), C_DARK)

    kaydet(img, os.path.join(OUT_DIR, "gorsel_1.png"))

if __name__ == "__main__":
    gorsel_1()
