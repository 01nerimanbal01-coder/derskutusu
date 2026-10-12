#!/usr/bin/env python3
"""Sosyal medya otomatik paylaşım: sosyal/kuyruk.json'daki zamanı gelmiş gönderileri Instagram'a ve Facebook sayfasına gönderir.

İki anahtar tanınır (GitHub Secrets); ikisi de isteğe bağlıdır, olan kanal paylaşılır, olmayan kanal bekler:
  IG_TOKEN       Instagram girişiyle alınan uzun ömürlü anahtar (Instagram API with Instagram Login; Facebook sayfası gerekmez).
                 İzinler: instagram_business_basic, instagram_business_content_publish. akis_guncelle.py her gün süresini uzatır.
                 Instagram: POST graph.instagram.com/{ig}/media (image_url, caption) → POST /{ig}/media_publish (creation_id)
  FB_PAGE_TOKEN  Uzun ömürlü Facebook sayfa anahtarı (pages_manage_posts; Instagram için instagram_content_publish).
                 Facebook: POST graph.facebook.com/{sayfa}/photos (url, caption). IG_TOKEN yoksa Instagram'ı da bu anahtarla paylaşır.
Görseller sitede durur (https://derskutusu.com/sosyal/<ad>.png); Instagram yalnız JPEG kabul ettiği için aynı addaki .jpg kullanılır.
Her gönderi kanal başına en çok bir kez paylaşılır (durum alanı). Anahtar yoksa hiçbir şey göndermez, yalnız durumu yazar.
GitHub Actions 15 dakikada bir çalıştırır (.github/workflows/sosyal.yml); her çalışmada en çok bir gönderi. Yerelde: python3 araclar/sosyal_paylas.py --dene
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KUYRUK = KOK / 'sosyal' / 'kuyruk.json'
API_FB = 'https://graph.facebook.com/v21.0'
API_IG = 'https://graph.instagram.com/v21.0'
TSI = timezone(timedelta(hours=3))


def istek(taban, yol, veri=None):
    govde = urllib.parse.urlencode(veri).encode() if veri is not None else None
    try:
        with urllib.request.urlopen(urllib.request.Request(f'{taban}/{yol}', data=govde), timeout=60) as y:
            return json.loads(y.read().decode())
    except urllib.error.HTTPError as h:           # Graph hata iletisini kuyruğa taşı (anahtar iletide yer almaz)
        try:
            e = json.loads(h.read().decode()).get('error', {})
            raise RuntimeError(f"Graph {h.code}: {e.get('message')} (kod {e.get('code')}/{e.get('error_subcode')})") from None
        except ValueError:
            raise RuntimeError(f'Graph {h.code}') from None


def ig_yayinla(taban, ig, gorsel, metin, anahtar):
    m = istek(taban, f'{ig}/media', {'image_url': gorsel, 'caption': metin, 'access_token': anahtar})
    for _ in range(12):                           # kapsayıcı hazır olana dek bekle (en çok 60 sn)
        if istek(taban, f"{m['id']}?fields=status_code&access_token={anahtar}").get('status_code') == 'FINISHED':
            break
        time.sleep(5)
    return istek(taban, f'{ig}/media_publish', {'creation_id': m['id'], 'access_token': anahtar})


def ig_gorsel(adres):
    """Instagram yalnız JPEG kabul eder: sitede aynı adlı .jpg varsa onu kullan."""
    if adres.endswith('.png') and (KOK / 'public' / 'sosyal' / (adres.rsplit('/', 1)[-1][:-4] + '.jpg')).exists():
        return adres[:-4] + '.jpg'
    return adres


def main():
    dene = '--dene' in sys.argv
    k = json.loads(KUYRUK.read_text(encoding='utf-8'))
    fb = os.environ.get('FB_PAGE_TOKEN', '').strip()
    igt = os.environ.get('IG_TOKEN', '').strip()
    uygun = {h for h, var in (('facebook', fb), ('instagram', igt or fb)) if var}
    simdi = datetime.now(TSI)
    sirada = [g for g in k['gonderiler'] if datetime.fromisoformat(g['zaman']) <= simdi
              and any(h in uygun and not g['durum'].get(h) for h in g['hedef'])]
    print(f'anahtar: Instagram {"var" if igt else ("sayfa anahtarıyla" if fb else "YOK")}, Facebook {"var" if fb else "YOK"}; '
          f'{len(sirada)} gönderinin zamanı geldi')
    if dene or not sirada:
        return
    sayfa = ig_fb = ig_id = None
    if fb:
        ben = istek(API_FB, f'me?fields=id,name,instagram_business_account&access_token={fb}')   # sayfa anahtarında 'me' = sayfa
        sayfa = ben['id']
        ig_fb = k.get('instagram_kimligi') or ben.get('instagram_business_account', {}).get('id')
        print(f"Facebook sayfası: {ben.get('name')} ({sayfa}); bağlı Instagram: {ig_fb or 'YOK'}")
    if igt:
        ben = istek(API_IG, f'me?fields=id,username&access_token={igt}')
        ig_id = ben['id']
        print(f"Instagram hesabı: @{ben.get('username')} ({ig_id})")
    degisti = False
    for g in sirada[:1]:                          # her çalışmada en çok bir gönderi (15 dk arayla düzenli akış)
        for h in g['hedef']:
            if g['durum'].get(h) or h not in uygun:
                continue
            try:
                if h == 'facebook':
                    r = istek(API_FB, f'{sayfa}/photos', {'url': g['gorsel'], 'caption': g['metin'], 'access_token': fb})
                    kimlik = r.get('post_id') or r.get('id')
                elif igt:
                    r = ig_yayinla(API_IG, ig_id, ig_gorsel(g['gorsel']), g['metin'], igt)
                    kimlik = r.get('id')
                elif ig_fb:
                    r = ig_yayinla(API_FB, ig_fb, ig_gorsel(g['gorsel']), g['metin'], fb)
                    kimlik = r.get('id')
                else:
                    continue
                g['durum'][h] = f'{simdi:%d.%m %H:%M} API ile paylaşıldı ({kimlik})'
                print(f'{g["kimlik"]} → {h}: {kimlik}')
                degisti = True
            except Exception as hata:              # hata kuyruğa yazılır, sonraki çalışmada yeniden denenir
                g.setdefault('hatalar', []).append(f'{simdi:%Y-%m-%d %H:%M} {h}: {hata}')
                print('HATA', g['kimlik'], h, hata, file=sys.stderr)
                degisti = True
    if degisti:
        KUYRUK.write_text(json.dumps(k, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
