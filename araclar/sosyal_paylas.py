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
    with urllib.request.urlopen(urllib.request.Request(f'{API}/{yol}', data=govde), timeout=60) as y:
        return json.loads(y.read().decode())


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
    sayfa = k['sayfa_kimligi']
    ig = k.get('instagram_kimligi') or istek(f'{sayfa}?fields=instagram_business_account&access_token={anahtar}').get('instagram_business_account', {}).get('id')
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
                    m = istek(f'{ig}/media', {'image_url': g['gorsel'], 'caption': g['metin'], 'access_token': anahtar})
                    r = istek(f'{ig}/media_publish', {'creation_id': m['id'], 'access_token': anahtar})
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
