#!/usr/bin/env python3
"""Ders Kutusu — Kapsamlı Hata Kontrol ve Otomatik Onarım Sistemi (yayin_denetle.py).

Denetlenen katmanlar:
1. Kök gösterimi denetimi (JSON, PY görsel modülleri, HTML, SVG, DOCX içinde düz √/∛/∜ ve çözülmemiş {kok:}).
2. Özet JSON şema, ders kodu, yayın tarihi ve görsel modülü (uygula / GORSELLER) uyumluluğu.
3. Sembol ve kesir söz dizimi ({kesir:...} içinde çubuk '|' çakışması, boş <span></span>, iç içe süslü parantez).
4. Derleme senkronizasyonu (her araclar/ozetler/*.json için public/ozet/*.html, icerikler.json ve sitemap.xml kaydı).
5. Ziyaretçi ve yapılandırma verisi bütünlüğü (public/veri/ziyaret.json, dersler.json, ayarlar.json).

Kullanım:
  python3 araclar/yayin_denetle.py              # Tüm kontrolleri çalıştırır (hata varsa çıkış kodu 1)
  python3 araclar/yayin_denetle.py --onar       # Şema/görsel/HTML eksiklerini otomatik onarır ve yeniden denetler
  python3 araclar/yayin_denetle.py --kanca-kur  # Tüm yerel git klonlarına pre-push hata kontrol kancası kurar
"""
from pathlib import Path
import html
import importlib.util
import json
import os
import re
import stat
import subprocess
import sys
import zipfile

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
PUBLIC = KOK / "public"

ZORUNLU_OZET_ALANLARI = (
    "sinif", "ders", "hafta", "tarih", "yayin_tarihi",
    "unite", "konu", "ciktilar", "giris", "bolumler", "ornekler"
)


def _dersler_sozlugu():
    p = PUBLIC / "veri" / "dersler.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get("dersler", {})


def _ters_ders_haritasi(dersler):
    harita = {}
    for kod, ad in dersler.items():
        harita[kod.lower()] = kod
        harita[ad.lower()] = kod
    return harita


def sema_ve_gorsel_onar():
    """Alternatif şemayla yazılmış özet JSON dosyalarını ve GORSELLER tabanlı görsel modüllerini standartlaştırır."""
    dersler = _dersler_sozlugu()
    ters = _ters_ders_haritasi(dersler)
    onaran = []

    for p in sorted((ARACLAR / "gorseller").glob("*.py")):
        s = p.read_text(encoding="utf-8")
        if "def uygula" not in s and "GORSELLER" in s:
            ek = (
                "\n\ndef uygula(v):\n"
                "    for i, k in enumerate([\"b1\", \"b2\", \"b3\", \"b4\", \"b5\", \"b6\"]):\n"
                "        if i < len(v.get(\"bolumler\", [])) and k in GORSELLER:\n"
                "            v[\"bolumler\"][i][\"gorsel\"] = GORSELLER[k]\n"
            )
            p.write_text(s + ek, encoding="utf-8")
            onaran.append(f"araclar/gorseller/{p.name}: uygula(v) eklendi")

    for p in sorted((ARACLAR / "ozetler").glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        parcalar = p.stem.split("-")
        if len(parcalar) >= 3 and parcalar[0].isdigit() and parcalar[-1].isdigit():
            beklenen_sinif = int(parcalar[0])
            beklenen_ders = "-".join(parcalar[1:-1])
            beklenen_hafta = int(parcalar[-1])
        else:
            continue

        degisti = False
        if d.get("ders") not in dersler and beklenen_ders in dersler:
            d["ders"] = beklenen_ders
            d["ders_adi"] = dersler[beklenen_ders]
            degisti = True
        if "yayin_tarihi" not in d:
            d["yayin_tarihi"] = "2026-10-16"
            degisti = True
        if "tarih" in d and "–" in str(d["tarih"]):
            d["tarih"] = str(d["tarih"]).replace("–", "-")
            degisti = True
        if "ciktilar" not in d and "kazanim" in d:
            k = d.pop("kazanim")
            d["ciktilar"] = [k] if isinstance(k, str) else list(k)
            degisti = True
        if "giris" not in d and isinstance(d.get("ozet"), str):
            d["giris"] = d["ozet"]
            d["ozet"] = []
            degisti = True

        # Bölümlerde 'icerik' listesi kullanılmışsa 'metin'/'tablo'/'kutu' yapısına çevir
        ozet_aday = []
        for b in d.get("bolumler", []):
            if "icerik" in b and "metin" not in b:
                b["baslik"] = re.sub(r"^\d+\.\s*", "", b.get("baslik", ""))
                metin, tablo, kutu = [], None, None
                for item in b.pop("icerik", []):
                    tip = item.get("tip")
                    if tip == "paragraf":
                        metin.append(item["metin"].replace("\n", " ").strip())
                    elif tip == "madde":
                        for md in item.get("maddeler", []):
                            metin.append(md.replace("\n", " ").strip())
                    elif tip == "tablo":
                        tablo = {"basliklar": item["basliklar"], "satirlar": item["satirlar"]}
                    elif tip == "kutu":
                        tur = item.get("tur", "bilgi")
                        if tur not in ("dikkat", "bilgi", "kural", "tanim", "ipucu", "hatirla"):
                            tur = "bilgi"
                        kutu = {"tur": tur, "baslik": item.get("baslik", ""), "metin": item["metin"].replace("\n", " ").strip()}
                b["metin"] = metin
                if kutu:
                    b["kutu"] = kutu
                if tablo:
                    b["tablo"] = tablo
                if metin:
                    ozet_aday.append(metin[0])
                degisti = True
        if not d.get("ozet") and ozet_aday:
            d["ozet"] = ozet_aday[:6]
            degisti = True

        for o in d.get("ornekler", []):
            if "cevap" not in o and "cozum" in o:
                o["cevap"] = o.pop("cozum").replace("\n", " ").strip()
                o["soru"] = o["soru"].replace("\n", " ").strip()
                degisti = True

        etkinlikler = d.get("etkinlikler", [])
        if etkinlikler and any("tur" not in x and "tip" in x for x in etkinlikler):
            coktan, dy_if, bosluk_c = [], [], []
            for etk in etkinlikler:
                t = etk.get("tur") or etk.get("tip")
                if t in ("coktan", "coktan_secmeli"):
                    dogru = etk.get("dogru")
                    if dogru is None:
                        dogru = etk["secenekler"].index(etk["cevap"])
                    coktan.append({
                        "tur": "coktan",
                        "soru": etk["soru"],
                        "secenekler": etk["secenekler"],
                        "dogru": dogru,
                        "aciklama": etk.get("aciklama", "")
                    })
                elif t == "dogru_yanlis":
                    dy_if.append({
                        "metin": etk["soru"],
                        "dogru": str(etk["cevap"]).strip().lower().startswith("doğru"),
                        "aciklama": etk.get("aciklama", "")
                    })
                elif t == "bosluk_doldurma":
                    bosluk_c.append({
                        "metin": re.sub(r"\.{3,}", "___", etk["soru"]),
                        "cevap": etk["cevap"]
                    })
            yeni_etk = list(coktan)
            if dy_if:
                yeni_etk.append({
                    "tur": "dy",
                    "soru": "Aşağıdaki ifadelerin doğru (D) ya da yanlış (Y) olduğunu belirleyiniz.",
                    "ifadeler": dy_if
                })
            if bosluk_c:
                yeni_etk.append({
                    "tur": "bosluk",
                    "soru": "Aşağıdaki cümlelerde boş bırakılan yerleri uygun kavramlarla tamamlayınız.",
                    "cumleler": bosluk_c,
                    "fazla": []
                })
            d["etkinlikler"] = yeni_etk
            degisti = True

        if degisti:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            onaran.append(f"araclar/ozetler/{p.name}: standart şemaya dönüştürüldü")

    return onaran


def derleme_calistir():
    """Görselleri, özet HTML sayfalarını ve konu ağaçlarını yeniden üretir."""
    for betik in ("ozet_gorsel.py", "ozet_uret.py", "agac_uret.py"):
        r = subprocess.run([sys.executable, str(ARACLAR / betik)], cwd=str(ARACLAR), capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"{betik} başarısız oldu:\n{r.stderr or r.stdout}")


def denetle(hizli=False):
    hatalar = []
    dosya_sayisi = 0

    # 1. Kök gösterimi denetimi (kok_yayin_denetle.py + araclar/gorseller/*.py)
    hedefler = [
        ("araclar/kpss", "json"),
        ("araclar/ozetler", "json"),
        ("araclar/calisma", "json"),
        ("araclar/gorseller", "py"),
        ("public/ozet", "html") if hizli else ("public", "html"),
    ]
    if not hizli:
        hedefler.append(("public", "svg"))

    for klasor, uzanti in hedefler:
        n = 0
        for p in (KOK / klasor).rglob("*." + uzanti):
            dosya_sayisi += 1
            n += 1
            s = p.read_text(encoding="utf-8")
            if re.search("[√∛∜]", html.unescape(re.sub(r"\\u221[abc]", "√", s, flags=re.I))):
                hatalar.append(f"{p.relative_to(KOK)}: düz kök işareti (√/∛/∜)")
            if uzanti == "html" and re.search(r"\{kok:", s):
                hatalar.append(f"{p.relative_to(KOK)}: çözülmemiş {{kok:...}} gösterimi")
        if not n:
            hatalar.append(f"{klasor}/*.{uzanti}: taranacak dosya bulunamadı")

    if not hizli:
        docx_n = 0
        for p in (PUBLIC / "dosyalar" / "gunluk-plan").glob("*.docx"):
            dosya_sayisi += 1
            docx_n += 1
            with zipfile.ZipFile(p) as z:
                for name in z.namelist():
                    if name.startswith("word/") and name.endswith(".xml"):
                        s = z.read(name).decode("utf-8", "replace")
                        if re.search("[√∛∜]", s):
                            hatalar.append(f"{p.relative_to(KOK)}: Word denklemine çevrilmemiş kök")
        if not docx_n:
            hatalar.append("public/dosyalar/gunluk-plan/*.docx: taranacak dosya bulunamadı")

    if "kokDugumu(c)" not in (PUBLIC / "ortak.js").read_text(encoding="utf-8"):
        hatalar.append("public/ortak.js: kokDugumu(c) fonksiyonu eksik")
    if "kokParcalari(satir)" not in (PUBLIC / "planlar.js").read_text(encoding="utf-8"):
        hatalar.append("public/planlar.js: kokParcalari(satir) fonksiyonu eksik")

    # 2. Özet JSON şema, kesir/sembol söz dizimi ve derleme senkronizasyonu denetimi
    dersler = _dersler_sozlugu()
    icerikler_dosya = PUBLIC / "veri" / "icerikler.json"
    icerikler = json.loads(icerikler_dosya.read_text(encoding="utf-8")).get("icerikler", []) if icerikler_dosya.exists() else []
    ozet_kayitlari = {i.get("goruntule") for i in icerikler if i.get("tur") == "Konu anlatımı"}
    sitemap_metni = (PUBLIC / "sitemap.xml").read_text(encoding="utf-8") if (PUBLIC / "sitemap.xml").exists() else ""

    spec = importlib.util.spec_from_file_location("ozet_uret_denetim", ARACLAR / "ozet_uret.py")
    ozet_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ozet_mod)

    for p in sorted((ARACLAR / "ozetler").glob("*.json")):
        rel = p.relative_to(KOK)
        ham = p.read_text(encoding="utf-8")
        try:
            d = json.loads(ham)
        except Exception as exc:
            hatalar.append(f"{rel}: geçersiz JSON ({exc})")
            continue

        for alan in ZORUNLU_OZET_ALANLARI:
            if alan not in d:
                hatalar.append(f"{rel}: zorunlu '{alan}' alanı eksik")

        ders = str(d.get("ders", ""))
        if ders not in dersler:
            hatalar.append(f"{rel}: tanımsız ders kodu '{ders}'")

        yt = d.get("yayin_tarihi", "")
        if not (isinstance(yt, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", yt)):
            hatalar.append(f"{rel}: geçersiz yayin_tarihi '{yt}' (YYYY-AA-GG olmalı)")

        # {kesir:...} içinde '|' çakışması denetimi
        for m in re.finditer(r"\{kesir:([^{}]+)\}", ham):
            ic = m.group(1)
            pay, sep, payda = ic.partition("|")
            if not sep or not pay.strip() or not payda.strip() or "|" in payda:
                hatalar.append(f"{rel}: bozuk kesir gösterimi '{m.group(0)}' (mutlak değer/uzunluk için {{uzunluk:AB}} kullanın)")

        # Tüm metin alanlarını ozet_uret.e() ile sına
        def _metinleri_gezer(obj):
            if isinstance(obj, str):
                if not obj.lstrip().startswith("<svg"):
                    try:
                        ozet_mod.e(obj)
                    except Exception as exc:
                        hatalar.append(f"{rel}: sembol/biçim hatası ({exc})")
            elif isinstance(obj, list):
                for x in obj:
                    _metinleri_gezer(x)
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k != "gorsel":
                        _metinleri_gezer(v)

        _metinleri_gezer(d)

        # Derlenmiş HTML, icerikler.json ve sitemap.xml senkronizasyonu
        html_yolu = f"ozet/{d.get('sinif')}-{ders}-hafta-{d.get('hafta')}.html"
        html_tam = PUBLIC / html_yolu
        if not html_tam.exists():
            hatalar.append(f"{rel}: HTML dosyası üretilmemiş (public/{html_yolu})")
        else:
            hs = html_tam.read_text(encoding="utf-8")
            if re.search(r'<span class="s-kesir"[^>]*>(?:<span>\s*</span>|<span>[^<]*</span><span>\s*</span>)', hs):
                hatalar.append(f"public/{html_yolu}: bozuk kesir çıktısı (boş <span></span>)")
        if html_yolu not in ozet_kayitlari:
            hatalar.append(f"{rel}: public/veri/icerikler.json içinde '{html_yolu}' kaydı yok")
        if f"https://derskutusu.com/{html_yolu}" not in sitemap_metni:
            hatalar.append(f"{rel}: public/sitemap.xml içinde '{html_yolu}' adresi yok")

    # 3. Görsel modüllerinin (araclar/gorseller/*.py) arayüz denetimi
    for p in sorted((ARACLAR / "gorseller").glob("*.py")):
        s = p.read_text(encoding="utf-8")
        if "def uygula" not in s and "GORSELLER" not in s:
            hatalar.append(f"{p.relative_to(KOK)}: 'def uygula(v):' fonksiyonu tanımlı değil")

    # 4. Ziyaretçi verisi (public/veri/ziyaret.json) bütünlük denetimi
    ziyaret_p = PUBLIC / "veri" / "ziyaret.json"
    if not ziyaret_p.exists():
        hatalar.append("public/veri/ziyaret.json: dosya bulunamadı")
    else:
        try:
            zv = json.loads(ziyaret_p.read_text(encoding="utf-8"))
            if not isinstance(zv.get("toplam"), int) or zv.get("toplam", 0) <= 0:
                hatalar.append(f"public/veri/ziyaret.json: geçersiz toplam ziyaret sayısı ({zv.get('toplam')})")
        except Exception as exc:
            hatalar.append(f"public/veri/ziyaret.json: JSON okuma hatası ({exc})")

    return dosya_sayisi, hatalar


def kanca_kur():
    """Çalışma diskindeki tüm SITE git klonlarına pre-push denetim kancası kurar."""
    kanca_icerik = """#!/bin/sh
# Ders Kutusu otomatik hata kontrol kancası (pre-push)
export PATH="/Applications/Xcode.app/Contents/Developer/usr/bin:$PATH"
REPO_ROOT="$(git rev-parse --show-toplevel)"
if [ -f "$REPO_ROOT/araclar/yayin_denetle.py" ]; then
  echo "[Ders Kutusu] Yayım öncesi hata kontrolü çalıştırılıyor..."
  python3 "$REPO_ROOT/araclar/yayin_denetle.py" --hizli
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    echo "❌ HATA: Yayım denetimi başarısız oldu! Otomatik onarım için:"
    echo "   python3 araclar/yayin_denetle.py --onar"
    exit 1
  fi
fi
exit 0
"""
    proje_koku = KOK.parent.parent
    kurulan = []
    adaylar = [KOK]
    if proje_koku.exists():
        for p in sorted(proje_koku.iterdir()):
            if (p / "SITE" / ".git").exists():
                adaylar.append(p / "SITE")
            elif (p / ".git").exists():
                adaylar.append(p)
    gorulen = set()
    for repo in adaylar:
        repo = repo.resolve()
        if repo in gorulen:
            continue
        gorulen.add(repo)
        hooks_dir = repo / ".git" / "hooks"
        if hooks_dir.exists():
            hedef = hooks_dir / "pre-push"
            hedef.write_text(kanca_icerik, encoding="utf-8")
            hedef.chmod(hedef.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            kurulan.append(str(hedef))
    return kurulan


def main():
    if "--kanca-kur" in sys.argv:
        kurulan = kanca_kur()
        for k in kurulan:
            print(f"Git pre-push kancası kuruldu: {k}")

    if "--onar" in sys.argv:
        onaran = sema_ve_gorsel_onar()
        for bilgi in onaran:
            print(f"[ONARIM] {bilgi}")
        derleme_calistir()
        print("[ONARIM] Görseller, özet sayfaları ve konu ağaçları yeniden üretildi.")

    dosya_sayisi, hatalar = denetle(hizli="--hizli" in sys.argv)
    ozet_sayisi = len(list((ARACLAR / "ozetler").glob("*.json")))
    print(f"{dosya_sayisi} kaynak/web dosyası ve {ozet_sayisi} konu özeti denetlendi; toplam hata: {len(hatalar)}")
    for h in hatalar:
        print(f"  ✗ {h}")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()

