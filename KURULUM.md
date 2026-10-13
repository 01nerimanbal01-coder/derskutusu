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

## Sayfa üretimi (elle düzenlenmeyen dosyalar)
Üst menü, alt bilgi ve simge takımının tek kaynağı `public/index.html`'dir; öteki sayfalar üreticilerle yazılır. Bir sayfayı elle düzeltirseniz bir sonraki üretimde kaybolur; düzeltmeyi üreticiye (ya da `araclar/ozetler`, `araclar/calisma` gibi kaynak klasörlere) yapın.
- `python3 araclar/sayfa_uret.py`: kök sayfalar (ogrenci, ogretmen, icerikler, yazili, planlar, belgeler, kelime, arapca, sinav, test, tahta, goruntule, kpss, gizlilik, telif, katki, 404 …). Betik sürümleri `BETIK_SURUMLERI` sözlüğünde, stil sürümü index.html'deki `stil.css?v=` değerinden alınır; bir .js/.css değişince sürümü yükseltip üreticiyi çalıştırın (önbellekteki eski kopya kalmasın).
- `python3 araclar/ozet_uret.py`: `araclar/ozetler/*.json` → `public/ozet/*.html` (konu anlatımları) ve `icerikler.json`'daki "Konu anlatımı" kayıtları.
- `python3 araclar/calisma_uret.py`: `araclar/calisma/*.json` → `public/calisma/*.html` + PDF'ler (Chrome gerekir) ve `icerikler.json`'daki "Çalışma kâğıdı" kayıtları. `icerikler.json` bu iki üretici tarafından yeniden yazılır; elle yalnız öteki türler (plan, kitap, video vb.) eklenir.
- `python3 araclar/kpss_uret.py`: `public/veri/kpss.json` → `public/kpss.html` ve `public/kpss/*.html`.
- `python3 araclar/ust_guncelle.py`: yeniden üretilmeyen sayfalara (çalışma kâğıtları vb.) güncel üst menü, alt bilgi ve stil/betik sürümlerini işler; index.html'in menüsü ya da bir sürüm değişince çalıştırılır.
- `python3 araclar/agac_uret.py`: `public/veri/gunluk-plan/*.json` (yıllık planlar) → `public/veri/agac/*.json` (öğrenci dalındaki ünite/konu/hafta ağacı, çevrimiçi testin konu kodları).
- `python3 araclar/soru_havuzu_uret.py`: çevrimiçi test havuzu (aşağıda). `python3 araclar/kok_yayin_denetle.py`: yayın öncesi kök sayfa denetimi; `ziyaret_guncelle.py`: `ziyaret.json`.

## Veri dosyaları (`public/veri/`)
`dersler.json` (sınıf/ders/tür ve kitle eşlemesi), `belgeler.json` (resmî belgeler ve kitaplar), `senaryolar.json` (ÖDSGM yazılı senaryoları), `yazili-kagitlari.json` ve `yazili-cikti.json` (hazır yazılı kâğıtları; `public/yazili/` PDF'leri), `sinavlar.json` (sınav takvimi), `gunluk-planlar.json` + `gunluk-plan/` (yıllık/günlük planlar), `agac/` (üretilir), `soru/` (üretilir), `kelimeler.json` ve `arapca-kelimeler.json` (kelime çalışmaları), `kpss.json`, `ziyaret.json`, `youtube.json`/`instagram.json` (üretilir).

## GitHub iş akışları (`.github/workflows/`)
- `guncelle.yml`: her gün 07.17 — YouTube/Instagram akışını çeker (`akis_guncelle.py`) ve siteyi yayımlar.
- `nobetci.yml`: 30 dakikada bir site denetimi (`nobetci.py`); sorun olursa "nobetci" etiketli issue açar, Pazartesi 08.43 derin denetim.
- `sosyal.yml`: 15 dakikada bir kuyruktaki sosyal medya kartını paylaşır (`sosyal_paylas.py`, anahtar girilmişse).
- `kesif-onizleme.yml`: değişikliklerde testleri çalıştırır (`tests/*.cjs`: ana-sayfa, arama-oneri, katalog-yukleme, soru-havuzu, site-renkleri, kesif-kapsam, ders-slayt, online-test).
- `slayt-kontrol.yml`: konu anlatımı slaytlarının kapsam denetimi.

## Çevrimiçi test (öğrenci soru havuzu)
- `public/test.html` + `public/test.js`: öğrenci sınıf → ders → ünite/konu → öğrenme çıktısı seçer; sorular havuzdan rastgele ve tekrarsız seçilir (son görülenler cihazda tutulur), dönüt anında ya da sonunda verilir; sonuç konu ve çıktıya göre dökülür. Her şey tarayıcıda kalır, sunucuya veri gitmez.
- `python3 araclar/soru_havuzu_uret.py`: havuzu üretir → `public/veri/soru/<sinif>-<ders>.json` ve `dizin.json`. Kaynaklar: konu özetlerinin etkinlikleri ve örnekleri (`araclar/ozetler`), çalışma kâğıtlarının soruları (`araclar/calisma`) ve ek soru dosyaları. Görsele dayanan sorular alınmaz. Yeni özet/çalışma kâğıdı eklenince yeniden çalıştırılır.
- Ek soru yazmak için `araclar/sorular/<sinif>-<ders>.json`: `{"sorular": [{"tur": "coktan", "konu": "<ağaçtaki konu kodu>", "cikti": ["MAT.5.3.1"], "soru": "...", "secenekler": ["...", "..."], "dogru": 1, "aciklama": "..."}]}`. Türler: `coktan`, `dy` (`ifadeler`: metin/dogru/aciklama), `bosluk` (`cumleler`: metin `___` ile / cevap, `fazla`), `eslestir` (`ciftler`), `siralama` (`ogeler` doğru sırada), `acik` (`cevap`, `ipuclari`). Metinlerde `{kesir:3|4}`, `{kok:2}`, `{us:2|3}`, `{ar:...}` gösterimleri kullanılabilir. `node tests/soru-havuzu.cjs` havuzu denetler.

## Sosyal medya kartları
- `araclar/sosyal/<kimlik>.json`: her "Bunu biliyor muydunuz?" kartının metni (`ozet`, `baslik`, `paragraflar`, `bilgi`). Kimlik `bilgi-<sınıf>-<ders>-<hafta>` biçimindedir (Din Kültürü → `din-kulturu`, İnkılap Tarihi → `inkilap-tarihi`).
- `python3 araclar/sosyal_gorsel.py`: görseli olmayan kartları `public/sosyal/<kimlik>.png` olarak üretir (1080×1350, Poppins yazı tipi `araclar/fontlar/`). `--kuyruk 2026-10-13T09:00` ile kuyrukta olmayan kartları günde 6 gönderi (09–19, iki saat arayla) olacak biçimde `sosyal/kuyruk.json`'a ekler.
- Paylaşım: `IG_TOKEN` (Instagram, aşağıdaki bölüm) ya da `FB_PAGE_TOKEN` (Facebook sayfası) gizli anahtarı girilmişse `araclar/sosyal_paylas.py` zamanı gelen gönderiyi 15 dakikada bir o kanala kendiliğinden paylaşır; anahtarı olmayan kanal bekler ve Meta Business Suite'ten elle paylaşılıp `durum` alanına not düşülür. `sosyal/bekleyen.md` bekleyenleri listeler (`--liste`).

## Instagram anahtarı: akış ve otomatik paylaşım (isteğe bağlı)
Aynı anahtar hem Instagram gönderilerini siteye çeker hem de kuyruktaki kartları Instagram'da kendiliğinden paylaşır. Yapılmazsa gönderiler siteye bağlantılarıyla tek tek eklenir, kartlar elle paylaşılır.
1. developers.facebook.com'da ücretsiz bir uygulama oluşturun. Uygulamaya **Instagram** ürününü ekleyin, "Instagram girişiyle API kurulumu" bölümünden @derskutusuinfo hesabını bağlayın ve **erişim anahtarı** oluşturun. Anahtar üretilirken `instagram_business_basic` ve `instagram_business_content_publish` izinleri seçili olmalı (paylaşım için ikincisi şart).
2. GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret**: ad `IG_TOKEN`, değer bu anahtar.
3. İsteğe bağlı: anahtarın kendiliğinden yenilenip GitHub'a yazılması için yalnız bu depoya "Secrets: Read and write" izni olan bir fine-grained token oluşturup `GH_PAT` adıyla ekleyin. Eklemezseniz anahtar 60 günde bir yenilenmelidir.

## Bilinmesi gerekenler
- Depoda 60 gün hiç etkinlik olmazsa GitHub zamanlanmış çalışmayı durdurur ve e-postayla haber verir; Actions sekmesinden yeniden açılır.
- Alan adlarının süresi 28.09.2027'de doluyor. Yenilemeden önce daha ucuz bir firmaya taşınması düşünülmeli.
- Ziyaretçi bir düğmeye basmadıkça tarayıcısı YouTube, Instagram ya da Facebook'a bağlanmaz; görseller sitenin kendisinden gelir (KVKK açısından güvenli düzen, ayrıntı `gizlilik.html`).
- Yerelde deneme: `python3 -m http.server 8765 --directory public`, sonra `http://127.0.0.1:8765`.
