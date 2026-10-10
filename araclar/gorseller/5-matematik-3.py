"""5. sınıf Matematik, 3. hafta: açı ölçme (tam açı, doğru açı, derece, açıölçerle ölçme).

Görseller yalnız MEB 5. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 39-44).
Renk anlamı: tam açı = mavi, doğru açı = mor, dik açı = yeşil; açıölçer görselinde ölçülen açı = turuncu,
açıölçer gövdesi = mavi. Açılar gerçek ölçülerine uygun, tek ölçekle çizilir.
"""
import math

from ozet_gorsel import svg, ok_isareti


def _nk(cx, cy, r, aci):
    """Merkezi (cx, cy) olan çember üzerinde, saat yönünün tersine ölçülen aci (derece) noktası."""
    t = math.radians(aci)
    return cx + r * math.cos(t), cy - r * math.sin(t)


def _yay(cx, cy, r, a0, a1):
    x0, y0 = _nk(cx, cy, r, a0)
    x1, y1 = _nk(cx, cy, r, a1)
    buyuk = 1 if (a1 - a0) > 180 else 0
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {buyuk} 0 {x1:.1f} {y1:.1f}'


def _dilim(cx, cy, r, a0, a1):
    return f'M{cx} {cy} L' + _yay(cx, cy, r, a0, a1)[1:] + ' Z'


def tam_ve_dogru_aci():
    """Işının bir tam turu (tam açı) ve yarım turu (doğru açı)."""
    ic = '<defs>' + ok_isareti('ok3tm', 'g-mf') + ok_isareti('ok3td', 'g-of') + '</defs>'
    # sol: tam açı (mavi)
    cx, cy = 110, 88
    ic += f'<circle cx="{cx}" cy="{cy}" r="44" class="g-ma"/><circle cx="{cx}" cy="{cy}" r="44" class="g-ms" stroke-width="1.5"/>'
    ic += f'<path d="{_yay(cx, cy, 58, 10, 346)}" class="g-ms" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3tm)"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 84}" y2="{cy}" class="g-ms" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="5" class="g-mf"/>'
    ic += f'<text x="{cx}" y="170" text-anchor="middle" font-size="15" font-weight="800" class="g-mf">Tam açı</text>'
    ic += f'<text x="{cx}" y="187" text-anchor="middle" font-size="12.5" class="g-s">bir tam tur</text>'
    # sağ: doğru açı (mor)
    cx, cy = 330, 88
    ic += f'<path d="{_dilim(cx, cy, 44, 0, 180)}" class="g-oa"/><path d="{_yay(cx, cy, 44, 0, 180)}" class="g-os" stroke-width="1.5"/>'
    ic += f'<path d="{_yay(cx, cy, 58, 10, 170)}" class="g-os" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3td)"/>'
    ic += f'<line x1="{cx - 84}" y1="{cy}" x2="{cx + 84}" y2="{cy}" class="g-os" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="5" class="g-of"/>'
    ic += f'<text x="{cx}" y="170" text-anchor="middle" font-size="15" font-weight="800" class="g-of">Doğru açı</text>'
    ic += f'<text x="{cx}" y="187" text-anchor="middle" font-size="12.5" class="g-s">yarım tur</text>'
    return svg(440, 194, ic, 'Tam açı ve doğru açı: ışının bir tam tur dönmesiyle tam açı, yarım tur dönmesiyle doğru açı oluşur.')


def ozel_olculer():
    """Dik açı 90°, doğru açı 180°, tam açı 360° (gerçek ölçülerle)."""
    ic = '<defs>' + ok_isareti('ok3y', 'g-yf') + ok_isareti('ok3d', 'g-of') + ok_isareti('ok3m', 'g-mf') + '</defs>'
    cy = 116
    # dik açı (yeşil)
    cx = 78
    ic += f'<path d="{_dilim(cx, cy, 36, 0, 90)}" class="g-ya"/><path d="{_yay(cx, cy, 36, 0, 90)}" class="g-ys" stroke-width="1.5"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 64}" y2="{cy}" class="g-ys" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3y)"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 64}" class="g-ys" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3y)"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="4.5" class="g-yf"/>'
    ic += f'<text x="{cx + 40}" y="{cy - 36}" text-anchor="middle" font-size="14" font-weight="800" class="g-yf">90°</text>'
    ic += f'<text x="{cx}" y="170" text-anchor="middle" font-size="14.5" font-weight="800" class="g-yf">Dik açı</text>'
    # doğru açı (mor)
    cx = 225
    ic += f'<path d="{_dilim(cx, cy, 40, 0, 180)}" class="g-oa"/><path d="{_yay(cx, cy, 40, 0, 180)}" class="g-os" stroke-width="1.5"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 64}" y2="{cy}" class="g-os" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3d)"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx - 64}" y2="{cy}" class="g-os" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3d)"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="4.5" class="g-of"/>'
    ic += f'<text x="{cx}" y="{cy - 17}" text-anchor="middle" font-size="14" font-weight="800" class="g-of">180°</text>'
    ic += f'<text x="{cx}" y="170" text-anchor="middle" font-size="14.5" font-weight="800" class="g-of">Doğru açı</text>'
    # tam açı (mavi)
    cx = 372
    ic += f'<circle cx="{cx}" cy="{cy}" r="40" class="g-ma"/><circle cx="{cx}" cy="{cy}" r="40" class="g-ms" stroke-width="1.5"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 66}" y2="{cy}" class="g-ms" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3m)"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="4.5" class="g-mf"/>'
    ic += f'<text x="{cx - 6}" y="{cy - 14}" text-anchor="middle" font-size="14" font-weight="800" class="g-mf">360°</text>'
    ic += f'<text x="{cx}" y="170" text-anchor="middle" font-size="14.5" font-weight="800" class="g-mf">Tam açı</text>'
    return svg(450, 182, ic, 'Dik açının ölçüsü 90 derece, doğru açının ölçüsü 180 derece, tam açının ölçüsü 360 derecedir.')


def aciolcer_45():
    """Açıölçerle ölçme: köşe merkezde, bir kol 0° çizgisinde, öbür kol 45°'yi gösterir."""
    cx, cy, R = 170, 170, 140
    ic = '<defs>' + ok_isareti('ok3a', 'g-tf') + '</defs>'
    ic += f'<path d="M{cx - R} {cy} A{R} {R} 0 0 1 {cx + R} {cy} Z" class="g-ma"/>'
    ic += f'<path d="M{cx - R} {cy} A{R} {R} 0 0 1 {cx + R} {cy} Z" class="g-ms" stroke-width="2"/>'
    for a in range(0, 181, 10):
        uzun = a % 30 == 0
        x0, y0 = _nk(cx, cy, R, a)
        x1, y1 = _nk(cx, cy, R - (14 if uzun else 8), a)
        ic += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" class="g-ms" stroke-width="{1.5 if uzun else 1}"/>'
    for a in range(0, 181, 30):
        x, y = _nk(cx, cy, 112, a)
        if a in (0, 180):
            y = cy - 12
        ic += f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="11.5" font-weight="700" class="g-y">{a}°</text>'
    # ölçülen açı (turuncu): [BC 0° çizgisinde, [BA 45°'yi gösterir
    ic += f'<path d="{_dilim(cx, cy, 66, 0, 45)}" class="g-ta"/><path d="{_yay(cx, cy, 66, 0, 45)}" class="g-ts" stroke-width="2"/>'
    xa, ya = _nk(cx, cy, 152, 45)
    ic += f'<line x1="{cx}" y1="{cy}" x2="{xa:.1f}" y2="{ya:.1f}" class="g-ts" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3a)"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 152}" y2="{cy}" class="g-ts" stroke-width="3" stroke-linecap="round" marker-end="url(#ok3a)"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="5" class="g-tf"/>'
    xl, yl = _nk(cx, cy, 90, 22.5)
    ic += f'<text x="{xl:.1f}" y="{yl + 5:.1f}" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">45°</text>'
    ic += f'<text x="{xa + 8:.1f}" y="{ya - 2:.1f}" font-size="16" font-weight="800" class="g-y">A</text>'
    ic += f'<text x="{cx + 156}" y="{cy + 22}" text-anchor="middle" font-size="16" font-weight="800" class="g-y">C</text>'
    ic += f'<text x="{cx}" y="{cy + 22}" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">B (merkez)</text>'
    ic += f'<text x="{cx}" y="{cy + 46}" text-anchor="middle" font-size="15" font-weight="800" class="g-y">m(ABC) = 45°</text>'
    return svg(340, 224, ic, 'Açıölçerle ölçme: ABC açısının köşesi B açıölçerin merkezindedir, BC kolu 0 derece çizgisinin üzerindedir, BA kolu 45 dereceyi gösterir; m(ABC) = 45 derece.')


def uygula(o):
    g = {'Tam açı, doğru açı': tam_ve_dogru_aci(),
         'Derece ve özel açı ölçüleri': ozel_olculer(),
         'Açıölçerle açı ölçme': aciolcer_45()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
