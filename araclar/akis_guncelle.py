#!/usr/bin/env python3
"""Sosyal medya akışlarını sitenin veri klasörüne yazar. Yalnız Python'un kendi kütüphanesini kullanır.

- YouTube: kanalın herkese açık RSS akışı (anahtar, hesap, ücret gerekmez).
- Instagram: IG_TOKEN ortam değişkeni varsa Instagram API (profesyonel hesap + Meta uygulaması, ücretsiz).
  Anahtar yoksa instagram.json'a dokunulmaz (elle eklenen ya da örnek gönderiler kalır).
- Facebook sayfası tarayıcıda resmî sayfa eklentisiyle gösterilir; burada iş yok.

Görseller public/veri/gorsel/ içine indirilir; ziyaretçinin tarayıcısı YouTube/Instagram'a bağlanmaz.
GitHub Actions her gün çalıştırır (.github/workflows/guncelle.yml). Yerelde: python3 araclar/akis_guncelle.py
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
VERI = KOK / 'public' / 'veri'
GORSEL = VERI / 'gorsel'
EN_COK = 12
BASLIK = {'User-Agent': 'Mozilla/5.0 (akis-guncelle; +https://github.com)', 'Accept-Language': 'tr-TR,tr;q=0.9'}
uyarilar = []


def uyar(metin):
    uyarilar.append(metin)
    print('UYARI:', metin, file=sys.stderr)


def al(adres, ikili=False):
    istek = urllib.request.Request(adres, headers=BASLIK)
    with urllib.request.urlopen(istek, timeout=30) as yanit:
        veri = yanit.read()
    return veri if ikili else veri.decode('utf-8')


def gorsel_indir(adresler, ad):
    """İlk açılan adresteki görseli indirir; zaten varsa yeniden indirmez. Sayfadaki yolu döndürür."""
    GORSEL.mkdir(parents=True, exist_ok=True)
    hedef = GORSEL / ad
    if not hedef.exists():
        for adres in adresler:
            try:
                hedef.write_bytes(al(adres, ikili=True))
                break
            except Exception:
                continue
        else:
            return ''
    return f'veri/gorsel/{ad}'


def yaz(dosya, alan, liste, kaynak):
    """Liste değiştiyse dosyayı yazar; değişmediyse dokunmaz (gereksiz kayıt ve yayın olmasın)."""
    yol = VERI / dosya
    try:
        eski = json.loads(yol.read_text('utf-8'))
    except Exception:
        eski = {}
    if eski.get(alan) == liste and eski.get('kaynak') == kaynak:
        return False
    icerik = {'kaynak': kaynak, 'guncelleme': datetime.now(timezone.utc).isoformat(timespec='seconds'), alan: liste}
    yol.write_text(json.dumps(icerik, ensure_ascii=False, indent=2) + '\n', 'utf-8')
    return True


def kullanilmayanlari_sil(onek, kullanilan):
    for dosya in GORSEL.glob(f'{onek}-*'):
        if f'veri/gorsel/{dosya.name}' not in kullanilan:
            dosya.unlink()


# ---------- YouTube ----------
def youtube_kanal_id(ayar):
    kanal = (ayar.get('kanal_id') or '').strip()
    if kanal:
        return kanal
    adres = (ayar.get('adres') or '').strip()
    if not adres:
        return ''
    m = re.search(r'/channel/(UC[\w-]{22})', adres)
    if m:
        return m.group(1)
    try:
        sayfa = al(adres)
    except Exception as hata:
        uyar(f'YouTube kanal sayfası açılamadı ({hata}); ayarlar.json içine kanal_id yazın.')
        return ''
    m = (re.search(r'<link rel="canonical" href="https://www\.youtube\.com/channel/(UC[\w-]{22})"', sayfa)
         or re.search(r'"externalId":"(UC[\w-]{22})"', sayfa))
    if not m:
        uyar('YouTube kanal kimliği sayfadan bulunamadı; ayarlar.json içine kanal_id yazın.')
        return ''
    return m.group(1)


def youtube(ayar):
    kanal = youtube_kanal_id(ayar)
    if not kanal:
        return False
    ad = {'a': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015',
          'media': 'http://search.yahoo.com/mrss/'}
    try:
        kok = ET.fromstring(al(f'https://www.youtube.com/feeds/videos.xml?channel_id={kanal}'))
    except Exception as hata:
        uyar(f'YouTube akışı alınamadı: {hata}')
        return False
    videolar = []
    for kayit in kok.findall('a:entry', ad)[:EN_COK]:
        kimlik = kayit.findtext('yt:videoId', '', ad)
        if not re.fullmatch(r'[\w-]{11}', kimlik):
            continue
        bag = kayit.find('a:link', ad)
        bag = bag.get('href', '') if bag is not None else f'https://www.youtube.com/watch?v={kimlik}'
        onizleme = [f'https://i.ytimg.com/vi/{kimlik}/{boy}.jpg' for boy in ('hq720', 'sddefault', 'mqdefault')]
        videolar.append({
            'id': kimlik,
            'baslik': kayit.findtext('a:title', '', ad).strip(),
            'tarih': kayit.findtext('a:published', '', ad),
            'kisa': '/shorts/' in bag,
            'gorsel': gorsel_indir(onizleme, f'yt-{kimlik}.jpg'),
            'baglanti': bag,
        })
    kullanilmayanlari_sil('yt', {v['gorsel'] for v in videolar})
    return yaz('youtube.json', 'videolar', videolar, 'youtube')


# ---------- Instagram ----------
def instagram():
    anahtar = os.environ.get('IG_TOKEN', '').strip()
    if not anahtar:
        return False
    # Uzun ömürlü anahtar 60 gün geçerli; her çalışmada süresi yeniden 60 güne uzatılır.
    try:
        yanit = json.loads(al('https://graph.instagram.com/refresh_access_token?'
                              + urllib.parse.urlencode({'grant_type': 'ig_refresh_token', 'access_token': anahtar})))
        yeni = yanit.get('access_token', '')
        if yeni and yeni != anahtar:
            # İş akışı bu dosyayı gizli değişkene yazar ve siler; .gitignore'da, depoya girmez.
            (KOK / '.yeni_ig_token').write_text(yeni, 'utf-8')
            anahtar = yeni
    except Exception as hata:
        uyar(f'Instagram anahtarı uzatılamadı (anahtar 24 saatten yeniyse normaldir): {type(hata).__name__}')
    alanlar = 'id,caption,media_type,media_url,thumbnail_url,permalink,timestamp'
    try:
        veri = json.loads(al('https://graph.instagram.com/me/media?'
                             + urllib.parse.urlencode({'fields': alanlar, 'limit': EN_COK, 'access_token': anahtar})))
    except Exception as hata:
        uyar(f'Instagram gönderileri alınamadı: {type(hata).__name__} {getattr(hata, "code", "")}')
        return False
    gonderiler = []
    for g in veri.get('data', [])[:EN_COK]:
        tur = g.get('media_type', 'IMAGE')
        kaynak = g.get('thumbnail_url') if tur == 'VIDEO' else g.get('media_url')
        kimlik = re.sub(r'\D', '', str(g.get('id', '')))
        if not kimlik or not kaynak:
            continue
        gonderiler.append({
            'id': kimlik,
            'aciklama': (g.get('caption') or '').strip(),
            'tur': tur,
            'tarih': g.get('timestamp', ''),
            'gorsel': gorsel_indir([kaynak], f'ig-{kimlik}.jpg'),
            'baglanti': g.get('permalink', ''),
        })
    kullanilmayanlari_sil('ig', {g['gorsel'] for g in gonderiler})
    return yaz('instagram.json', 'gonderiler', gonderiler, 'instagram')


def main():
    ayar = json.loads((VERI / 'ayarlar.json').read_text('utf-8'))
    degisen = [ad for ad, degisti in (('youtube', youtube(ayar.get('youtube', {}))), ('instagram', instagram())) if degisti]
    print('Değişen akış:', ', '.join(degisen) or 'yok')
    if uyarilar:
        print(f'{len(uyarilar)} uyarı var.')


if __name__ == '__main__':
    main()
