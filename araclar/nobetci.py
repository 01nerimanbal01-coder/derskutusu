"""Site nöbetçisi: derskutusu.com'un açık ve sağlıklı olduğunu denetler.

GitHub Actions'ta 30 dakikada bir çalışır (.github/workflows/nobetci.yml).
Yalnız standart kütüphane kullanır.

  python3 araclar/nobetci.py            # hızlı denetim
  python3 araclar/nobetci.py --derin    # + site haritası ve dış bağlantılar

Çıktılar:
  nobetci-rapor.md   bulunan sorunlar (sorun yoksa boş)
  GITHUB_OUTPUT      durum=tamam|sorun, ana_sayfa=var|yok
Çıkış kodu her zaman 0'dır; karar iş akışında verilir.
"""
import datetime as dt
import json
import os
import re
import socket
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ALAN = 'derskutusu.com'
KOK = f'https://{ALAN}'
GITHUB_IP = {'185.199.108.153', '185.199.109.153', '185.199.110.153', '185.199.111.153'}
KLASOR = Path(__file__).resolve().parent.parent

# Her denetimde bakılan sayfalar ve içinde bulunması gereken işaret
ONEMLI = [
    ('/', 'Ders Kutusu'),
    ('/sinif.html', 'Ders Kutusu'),
    ('/icerikler.html', 'Ders Kutusu'),
    ('/belgeler.html', 'Ders Kutusu'),
    ('/tahta.html', 'Ders Kutusu'),
    ('/sinav.html', 'Ders Kutusu'),
    ('/ara.html', 'Ders Kutusu'),
    ('/veri/ayarlar.json', 'site_adi'),
    ('/veri/icerikler.json', '['),
    ('/stil.css', '{'),
    ('/logo.svg', '<svg'),
]
SERTIFIKA_UYARI_GUN = 14   # GitHub normalde 30 gün kala yeniler
ALAN_ADI_UYARI_GUN = 45
AJAN = 'Mozilla/5.0 (derskutusu-nobetci; +https://derskutusu.com)'


def getir(adres, zaman=20, bayt=None):
    """(durum kodu, gövde metni ya da hata) döndürür."""
    istek = urllib.request.Request(adres, headers={'User-Agent': AJAN})
    if bayt:
        istek.add_header('Range', f'bytes=0-{bayt - 1}')
    try:
        with urllib.request.urlopen(istek, timeout=zaman) as y:
            govde = y.read(bayt or 2_000_000)
            return y.status, govde.decode('utf-8', 'replace')
    except urllib.error.HTTPError as h:
        return h.code, str(h)
    except Exception as h:  # zaman aşımı, DNS, TLS
        return 0, f'{type(h).__name__}: {h}'


def sayfalar():
    sorun = []
    ana_var = True
    for yol, isaret in ONEMLI:
        kod, govde = getir(KOK + yol)
        if kod != 200 or isaret not in govde:
            sorun.append(f'`{yol}` açılmıyor ya da eksik (kod {kod}): {govde[:120]}')
            if yol == '/':
                ana_var = False
    return sorun, ana_var


def dns():
    try:
        ipler = {a[4][0] for a in socket.getaddrinfo(ALAN, 443, socket.AF_INET)}
    except Exception as h:
        return [f'DNS çözülemedi: {h}']
    if not ipler & GITHUB_IP:
        return [f'DNS GitHub Pages adreslerini göstermiyor: {sorted(ipler)} (Turkticaret DNS ayarı)']
    return []


def sertifika():
    try:
        bag = ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=ALAN)
        bag.settimeout(15)
        bag.connect((ALAN, 443))
        bitis = dt.datetime.strptime(bag.getpeercert()['notAfter'], '%b %d %H:%M:%S %Y %Z')
        bag.close()
    except Exception as h:
        return [f'HTTPS sertifikası okunamadı: {h}']
    kalan = (bitis - dt.datetime.utcnow()).days
    if kalan < SERTIFIKA_UYARI_GUN:
        return [f'HTTPS sertifikasının bitmesine {kalan} gün var ({bitis:%d.%m.%Y}); '
                'GitHub → Settings → Pages → "Enforce HTTPS" ve özel alan adı ayarına bakılmalı.']
    return []


def alan_adi():
    kod, govde = getir(f'https://rdap.verisign.com/com/v1/domain/{ALAN}', zaman=20)
    if kod != 200:
        return []  # kayıt servisi yanıt vermezse site sorunu sayılmaz
    try:
        olaylar = json.loads(govde).get('events', [])
        bitis = next(o['eventDate'] for o in olaylar if o.get('eventAction') == 'expiration')
        bitis = dt.datetime.fromisoformat(bitis.replace('Z', '+00:00')).replace(tzinfo=None)
    except Exception:
        return []
    kalan = (bitis - dt.datetime.utcnow()).days
    if kalan < ALAN_ADI_UYARI_GUN:
        return [f'Alan adı {ALAN} {bitis:%d.%m.%Y} tarihinde bitiyor ({kalan} gün kaldı). '
                'Turkticaret hesabından yenilenmeli (otomatik yenileme açık olmalı).']
    return []


def site_haritasi():
    kod, govde = getir(KOK + '/sitemap.xml')
    if kod != 200:
        return [f'`/sitemap.xml` açılmıyor (kod {kod})']
    adresler = re.findall(r'<loc>([^<]+)</loc>', govde)
    with ThreadPoolExecutor(8) as h:
        sonuc = list(h.map(lambda a: (a, getir(a)[0]), adresler))
    return [f'Site haritasındaki sayfa açılmıyor: {a} (kod {k})' for a, k in sonuc if k != 200]


def dis_baglantilar():
    """Belgelerdeki resmî dış bağlantılar (MEB, ÖDSGM, ÖSYM). Yalnız ilk baytları ister."""
    adresler = set()
    for ad in ('belgeler.json', 'sinavlar.json'):
        yol = KLASOR / 'public' / 'veri' / ad
        if yol.exists():
            adresler |= set(re.findall(r'"(https?://[^"\s]+)"', yol.read_text(encoding='utf-8')))
    adresler = sorted(a for a in adresler if ALAN not in a)

    def bak(a):
        kod, _ = getir(a, zaman=25, bayt=1024)
        if kod in (0, 403, 405, 429, 500, 502, 503):   # bazı resmî siteler robotları geri çevirir
            kod, _ = getir(a, zaman=25)
        return a, kod

    with ThreadPoolExecutor(6) as h:
        sonuc = list(h.map(bak, adresler))
    kirik = [(a, k) for a, k in sonuc if k not in (200, 206)]
    if len(kirik) > len(adresler) / 2:
        # Çoğu açılmıyorsa sorun bağlantılarda değil, resmî sitelerin yurt dışı
        # erişimi kısmasındadır; tek tek listelemek yanıltır.
        return [], len(adresler)
    return [f'Dış bağlantı açılmıyor (kod {k}): {a}' for a, k in kirik], len(adresler)


def main():
    derin = '--derin' in sys.argv
    sorun, ana_var = sayfalar()
    sorun += dns() + sertifika() + alan_adi()
    uyari = []
    if derin:
        sorun += site_haritasi()
        kirik, toplam = dis_baglantilar()
        uyari += kirik
        print(f'Dış bağlantı: {toplam} denetlendi, {len(kirik)} açılmadı')

    zaman = dt.datetime.utcnow() + dt.timedelta(hours=3)
    bas = f'**Denetim:** {zaman:%d.%m.%Y %H:%M} (TSİ){" · derin" if derin else ""}\n\n'
    rapor = bas + '### Sorunlar\n' + ''.join(f'- {s}\n' for s in sorun) if sorun else ''
    uyari_rapor = (bas + '### Açılmayan resmî bağlantılar\nBelgeler sayfasındaki bu adresler '
                   'kaynağında taşınmış ya da kaldırılmış olabilir:\n'
                   + ''.join(f'- {u}\n' for u in uyari)) if uyari else ''
    Path('nobetci-rapor.md').write_text(rapor, encoding='utf-8')
    Path('nobetci-uyari.md').write_text(uyari_rapor, encoding='utf-8')
    print(rapor or 'Sorun yok.')
    print(uyari_rapor)

    cikti = os.environ.get('GITHUB_OUTPUT')
    if cikti:
        with open(cikti, 'a', encoding='utf-8') as f:
            f.write(f'durum={"sorun" if sorun else "tamam"}\n')
            f.write(f'uyari={"var" if uyari else "yok"}\n')
            f.write(f'derin={"evet" if derin else "hayir"}\n')
            f.write(f'ana_sayfa={"var" if ana_var else "yok"}\n')


if __name__ == '__main__':
    main()
