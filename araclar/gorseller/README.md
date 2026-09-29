Ders başına görsel modülleri. Dosya adı özet JSON'unun adıyla aynıdır (ör. `9-fizik-1.py` ↔ `ozetler/9-fizik-1.json`).
Her modül `def uygula(o)` tanımlar ve `o['bolumler'][i]['gorsel']` (ya da örnek/etkinlik görseli) alanına SVG yazar.
Yardımcılar: `from ozet_gorsel import svg, ok_isareti, dugum, dal` (renk sınıfları stil.css "Özet görselleri": g-mf/g-ma/g-ms mavi, g-tf/g-ta/g-ts turuncu,
g-yf/g-ya/g-ys yeşil, g-of/g-oa/g-os mor, g-c çizgi, g-y metin, g-s soluk, g-b beyaz). Kurallar AGENTS.md: estetik, renkli, anlamlı renk,
çizgi yazıya değmez, harf ok ucuna binmez, yazılar ≥ 11 punto, taşma yok.
