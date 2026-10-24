# Ders Kutusu

**https://derskutusu.com** — 5–12. sınıf öğrencileri ve öğretmenleri için ücretsiz eğitim sitesi.

Sitede haftalık konu özetleri, etkileşimli etkinlikler, akıllı tahta için sunum ve kalem aracı, yazılı kâğıtları, yıllık ve günlük planlar ile MEB ders kitaplarına resmî bağlantılar vardır. İçerik, Türkiye Yüzyılı Maarif Modeli ders kitaplarına dayanır ve özgün yazılır.

## Klasörler

| Klasör | İçerik |
|---|---|
| `public/` | Yayımlanan site: sayfalar, konu özetleri (`ozet/`), yazılılar, planlar, betikler ve veri dosyaları (`veri/`) |
| `araclar/` | Sayfaları, özetleri ve site haritasını üreten Python betikleri; site denetimleri |
| `sosyal/` | Sosyal medya paylaşım kuyruğu ve görselleri |
| `tests/` | Tarayıcıda çalışan otomatik denetimler (ders slaytı) |
| `.github/workflows/` | GitHub Actions iş akışları |

## Yayın ve otomatik işler

Site GitHub Pages'te yayımlanır; `main` dalına gelen her değişiklik birkaç dakika içinde canlıya çıkar.

| İş akışı | Görevi |
|---|---|
| Akışları güncelle ve yayımla | Siteyi derler, ziyaret sayısını ve sosyal medya akışlarını saatte bir yeniler, Pages'e yayımlar |
| Site nöbetçisi | Sitenin açık olduğunu ve resmî bağlantıları denetler; sorun bulursa "Sorunlar" bölümüne yazar |
| Sosyal medya paylaşımı | Onaylı kuyruktaki gönderileri paylaşır |
| Ders slaytı tarayıcı kontrolü | Sunum, etkinlik, kalem ve dar ekran davranışını Chromium ve WebKit'te sınar |
| Kategori önizlemesi | Ders kapsamını ve kategori sayfalarını denetler |
| Haftalık özetleri Claude API ile üret | Elle başlatılır; seçilen haftanın konu özetlerini, görsellerini ve sosyal medya kartlarını Max planının API kredisiyle üretir |

## Yerelde önizleme

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory public
```

Ardından tarayıcıda `http://127.0.0.1:8765` açılır.

Kurulum, alan adı, e-posta ve hesap ayrıntıları için [KURULUM.md](KURULUM.md) dosyasına bakın.

## Gizlilik

Ziyaret sayımı çerezsiz Cloudflare sayacıyla yapılır. Reklam betiği yalnız ziyaretçi izin verirse yüklenir. Ayrıntılar: https://derskutusu.com/gizlilik.html
