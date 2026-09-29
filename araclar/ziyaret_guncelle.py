#!/usr/bin/env python3
"""Toplam ziyaret sayısını Cloudflare Web Analytics'ten alıp public/veri/ziyaret.json'a yazar.

GitHub Actions günde bir çalıştırır. Gerekli gizli değişkenler (GitHub → Settings → Secrets → Actions):
    CF_API_TOKEN   Cloudflare API anahtarı (izin: Account → Account Analytics → Read)
    CF_ACCOUNT_ID  Cloudflare hesap kimliği (gizli değil; guncelle.yml içinde yazılı)
Anahtar yoksa hiçbir şey yapmaz. Günlük değerler dosyada saklanır; Cloudflare eski günleri silse de toplam korunur.
Yalnız toplu sayılar alınır; kişisel veri yoktur.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

DOSYA = Path(__file__).resolve().parent.parent / 'public' / 'veri' / 'ziyaret.json'
SITE = 'derskutusu.com'
GUN = 7   # her çalışmada son 7 gün yeniden alınır (geç gelen verileri de kapsar)

SORGU = '''query($hesap: String!, $bas: Time!, $son: Time!, $site: String!) {
  viewer { accounts(filter: {accountTag: $hesap}) {
    rumPageloadEventsAdaptiveGroups(limit: 100, orderBy: [date_ASC],
      filter: {AND: [{datetime_geq: $bas}, {datetime_lt: $son}, {requestHost: $site}]}) {
      count
      sum { visits }
      dimensions { date }
    }
  } }
}'''


def main():
    anahtar, hesap = os.environ.get('CF_API_TOKEN'), os.environ.get('CF_ACCOUNT_ID')
    if not anahtar or not hesap:
        print('ziyaret: Cloudflare anahtarı yok, atlandı')
        return
    simdi = datetime.now(timezone.utc)
    bas = (simdi - timedelta(days=GUN)).replace(hour=0, minute=0, second=0, microsecond=0)
    govde = json.dumps({'query': SORGU, 'variables': {'hesap': hesap, 'bas': bas.strftime('%Y-%m-%dT%H:%M:%SZ'),
                                                      'son': simdi.strftime('%Y-%m-%dT%H:%M:%SZ'), 'site': SITE}}).encode()
    istek = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql', data=govde,
                                   headers={'Authorization': f'Bearer {anahtar}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(istek, timeout=30) as y:
            cevap = json.load(y)
    except Exception as hata:
        print(f'ziyaret: Cloudflare yanıt vermedi ({hata})')
        return
    if cevap.get('errors'):
        print('ziyaret: Cloudflare hatası:', cevap['errors'][0].get('message'))
        return
    gruplar = cevap['data']['viewer']['accounts'][0]['rumPageloadEventsAdaptiveGroups']

    eski = json.loads(DOSYA.read_text(encoding='utf-8')) if DOSYA.exists() else {}
    gunler = eski.get('gunler', {})
    for g in gruplar:
        gunler[g['dimensions']['date']] = {'ziyaret': g['sum']['visits'], 'goruntuleme': g['count']}
    yeni = {
        'toplam': sum(v['ziyaret'] for v in gunler.values()),
        'goruntuleme': sum(v['goruntuleme'] for v in gunler.values()),
        'guncelleme': simdi.isoformat(timespec='seconds'),
        'gunler': dict(sorted(gunler.items())),
    }
    if {k: v for k, v in yeni.items() if k != 'guncelleme'} != {k: v for k, v in eski.items() if k != 'guncelleme'}:
        DOSYA.write_text(json.dumps(yeni, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f"ziyaret: toplam {yeni['toplam']}, görüntüleme {yeni['goruntuleme']}")
    else:
        print('ziyaret: değişiklik yok')


if __name__ == '__main__':
    sys.exit(main())
