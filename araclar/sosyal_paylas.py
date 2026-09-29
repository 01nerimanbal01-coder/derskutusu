#!/usr/bin/env python3
"""Sosyal medya otomatik paylaşım: sosyal/kuyruk.json'daki zamanı gelmiş gönderileri Facebook sayfasına ve Instagram'a gönderir.

Meta Graph API (resmî, ücretsiz):
  Facebook: POST /{sayfa}/photos  (url = public görsel adresi, caption)
  Instagram: POST /{ig}/media (image_url, caption) → POST /{ig}/media_publish (creation_id)
Görseller sitede durur (https://derskutusu.com/sosyal/<ad>.png); dosya yüklemeye gerek yoktur.
Anahtar: GitHub Secrets → FB_PAGE_TOKEN (uzun ömürlü sayfa erişim anahtarı; pages_manage_posts, instagram_content_publish).
Anahtar yoksa hiçbir şey göndermez, yalnız durumu yazar. Her gönderi en çok bir kez paylaşılır (durum alanı).
GitHub Actions 15 dakikada bir çalıştırır (.github/workflows/sosyal.yml). Yerelde: python3 araclar/sosyal_paylas.py --dene
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
API = 'https://graph.facebook.com/v21.0'
TSI = timezone(timedelta(hours=3))


def istek(yol, veri=None):
    govde = urllib.parse.urlencode(veri).encode() if veri is not None else None
    try:
        with urllib.request.urlopen(urllib.request.Request(f'{API}/{yol}', data=govde), timeout=60) as y:
            return json.loads(y.read().decode())
    except urllib.error.HTTPError as h:           # Graph hata iletisini kuyruğa taşı (anahtar iletide yer almaz)
        try:
            e = json.loads(h.read().decode()).get('error', {})
            raise RuntimeError(f"Graph {h.code}: {e.get('message')} (kod {e.get('code')}/{e.get('error_subcode')})") from None
        except ValueError:
            raise RuntimeError(f'Graph {h.code}') from None


def ig_yayinla(ig, gorsel, metin, anahtar):
    m = istek(f'{ig}/media', {'image_url': gorsel, 'caption': metin, 'access_token': anahtar})
    for _ in range(12):                           # kapsayıcı hazır olana dek bekle (en çok 60 sn)
        if istek(f"{m['id']}?fields=status_code&access_token={anahtar}").get('status_code') == 'FINISHED':
            break
        time.sleep(5)
    return istek(f'{ig}/media_publish', {'creation_id': m['id'], 'access_token': anahtar})


def main():
    dene = '--dene' in sys.argv
    k = json.loads(KUYRUK.read_text(encoding='utf-8'))
    anahtar = os.environ.get('FB_PAGE_TOKEN', '').strip()
    simdi = datetime.now(TSI)
    sirada = [g for g in k['gonderiler'] if datetime.fromisoformat(g['zaman']) <= simdi
              and any(not g['durum'].get(h) for h in g['hedef'])]
    print(f'{len(sirada)} gönderinin zamanı geldi; anahtar {"var" if anahtar else "YOK"}')
    if not anahtar or dene or not sirada:
        return
    ben = istek(f'me?fields=id,name,instagram_business_account&access_token={anahtar}')   # sayfa anahtarında 'me' = sayfa
    sayfa = ben['id']
    ig = k.get('instagram_kimligi') or ben.get('instagram_business_account', {}).get('id')
    print(f"sayfa: {ben.get('name')} ({sayfa}); Instagram: {ig or 'BAĞLI DEĞİL'}")
    degisti = False
    for g in sirada[:1]:                          # her çalışmada en çok bir gönderi (15 dk arayla düzenli akış)
        for h in g['hedef']:
            if g['durum'].get(h):
                continue
            try:
                if h == 'facebook':
                    r = istek(f'{sayfa}/photos', {'url': g['gorsel'], 'caption': g['metin'], 'access_token': anahtar})
                    g['durum'][h] = r.get('post_id') or r.get('id')
                elif h == 'instagram' and ig:
                    r = ig_yayinla(ig, g['gorsel'], g['metin'], anahtar)
                    g['durum'][h] = r.get('id')
                print(f'{g["kimlik"]} → {h}: {g["durum"].get(h)}')
                degisti = True
            except Exception as hata:              # hata kuyruğa yazılır, sonraki çalışmada yeniden denenir
                g.setdefault('hatalar', []).append(f'{simdi:%Y-%m-%d %H:%M} {h}: {hata}')
                print('HATA', g['kimlik'], h, hata, file=sys.stderr)
                degisti = True
    if degisti:
        KUYRUK.write_text(json.dumps(k, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
