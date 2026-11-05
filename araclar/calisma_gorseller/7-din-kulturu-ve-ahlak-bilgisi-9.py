"""7. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta (Haccın Farzları, Vacipleri, Adım Adım Uygulanışı ve Hac-Umre Farkları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def uc_tavaf_panosu():
    kartlar = [
        ('1. Kudüm Tavafı', 'Mekke’ye ilk gelişte', 'Hükmü: Sünnet', MAVI, MAVI_A),
        ('2. Ziyaret Tavafı', 'Vakfeden sonra bayramda', 'Hükmü: Farz (Rükün)', YES, YES_A),
        ('3. Veda Tavafı', 'Mekke’den ayrılırken', 'Hükmü: Vacip', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 22, bas, 10.2, r)
        ic += yazi(x + 56, 44, s1, 9.5, LAC, ince=True)
        ic += yazi(x + 56, 65, s2, 9.8, r)
    return svg(360, 86, ic, 'Kudüm, Ziyaret ve Veda tavaflarının zaman ve hüküm karşılaştırması.', 15)


def dort_ibadet_mekan_karti():
    kartlar = [
        ('1. Gündüz Vakfesi', 'Arafat · Farz', YES, YES_A),
        ('2. Gece Vakfesi', 'Müzdelife · ?', MAVI, MAVI_A),
        ('3. Şeytan Taşlama', '? · Vacip', TUR, TUR_A),
        ('4. Ziyaret Tavafı', 'Kâbe · ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.4, LAC, ince=True)
    return svg(360, 82, ic, 'Dört hac uygulamasının mekân ve hüküm kartları.', 14)


def cem_namazlari_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Arafat (Arife Günü)', 10.3, YES)
    ic += yazi(91, 44, 'Öğle + İkindi (Öğle vaktinde)', 9.6, LAC, ince=True)
    ic += yazi(91, 65, 'K Kutusu : ?', 10.0, YES)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, '2. Müzdelife (Arife Gecesi)', 10.3, MAVI)
    ic += yazi(269, 44, 'Akşam + Yatsı (Yatsı vaktinde)', 9.6, LAC, ince=True)
    ic += yazi(269, 65, 'L Kutusu : ?', 10.0, MAVI)
    return svg(360, 88, ic, 'Arafat ve Müzdelife’de namazların cem edilmesi şeması.', 15)


def bayram_sabahi_gorevleri():
    kutular = [
        ('1. Görev', 'Akabe Cemresi 7 taş', TUR, TUR_A),
        ('2. Görev', 'Kurban (hedy) kesimi', YES, YES_A),
        ('3. Görev', 'Saç tıraşı (İhramdan çıkış)', MOR, MOR_A),
        ('4. Görev', 'Ziyaret Tavafı ve Sa’y', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r)
        ic += yazi(x + 86, y + 14, bas, 10.0, r)
        ic += yazi(x + 86, y + 29, icerik, 9.5, LAC, ince=True)
    return svg(360, 90, ic, 'Kurban Bayramı sabahı yapılan dört temel hac görevi.', 15)


def seytan_taslama_sembol_karti():
    ic = kutu(6, 6, 348, 74, TUR_A, TUR)
    ic += yazi(180, 24, 'Mina · Remy-i Cimâr (Şeytan Taşlama)', 10.5, TUR)
    ic += yazi(180, 46, 'Küçük, Orta ve Akabe cemrelerine taş atılması', 9.8, LAC, ince=True)
    ic += yazi(180, 66, 'Hatırası: ? Ailesi  ·  Sembolik Anlamı: ?', 9.8, KIR)
    return svg(360, 86, ic, 'Mina’da şeytan taşlama ibadetinin sembolik anlam levhası.', 14)


def umre_rehberi_seridi():
    adimlar = [
        ('1. Mîkat', 'İhram ve Niyet', MAVI, MAVI_A),
        ('2. Kâbe', '7 Şavt Tavaf', YES, YES_A),
        ('3. Safa-Merve', '7 Şavt Sa’y', TUR, TUR_A),
        ('4. Tıraş', 'Halk / Taksir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 52, alt, 9.4, LAC, ince=True)
    return svg(360, 82, ic, 'Umre ibadetinin dört aşamalı uygulanış şeridi.', 14)


def hac_umre_karsilastirma_pano():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += yazi(91, 22, 'HAC İBADETİ', 10.4, MAVI)
    ic += yazi(91, 42, 'Farz · Zilhicce ayında yılda 1 kez', 9.4, LAC, ince=True)
    ic += yazi(91, 60, 'Ortak: İhram, Tavaf, Sa’y, Tıraş', 9.4, LAC, ince=True)
    ic += yazi(91, 76, 'Fark: Vakfe, Taşlama, Kurban VAR', 9.4, MAVI)

    ic += kutu(184, 6, 170, 78, YES_A, YES)
    ic += yazi(269, 22, 'UMRE İBADETİ', 10.4, YES)
    ic += yazi(269, 42, 'Sünnet · Yılın her zamanı', 9.4, LAC, ince=True)
    ic += yazi(269, 60, 'Ortak: İhram, Tavaf, Sa’y, Tıraş', 9.4, LAC, ince=True)
    ic += yazi(269, 76, 'Fark: Vakfe, Taşlama, Kurban YOK', 9.4, KIR)
    return svg(360, 90, ic, 'Hac ve umre ibadetlerinin karşılaştırma panosu.', 15)


def farz_vacip_hukum_karti():
    ic = kutu(6, 6, 170, 74, KIR_A, KIR)
    ic += yazi(91, 22, 'Haccın Farzları (3 Rükün)', 10.2, KIR)
    ic += yazi(91, 43, 'İhram · Arafat Vakfesi · Ziyaret Tavafı', 9.2, LAC, ince=True)
    ic += yazi(91, 64, 'Biri terk edilirse sonuç: ?', 9.6, KIR)

    ic += kutu(184, 6, 170, 74, TUR_A, TUR)
    ic += yazi(269, 22, 'Haccın Vacipleri', 10.2, TUR)
    ic += yazi(269, 43, 'Sa’y · Müzdelife · Taşlama · Veda', 9.2, LAC, ince=True)
    ic += yazi(269, 64, 'Biri terk edilirse sonuç: ?', 9.6, TUR)
    return svg(360, 86, ic, 'Haccın farzları ve vaciplerinin terk edilmesi durumunda hüküm farkı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = uc_tavaf_panosu()
    s[2]['gorsel'] = dort_ibadet_mekan_karti()
    s[5]['gorsel'] = cem_namazlari_karti()
    s[6]['gorsel'] = bayram_sabahi_gorevleri()
    s[7]['gorsel'] = seytan_taslama_sembol_karti()
    s[8]['gorsel'] = umre_rehberi_seridi()
    s[9]['gorsel'] = hac_umre_karsilastirma_pano()
    s[11]['gorsel'] = farz_vacip_hukum_karti()
