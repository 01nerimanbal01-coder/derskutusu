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
                       "img", "ozetler", "6-kuran-i-kerim-7")

def gorsel_1():
    img, d = yeni_kart("SALLİ VE BARİK DUALARI İLE ANLAMLARI",
                       "6. Sınıf Kur'an-ı Kerim • 1. Ünite • 7. Hafta", C_GREEN)

    ciz_baslik_kutu(d, 50, 120, 560, 420, "ALLAHÜMME SALLİ DUASI", C_GREEN, C_LIGHT_GREEN)
    ciz_kutu(d, 70, 175, 520, 165, C_WHITE, C_GREEN, r=10)
    d.text((88, 188), "OKUNUŞU:", font=font(14, True), fill=C_GREEN)
    salli_okunus = [
        "Allâhümme salli alâ Muhammedin",
        "ve alâ âli Muhammed.",
        "Kemâ salleyte alâ İbrâhîme",
        "ve alâ âli İbrâhîm.",
        "İnneke hamîdün mecîd."
    ]
    y = 212
    for s in salli_okunus:
        d.text((95, y), s, font=font(14, True), fill=C_DARK)
        y += 24

    ciz_kutu(d, 70, 355, 520, 165, C_WHITE, C_TEAL, r=10)
    d.text((88, 368), "TÜRKÇE ANLAMI:", font=font(14, True), fill=C_TEAL)
    salli_anlam = (
        "Allah'ım! حضرت İbrahim'e ve İbrahim'in ailesine "
        "rahmet ettiğin gibi Muhammed'e ve Muhammed'in "
        "ailesine de rahmet et (şerefini yücelt). "
        "Şüphesiz Sen övülmeye layık ve şanı yüce olansın."
    )
    sarili_yazi(d, "Allah'ım! İbrahim'e ve İbrahim'in ailesine rahmet ettiğin gibi, Muhammed'e ve Muhammed'in ailesine de rahmet et. Şüphesiz Sen övülmeye layık (Hamîd) ve şanı yüce (Mecîd) olansın.", 90, 396, 480, font(13), C_DARK)

    ciz_baslik_kutu(d, 640, 120, 590, 420, "ALLAHÜMME BARİK DUASI", C_BLUE, C_LIGHT_BLUE)
    ciz_kutu(d, 660, 175, 550, 165, C_WHITE, C_BLUE, r=10)
    d.text((678, 188), "OKUNUŞU:", font=font(14, True), fill=C_BLUE)
    barik_okunus = [
        "Allâhümme bârik alâ Muhammedin",
        "ve alâ âli Muhammed.",
        "Kemâ bârekte alâ İbrâhîme",
        "ve alâ âli İbrâhîm.",
        "İnneke hamîdün mecîd."
    ]
    y = 212
    for s in barik_okunus:
        d.text((685, y), s, font=font(14, True), fill=C_DARK)
        y += 24

    ciz_kutu(d, 660, 355, 550, 165, C_WHITE, C_PURPLE, r=10)
    d.text((678, 368), "TÜRKÇE ANLAMI:", font=font(14, True), fill=C_PURPLE)
    sarili_yazi(d, "Allah'ım! İbrahim'i ve İbrahim'in ailesini mübarek (bereketli) kıldığın gibi, Muhammed'i ve Muhammed'in ailesini de mübarek kıl. Şüphesiz Sen övülmeye layık (Hamîd) ve şanı yüce (Mecîd) olansın.", 680, 396, 510, font(13), C_DARK)

    ciz_kutu(d, 50, 560, 1180, 75, C_LIGHT_YELLOW, C_ORANGE, r=12)
    ortali_yazi(d, "Salli ve Barik duaları namazların son oturuşunda (Ka'de-i Ahîre) Ettehiyyâtü duasından sonra ve cenaze namazında 2. tekbirden sonra okunur.", 597, font(14, True), C_DARK)

    kaydet(img, os.path.join(OUT_DIR, "gorsel_1.png"))

if __name__ == "__main__":
    gorsel_1()
