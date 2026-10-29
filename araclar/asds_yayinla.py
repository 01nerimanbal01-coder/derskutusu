#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""asds_yayinla.py — Akademik Süreç Değerlendirme Sınavlarını (ASDS) derskutusu.com sitesine hazırlar.

Her sınıf (5, 6, 7, 8) ve her hafta (2026-09-H3 .. 2026-11-H2) için:
  1. Cevapsız A Kitapçığı: /asds/pdf/asds-<sinif>-<hafta>-a.pdf
  2. Cevapsız B Kitapçığı: /asds/pdf/asds-<sinif>-<hafta>-b.pdf
  3. Cevaplı A Kitapçığı (Doğru şıklar işaretli + A Cevap Anahtarı): /asds/pdf/asds-<sinif>-<hafta>-a-cevapli.pdf
  4. Cevaplı B Kitapçığı (Doğru şıklar işaretli + B Cevap Anahtarı): /asds/pdf/asds-<sinif>-<hafta>-b-cevapli.pdf
  5. Cevap Anahtarı (A & B Birleşik): /asds/pdf/asds-<sinif>-<hafta>-anahtar.pdf

Ayrıca public/veri/asds.json, public/veri/dersler.json ve public/veri/icerikler.json dosyalarını günceller.
"""

import json
import re
import shutil
import sys
from pathlib import Path

import fitz  # PyMuPDF

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
PUBLIC = KOK / "public"
ASDS_PROJE = Path("/Volumes/MFB-ÇALIŞMA/01-PROJELER/OKUL-ASDS-AKADEMIK-SUREC-DEGERLENDIRME-171020262341")
ASDS_PDF_KOK = ASDS_PROJE / "05-PDF"
ASDS_ICERIK_KOK = ASDS_PROJE / "04-ICERIK"
FONT_YOL = Path("/Volumes/MFB-ÇALIŞMA/01-PROJELER/SITE-EGITIM-SOSYAL-280920262119/03-ARACLAR/_calisma/font/Montserrat-700.ttf")

sys.path.insert(0, str(ASDS_PROJE / "03-ARACLAR"))
import flipbook_uret as F  # noqa: E402

HAFTA_BILGI = [
    ("2026-09-H3", 1, "Eylül · 3. Hafta", "21–25 Eylül 2026", "1. Okul Haftası Kazanımları (14–18 Eylül)", "2026-09-25"),
    ("2026-09-H4", 2, "Eylül · 4. Hafta", "28 Eylül – 2 Ekim 2026", "2. Okul Haftası Kazanımları (21–25 Eylül)", "2026-10-02"),
    ("2026-10-H1", 3, "Ekim · 1. Hafta", "5–9 Ekim 2026", "3. Okul Haftası Kazanımları (28 Eylül – 2 Ekim)", "2026-10-09"),
    ("2026-10-H2", 4, "Ekim · 2. Hafta", "12–16 Ekim 2026", "4. Okul Haftası Kazanımları (5–9 Ekim)", "2026-10-16"),
    ("2026-10-H3", 5, "Ekim · 3. Hafta", "19–23 Ekim 2026", "5. Okul Haftası Kazanımları (12–16 Ekim)", "2026-10-23"),
    ("2026-10-H4", 6, "Ekim · 4. Hafta", "26–30 Ekim 2026", "6. Okul Haftası Kazanımları (19–23 Ekim)", "2026-10-27"),
    ("2026-11-H1", 7, "Kasım · 1. Hafta", "2–6 Kasım 2026", "7. Okul Haftası Kazanımları (26–30 Ekim)", "2026-10-28"),
    ("2026-11-H2", 8, "Kasım · 2. Hafta", "9–13 Kasım 2026", "8. Okul Haftası Kazanımları (2–6 Kasım)", "2026-10-29"),
]

H1_KAPSAM = {
    "5": [
        ["Türkçe", "T.D.5.1 · T.D.5.4 · “Oyun Durdu!” dinleme/izleme metni, söz varlığı ve bağlamdan anlam"],
        ["Matematik", "MAT.5.3.1 · Temel geometrik çizimler (nokta, doğru, doğru parçası, ışın ve açı)"],
        ["Fen Bilimleri", "FB.5.1.1 · Gökyüzündeki komşumuz Güneş: Güneş’in yapısı ve dönme hareketi"],
        ["Sosyal Bilgiler", "SB.5.1.1 · Gruplar ve roller: dahil olunan gruplar ve bu gruplardaki roller"],
        ["Din Kültürü", "DKAB.5.1.1 · Evrendeki mükemmel düzen ve Allah’ın (cc) varlığı/birliği"],
    ],
    "6": [
        ["Türkçe", "T.D.6.1 · T.D.6.4 · Dilimizin zenginliği, sözcükte ve söz öbeklerinde anlam"],
        ["Matematik", "MAT.6.1.1 · Doğal sayıların çarpanları ve katları, bölünebilme kuralları"],
        ["Fen Bilimleri", "FB.6.1.1 · Güneş sistemi ve gezegenlerin temel özellikleri"],
        ["Sosyal Bilgiler", "SB.6.1.1 · Zaman içinde değişen grup, kurum ve sosyal roller"],
        ["Din Kültürü", "DKAB.6.1.1 · Peygamber ve ilahi kitap inancı, vahyin gönderiliş amacı"],
    ],
    "7": [
        ["Türkçe", "T.7.3.5 · Bağlamdan hareketle kelime ve kelime gruplarının anlamını çıkarma"],
        ["Matematik", "M.7.1.1.1 · Tam sayılarla toplama ve çıkarma işlemleri, sayı doğrusu modelleri"],
        ["Fen Bilimleri", "F.7.1.1.1 · Uzay araştırmaları, uzay teknolojileri ve teleskobun yapısı"],
        ["Sosyal Bilgiler", "SB.7.1.1 · İletişim ve insan ilişkileri: olumlu iletişim yolları ve empati"],
        ["Din Kültürü", "DKAB.7.1.1 · Varlıklar âlemi: görülen ve görülmeyen varlıklar, melekler"],
    ],
    "8": [
        ["Türkçe", "T.8.3.5 · Sözcükte ve söz öbeklerinde anlam, fiilimsiler (eylemsi) giriş"],
        ["İnkılap Tarihi", "İTA.8.1.1 · Uyanan Avrupa ve sarsılan Osmanlı: Fransız İhtilali ve Sanayi İnkılabı"],
        ["Din Kültürü", "8.1.1 · Kader ve kaza inancı, Allah’ın her şeyi bir ölçüye göre yaratması"],
        ["İngilizce", "E8.1.R1 · Friendship: arkadaşlık özellikleri, davet kabul ve ret ifadeleri"],
        ["Matematik", "M.8.1.1.1 · Verilen pozitif tam sayıların pozitif tam sayı çarpanları ve asal çarpanlar"],
        ["Fen Bilimleri", "F.8.1.1.1 · Mevsimlerin oluşumu: Dünya’nın eksen eğikliği ve dolanma hareketi"],
    ],
}

SINIF_META = {
    "5": {
        "sinif": 5,
        "baslik": "5. Sınıf Akademik Süreç Değerlendirme Sınavları (ASDS)",
        "kisa_baslik": "5. Sınıf Deneme Sınavları",
        "renk": "yesil",
        "soru_sayisi": 45,
        "sure": 40,
        "sayfa_sayisi": 24,
        "puanlama": "3 yanlış 1 doğruyu götürür · TYMM ve İOKBS bursluluk sınavı dağılımı",
        "ders_dagilimi": [
            {"ders": "Türkçe", "kod": "turkce", "soru": 10},
            {"ders": "Matematik", "kod": "matematik", "soru": 10},
            {"ders": "Fen Bilimleri", "kod": "fen-bilimleri", "soru": 10},
            {"ders": "Sosyal Bilgiler", "kod": "sosyal-bilgiler", "soru": 10},
            {"ders": "Din Kültürü ve Ahlak Bilgisi", "kod": "din-kulturu-ve-ahlak-bilgisi", "soru": 5},
        ],
    },
    "6": {
        "sinif": 6,
        "baslik": "6. Sınıf Akademik Süreç Değerlendirme Sınavları (ASDS)",
        "kisa_baslik": "6. Sınıf Deneme Sınavları",
        "renk": "turuncu",
        "soru_sayisi": 45,
        "sure": 40,
        "sayfa_sayisi": 24,
        "puanlama": "3 yanlış 1 doğruyu götürür · TYMM ve İOKBS bursluluk sınavı dağılımı",
        "ders_dagilimi": [
            {"ders": "Türkçe", "kod": "turkce", "soru": 10},
            {"ders": "Matematik", "kod": "matematik", "soru": 10},
            {"ders": "Fen Bilimleri", "kod": "fen-bilimleri", "soru": 10},
            {"ders": "Sosyal Bilgiler", "kod": "sosyal-bilgiler", "soru": 10},
            {"ders": "Din Kültürü ve Ahlak Bilgisi", "kod": "din-kulturu-ve-ahlak-bilgisi", "soru": 5},
        ],
    },
    "7": {
        "sinif": 7,
        "baslik": "7. Sınıf Akademik Süreç Değerlendirme Sınavları (ASDS)",
        "kisa_baslik": "7. Sınıf Deneme Sınavları",
        "renk": "mor",
        "soru_sayisi": 45,
        "sure": 40,
        "sayfa_sayisi": 24,
        "puanlama": "3 yanlış 1 doğruyu götürür · TYMM ve İOKBS bursluluk sınavı dağılımı",
        "ders_dagilimi": [
            {"ders": "Türkçe", "kod": "turkce", "soru": 10},
            {"ders": "Matematik", "kod": "matematik", "soru": 10},
            {"ders": "Fen Bilimleri", "kod": "fen-bilimleri", "soru": 10},
            {"ders": "Sosyal Bilgiler", "kod": "sosyal-bilgiler", "soru": 10},
            {"ders": "Din Kültürü ve Ahlak Bilgisi", "kod": "din-kulturu-ve-ahlak-bilgisi", "soru": 5},
        ],
    },
    "8": {
        "sinif": 8,
        "baslik": "8. Sınıf Akademik Süreç Değerlendirme Sınavları (ASDS · LGS)",
        "kisa_baslik": "8. Sınıf (LGS) Deneme Sınavları",
        "renk": "lacivert",
        "soru_sayisi": 45,
        "sure": 40,
        "sayfa_sayisi": 24,
        "puanlama": "3 yanlış 1 doğruyu götürür · LGS Sözel (25 soru) ve Sayısal (20 soru) katsayılı puanlama",
        "ders_dagilimi": [
            {"ders": "Türkçe", "kod": "turkce", "soru": 10, "bolum": "Sözel"},
            {"ders": "T.C. İnkılap Tarihi ve Atatürkçülük", "kod": "tc-inkilap-tarihi-ve-ataturkculuk", "soru": 5, "bolum": "Sözel"},
            {"ders": "Din Kültürü ve Ahlak Bilgisi", "kod": "din-kulturu-ve-ahlak-bilgisi", "soru": 5, "bolum": "Sözel"},
            {"ders": "İngilizce", "kod": "ingilizce", "soru": 5, "bolum": "Sözel"},
            {"ders": "Matematik", "kod": "matematik", "soru": 10, "bolum": "Sayısal"},
            {"ders": "Fen Bilimleri", "kod": "fen-bilimleri", "soru": 10, "bolum": "Sayısal"},
        ],
    },
}


def temiz_metin(s: str) -> str:
    """yayin_denetle.py kurallarına uygun olarak düz karekök işaretini temizler."""
    return re.sub(r"[√∛∜]", "kök ", str(s or "")).strip()


def kapsam_bul(sinif: str, hafta_idx: int) -> list:
    if hafta_idx == 0:
        return [[temiz_metin(a), temiz_metin(b)] for a, b in H1_KAPSAM[sinif]]
    onceki_kod = HAFTA_BILGI[hafta_idx - 1][0]
    p = ASDS_ICERIK_KOK / onceki_kod / sinif / "KAPSAM-SONRAKI.json"
    if p.exists():
        veri = json.loads(p.read_text(encoding="utf-8"))
        return [[temiz_metin(x[0]), temiz_metin(x[1])] for x in veri.get("satirlar", [])]
    return [[temiz_metin(a), temiz_metin(b)] for a, b in H1_KAPSAM[sinif]]


def cevapli_kitapcik_uret(kaynak_pdf: Path, anahtar_pdf: Path, kitapcik: str, hedef_pdf: Path) -> int:
    """Kitapçık PDF'inde her sorunun doğru şıkkını yeşil vurgu çerçevesiyle işaretler,
    kapağa 'CEVAPLI KİTAPÇIK · ÇÖZÜM ANAHTARLI' rozeti ekler ve sonuna ilgili kitapçığın
    Cevap Anahtarı sayfasını birleştirir."""
    ans = F.anahtar_cozumle(str(anahtar_pdf), kitapcik)
    doc = fitz.open(str(kaynak_pdf))
    anahtar_doc = fitz.open(str(anahtar_pdf))
    _bol, sv = F.sayfa_bolumlerini_ve_siklarini_cikar(doc, ans)

    eslesen = 0
    for pinfo in sv:
        pno = pinfo["sayfa"] - 1
        page = doc[pno]
        tb = page.trimbox if page.trimbox else page.mediabox
        tw, th = tb.width, tb.height
        ox, oy = tb.x0, tb.y0
        for q in pinfo["sorular"]:
            dogru = q["dogru"]
            for s in q["siklar"]:
                if s["harf"] == dogru:
                    eslesen += 1
                    x0 = ox + (s["x"] / 100.0) * tw
                    y0 = oy + (s["y"] / 100.0) * th
                    x1 = x0 + (s["w"] / 100.0) * tw
                    y1 = y0 + (s["h"] / 100.0) * th
                    r = fitz.Rect(x0 - 2.0, y0 - 0.6, x1 + 1.2, y1 + 0.6)
                    shape = page.new_shape()
                    shape.draw_rect(r, radius=0.22)
                    shape.finish(
                        color=(0.06, 0.50, 0.23),
                        fill=(0.09, 0.68, 0.31),
                        fill_opacity=0.20,
                        width=0.75,
                    )
                    shape.commit()

    # Kapak sayfasına CEVAPLI KİTAPÇIK rozeti
    p0 = doc[0]
    tb0 = p0.trimbox if p0.trimbox else p0.mediabox
    r_etiket = fitz.Rect(tb0.x0 + 99.0, tb0.y0 + 55.5, tb0.x0 + 326.0, tb0.y0 + 68.5)
    sh0 = p0.new_shape()
    sh0.draw_rect(r_etiket, radius=0.25)
    sh0.finish(
        color=(0.05, 0.45, 0.21),
        fill=(0.07, 0.55, 0.26),
        fill_opacity=0.96,
        width=0.75,
    )
    sh0.commit()
    if FONT_YOL.exists():
        p0.insert_font(fontname="MontBold", fontfile=str(FONT_YOL))
        p0.insert_textbox(
            fitz.Rect(r_etiket.x0, r_etiket.y0 + 1.8, r_etiket.x1, r_etiket.y1),
            f"CEVAPLI {kitapcik} KİTAPÇIĞI  ·  ÇÖZÜM ANAHTARLI",
            fontsize=6.5,
            fontname="MontBold",
            color=(1, 1, 1),
            align=fitz.TEXT_ALIGN_CENTER,
        )

    # Son sayfaya ilgili kitapçığın (A -> 0, B -> 1) cevap anahtarını ekle
    anahtar_sayfa = 0 if kitapcik.upper() == "A" else (1 if len(anahtar_doc) > 1 else 0)
    doc.insert_pdf(anahtar_doc, from_page=anahtar_sayfa, to_page=anahtar_sayfa)

    hedef_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(hedef_pdf), garbage=3, deflate=True)
    doc.close()
    anahtar_doc.close()
    return eslesen


def main():
    pdf_hedef_kl = PUBLIC / "asds" / "pdf"
    pdf_hedef_kl.mkdir(parents=True, exist_ok=True)

    sinif_bloklari = {s: dict(SINIF_META[s], sinavlar=[]) for s in ("5", "6", "7", "8")}
    icerik_kayitlari = []
    toplam_pdf = 0

    for h_idx, (h_kod, deneme_no, h_ad, tarih_araligi, olculen_aciklama, yayin_tarihi) in enumerate(HAFTA_BILGI):
        kaynak_kl = ASDS_PDF_KOK / h_kod
        if not kaynak_kl.exists():
            continue
        for s in ("5", "6", "7", "8"):
            kaynak_a = kaynak_kl / f"ASDS-{s}-{h_kod}-A.pdf"
            kaynak_b = kaynak_kl / f"ASDS-{s}-{h_kod}-B.pdf"
            kaynak_anahtar = kaynak_kl / f"ASDS-{s}-{h_kod}-ANAHTAR.pdf"
            if not (kaynak_a.exists() and kaynak_b.exists() and kaynak_anahtar.exists()):
                print(f"ATLANDI (eksik PDF): Sınıf {s} · {h_kod}")
                continue

            kod_kucuk = h_kod.lower()
            rel_a = f"asds/pdf/asds-{s}-{kod_kucuk}-a.pdf"
            rel_b = f"asds/pdf/asds-{s}-{kod_kucuk}-b.pdf"
            rel_a_cevapli = f"asds/pdf/asds-{s}-{kod_kucuk}-a-cevapli.pdf"
            rel_b_cevapli = f"asds/pdf/asds-{s}-{kod_kucuk}-b-cevapli.pdf"
            rel_anahtar = f"asds/pdf/asds-{s}-{kod_kucuk}-anahtar.pdf"

            shutil.copy2(kaynak_a, PUBLIC / rel_a)
            shutil.copy2(kaynak_b, PUBLIC / rel_b)
            shutil.copy2(kaynak_anahtar, PUBLIC / rel_anahtar)

            es_a = cevapli_kitapcik_uret(kaynak_a, kaynak_anahtar, "A", PUBLIC / rel_a_cevapli)
            es_b = cevapli_kitapcik_uret(kaynak_b, kaynak_anahtar, "B", PUBLIC / rel_b_cevapli)
            toplam_pdf += 5

            kapsam = kapsam_bul(s, h_idx)
            cevap_ozeti = F.anahtar_cozumle(str(kaynak_anahtar), "A") or {}

            sinav_nesnesi = {
                "kimlik": f"asds-{s}-{kod_kucuk}",
                "sinif": int(s),
                "deneme_no": deneme_no,
                "hafta_kodu": h_kod,
                "hafta": deneme_no,
                "ad": f"ASDS Deneme {deneme_no} · {h_ad}",
                "hafta_adi": h_ad,
                "tarih_araligi": tarih_araligi,
                "olculen_hafta": olculen_aciklama,
                "yayin_tarihi": yayin_tarihi,
                "soru_sayisi": 45,
                "sure": 40,
                "sayfa_sayisi": 24,
                "kapsam": kapsam,
                "dosyalar": {
                    "a_cevapsiz": f"/{rel_a}",
                    "b_cevapsiz": f"/{rel_b}",
                    "a_cevapli": f"/{rel_a_cevapli}",
                    "b_cevapli": f"/{rel_b_cevapli}",
                    "anahtar": f"/{rel_anahtar}",
                },
                "anahtar_a": {k: "".join(v) for k, v in cevap_ozeti.items()},
            }
            sinif_bloklari[s]["sinavlar"].append(sinav_nesnesi)

            kapsam_kisa = " · ".join(f"{ d_ad }: { d_konu.split('·')[-1].strip() }" for d_ad, d_konu in kapsam[:3])
            ana_ders = "matematik" if s != "8" else "turkce"
            icerik_kayitlari.append({
                "sinif": int(s),
                "ders": ana_ders,
                "tur": "Deneme sınavı",
                "kitle": "ogrenci",
                "baslik": f"{s}. Sınıf ASDS Deneme Sınavı {deneme_no} ({h_ad}) — A & B Kitapçığı (Cevapsız ve Cevaplı)",
                "aciklama": f"45 soru, 40 dakika · Cevapsız A ve B kitapçıkları, doğru seçenekleri işaretli Cevaplı A/B kitapçıkları ve cevap anahtarı PDF ({kapsam_kisa}).",
                "goruntule": f"sinav.html?sinif={s}#asds-{s}-{kod_kucuk}",
                "dosya": rel_a,
                "kaynak": "Ders Kutusu",
                "hafta": deneme_no,
                "tarih": yayin_tarihi,
            })
            print(f"Hazır: {s}. Sınıf · {h_kod} ({h_ad}) -> A({es_a}/45), B({es_b}/45) cevaplı + cevapsız + anahtar")

    asds_veri = {
        "aciklama": "Akademik Süreç Değerlendirme Sınavı (ASDS) — 5, 6, 7 ve 8. sınıflar için haftalık sarmal/kazanım değerlendirme sınavları. Her sınıf için ayrı başlık altında Cevapsız A ve B kitapçıkları ile Cevaplı A/B kitapçıkları ve Cevap Anahtarı yer alır.",
        "guncelleme": "2026-10-29",
        "toplam_sinav": sum(len(b["sinavlar"]) for b in sinif_bloklari.values()),
        "toplam_pdf": toplam_pdf,
        "siniflar": [sinif_bloklari[s] for s in ("5", "6", "7", "8")],
    }
    (PUBLIC / "veri" / "asds.json").write_text(
        json.dumps(asds_veri, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )

    # dersler.json içine "Deneme sınavı" türünü ekle
    dersler_p = PUBLIC / "veri" / "dersler.json"
    dersler_v = json.loads(dersler_p.read_text(encoding="utf-8"))
    mevcut_turler = {t["ad"] for t in dersler_v.get("turler", [])}
    if "Deneme sınavı" not in mevcut_turler:
        dersler_v["turler"].insert(2, {"ad": "Deneme sınavı", "kitle": "ogretmen"})
        dersler_p.write_text(json.dumps(dersler_v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # icerikler.json güncelle
    icerikler_p = PUBLIC / "veri" / "icerikler.json"
    icerikler_v = json.loads(icerikler_p.read_text(encoding="utf-8"))
    diger = [k for k in icerikler_v.get("icerikler", []) if k.get("tur") != "Deneme sınavı"]
    icerikler_v["icerikler"] = diger + icerik_kayitlari
    icerikler_p.write_text(json.dumps(icerikler_v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"Tamamlandı: {asds_veri['toplam_sinav']} sınav, {toplam_pdf} PDF, public/veri/asds.json ve icerikler.json güncellendi.")


if __name__ == "__main__":
    main()
