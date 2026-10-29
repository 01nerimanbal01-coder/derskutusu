# Ders Kutusu

**https://derskutusu.com** — 5–12. sınıf öğrencileri ve öğretmenleri için ücretsiz eğitim sitesi.

Sitede haftalık konu özetleri, etkileşimli etkinlikler, akıllı tahta için sunum ve kalem aracı, yazılı kâğıtları, yıllık ve günlük planlar ile MEB ders kitaplarına resmî bağlantılar vardır. İçerik, Türkiye Yüzyılı Maarif Modeli ders kitaplarına dayanır ve özgün yazılır.

## Klasörler

| Klasör | İçerik |
|---|---|
| `public/` | Yayımlanan site: sayfalar, konu özetleri (`ozet/`), yazılılar, planlar, betikler ve veri dosyaları (`veri/`) |
| `araclar/` | Sayfaları, özetleri ve site haritasını üreten Python betikleri; site denetimleri (`sekiz_kapi.py`) |
| `sosyal/` | Sosyal medya paylaşım kuyruğu ve görselleri |
| `tests/` | Tarayıcıda çalışan otomatik denetimler (ders slaytı, yerleşim) |
| `.claude/` | Claude Code bulut oturumu başlangıç kancası (denetim araçlarını kendiliğinden kurar) |
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
| Sekiz Kapı denetimi | Ana dala her gönderimde ve çekme isteklerinde siteyi, soruları ve kitapçıkları sekiz kapıdan geçirir; pazar sabahı canlı siteyle tam denetim yapar, kapalı kapı varsa issue açar |
| Haftalık özetleri Claude API ile üret | Elle başlatılır; seçilen haftanın konu özetlerini, görsellerini ve sosyal medya kartlarını Max planının API kredisiyle üretir. İki saatte bir de kendiliğinden çalışıp biten toplu isteklerin sonuçlarını yazar ve yayımlar |

## Denetim: Sekiz Kapı

Yayından önce site, sorular ve kitapçıklar sekiz kapıdan geçer (yayın denetimi, soru bütünlüğü, tekrar ve çakışma, bağlantı ve dosya, PDF kitapçıklar, tarayıcıda yerleşim, veri tutarlılığı, canlı site):

```bash
python3 araclar/sekiz_kapi.py --hizli
```

Tam denetim için `--hizli` kaldırılır; rapor `sekiz-kapi-sonuc/rapor.md` dosyasına yazılır. Ayrıntı: [KURULUM.md](KURULUM.md#sekiz-kapı-denetimi).

## Yerelde önizleme

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory public
```

Ardından tarayıcıda `http://127.0.0.1:8765` açılır.

Kurulum, alan adı, e-posta ve hesap ayrıntıları için [KURULUM.md](KURULUM.md) dosyasına bakın.

## Gizlilik

Ziyaret sayımı çerezsiz Cloudflare sayacıyla yapılır. Reklam betiği yalnız ziyaretçi izin verirse yüklenir. Ayrıntılar: https://derskutusu.com/gizlilik.html
