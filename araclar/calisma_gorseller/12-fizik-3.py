"""12. sınıf Fizik 3. hafta (Dönerek Öteleme ve Eylemsizlik Momenti) çalışma kâğıdı görselleri."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'

YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, on_metin, ic_metin, son_metin='', renk=LAC, boy=9.2, ince=False):
    ic_str = str(ic_metin)
    on_str = str(on_metin) if on_metin else ''
    son_str = str(son_metin) if son_metin else ''
    w_ic = max(12, len(ic_str) * (boy * 0.62) + 4)
    w_on = len(on_str) * (boy * 0.56) + (2 if on_str else 0)
    w_son = len(son_str) * (boy * 0.56) + (2 if son_str else 0)
    toplam_w = w_on + 10 + w_ic + w_son
    sol = cx - toplam_w / 2
    out = ''
    if on_str:
        out += yazi(sol + w_on - 1, y, on_str, boy, renk, 'end', ince=ince)
    rx = sol + w_on
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.5
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.5:.1f} {orta_y - 1.5:.1f} '
            f'L{rx + 5.5:.1f} {alt_y:.1f} L{rx + 9.5:.1f} {ust_y:.1f} '
            f'H{rx + 10 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.2" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 10 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    if son_str:
        out += yazi(rx + 10 + w_ic + 1, y, son_str, boy, renk, 'start', ince=ince)
    return out

def dort_donme_kavrami_karti():
    kartlar = [
        ('1. Eylemsizlik', 'Dönme Direnci · I = k·m·r²', MAVI, MAVI_A),
        ('2. Öteleme Hızı', 'Kütle Merkezi · v = ω·r', YES, YES_A),
        ('3. Dönme Enerjisi', 'Açısal Kinetik · ½Iω²', TUR, TUR_A),
        ('4. Yuvarlanma', 'Dönme + Öteleme Hareketi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:
            ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört dönme dinamiği kavramı kartı.", 34)

def yuvarlanan_tekerlek_hiz_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "YUVARLANAN TEKERLEKTE ANLIK HIZ DAĞILIMI", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, KIR_A, KIR)
    ic += yazi(95, 54, "En Üst Nokta: 2v", 10.0, KIR)
    ic += yazi(95, 74, "v_öteleme + v_dönme = 2v", 9.0, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, "Temas Noktası: 0", 10.0, YES)
    ic += yazi(265, 74, "v_öteleme - v_dönme = 0", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Yuvarlanan tekerlek anlık hız modeli.", 34)

def donme_enerjisi_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "DÖNME KİNETİK ENERJİSİ VE MOMENT HESABI", 10.5, TUR)
    ic += yazi(90, 56, "Eylemsizlik Momenti: I = 2 kg·m²", 9.6, LAC)
    ic += yazi(90, 76, "Açısal Hız: ω = 4 rad/s", 9.6, MAVI)
    ic += yazi(270, 56, "E_dönme = ½ · I · ω²", 10.0, YES)
    ic += yazi(270, 76, "E_dönme = ½ · 2 · 16 = 16 J", 9.6, YES)
    return svg(360, 110, ic, "Dönme kinetik enerjisi hesap panosu.", 34)

def yuvarlanma_dinamik_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "KAYMADAN YUVARLANMA ŞARTLARI", 10.6, MOR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Kütle Merkezi", 10.0, MAVI)
    ic += yazi(92, 74, "Doğrusal Hız: v = ω·r", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Toplam Enerji", 10.0, YES)
    ic += yazi(267, 74, "E_top = ½mv² + ½Iω²", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Kaymadan yuvarlanma dinamik şeması.", 34)

def egik_duzlem_yaris_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "EĞİK DÜZLEMDE YUVARLANMA YARIŞI (SÜRE SIRASI)", 10.5, YES)
    adimlar = ["1. Dolu Küre", "2. Dolu Silindir", "3. İçi Boş Halka"]
    for i, a in enumerate(adimlar):
        x = 24 + i * 110
        ic += kutu(x, 42, 100, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 50, 70, a, 9.4, LAC)
        if i < 2:
            ic += yazi(x + 105, 70, "&lt;", 12.0, TUR)
    return svg(360, 110, ic, "Eğik düzlem yarış sıralaması şeması.", 34)

def silindir_enerji_orani_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "DOLU SİLİNDİR ENERJİ PAYLAŞIM ORANI", 10.6, MAVI)
    ic += yazi(180, 52, "E_öt = ½mv²   ve   E_dön = ½(½mr²)ω² = ¼mv²", 10.0, LAC)
    ic += yazi(180, 76, "E_dönme / E_öteleme = (¼mv²) / (½mv²) = 1/2", 9.5, MAVI)
    return svg(360, 110, ic, "Silindir enerji paylaşım oranı panosu.", 34)

def dort_nokta_hiz_karti():
    kartlar = [
        ('1. Tepe Noktası', 'v_yer = 2v', KIR, KIR_A),
        ('2. Merkez (O)', 'v_yer = v', MAVI, MAVI_A),
        ('3. Taban Noktası', 'v_yer = 0 (Sıfır)', YES, YES_A),
        ('4. Yan Kenar', None, MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if alt is None:
            ic += kok_ciz(x + 41, 70, 'v_yer = ', '2', ' v', LAC, 9.2, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)
    return svg(360, 110, ic, "Dört nokta anlık hız kartı.", 34)

def sifre_donme_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "DÖNME DİNAMİĞİ KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "DİSK · ÖTELEME · NEWTON · MOMENT · ENERJİ", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli kinematik hareketi (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre dönme hareket panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_donme_kavrami_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = yuvarlanan_tekerlek_hiz_modeli()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = donme_enerjisi_hesap_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = yuvarlanma_dinamik_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = egik_duzlem_yaris_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = silindir_enerji_orani_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_nokta_hiz_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_donme_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True