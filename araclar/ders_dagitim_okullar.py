#!/usr/bin/env python3
"""Ders dağıtım programını kullanmaya başlayan okulları toplar, sitedeki sayacı günceller, e-postayla bildirir.

Akış:
  Uygulama (ders-dagitim-uygulama.html) izin veren okul için programı ilk oluşturduğunda gizli bir çerçevede
  /okul-bildir.html#<kod> açar; o sayfa adresini /okul-bildir/<kod> yapıp Cloudflare Web Analytics betiğini yükler.
  <kod> = "1|okul|ilçe|öğretmen sayısı|sınıf sayısı" metninin UTF-8 baytlarının onaltılık yazımı.
  Bu betik saatte bir (guncelle.yml) son 8 günün /okul-bildir/ yollarını Cloudflare'den okur ve:
    - yeni okulları araclar/veri/ders-dagitim-okullar.json listesine ekler (site klasörü public/ DIŞINDA:
      okul adları derskutusu.com'da hiçbir yerde yayımlanmaz),
    - public/veri/ders-dagitim-sayac.json'a YALNIZ toplam sayıyı yazar (sitedeki sayaç bunu okur),
    - her yeni okul için depo sahibini anan bir issue açar; GitHub bunu e-postayla bildirir.

Gerekli (GitHub Actions): CF_API_TOKEN (Account Analytics: Read), CF_ACCOUNT_ID; issue için GH_TOKEN (github.token),
GITHUB_REPOSITORY_OWNER. Anahtar yoksa ya da Cloudflare hata verirse hiçbir şey değiştirmez (yayın akışı durmaz).
Deneme: --yollar dosya.txt (Cloudflare yerine satır satır yol) · --kuru (issue açmaz, ne açacağını yazar)
Kayıt silme: okulun 'anahtar'ını araclar/veri/ders-dagitim-haric.json listesine ekleyin; sonraki çalışmada listeden ve sayaçtan çıkar,
  Cloudflare verisinden de geri eklenmez (deneme ve sahte kayıtlar için).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
LISTE = KOK / 'araclar' / 'veri' / 'ders-dagitim-okullar.json'
SAYAC = KOK / 'public' / 'veri' / 'ders-dagitim-sayac.json'
HARIC = KOK / 'araclar' / 'veri' / 'ders-dagitim-haric.json'   # listeden çıkarılan deneme/sahte kayıtların anahtarları
SITE = 'derskutusu.com'
ON_EK = '/okul-bildir/'
ETIKET = 'ders-dagitim-okul'
GUN = 8
ORNEK = {'örnekortaokulu'}   # uygulamadaki "Örnek okul verisiyle dene" verisi okul sayılmaz
EN_FAZLA_ISSUE = 20   # bir çalışmada bundan fazla yeni okul gelirse tek toplu issue açılır (kötüye kullanım)
TR = timezone(timedelta(hours=3))

SORGU = '''query($hesap: String!, $bas: Time!, $son: Time!, $site: String!, $yol: String!) {
  viewer { accounts(filter: {accountTag: $hesap}) {
    rumPageloadEventsAdaptiveGroups(limit: 5000, orderBy: [datetimeHour_ASC],
      filter: {AND: [{datetime_geq: $bas}, {datetime_lt: $son}, {requestHost: $site}, {requestPath_like: $yol}]}) {
      count
      dimensions { requestPath datetimeHour }
    }
  } }
}'''

# okul adları asla site klasörüne yazılmaz
assert 'public' not in LISTE.relative_to(KOK).parts


def norm(s: str) -> str:
    """Aynı okulun farklı yazımlarını birleştirir: büyük/küçük harf, boşluk, noktalama."""
    s = s.replace('İ', 'i').replace('I', 'ı').lower()
    return re.sub(r'[^0-9a-zçğıöşüâîû]+', '', s)


def temiz(s: str, n: int) -> str:
    """Okul/ilçe adı herkese açık issue'ya yazılır: yalnız harf, rakam ve . , ' ’ - / ( ) kalır (@ anma, bağlantı, Markdown olmaz)."""
    s = re.sub(r"[^0-9A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû .,'’/()-]", ' ', s)
    return re.sub(r'\s+', ' ', s).strip(' .,-/')[:n]


def coz(yol: str):
    """'/okul-bildir/<kod>' → {okul, ilce, ogretmen, sinif} ya da None."""
    if not yol.startswith(ON_EK):
        return None
    kod = yol[len(ON_EK):].strip('/').lower()
    if not re.fullmatch(r'[0-9a-f]{16,600}', kod) or len(kod) % 2:
        return None
    try:
        parca = bytes.fromhex(kod).decode('utf-8').split('|')
    except (ValueError, UnicodeDecodeError):
        return None
    if len(parca) != 5 or parca[0] != '1':
        return None
    okul, ilce = temiz(parca[1], 80), temiz(parca[2], 40)
    try:
        ogr, snf = int(parca[3]), int(parca[4])
    except ValueError:
        return None
    if len(okul) < 3 or not (2 <= ogr <= 500) or not (1 <= snf <= 300):
        return None
    return {'okul': okul, 'ilce': ilce, 'ogretmen': ogr, 'sinif': snf}


def cloudflare_yollari():
    anahtar, hesap = os.environ.get('CF_API_TOKEN'), os.environ.get('CF_ACCOUNT_ID')
    if not anahtar or not hesap:
        print('CF_API_TOKEN / CF_ACCOUNT_ID yok; okul listesi güncellenmedi.')
        return None
    son = datetime.now(timezone.utc).replace(microsecond=0)
    degisken = {'hesap': hesap, 'site': SITE, 'yol': ON_EK + '%',
                'bas': (son - timedelta(days=GUN)).isoformat().replace('+00:00', 'Z'), 'son': son.isoformat().replace('+00:00', 'Z')}
    istek = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql',
                                   data=json.dumps({'query': SORGU, 'variables': degisken}).encode(),
                                   headers={'Authorization': 'Bearer ' + anahtar, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(istek, timeout=60) as y:
            veri = json.load(y)
    except Exception as e:  # ağ / yetki: yayın akışını durdurma
        print('Cloudflare sorgusu başarısız:', e)
        return None
    if veri.get('errors'):
        print('Cloudflare hatası:', veri['errors'])
        return None
    gruplar = ((veri.get('data') or {}).get('viewer') or {}).get('accounts') or [{}]
    satirlar = gruplar[0].get('rumPageloadEventsAdaptiveGroups') or []
    return [(s['dimensions']['requestPath'], s['dimensions'].get('datetimeHour')) for s in satirlar]


def gh(*arg, girdi=None):
    return subprocess.run(['gh', *arg], input=girdi, capture_output=True, text=True, check=False)


def duyurulmus_anahtarlar():
    """Daha önce issue'su açılmış okullar (gövdedeki gizli işaretten) — yarıda kalan çalışmada çift issue olmasın."""
    r = gh('issue', 'list', '--label', ETIKET, '--state', 'all', '--limit', '1000', '--json', 'body')
    if r.returncode:
        return set()
    return set(re.findall(r'<!-- okul-anahtar: (.+?) -->', ' '.join(i.get('body', '') for i in json.loads(r.stdout or '[]'))))


def liste_metni(okullar):
    return '\n'.join(f"{i}. {o['okul']}" + (f" ({o['ilce']})" if o['ilce'] else '') + f" — ilk kullanım {o['ilk']}"
                     for i, o in enumerate(okullar, 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--yollar', help='Cloudflare yerine bu dosyadaki yolları kullan (deneme)')
    ap.add_argument('--kuru', action='store_true', help='issue açma, yalnız yaz')
    a = ap.parse_args()

    if a.yollar:
        kayit = [(s.strip(), None) for s in Path(a.yollar).read_text(encoding='utf-8').splitlines() if s.strip()]
    else:
        kayit = cloudflare_yollari()
        if kayit is None:
            return 0

    haric = set(json.loads(HARIC.read_text(encoding='utf-8'))) if HARIC.exists() else set()
    okullar = [o for o in (json.loads(LISTE.read_text(encoding='utf-8')) if LISTE.exists() else []) if o['anahtar'] not in haric]
    bilinen = {o['anahtar'] for o in okullar}
    yeniler, simdi = [], datetime.now(TR).strftime('%d.%m.%Y %H:%M')
    for yol, saat in kayit:
        o = coz(yol)
        if not o:
            continue
        if norm(o['okul']) in ORNEK:
            continue
        o['anahtar'] = norm(o['okul']) + '|' + norm(o['ilce'])
        if o['anahtar'] in bilinen or o['anahtar'] in haric:
            continue
        bilinen.add(o['anahtar'])
        o['ilk'] = (datetime.fromisoformat(saat.replace('Z', '+00:00')).astimezone(TR).strftime('%d.%m.%Y %H:00') if saat else simdi)
        okullar.append(o)
        yeniler.append(o)

    LISTE.parent.mkdir(parents=True, exist_ok=True)
    LISTE.write_text(json.dumps(okullar, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    SAYAC.parent.mkdir(parents=True, exist_ok=True)
    eski = json.loads(SAYAC.read_text(encoding='utf-8')).get('sayi') if SAYAC.exists() else None
    if eski != len(okullar):
        SAYAC.write_text(json.dumps({'sayi': len(okullar)}) + '\n', encoding='utf-8')
    print(f'okul sayısı: {len(okullar)} (yeni: {len(yeniler)})')
    if not yeniler:
        return 0

    sahip = os.environ.get('GITHUB_REPOSITORY_OWNER', '')
    anan = f'@{sahip} ' if sahip else ''
    if not a.kuru:
        gh('label', 'create', ETIKET, '--color', '1E4C8B', '--description', 'Ders dağıtım programını kullanan okul', '--force')
    duyurulan = set() if a.kuru else duyurulmus_anahtarlar()
    yeniler = [o for o in yeniler if o['anahtar'] not in duyurulan]
    toplu = len(yeniler) > EN_FAZLA_ISSUE
    gruplar = [yeniler] if toplu else [[o] for o in yeniler]
    for grup in gruplar:
        sira = okullar.index(grup[-1]) + 1
        baslik = (f'Ders dağıtım programı: {len(grup)} yeni okul (toplam {len(okullar)})' if toplu
                  else f"Ders dağıtım programı: {sira}. okul — {grup[0]['okul']}")
        govde = (f"{anan}ders dağıtım programını yeni okul kullanmaya başladı.\n\n" +
                 ''.join(f"**Yeni okul:** {o['okul']}" + (f" ({o['ilce']})" if o['ilce'] else '') +
                         f" · öğretmen {o['ogretmen']} · sınıf {o['sinif']}\n" for o in grup) +
                 f"\n**Toplam {sira if not toplu else len(okullar)} okul:**\n" +
                 liste_metni(okullar[:sira] if not toplu else okullar) + '\n\n' +
                 ''.join(f"<!-- okul-anahtar: {o['anahtar']} -->\n" for o in grup))
        if a.kuru:
            print('--- issue (kuru) ---\n' + baslik + '\n' + govde)
            continue
        r = gh('issue', 'create', '--label', ETIKET, '--title', baslik, '--body-file', '-', girdi=govde)
        print(('issue açıldı: ' + r.stdout.strip()) if not r.returncode else ('issue açılamadı: ' + r.stderr.strip()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
