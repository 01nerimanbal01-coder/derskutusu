#!/usr/bin/env python3
"""Ders Kutusu Kapsamlı Test ve Hata Tespit Motoru.
Tüm HTML, JS, JSON ve medya kaynaklarını derinlemesine denetler.
"""
import os
import sys
import re
import json
import subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

KOK = Path(__file__).resolve().parent.parent
PUBLIC = KOK / "public"

class BaglantiToplayici(HTMLParser):
    def __init__(self, kaynak_dosya):
        super().__init__()
        self.kaynak = kaynak_dosya
        self.baglantilar = [] # (etiket, attr, deger, satir)
        self.id_ler = set()
        self.etiket_yigini = []
        self.etiket_hatalari = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        satir = self.getpos()[0]
        if "id" in attrs_dict:
            self.id_ler.add(attrs_dict["id"])

        for attr in ("href", "src", "action", "data-src"):
            if attr in attrs_dict and attrs_dict[attr]:
                self.baglantilar.append((tag, attr, attrs_dict[attr], satir))

        # Kapanmayan tekil etiketler haricindekileri yığına ekle
        if tag not in ("area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"):
            self.etiket_yigini.append((tag, satir))

    def handle_endtag(self, tag):
        if tag in ("area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"):
            return
        if self.etiket_yigini:
            son_tag, satir = self.etiket_yigini[-1]
            if son_tag == tag:
                self.etiket_yigini.pop()
            else:
                # Eşleşmeyen tag
                pass

def test_javascript_syntax():
    print("=== 1. JAVASCRIPT SÖZDİZİMİ VE ÇALIŞMA DENETİMİ ===")
    jsc = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
    hatalar = []
    js_dosyalar = list(PUBLIC.glob("*.js"))
    for f in js_dosyalar:
        # jsc ile tarayıcı stub'ları ekleyerek sözdizimini doğrula
        kod = f.read_text(encoding="utf-8")
        sarmalayici = f"""
        var window = this;
        var document = {{ addEventListener: function(){{}}, getElementById: function(){{ return {{}}; }}, querySelector: function(){{ return null; }}, querySelectorAll: function(){{ return []; }} }};
        var navigator = {{ userAgent: 'test', mediaDevices: {{}} }};
        var localStorage = {{ getItem: function(){{ return null; }}, setItem: function(){{}} }};
        var location = {{ search: '', pathname: '/', href: 'https://derskutusu.com/' }};
        var history = {{ pushState: function(){{}}, replaceState: function(){{}} }};
        var AudioContext = function(){{}};
        var MediaRecorder = function(){{}};
        try {{
            // Sözdizimi analizi için Function oluşturucu
            new Function({json.dumps(kod)});
        }} catch(e) {{
            print("HATA: " + e.message + " | Satır: " + e.line);
        }}
        """
        sonuc = subprocess.run([jsc, "-e", sarmalayici], capture_output=True, text=True)
        if "HATA:" in sonuc.stdout or sonuc.returncode != 0:
            hatalar.append(f"{f.name}: {sonuc.stdout.strip() or sonuc.stderr.strip()}")
        else:
            print(f"  ✓ {f.name} sözdizimi kusursuz")

    return hatalar

def test_html_ve_kirik_linkler():
    print("\n=== 2. HTML, KIRIK BAĞLANTI VE EKSİK KAYNAK DENETİMİ ===")
    kirik_linkler = []
    eksik_gorseller = []
    eksik_script_css = []
    
    html_dosyalar = list(PUBLIC.glob("*.html"))
    ozet_html_dosyalar = list((PUBLIC / "ozet").glob("*.html"))
    tum_html = html_dosyalar + ozet_html_dosyalar
    
    print(f"  Toplam {len(tum_html)} HTML sayfası inceleniyor...")

    # Sayfaların id haritası
    sayfa_id_haritasi = {}
    parsers = {}

    for f in tum_html:
        icerik = f.read_text(encoding="utf-8")
        p = BaglantiToplayici(f)
        try:
            p.feed(icerik)
        except Exception as e:
            kirik_linkler.append(f"{f.relative_to(KOK)}: HTML ayrıştırma hatası: {e}")
        sayfa_id_haritasi[f] = p.id_ler
        parsers[f] = p

    for f, p in parsers.items():
        for tag, attr, val, satir in p.baglantilar:
            val = val.strip()
            if not val or val.startswith("javascript:") or val.startswith("mailto:") or val.startswith("tel:"):
                continue
            if val.startswith("http://") or val.startswith("https://") or val.startswith("//"):
                continue # Harici link
            
            # Sayfa içi çapa (#id)
            if val.startswith("#"):
                hedef_id = val[1:]
                if hedef_id and hedef_id not in p.id_ler:
                    # id gerçekten var mı?
                    kirik_linkler.append(f"{f.relative_to(KOK)}:{satir} -> Kırık iç çapa '#{hedef_id}' (sayfada bulunamadı)")
                continue

            # Ayrıştırma: path + query + fragment
            ayrik = urlparse(val)
            yol = unquote(ayrik.path)
            hedef_id = ayrik.fragment

            if not yol:
                # Sadece fragment
                continue

            # Mutlak ya da göreceli yol çözümleme
            if yol.startswith("/"):
                hedef_dosya = PUBLIC / yol.lstrip("/")
            else:
                hedef_dosya = (f.parent / yol).resolve()

            # Klasör ise index.html ekle
            if hedef_dosya.is_dir():
                if (hedef_dosya / "index.html").exists():
                    hedef_dosya = hedef_dosya / "index.html"

            # Dosya var mı?
            if not hedef_dosya.exists():
                # .html uzantısız link olabilir mi? (örn /kpss -> /kpss.html)
                if hedef_dosya.with_suffix(".html").exists():
                    hedef_dosya = hedef_dosya.with_suffix(".html")
                else:
                    hata_metni = f"{f.relative_to(KOK)}:{satir} -> Kırık {attr}='{val}' (Dosya yok: {hedef_dosya.relative_to(KOK) if KOK in hedef_dosya.parents else hedef_dosya})"
                    if tag in ("img", "image"):
                        eksik_gorseller.append(hata_metni)
                    elif tag in ("script", "link"):
                        eksik_script_css.append(hata_metni)
                    else:
                        kirik_linkler.append(hata_metni)
                    continue

            # Eğer hedef bir HTML dosyası ve fragment varsa id kontrolü
            if hedef_id and hedef_dosya in sayfa_id_haritasi:
                if hedef_id not in sayfa_id_haritasi[hedef_dosya]:
                    kirik_linkler.append(f"{f.relative_to(KOK)}:{satir} -> Kırık hedef çapa '{val}' (Hedefte '#{hedef_id}' yok)")

    return kirik_linkler, eksik_gorseller, eksik_script_css

def test_veri_dosyalari_ve_pdf():
    print("\n=== 3. VERİ DOSYALARI VE PDF İNDİRME LİNKLERİ DENETİMİ ===")
    hatalar = []
    veri_dir = PUBLIC / "veri"
    for jf in veri_dir.glob("*.json"):
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
            print(f"  ✓ {jf.name} geçerli JSON")
        except Exception as e:
            hatalar.append(f"veri/{jf.name}: Geçersiz JSON: {e}")

    # icerikler.json içindeki dosyalar
    ic_path = veri_dir / "icerikler.json"
    if ic_path.exists():
        d = json.loads(ic_path.read_text(encoding="utf-8"))
        icerikler = d.get("icerikler", [])
        print(f"  icerikler.json: {len(icerikler)} içerik kontrol ediliyor...")
        for i, item in enumerate(icerikler):
            dosya = item.get("dosya")
            if dosya:
                temiz_dosya = urlparse(dosya).path.lstrip("/")
                gercek_yol = PUBLIC / temiz_dosya
                if not gercek_yol.exists():
                    hatalar.append(f"icerikler.json [{i}] '{item.get('baslik')}': dosya='{dosya}' diskte bulunamadı!")
            goruntule = item.get("goruntule")
            if goruntule:
                temiz_goruntule = urlparse(goruntule).path.lstrip("/")
                gercek_yol = PUBLIC / temiz_goruntule
                if not gercek_yol.exists():
                    hatalar.append(f"icerikler.json [{i}] '{item.get('baslik')}': goruntule='{goruntule}' diskte bulunamadı!")

    # belgeler.json içindeki dosyalar
    b_path = veri_dir / "belgeler.json"
    if b_path.exists():
        d = json.loads(b_path.read_text(encoding="utf-8"))
        for g in d.get("gruplar", []):
            for b in g.get("belgeler", []):
                dosya = b.get("dosya")
                if dosya:
                    gercek_yol = PUBLIC / dosya.lstrip("/")
                    if not gercek_yol.exists():
                        hatalar.append(f"belgeler.json '{b.get('ad')}': dosya='{dosya}' diskte bulunamadı!")

    return hatalar

def main():
    js_hatalar = test_javascript_syntax()
    kirik, eksik_gorsel, eksik_kaynak = test_html_ve_kirik_linkler()
    veri_hatalar = test_veri_dosyalari_ve_pdf()

    print("\n================ ÖZET RAPOR ================")
    toplam_hata = len(js_hatalar) + len(kirik) + len(eksik_gorsel) + len(eksik_kaynak) + len(veri_hatalar)
    print(f"JavaScript Hataları: {len(js_hatalar)}")
    for h in js_hatalar[:10]:
        print(f"  ❌ {h}")
    print(f"Kırık Bağlantılar (A HREF): {len(kirik)}")
    for h in kirik[:20]:
        print(f"  ❌ {h}")
    if len(kirik) > 20:
        print(f"  ... ve {len(kirik)-20} daha fazla kırık bağlantı")
    print(f"Eksik Görseller (IMG SRC): {len(eksik_gorsel)}")
    for h in eksik_gorsel[:10]:
        print(f"  ❌ {h}")
    print(f"Eksik Script / CSS: {len(eksik_kaynak)}")
    for h in eksik_kaynak[:10]:
        print(f"  ❌ {h}")
    print(f"Veri / Dosya Hataları: {len(veri_hatalar)}")
    for h in veri_hatalar[:10]:
        print(f"  ❌ {h}")

    print(f"\nTOPLAM BULGU SAYISI: {toplam_hata}")
    if toplam_hata > 0:
        # Detaylı log dosyasına yaz
        rapor_dosyasi = KOK / "test_raporu.json"
        rapor_dosyasi.write_text(json.dumps({
            "js_hatalar": js_hatalar,
            "kirik_linkler": kirik,
            "eksik_gorseller": eksik_gorsel,
            "eksik_kaynaklar": eksik_kaynak,
            "veri_hatalari": veri_hatalar
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Detaylı rapor kaydedildi: {rapor_dosyasi}")

if __name__ == "__main__":
    main()
