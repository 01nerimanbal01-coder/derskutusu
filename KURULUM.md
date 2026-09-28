# Eğitim sitesi — ücretsiz kurulum

Site GitHub Pages'te ücretsiz yayımlanır. GitHub her sabah 07.17'de YouTube ve Instagram'daki yeni paylaşımları alır ve siteyi kendiliğinden yeniler. Facebook sayfasının akışı ziyaretçi "göster" düğmesine basınca Facebook'tan yüklenir.

Hesap açma, giriş ve anahtar/şifre girme işlerini siz yaparsınız. Anahtarları Claude'a yazmayın; doğrudan GitHub'daki gizli alana girin.

## 1. GitHub (bir kez)
1. github.com'da ücretsiz hesap açın.
2. Yeni bir depo oluşturun (Public). Adı `kullaniciadiniz.github.io` olursa site adresi `https://kullaniciadiniz.github.io` olur. Başka bir ad verirseniz adres `https://kullaniciadiniz.github.io/depo-adi` olur.
3. Bu `SITE` klasörünün içindekileri depoya yükleyin. En kolayı ücretsiz **GitHub Desktop** uygulamasıdır; gizli `.github` klasörü de yüklenmelidir.
4. Depoda **Settings → Pages → Build and deployment → Source: GitHub Actions** seçin.

## 2. Hesap adresleri
`public/veri/ayarlar.json` içine site adı, slogan ve hesap adresleri yazılır. Bu dosyayı Claude doldurur; adresleri söylemeniz yeterli.
- YouTube: kanal adresi (ör. `https://www.youtube.com/@kanaliniz`). Kanal kimliği kendiliğinden bulunur.
- Instagram: profil adresi.
- Facebook: sayfanın adresi. Sayfa herkese açık olmalıdır.

## 3. Instagram paylaşımlarının kendiliğinden gelmesi (isteğe bağlı)
Bu adım yapılmazsa Instagram gönderileri siteye bağlantılarıyla tek tek eklenir (Claude ekler).
1. Instagram hesabını **Profesyonel hesap** yapın (İçerik üreticisi ya da İşletme; ücretsiz).
2. developers.facebook.com'da ücretsiz bir uygulama oluşturun. Uygulamaya **Instagram** ürününü ekleyin, "Instagram girişiyle API kurulumu" bölümünden hesabınızı bağlayın ve **erişim anahtarı** oluşturun.
3. GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret**: ad `IG_TOKEN`, değer bu anahtar.
4. İsteğe bağlı: anahtar yenilendiğinde GitHub'a kendiliğinden yazılması için yalnız bu depoya "Secrets: Read and write" izni olan bir fine-grained token oluşturup `GH_PAT` adıyla ekleyin. Eklemezseniz anahtar 60 günde bir yenilenmelidir.

## 4. İlk yayın
Depoda **Actions → Akışları güncelle ve yayımla → Run workflow**. Birkaç dakika sonra site adresinde açılır.

## Bilinmesi gerekenler
- Ücretli olan tek şey kendi alan adıdır (isteğe bağlı). Alınırsa Settings → Pages → Custom domain'e yazılır.
- Depoda 60 gün hiç etkinlik olmazsa GitHub zamanlanmış çalışmayı durdurur ve e-postayla haber verir; Actions sekmesinden yeniden açılır.
- Ziyaretçi bir düğmeye basmadıkça tarayıcısı YouTube, Instagram ya da Facebook'a bağlanmaz; görseller sitenin kendisinden gelir. Bu, KVKK açısından da güvenli bir düzendir.
- Yerelde deneme: `python3 -m http.server 8765 --directory public`, sonra `http://127.0.0.1:8765`.
