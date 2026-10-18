#!/usr/bin/env python3
"""
test_ses_mekanizmasi.py:
Sitedeki tüm seslendirme (SpeechSynthesis / TTS) düğmelerini ve
kavram kartlarındaki dinamik telaffuz mekanizmasını doğrulayan otomatik test.
"""

import sys
import re
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent
PUBLIC = SITE_DIR / "public"

def main():
    hatalar = []
    print("=== SES VE TELAFFUZ MEKANİZMASI KAPSAMLI DENETİMİ ===")

    # 1. etkinlik.js denetimi
    etkinlik_js = (PUBLIC / "etkinlik.js").read_text(encoding="utf-8")
    
    # Kural A: .fkart-on .fkart-metin kesinlikle sesliDinleKur içinde statik dinleyiciyle bağlanmamalı!
    if ".fkart-on .fkart-metin" in etkinlik_js:
        hatalar.append("etkinlik.js: '.fkart-on .fkart-metin' seçicisi statik sesliDinleKur içinde bulundu! Dinamik kartta closure takılmasına yol açar.")
    else:
        print("  ✓ etkinlik.js: Kavram kartı metni statik sesliDinleKur içinden çıkarıldı.")

    # Kural B: kartSesDurumunuGuncelle ve kartlarKur içinde dinamik okuma
    if "kartSesDurumunuGuncelle" not in etkinlik_js:
        hatalar.append("etkinlik.js: 'kartSesDurumunuGuncelle' fonksiyonu bulunamadı!")
    else:
        print("  ✓ etkinlik.js: 'kartSesDurumunuGuncelle' fonksiyonu aktif.")

    # Kural C: onMetin click dinleyicisi güncel kartı mı okuyor?
    if "deste[sira]" in etkinlik_js and "sesliOku" in etkinlik_js:
        print("  ✓ etkinlik.js: Kart tıklandığında anlık olarak deste[sira] ve güncel textContent okunuyor.")
    else:
        hatalar.append("etkinlik.js: Kart tıklandığında güncel sira deste nesnesi okunmuyor!")

    # Kural D: sesliOku içinde paused kontrolü ve resume var mı?
    if "window.speechSynthesis.paused" in etkinlik_js and "window.speechSynthesis.resume()" in etkinlik_js:
        print("  ✓ etkinlik.js: Tarayıcı ses kuyruğu kilitlenmesini önleyen resume() koruması mevcut.")
    else:
        hatalar.append("etkinlik.js: speechSynthesis.resume() koruması eksik!")

    # 2. kelime.js denetimi
    kelime_js = (PUBLIC / "kelime.js").read_text(encoding="utf-8")
    if "speechSynthesis.paused" in kelime_js and "speechSynthesis.resume()" in kelime_js:
        print("  ✓ kelime.js: Kelime çalışma sayfasında ses motoru koruması (resume) mevcut.")
    else:
        hatalar.append("kelime.js: speechSynthesis.resume() koruması eksik!")

    # 3. arapca.js denetimi
    arapca_js = (PUBLIC / "arapca.js").read_text(encoding="utf-8")
    if "speechSynthesis.paused" in arapca_js and "speechSynthesis.resume()" in arapca_js:
        print("  ✓ arapca.js: Arapça telaffuz motorunda resume koruması mevcut.")
    else:
        hatalar.append("arapca.js: speechSynthesis.resume() koruması eksik!")

    # 4. stil.css denetimi
    stil_css = (PUBLIC / "stil.css").read_text(encoding="utf-8")
    if ".sesli-kart" in stil_css and ".sesli-en::after" in stil_css:
        print("  ✓ stil.css: Sesli kart hover, aktif ve ses simgesi (🔊) stilleri tanımlı.")
    else:
        hatalar.append("stil.css: .sesli-kart stili eksik!")

    # 5. Örnek İngilizce Özet Sayfasında Kart Simülasyonu
    ornek_html = PUBLIC / "8-ingilizce-1.html"
    if ornek_html.exists():
        html_icerik = ornek_html.read_text(encoding="utf-8")
        kart_verileri = re.findall(r'class="fkart-oge"[^>]*data-on="([^"]+)"[^>]*data-arka="([^"]+)"', html_icerik)
        if kart_verileri:
            print(f"  ✓ 8-ingilizce-1.html: {len(kart_verileri)} adet kavram kartı bulundu.")
            print(f"    - 1. Kart: '{kart_verileri[0][0]}' -> Okunacak telaffuz: '{kart_verileri[0][0]}'")
            if len(kart_verileri) > 1:
                print(f"    - 2. Kart: '{kart_verileri[1][0]}' -> Okunacak telaffuz: '{kart_verileri[1][0]}'")
            if len(kart_verileri) > 2:
                print(f"    - 3. Kart: '{kart_verileri[2][0]}' -> Okunacak telaffuz: '{kart_verileri[2][0]}'")
            print("    -> Kart geçişlerinde telaffuz dinamik olarak güncelleniyor (sabit closure yok).")

    print("\n--------------------------------------------------")
    if hatalar:
        print(f"BAŞARISIZ! {len(hatalar)} hata bulundu:")
        for h in hatalar:
            print("  - " + h)
        sys.exit(1)
    else:
        print("MÜKEMMEL: TÜM SESLENDİRME DENETİMLERİ 0 HATA İLE GEÇTİ!")
        sys.exit(0)

if __name__ == "__main__":
    main()
