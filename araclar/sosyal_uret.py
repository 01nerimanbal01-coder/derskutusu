#!/usr/bin/env python3
"""Sosyal medya afişi üretici: sosyal/bilgiler.json'daki "Bunu biliyor muydunuz?" kartlarını 1080×1350 PNG olarak public/sosyal/ altına çizer
ve isteğe bağlı olarak sosyal/kuyruk.json paylaşım kuyruğuna ekler.

Kullanım:
  python3 araclar/sosyal_uret.py                 # görseli olmayan kartları çizer
  python3 araclar/sosyal_uret.py --hepsi         # bütün kartları yeniden çizer
  python3 araclar/sosyal_uret.py --kuyruk 2026-10-06T12:30   # kuyrukta olmayan kartları bu andan başlayarak günde iki kez (12.30, 18.30 TSİ) sıraya koyar
  python3 araclar/sosyal_uret.py --sadece bilgi-10-kimya-1    # tek kart

Çizim Node Playwright + Chromium ile yapılır (node -e "require('playwright')" çalışmalı). Yazı tipi Montserrat (Google Fonts);
ilk çalışmada araclar/sosyal_font/ içine indirilir, dosya yoksa ve ağ kapalıysa sitenin DKPlan yazı tipi kullanılır.

bilgiler.json kaydı: {"kimlik": "bilgi-10-kimya-1", "dosya": "10-kimya-1" (araclar/ozetler dosyası), "baslik", "metin": [2 paragraf], "ozet" (altyazı cümlesi), "renk" (isteğe bağlı, #hex)}
Sınıf, ders adı ve hafta bilgisi ozetler/<dosya>.json'dan okunur.
"""
import json
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
BILGILER = KOK / 'sosyal' / 'bilgiler.json'
KUYRUK = KOK / 'sosyal' / 'kuyruk.json'
OZETLER = KOK / 'araclar' / 'ozetler'
CIKTI = KOK / 'public' / 'sosyal'
FONT = KOK / 'araclar' / 'sosyal_font'
DERSLER = json.loads((KOK / 'public' / 'veri' / 'dersler.json').read_text(encoding='utf-8'))['dersler']
TSI = timezone(timedelta(hours=3))
SITE = 'https://derskutusu.com/sosyal/'

# Vurgu renkleri: önceki afişlerde kullanılan tonlar; kart kendi rengini vermezse sırayla dağıtılır.
RENKLER = ['#2b6cb0', '#9b2c2c', '#2f855a', '#6b46c1', '#c05621', '#b83280', '#2c7a7b', '#d97706', '#3b4cca', '#c2366b',
           '#0e8fa8', '#744210', '#2451d6', '#dd6b20', '#1f9d55', '#97266d', '#5a67d8', '#b7791f', '#319795', '#8b3fd6',
           '#d64545', '#975a16', '#3182ce', '#e0662b', '#c53030', '#9c4221']
ETIKET = {'din-kulturu-ve-ahlak-bilgisi': 'dinkültürü', 'turk-dili-ve-edebiyati': 'edebiyat', 'fen-bilimleri': 'fenbilimleri',
          'sosyal-bilgiler': 'sosyalbilgiler', 'tc-inkilap-tarihi-ve-ataturkculuk': 'inkılaptarihi', 'kuran-i-kerim': 'kuranıkerim',
          'peygamberimizin-hayati': 'peygamberimizinhayatı', 'temel-dini-bilgiler': 'temeldinibilgiler', 'mesleki-arapca': 'arapça',
          'hitabet-ve-mesleki-uygulama': 'hitabet', 'islam-kultur-ve-medeniyeti': 'islammedeniyeti', 'dinler-tarihi': 'dinlertarihi',
          'turkce': 'türkçe', 'cografya': 'coğrafya'}

SABLON = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
@font-face{font-family:M;font-weight:400;src:url(FONT/Montserrat-400.ttf)}@font-face{font-family:M;font-weight:500;src:url(FONT/Montserrat-500.ttf)}
@font-face{font-family:M;font-weight:600;src:url(FONT/Montserrat-600.ttf)}@font-face{font-family:M;font-weight:700;src:url(FONT/Montserrat-700.ttf)}
@font-face{font-family:M;font-weight:800;src:url(FONT/Montserrat-800.ttf)}
@font-face{font-family:DK;font-weight:400;src:url(KOK/public/kutuphane/font/DKPlan-Regular.ttf)}@font-face{font-family:DK;font-weight:700;src:url(KOK/public/kutuphane/font/DKPlan-Bold.ttf)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#f6f8fd;font-family:M,DK,sans-serif;color:#26314d}
.bas{height:210px;background:#0b2257;display:flex;align-items:center;padding:0 64px 0 72px;position:relative}
.bas img{width:124px;height:124px}
.marka{margin-left:20px}.marka b{display:block;font-size:44px;font-weight:800;color:#fff;letter-spacing:.01em;line-height:1.05}
.marka b span{color:#9db2ff}.marka i{display:block;font-style:normal;font-size:20px;font-weight:700;color:#f2b33d;letter-spacing:.06em;margin-top:8px}
.pill{position:absolute;right:64px;top:84px;height:42px;padding:0 20px;border-radius:21px;background:ACCENT;color:#fff;font-size:22px;font-weight:700;letter-spacing:.04em;display:flex;align-items:center;text-transform:uppercase}
.govde{position:relative;height:986px;padding:58px 72px 0;background-image:radial-gradient(#d6dced 2px,transparent 2.2px);background-size:46px 46px;background-position:36px 20px;overflow:hidden}
.etiket{font-size:28px;font-weight:800;color:ACCENT;text-transform:uppercase;letter-spacing:.02em}
h1{font-size:64px;font-weight:800;color:#0f2a6b;line-height:1.16;margin-top:22px;max-width:960px;letter-spacing:-.01em;hyphens:manual;word-break:keep-all}
.cizgi{width:160px;height:12px;border-radius:6px;background:ACCENT;margin:34px 0 36px}
p{font-size:36px;font-weight:500;line-height:1.4;max-width:910px;margin-bottom:22px;position:relative;z-index:1}
.soru{position:absolute;right:-30px;bottom:-200px;width:520px;height:520px;border-radius:50%;background:ACCENT;opacity:.1}
.soru-isaret{position:absolute;right:86px;bottom:-62px;font-size:400px;font-weight:800;color:ACCENT;opacity:.3;line-height:1}
.alt{height:154px;background:ACCENT;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 72px}
.alt b{display:block;font-size:30px;font-weight:700}.alt small{display:block;font-size:24px;font-weight:500;margin-top:8px}
.alt .site{font-size:36px;font-weight:800}
</style></head><body>
<div class="bas"><img src="KOK/public/logo.svg" alt=""><div class="marka"><b>DERS <span>KUTUSU</span></b><i>DERSKUTUSU.COM</i></div><div class="pill">PILL</div></div>
<div class="govde"><div class="soru"></div><div class="soru-isaret">?</div><div class="etiket">Bunu biliyor muydunuz?</div><h1>BASLIK</h1><div class="cizgi"></div>PARAGRAFLAR</div>
<div class="alt"><div><b>ALTBAS</b><small>Özet, çözümlü örnekler ve etkinlikler sitemizde</small></div><div class="site">derskutusu.com</div></div>
</body></html>"""

NODE = """
const { chromium } = require('playwright');
(async () => {
  const isler = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const [html, png] of isler) {
    await p.goto('file://' + html);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: png, type: 'png' });
    const alt = await p.evaluate(() => Math.max(...[...document.querySelectorAll('p')].map(e => e.getBoundingClientRect().bottom)));
    console.log('çizildi', png, alt > 1120 ? `UYARI: metin çok uzun (alt kenar ${Math.round(alt)}px)` : '');
  }
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def kacir(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('-', '\u2011')   # kısa çizgiden satır bölünmesin


def font_hazirla():
    FONT.mkdir(exist_ok=True)
    for w in (400, 500, 600, 700, 800):
        hedef = FONT / f'Montserrat-{w}.ttf'
        if hedef.exists():
            continue
        try:
            css = urllib.request.urlopen(urllib.request.Request(
                f'https://fonts.googleapis.com/css2?family=Montserrat:wght@{w}&display=swap', headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read().decode()
            url = css.split('url(')[1].split(')')[0]
            hedef.write_bytes(urllib.request.urlopen(url, timeout=60).read())
        except Exception as hata:                 # ağ yoksa DKPlan ile devam edilir
            print(f'Montserrat {w} indirilemedi ({hata}); DKPlan kullanılacak', file=sys.stderr)


def bilgi_oku(k):
    o = json.loads((OZETLER / f"{k['dosya']}.json").read_text(encoding='utf-8'))
    return {'sinif': o['sinif'], 'ders': o['ders'], 'ders_adi': DERSLER.get(o['ders'], o['ders'].replace('-', ' ').title()), 'hafta': o.get('hafta', 1)}


def html_uret(k, i):
    b = bilgi_oku(k)
    renk = k.get('renk') or RENKLER[i % len(RENKLER)]
    paragraflar = ''.join(f'<p>{kacir(p)}</p>' for p in k['metin'])
    return (SABLON.replace('ACCENT', renk).replace('FONT', FONT.as_posix()).replace('KOK', KOK.as_posix())
            .replace('PILL', kacir(f"{b['sinif']}. SINIF · {b['ders_adi']}")).replace('BASLIK', kacir(k['baslik']))
            .replace('PARAGRAFLAR', paragraflar).replace('ALTBAS', kacir(f"{b['sinif']}. sınıf {b['ders_adi']} · {b['hafta']}. hafta konu özeti")))


def ciz(kartlar):
    if not kartlar:
        print('Çizilecek kart yok.')
        return
    font_hazirla()
    CIKTI.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as gecici:
        isler = []
        for i, k in enumerate(kartlar):
            html = Path(gecici) / f"{k['kimlik']}.html"
            html.write_text(html_uret(k, k['_sira']), encoding='utf-8')
            isler.append([html.as_posix(), (CIKTI / f"{k['kimlik']}.png").as_posix()])
        liste = Path(gecici) / 'isler.json'
        liste.write_text(json.dumps(isler), encoding='utf-8')
        betik = Path(gecici) / 'ciz.cjs'
        betik.write_text(NODE, encoding='utf-8')
        subprocess.run(['node', betik.as_posix(), liste.as_posix()], check=True, cwd=KOK)


def metin_uret(k):
    b = bilgi_oku(k)
    etiket = ETIKET.get(b['ders'], b['ders'].replace('-', ''))
    hafta = f"{b['hafta']}. hafta " if b.get('hafta') else ''
    return (f"Bunu biliyor muydunuz? {k['ozet']}\n"
            f"📘 {b['sinif']}. sınıf {b['ders_adi']} {hafta}konu özeti, çözümlü örnekler ve etkinlikler: derskutusu.com\n"
            f"#derskutusu #{etiket} #{b['sinif']}sınıf #bunubiliyormuydunuz #maarifmodeli")


def kuyruga_ekle(kartlar, baslangic):
    ku = json.loads(KUYRUK.read_text(encoding='utf-8'))
    varolan = {g['kimlik'] for g in ku['gonderiler']}
    zaman = datetime.fromisoformat(baslangic).replace(tzinfo=TSI) if 'T' in baslangic else datetime.fromisoformat(baslangic + 'T12:30').replace(tzinfo=TSI)
    eklenen = 0
    for k in kartlar:
        if k['kimlik'] in varolan:
            continue
        ku['gonderiler'].append({'kimlik': k['kimlik'], 'zaman': zaman.isoformat(), 'gorsel': SITE + k['kimlik'] + '.png',
                                 'metin': metin_uret(k), 'hedef': ['instagram', 'facebook'], 'durum': {}})
        eklenen += 1
        zaman = zaman.replace(hour=18, minute=30) if zaman.hour < 18 else (zaman + timedelta(days=1)).replace(hour=12, minute=30)   # günde iki paylaşım
    KUYRUK.write_text(json.dumps(ku, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{eklenen} gönderi kuyruğa eklendi; son zaman {zaman:%Y-%m-%d %H:%M}')


def main():
    arg = sys.argv[1:]
    kartlar = json.loads(BILGILER.read_text(encoding='utf-8'))
    for i, k in enumerate(kartlar):
        k['_sira'] = i
    if '--sadece' in arg:
        kartlar = [k for k in kartlar if k['kimlik'] == arg[arg.index('--sadece') + 1]]
    if '--kuyruk' in arg:
        kuyruga_ekle(kartlar, arg[arg.index('--kuyruk') + 1])
        return
    if '--hepsi' not in arg and '--sadece' not in arg:
        kartlar = [k for k in kartlar if not (CIKTI / f"{k['kimlik']}.png").exists()]
    ciz(kartlar)


if __name__ == '__main__':
    main()
