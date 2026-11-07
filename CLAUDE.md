# Ders Kutusu — çalışma notları (her oturumda okunur)

derskutusu.com: 5–12. sınıf için ücretsiz eğitim sitesi (GitHub Pages, `public/`). Üretici betikler `araclar/`,
tarayıcı testleri `tests/`, iş akışları `.github/workflows/`. Ayrıntı: README.md ve KURULUM.md. Adlandırma ve
yorumlar Türkçedir; betikler yalnız standart kütüphane kullanır (isteğe bağlı araçlar yoksa ilgili adım atlanır).

## Sekiz Kapı denetim sistemi (kurulu; yeniden kurma, buradan çalıştır)

Site kontrolü, soru bütünlüğü, üst üste binme ve veri tutarlılığı **tek araçla** denetlenir:

```bash
python3 araclar/sekiz_kapi.py --hizli      # değişiklik sonrası (1-2 dk): yayın denetimi hızlı, PDF binme taraması yok
python3 araclar/sekiz_kapi.py              # tam denetim (5-8 dk): 1-7. kapılar; tarayıcı varsa 6. kapı dahil
python3 araclar/sekiz_kapi.py --kapi 2,3   # yalnız seçilen kapılar
python3 araclar/sekiz_kapi.py --canli      # 8. kapı: canlı derskutusu.com
```

| Kapı | Denetim | Kaynak |
|---|---|---|
| 1 | Yayın denetimi: özet şeması, kök/gösterim, kesir, derleme senkronu | `araclar/yayin_denetle.py`, `kok_yayin_denetle.py` |
| 2 | Soru bütünlüğü: özet etkinlik/örnekleri, çalışma kâğıdı ve KPSS soruları, ASDS cevap anahtarları | `sekiz_kapi.py` → `kapi_2` |
| 3 | Tekrar ve çakışma: aynı soru iki kez, haftalar arası kopya, dosya adı/alan uyuşmazlığı, katalog/sitemap/kuyruk tekrarı | `kapi_3` |
| 4 | Bağlantı ve dosya: HTML iç bağlantıları, veri dosyalarının işaret ettiği dosyalar, sitemap, JS söz dizimi | `kapi_4` |
| 5 | PDF kitapçıklar: açılıyor mu, sayfa sayısı, site üretimi PDF'lerde üst üste binen kelimeler (pdftotext -bbox) | `kapi_5` |
| 6 | Yerleşim: gerçek Chromium'da yatay taşma, üst üste binen metin, betik hatası | `tests/sekiz-kapi-yerlesim.cjs` |
| 7 | Veri tutarlılığı: JSON geçerliliği, katalog alanları, ASDS/yazılı/plan/kelime/sosyal kuyruk | `kapi_7` |
| 8 | Canlı site (yalnız `--canli`): sayfalar, DNS, sertifika, yayın güncelliği | `araclar/nobetci.py` |

- Rapor `sekiz-kapi-sonuc/` klasörüne yazılır (`rapor.md`, `rapor.json`, `yerlesim.json`, `ekran/`); klasör git dışıdır.
- Çıkış kodu: herhangi bir kapıda hata varsa 1. "Uyarı" kapıyı kapatmaz.
- GitHub'da `.github/workflows/sekiz-kapi.yml` ana dala her gönderimde ve çekme isteklerinde çalışır; pazar sabahı
  canlı siteyle tam denetim yapar, kapalı kapı varsa `sekiz-kapi` etiketli issue açar.
- Yeni bir denetim gerekince **yeni araç yazma**: ilgili `kapi_N` fonksiyonuna ekle; tarayıcı ölçümü gerekiyorsa
  `tests/sekiz-kapi-yerlesim.cjs` içindeki `sayfaOlc` fonksiyonunu genişlet. Bulgu seviyesi: veriyi bozan ya da
  ziyaretçinin göreceği şey `hata`, biçim/öneri `uyarı`.
- Ana dala göndermeden önce en az `--hizli` çalıştır; içerik (özet, çalışma kâğıdı, PDF) değiştiyse tam denetim.

## Bulut oturumu kurulumu (kendiliğinden)

`.claude/hooks/session-start.sh` her Claude Code bulut oturumunda çalışır: poppler-utils, pypdf ve bulut imajındaki
Playwright ile aynı sürümde `@playwright/test` (`~/.derskutusu-qa`, depo dışı) hazırlanır; `NODE_PATH` ve
`PLAYWRIGHT_BROWSERS_PATH` oturuma yazılır. Elle kurulum gerekmez; ortam ayarlarındaki "Kurulum betiği" boş kalabilir.
Tarayıcılar `/opt/pw-browsers` altındadır; `playwright install` çalıştırma (sürüm uyuşmaz). WebKit bulut imajında yoktur:
`tests/ders-slayt.cjs` gibi WebKit isteyen eski testler orada yalnız CI'da tam çalışır.

## Diğer kurallar

- Düz kök işareti (√ ∛ ∜) hiçbir kaynakta kullanılmaz; `{kok:...}` gösterimi ve `kok_yayin_denetle.py` bunu korur.
- Özet JSON şeması ve otomatik onarım: `python3 araclar/yayin_denetle.py --onar` (derleme + denetim).
- `public/veri/youtube.json`, `instagram.json`, `ziyaret.json`, `indirmeler.json` botlar yazar; elle değiştirme.
- `main` dalına giden her değişiklik birkaç dakika içinde yayına çıkar; deneme işi dalda yapılır.
