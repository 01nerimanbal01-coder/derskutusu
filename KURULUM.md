# Ders Kutusu — kurulum ve bakım

Site adresi: **https://derskutusu.com**. Site GitHub Pages'te ücretsiz yayımlanır. GitHub her sabah 07.17'de YouTube'daki (anahtar girilirse Instagram'daki) yeni paylaşımları alır ve siteyi kendiliğinden yeniler. Depoya yapılan her değişiklik de birkaç dakika içinde yayına çıkar.

Hesap açma, giriş ve anahtar/şifre girme işlerini siz yaparsınız. Anahtarları kimseye yazmayın; doğrudan GitHub'daki gizli alana girin.

## Kurulu olanlar
| Parça | Durum |
|---|---|
| Barındırma | GitHub deposu `derskutusu`, Settings → Pages → Source: GitHub Actions, özel alan adı `derskutusu.com`, HTTPS zorunlu (Let's Encrypt sertifikasını GitHub kendisi yeniler) |
| Alan adları | derskutusu.com (asıl), .net, .info, .online, .com.tr; hepsi 28.09.2027'ye kadar kayıtlı (.com.tr 27.09.2027), otomatik yenileme kapalı |
| Yönlendirmeler | Turkticaret → Domain Yönlendirme: .net, .info, .online, .com.tr (ana ad + www) → https://derskutusu.com, 301 kalıcı, sayfa yolu korunur, SSL etkin |
| DNS (derskutusu.com) | A @ → 185.199.108.153, .109, .110, .111; CNAME www → GitHub Pages; MX → mx/mx2/mx3.zoho.eu; TXT SPF, DKIM (zmail._domainkey), DMARC (_dmarc, p=none), Zoho ve Google doğrulama |
| E-posta | info@derskutusu.com, Zoho Mail ücretsiz plan (mail.zoho.eu). Sitelerin gönderdiği bildirim ve kod e-postaları Zoho'da **Notification** klasörüne düşer. |
| Google arama | Search Console'da alan mülkü `derskutusu.com` (Google hesabıyla), site haritası `https://derskutusu.com/sitemap.xml` |
| YouTube | https://www.youtube.com/@derskutusuinfo |
| Instagram | https://www.instagram.com/derskutusuinfo/ (profesyonel hesap) |
| Facebook | https://www.facebook.com/derskutusuinfo (sayfa) |

## Sitedeki dosyalar
- `public/veri/ayarlar.json`: site adı, slogan, açıklama, hesap adresleri, e-posta.
- `public/veri/icerikler.json`: içerik kartları (başlık, ders, sınıf, tür, açıklama, bağlantı). Liste boşken sitede tanıtım kartları görünür.
- `public/veri/youtube.json`, `instagram.json`: `araclar/akis_guncelle.py` üretir; elle değiştirilmez.
- `public/gizlilik.html` (gizlilik ve çerezler), `404.html`, `robots.txt`, `sitemap.xml`, simgeler ve paylaşım görseli (`paylasim.png`).

## Sosyal medya kartları
- `araclar/sosyal/<kimlik>.json`: her "Bunu biliyor muydunuz?" kartının metni (`ozet`, `baslik`, `paragraflar`, `bilgi`). Kimlik `bilgi-<sınıf>-<ders>-<hafta>` biçimindedir (Din Kültürü → `din-kulturu`, İnkılap Tarihi → `inkilap-tarihi`).
- `python3 araclar/sosyal_gorsel.py`: görseli olmayan kartları `public/sosyal/<kimlik>.png` olarak üretir (1080×1350, Poppins yazı tipi `araclar/fontlar/`). `--kuyruk 2026-10-13T09:00` ile kuyrukta olmayan kartları günde 6 gönderi (09–19, iki saat arayla) olacak biçimde `sosyal/kuyruk.json`'a ekler.
- Paylaşım: `IG_TOKEN` (Instagram, aşağıdaki bölüm) ya da `FB_PAGE_TOKEN` (Facebook sayfası) gizli anahtarı girilmişse `araclar/sosyal_paylas.py` zamanı gelen gönderiyi 15 dakikada bir o kanala kendiliğinden paylaşır; anahtarı olmayan kanal bekler ve Meta Business Suite'ten elle paylaşılıp `durum` alanına not düşülür. `sosyal/bekleyen.md` bekleyenleri listeler (`--liste`).

## Instagram anahtarı: akış ve otomatik paylaşım (isteğe bağlı)
Aynı anahtar hem Instagram gönderilerini siteye çeker hem de kuyruktaki kartları Instagram'da kendiliğinden paylaşır. Yapılmazsa gönderiler siteye bağlantılarıyla tek tek eklenir, kartlar elle paylaşılır.
1. developers.facebook.com'da ücretsiz bir uygulama oluşturun. Uygulamaya **Instagram** ürününü ekleyin, "Instagram girişiyle API kurulumu" bölümünden @derskutusuinfo hesabını bağlayın ve **erişim anahtarı** oluşturun. Anahtar üretilirken `instagram_business_basic` ve `instagram_business_content_publish` izinleri seçili olmalı (paylaşım için ikincisi şart).
2. GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret**: ad `IG_TOKEN`, değer bu anahtar.
3. İsteğe bağlı: anahtarın kendiliğinden yenilenip GitHub'a yazılması için yalnız bu depoya "Secrets: Read and write" izni olan bir fine-grained token oluşturup `GH_PAT` adıyla ekleyin. Eklemezseniz anahtar 60 günde bir yenilenmelidir.

## Claude API kredisiyle özet üretme
Max planı her ay API kredisi verir (Max 5x: 100 $). Bu kredi, haftalık konu özetlerini GitHub'da kendiliğinden ürettirmek için kullanılır. Kredi claude.ai sohbet kullanımından ayrıdır ve ay devrinde biter, sonraki aya aktarılmaz (yenileme tarihi Faturalandırma sayfasında yazar).

Bir kez yapılacaklar:
1. claude.ai → **Ayarlar → Faturalandırma → API kredileri → Kuruluş oluştur**. Açılan Claude Console'da kuruluşu oluşturun. Bu bağlantı sonradan değiştirilemez.
2. platform.claude.com → **API Keys → Create Key**. Anahtarı kopyalayın, kimseye yazmayın.
3. GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret**: ad `ANTHROPIC_API_KEY`, değer bu anahtar.

Her hafta:
1. GitHub → **Actions → Haftalık özetleri Claude API ile üret → Run workflow**.
2. `hafta` alanına hafta numarasını yazın. İlk seferde `dersler` alanına iki üç ders yazıp deneyin (ör. `7-matematik,10-tarih`); özet sayfasında harcanan tutar görünür.
3. Sonuç iyiyse `dersler` boş bırakılarak 103 dersin hepsi üretilir. Var olan özetler atlanır; bütçe dolarsa aynı hafta yeniden çalıştırılınca kaldığı yerden sürer.

İş akışı özetleri, görsel modüllerini, sosyal medya kartlarını ve paylaşım kuyruğunu üretir; yayın denetiminden geçerse siteye gönderir. Yerelde aynı iş: `python3 araclar/ozet_api_uret.py --hafta 15` (yardım: `--help`).

Kalan kredi: platform.claude.com → **Settings → Billing**, "Promotional credits" satırı (tutar ve bitiş tarihi). Harcamanın gün gün dökümü **Usage** ve **Cost** sayfalarındadır. Kredi biterse araç durur ve kredi yenilenince kaldığı yerden devam eder.

Yaklaşık maliyet (ilk denemede gerçek tutar ölçülmeli):

| Model | Bir özet | Bir hafta (103 ders) |
|---|---|---|
| claude-opus-5-5 (varsayılan) | 0,7-1 $ | 70-100 $ |
| claude-sonnet-5-5 | 0,35-0,5 $ | 35-50 $ |

## Bilinmesi gerekenler
- Depoda 60 gün hiç etkinlik olmazsa GitHub zamanlanmış çalışmayı durdurur ve e-postayla haber verir; Actions sekmesinden yeniden açılır.
- Alan adlarının süresi 28.09.2027'de doluyor. Yenilemeden önce daha ucuz bir firmaya taşınması düşünülmeli.
- Ziyaretçi bir düğmeye basmadıkça tarayıcısı YouTube, Instagram ya da Facebook'a bağlanmaz; görseller sitenin kendisinden gelir (KVKK açısından güvenli düzen, ayrıntı `gizlilik.html`).
- Yerelde deneme: `python3 -m http.server 8765 --directory public`, sonra `http://127.0.0.1:8765`.
