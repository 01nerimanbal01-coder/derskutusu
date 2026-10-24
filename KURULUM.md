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
Max planı her ay API kredisi verir (Max 5x: 100 $). Bu kredi, haftalık konu özetlerini GitHub'da kendiliğinden ürettirmek için kullanılır. Kredi claude.ai ve Claude Code kullanımından ayrıdır; ay devrinde biter, sonraki aya aktarılmaz (yenileme tarihi claude.ai → Ayarlar → Faturalandırma sayfasında yazar).

Bir kez yapılanlar (24.10.2026'da tamamlandı):
1. claude.ai → **Ayarlar → Faturalandırma → API kredileri**: Console kuruluşu bağlandı ("Bağlı"). Bu bağlantı sonradan değiştirilemez.
2. platform.claude.com → **API Keys → Create Key** ile anahtar oluşturuldu.
3. GitHub deposunda **Settings → Secrets and variables → Actions**: `ANTHROPIC_API_KEY` adıyla eklendi. Anahtar değişirse aynı yerde kaleme basıp güncellenir.

Her hafta:
1. GitHub → **Actions → Haftalık özetleri Claude API ile üret → Run workflow**.
2. `hafta` alanına hafta numarasını yazın; `dersler` boş kalırsa 103 dersin hepsi üretilir.
3. Diğer alanlar varsayılan kalabilir: `toplu` (yarı fiyat), `claude-opus-5-5`, `medium`, bütçe 50 $.
4. Çalıştırma istekleri gönderir ve bir saat bekler; bu sürede biten özetler yayımlanır. Toplu istekler bazen saatler sürer (en geç 24 saat). Bitmeyenleri aynı iş akışı **iki saatte bir kendiliğinden** çalışarak toplar, yayımlar ve denetime takılanlar için düzeltme turunu gönderir. Elle bir şey yapmak gerekmez.
5. Özet sayfasında üretilen, hatalı, bekleyen ve gönderilmeyen dersler ile harcanan tutar yazar. Bütçe dolduysa ya da bazı dersler hatalıysa aynı hafta yeniden çalıştırılır: var olan ve toplu istekte bekleyen dersler atlanır, yalnız eksikler gönderilir.

Gönderilen her toplu isteğin hangi dersleri içerdiği `araclar/veri/toplu_durum.json` dosyasında kayıtlıdır; elle değiştirilmez. Bu kayıt sayesinde aynı derse iki kez ödenmez, bitmiş isteğin sonucu bir kez yazılır (sonradan bilerek silinen özet geri gelmez) ve içindeki dersler başka yoldan yazılmış bir istek iptal edilir. Kayıtta olmayan bir toplu istek sürerken (ör. yerelden gönderilmiş) yeni istek gönderilmez; o istek bitip toplanınca devam edilir.

Bir çalıştırma sürerken ikincisini başlatmayın: sırada bekleyen çalıştırmayı iki saatte bir gelen toplayıcı iptal edebilir. Önceki bitince başlatın. Toplu kip yalnız `main` dalında çalışır; düzeltme turu ilk turun modeli ve çabasıyla gönderilir.

İş akışı özetleri, görsel modüllerini, sosyal medya kartlarını ve paylaşım kuyruğunu üretir; her özet sitenin sayfa üreticisiyle derlenip yayın denetiminden geçirilir. Denetime takılan özet ayıklanır, kalanlar yayımlanır. Üretilen dosyalar her çalıştırmanın **Artifacts** bölümünde 30 gün saklanır. Yerelde aynı iş: `python3 araclar/ozet_api_uret.py --hafta 15 --toplu`, yalnız toplama: `--topla` (yardım: `--help`; API'siz prova: `--kuru`).

Kalan kredi: platform.claude.com/settings/billing, **Promotional credits** satırı (tutar ve bitiş tarihi). Harcamanın dökümü platform.claude.com/cost sayfasındadır; birkaç dakika gecikmeli yansıyabilir. Kredi biterse araç durur; kredi yenilenince aynı hafta yeniden çalıştırılır ve kaldığı yerden devam eder. Anahtar silinirse otomatik toplayıcı sessizce atlanır.

Maliyet (bir özet ortalama 34 bin jeton girdi, 58 bin jeton çıktı; çıktının çoğu modelin düşünmesi ve 60-75 KB JSON):

| Ayar | Bir özet | Bir hafta (103 ders) |
|---|---|---|
| Opus 5.5, high, anlık (24.10.2026 ölçümü: 2 özet + 1 düzeltme = 3,96 $) | yaklaşık 2 $ | yaklaşık 200 $ |
| Opus 5.5, high, toplu | yaklaşık 1 $ | yaklaşık 100 $ |
| Opus 5.5, medium, toplu (varsayılan) | tahminen 0,5-0,8 $ | tahminen 50-80 $ |
| Sonnet 5.5, medium, toplu | tahminen 0,25-0,4 $ | tahminen 25-40 $ |

## Bilinmesi gerekenler
- Depoda 60 gün hiç etkinlik olmazsa GitHub zamanlanmış çalışmayı durdurur ve e-postayla haber verir; Actions sekmesinden yeniden açılır.
- Alan adlarının süresi 28.09.2027'de doluyor. Yenilemeden önce daha ucuz bir firmaya taşınması düşünülmeli.
- Ziyaretçi bir düğmeye basmadıkça tarayıcısı YouTube, Instagram ya da Facebook'a bağlanmaz; görseller sitenin kendisinden gelir (KVKK açısından güvenli düzen, ayrıntı `gizlilik.html`).
- Yerelde deneme: `python3 -m http.server 8765 --directory public`, sonra `http://127.0.0.1:8765`.
