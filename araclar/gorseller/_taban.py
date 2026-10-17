"""Görsel modülleri için ortak SVG ilkel (primitive) ve renk yardımcıları."""
import html

SON_SVG = {}

DERS_RENKLERI = {
    'biyoloji': {'koyu': '#065f46', 'orta': '#059669', 'acik': '#ecfdf5'},
    'cografya': {'koyu': '#92400e', 'orta': '#d97706', 'acik': '#fffbeb'},
    'din-kulturu-ve-ahlak-bilgisi': {'koyu': '#065f46', 'orta': '#10b981', 'acik': '#ecfdf5'},
    'fizik': {'koyu': '#1e3a8a', 'orta': '#2563eb', 'acik': '#eff6ff'},
    'ingilizce': {'koyu': '#5b21b6', 'orta': '#7c3aed', 'acik': '#f5f3ff'},
    'kimya': {'koyu': '#0f766e', 'orta': '#0d9488', 'acik': '#f0fdfa'},
    'kuran-i-kerim': {'koyu': '#065f46', 'orta': '#059669', 'acik': '#f0fdf4'},
    'matematik': {'koyu': '#1e3a8a', 'orta': '#2563eb', 'acik': '#eff6ff'},
    'peygamberimizin-hayati': {'koyu': '#065f46', 'orta': '#059669', 'acik': '#f0fdf4'},
    'tarih': {'koyu': '#92400e', 'orta': '#d97706', 'acik': '#fffbeb'},
    'tc-inkilap-tarihi-ve-ataturkculuk': {'koyu': '#991b1b', 'orta': '#dc2626', 'acik': '#fef2f2'},
    'turk-dili-ve-edebiyati': {'koyu': '#1e3a8a', 'orta': '#2563eb', 'acik': '#eff6ff'},
}


def renkler(ders):
    return DERS_RENKLERI.get(ders, {'koyu': '#1e3a8a', 'orta': '#2563eb', 'acik': '#eff6ff'})


class Primitifler:
    def baslik(self, x, y, yazi, renk='#1e293b'):
        return (
            f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="14.5" '
            f'font-weight="bold" fill="{renk}" text-anchor="middle">{html.escape(str(yazi))}</text>'
        )

    def kutu(self, x, y, w, h, dolgu='#f8fafc', cizgi='#94a3b8', rx=8):
        return (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{dolgu}" stroke="{cizgi}" stroke-width="1.6"/>'
        )

    def metin(self, x, y, yazi, renk='#1e293b', boy=12, kalinlik='normal', hiza='start'):
        return (
            f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{boy}" '
            f'font-weight="{kalinlik}" fill="{renk}" text-anchor="{hiza}">{html.escape(str(yazi))}</text>'
        )

    def sar(self, ic, w=800, h=424):
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="Konu özet şeması">{"".join(ic)}</svg>'
        )


def kaydet(ad, svg_icerik):
    SON_SVG[ad] = svg_icerik
    SON_SVG['_son'] = svg_icerik
    return svg_icerik
