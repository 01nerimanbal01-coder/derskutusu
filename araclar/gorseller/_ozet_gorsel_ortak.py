# -*- coding: utf-8 -*-
"""Görsel modülleri için ortak SVG üretim yardımcıları (tuval/kutu/ok/bitir ve svg_baslat/svg_bitir)."""
import html

DERS_RENK = {
    "peygamberimizin-hayati": {"ana": "#059669", "koyu": "#065F46", "acik": "#ECFDF5"},
    "tarih": {"ana": "#D97706", "koyu": "#92400E", "acik": "#FFFBEB"},
    "tefsir": {"ana": "#0D9488", "koyu": "#115E59", "acik": "#F0FDFA"},
    "temel-dini-bilgiler": {"ana": "#059669", "koyu": "#065F46", "acik": "#ECFDF5"},
    "turk-dili-ve-edebiyati": {"ana": "#2563EB", "koyu": "#1E3A8A", "acik": "#EFF6FF"},
}


def _esc(s):
    return html.escape(str(s or ""), quote=True)


def tuval(w, h, baslik=""):
    b = {
        "w": w,
        "h": h,
        "etiket": _esc(baslik or "Konu özet şeması"),
        "parcalar": [
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>'
        ],
    }
    if baslik:
        b["parcalar"].append(
            f'<rect x="16" y="14" width="{w - 32}" height="42" rx="10" fill="#1E293B"/>'
            f'<text x="{w // 2}" y="41" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">{_esc(baslik)}</text>'
        )
    return b, w, h


def svg_baslat(w=760, h=250):
    b = {
        "w": w,
        "h": h,
        "etiket": "Konu özet şeması",
        "parcalar": [],
    }
    return b, w, h


def arka_plan(b, w, h, renk=None):
    acik = (renk or {}).get("acik", "#F8FAFC")
    ana = (renk or {}).get("ana", "#94A3B8")
    b["parcalar"].append(
        f'<rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="14" fill="{acik}" stroke="{ana}" stroke-width="1.5"/>'
    )


def baslik_eki(b, w, baslik, alt_baslik="", renk=None):
    koyu = (renk or {}).get("koyu", "#1E3A8A")
    ana = (renk or {}).get("ana", "#2563EB")
    b["etiket"] = _esc(f"{baslik} — {alt_baslik}" if alt_baslik else baslik)
    b["parcalar"].append(
        f'<rect x="16" y="12" width="{w - 32}" height="50" rx="10" fill="{koyu}"/>'
        f'<text x="{w // 2}" y="34" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="800" fill="#FFFFFF">{_esc(baslik)}</text>'
    )
    if alt_baslik:
        b["parcalar"].append(
            f'<text x="{w // 2}" y="52" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#E2E8F0">{_esc(alt_baslik)}</text>'
        )


def kutu(b, x, y, w, h, baslik, maddeler, renk_koyu_veya_sozluk="#1E3A8A", renk_acik="#EFF6FF"):
    if isinstance(renk_koyu_veya_sozluk, dict):
        koyu = renk_koyu_veya_sozluk.get("koyu", "#1E3A8A")
        acik = "#FFFFFF"
    else:
        koyu = str(renk_koyu_veya_sozluk)
        acik = str(renk_acik)
    b["parcalar"].append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{acik}" stroke="{koyu}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" fill="{koyu}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" text-anchor="middle" font-family="sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">{_esc(baslik)}</text>'
    )
    if isinstance(maddeler, str):
        maddeler = [maddeler]
    sy = y + 54
    for m in maddeler or []:
        b["parcalar"].append(
            f'<text x="{x + 12}" y="{sy}" font-family="sans-serif" font-size="12" font-weight="600" fill="#1E293B">• {_esc(m)}</text>'
        )
        sy += 22


def ok(b, x1, y1, x2, y2, renk="#2563EB", etiket=""):
    b["parcalar"].append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="2.5" stroke-linecap="round"/>'
        f'<circle cx="{x2}" cy="{y2}" r="4" fill="{renk}"/>'
    )
    if etiket:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2 - 8
        b["parcalar"].append(
            f'<text x="{mx}" y="{my}" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="{renk}">{_esc(etiket)}</text>'
        )


def ok_ciz(b, x1, y1, x2, y2, renk="#2563EB"):
    ok(b, x1, y1, x2, y2, renk)


def kart_Akis(b, x, y, w, h, adimlar, renk=None):
    koyu = (renk or {}).get("koyu", "#1E3A8A")
    ana = (renk or {}).get("ana", "#2563EB")
    n = max(1, len(adimlar))
    gap = 12
    kw = (w - gap * (n - 1)) // n
    for i, (bas, acik) in enumerate(adimlar):
        kx = x + i * (kw + gap)
        b["parcalar"].append(
            f'<rect x="{kx}" y="{y}" width="{kw}" height="{h}" rx="10" fill="#FFFFFF" stroke="{ana}" stroke-width="2"/>'
            f'<rect x="{kx}" y="{y}" width="{kw}" height="30" rx="10" fill="{koyu}"/>'
            f'<text x="{kx + kw // 2}" y="{y + 20}" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="800" fill="#FFFFFF">{_esc(bas)}</text>'
        )
        kelimeler = str(acik).split()
        satirlar, cur = [], ""
        for kel in kelimeler:
            if len(cur) + len(kel) + 1 <= 22:
                cur = f"{cur} {kel}".strip()
            else:
                if cur:
                    satirlar.append(cur)
                cur = kel
        if cur:
            satirlar.append(cur)
        for j, st in enumerate(satirlar[:4]):
            b["parcalar"].append(
                f'<text x="{kx + kw // 2}" y="{y + 52 + j * 18}" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#1E293B">{_esc(st)}</text>'
            )


def merkez_Etiket(b, cx, cy, merkez_yazi, dallar, renk=None):
    koyu = (renk or {}).get("koyu", "#1E3A8A")
    ana = (renk or {}).get("ana", "#2563EB")
    konumlar = [
        (40, 75, 220, 62),
        (500, 75, 220, 62),
        (40, 160, 220, 62),
        (500, 160, 220, 62),
    ]
    for i, (bas, acik) in enumerate(dallar[:4]):
        kx, ky, kw, kh = konumlar[i]
        hx = kx + kw if kx < cx else kx
        hy = ky + kh // 2
        b["parcalar"].append(
            f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="{ana}" stroke-width="2" stroke-dasharray="4 3"/>'
            f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="8" fill="#FFFFFF" stroke="{ana}" stroke-width="1.8"/>'
            f'<text x="{kx + 10}" y="{ky + 22}" font-family="sans-serif" font-size="12.5" font-weight="800" fill="{koyu}">{_esc(bas)}</text>'
            f'<text x="{kx + 10}" y="{ky + 44}" font-family="sans-serif" font-size="11" font-weight="600" fill="#334155">{_esc(acik[:36])}</text>'
        )
    b["parcalar"].append(
        f'<rect x="{cx - 85}" y="{cy - 26}" width="170" height="52" rx="26" fill="{koyu}" stroke="#FFFFFF" stroke-width="2"/>'
        f'<text x="{cx}" y="{cy + 6}" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">{_esc(merkez_yazi)}</text>'
    )


def alt_not(b, w, h, metin):
    b["parcalar"].append(
        f'<rect x="24" y="{h - 42}" width="{w - 48}" height="28" rx="8" fill="#E2E8F0"/>'
        f'<text x="{w // 2}" y="{h - 23}" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1E293B">{_esc(metin)}</text>'
    )


def bitir(b):
    ic = "".join(b["parcalar"])
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {b["w"]} {b["h"]}" role="img" aria-label="{b["etiket"]}">{ic}</svg>'


def svg_bitir(b):
    return bitir(b)
