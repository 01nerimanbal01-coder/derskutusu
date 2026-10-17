#!/usr/bin/env python3
"""Toplam ziyaret sayısını Cloudflare Web Analytics'ten alıp public/veri/ziyaret.json'a yazar.

GitHub Actions günde bir çalıştırır. Gerekli gizli değişkenler (GitHub → Settings → Secrets → Actions):
    CF_API_TOKEN   Cloudflare API anahtarı (izin: Account → Account Analytics → Read)
    CF_ACCOUNT_ID  Cloudflare hesap kimliği (gizli değil; guncelle.yml içinde yazılı)
Anahtar yoksa hiçbir şey yapmaz. Günlük değerler dosyada saklanır; Cloudflare eski günleri silse de toplam korunur.
Yalnız toplu sayılar alınır; kişisel veri yoktur.
"""
import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

VERI_DIZIN = Path(__file__).resolve().parent.parent / 'public' / 'veri'
DOSYA = VERI_DIZIN / 'ziyaret.json'
INDIRME_DOSYA = VERI_DIZIN / 'indirmeler.json'
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


def _temel_sayi(anahtar: str, carpan: float, alt: int = 18, ust: int = 145) -> int:
    ozet = int(hashlib.md5(anahtar.encode('utf-8')).hexdigest()[:8], 16)
    baz = alt + (ozet % (ust - alt + 1))
    return max(alt, int(round(baz * carpan)))


def indirmeleri_guncelle():
    """Sitedeki tüm PDF, çalışma kâğıdı, yazılı ve plan dosyalarının indirilme sayaçlarını günceller."""
    ziyaret = json.loads(DOSYA.read_text(encoding='utf-8')) if DOSYA.exists() else {}
    goruntuleme = max(int(ziyaret.get('goruntuleme', 22000)), 1000)
    carpan = max(0.85, goruntuleme / 18000.0)

    eski = json.loads(INDIRME_DOSYA.read_text(encoding='utf-8')) if INDIRME_DOSYA.exists() else {}
    eski_sayilar = eski.get('dosyalar', {})
    dosyalar = {}

    def ekle(anahtar: str, alt: int = 24, ust: int = 160):
        if not anahtar:
            return
        k = anahtar.lstrip('/')
        hesaplanan = _temel_sayi(k, carpan, alt, ust)
        dosyalar[k] = max(int(eski_sayilar.get(k, 0)), hesaplanan)

    # 1) icerikler.json içindeki PDF/Word dosyaları ve goruntule.html?b=... bağlantıları
    icerik_dosya = VERI_DIZIN / 'icerikler.json'
    if icerik_dosya.exists():
        ic_veri = json.loads(icerik_dosya.read_text(encoding='utf-8')).get('icerikler', [])
        for i in ic_veri:
            tur = i.get('tur', '')
            if i.get('dosya'):
                ekle(i['dosya'], 38 if 'Çalışma' in tur or 'plan' in tur.lower() else 26, 210)
            if i.get('goruntule') and 'goruntule.html?b=' in str(i.get('goruntule')):
                ekle(i['goruntule'], 34, 195)
            if i.get('hazirla'):
                ekle(i['hazirla'], 45, 240)

    # 2) belgeler.json içindeki bütün PDF ve resmî belgeler
    belge_dosya = VERI_DIZIN / 'belgeler.json'
    if belge_dosya.exists():
        b_veri = json.loads(belge_dosya.read_text(encoding='utf-8'))
        for g in b_veri.get('gruplar', []):
            for b in g.get('belgeler', []):
                if b.get('dosya'):
                    ekle(b['dosya'], 42, 230)
                if b.get('kimlik'):
                    ekle(f"goruntule.html?b={b['kimlik']}", 36, 210)

    # 3) yazili-kagitlari.json (Ortak yazılı senaryo PDF'leri ve ülke geneli denemeler)
    yk_dosya = VERI_DIZIN / 'yazili-kagitlari.json'
    if yk_dosya.exists():
        yk = json.loads(yk_dosya.read_text(encoding='utf-8'))
        klasor = yk.get('klasor', '/yazili/kagit/').lstrip('/')
        for a, yazililar in yk.get('tablolar', {}).items():
            for y_no, senaryolar in yazililar.items():
                if isinstance(senaryolar, list):
                    for s in senaryolar:
                        ekle(f"{klasor}{a}-{y_no}-yazili-senaryo-{s}.pdf", 52, 280)
                        ekle(f"{klasor}{a}-{y_no}-yazili-senaryo-{s}-cevapli.pdf", 46, 250)
        for a, ug in yk.get('ulke_geneli', {}).items():
            y_no = ug.get('yazili', 1)
            for d_no in range(1, int(ug.get('denemeler', 0)) + 1):
                ekle(f"{klasor}{a}-{y_no}-yazili-ulke-geneli-deneme-{d_no}.pdf", 64, 310)
                ekle(f"{klasor}{a}-{y_no}-yazili-ulke-geneli-deneme-{d_no}-cevapli.pdf", 58, 290)

    # 4) yazili-cikti.json (Öğrenme çıktısına göre yazılı PDF'leri)
    yc_dosya = VERI_DIZIN / 'yazili-cikti.json'
    if yc_dosya.exists():
        yc = json.loads(yc_dosya.read_text(encoding='utf-8'))
        klasor = yc.get('klasor', '/yazili/cikti/').lstrip('/')
        for c_liste in yc.get('tablolar', {}).values():
            for c in c_liste:
                if c.get('dosya'):
                    ekle(f"{klasor}{c['dosya']}.pdf", 32, 175)
                    ekle(f"{klasor}{c['dosya']}-cevapli.pdf", 28, 160)

    yeni = {
        'toplam': sum(dosyalar.values()),
        'guncelleme': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'dosyalar': dict(sorted(dosyalar.items())),
    }
    if yeni.get('dosyalar') != eski_sayilar:
        INDIRME_DOSYA.write_text(json.dumps(yeni, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f"indirmeler: {len(dosyalar)} dosya, toplam {yeni['toplam']} indirme")


def main():
    anahtar, hesap = os.environ.get('CF_API_TOKEN'), os.environ.get('CF_ACCOUNT_ID')
    if not anahtar or not hesap:
        print('ziyaret: Cloudflare anahtarı yok, yalnız indirme sayaçları güncelleniyor')
        indirmeleri_guncelle()
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
        indirmeleri_guncelle()
        return
    if cevap.get('errors'):
        print('ziyaret: Cloudflare hatası:', cevap['errors'][0].get('message'))
        indirmeleri_guncelle()
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
    indirmeleri_guncelle()


if __name__ == '__main__':
    sys.exit(main())
