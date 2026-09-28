# Ders Kutusu — kurulum ve bakım

Site adresi: **https://derskutusu.com**. Site GitHub Pages'te ücretsiz yayımlanır. GitHub her sabah 07.17'de YouTube'daki (anahtar girilirse Instagram'daki) yeni paylaşımları alır ve siteyi kendiliğinden yeniler. Depoya yapılan her değişiklik de birkaç dakika içinde yayına çıkar.

Hesap açma, giriş ve anahtar/şifre girme işlerini siz yaparsınız. Anahtarları kimseye yazmayın; doğrudan GitHub'daki gizli alana girin.

## Kurulu olanlar
| Parça | Durum |
|---|---|
| Barındırma | GitHub deposu `derskutusu`, Settings → Pages → Source: GitHub Actions, özel alan adı `derskutusu.com` |
| Alan adları | derskutusu.com (asıl), .net, .info, .online, .com.tr; hepsi 28.09.2027'ye kadar kayıtlı, otomatik yenileme kapalı |
| DNS (derskutusu.com) | A @ → 185.199.108.153, .109, .110, .111; CNAME www → GitHub Pages; MX → mx/mx2/mx3.zoho.eu; TXT SPF, DKIM (zmail._domainkey), Zoho doğrulama |
| E-posta | info@derskutusu.com, Zoho Mail ücretsiz plan (mail.zoho.eu) |
| YouTube | https://www.youtube.com/@derskutusuinfo |
| Instagram | https://www.instagram.com/derskutusuinfo/ (profesyonel hesap) |
| Facebook | https://www.facebook.com/derskutusuinfo (sayfa) |

## Sitedeki dosyalar
- `public/veri/ayarlar.json`: site adı, slogan, açıklama, hesap adresleri, e-posta.
- `public/veri/icerikler.json`: içerik kartları (başlık, ders, sınıf, tür, açıklama, bağlantı). Liste boşken sitede tanıtım kartları görünür.
- `public/veri/youtube.json`, `instagram.json`: `araclar/akis_guncelle.py` üretir; elle değiştirilmez.
- `public/gizlilik.html` (gizlilik ve çerezler), `404.html`, `robots.txt`, `sitemap.xml`, simgeler ve paylaşım görseli (`paylasim.png`).

## Instagram paylaşımlarının kendiliğinden gelmesi (isteğe bağlı)
Bu adım yapılmazsa Instagram gönderileri siteye bağlantılarıyla tek tek eklenir.
1. developers.facebook.com'da ücretsiz bir uygulama oluşturun. Uygulamaya **Instagram** ürününü ekleyin, "Instagram girişiyle API kurulumu" bölümünden @derskutusuinfo hesabını bağlayın ve **erişim anahtarı** oluşturun.
2. GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret**: ad `IG_TOKEN`, değer bu anahtar.
3. İsteğe bağlı: anahtarın kendiliğinden yenilenip GitHub'a yazılması için yalnız bu depoya "Secrets: Read and write" izni olan bir fine-grained token oluşturup `GH_PAT` adıyla ekleyin. Eklemezseniz anahtar 60 günde bir yenilenmelidir.

## Bilinmesi gerekenler
- Depoda 60 gün hiç etkinlik olmazsa GitHub zamanlanmış çalışmayı durdurur ve e-postayla haber verir; Actions sekmesinden yeniden açılır.
- Alan adlarının süresi 28.09.2027'de doluyor. Yenilemeden önce daha ucuz bir firmaya taşınması düşünülmeli.
- Ziyaretçi bir düğmeye basmadıkça tarayıcısı YouTube, Instagram ya da Facebook'a bağlanmaz; görseller sitenin kendisinden gelir (KVKK açısından güvenli düzen, ayrıntı `gizlilik.html`).
- Yerelde deneme: `python3 -m http.server 8765 --directory public`, sonra `http://127.0.0.1:8765`.
