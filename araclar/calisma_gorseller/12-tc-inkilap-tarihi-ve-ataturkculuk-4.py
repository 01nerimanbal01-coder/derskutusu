"""12. sınıf İnkılap Tarihi 4. hafta (Osmanlı Savunma Cepheleri) çalışma kâğıdı görselleri."""

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

def dort_savunma_cephesi_karti():
    kartlar = [
        ('1. Çanakkale', '18 Mart Zaferi · Boğaz', KIR, KIR_A),
        ('2. Irak Cephesi', 'Kutül Amare Zaferi', YES, YES_A),
        ('3. Hicaz-Yemen', 'Fahreddin Paşa · Medine', TUR, TUR_A),
        ('4. Suriye Cephesi', 'Mustafa Kemal · Katma', MAVI, MAVI_A),
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
    return svg(360, 110, ic, "Dört savunma cephesi kartı.", 34)

def kutulamare_zafer_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "29 NİSAN 1916 KUTÜ’L-AMARE BÜYÜK ZAFERİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "General Townshend Esir", 9.8, YES)
    ic += yazi(95, 74, "13.000 İngiliz askeri teslim alındı", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, "Halil Paşa Komutası", 9.8, TUR)
    ic += yazi(265, 74, "İngiliz sömürge prestiji yıkıldı", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Kutü’l-Amare zafer panosu.", 34)

def fahreddin_pasa_medine_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "ÇÖL KAPLANI FAHREDDİN PAŞA VE MEDİNE", 10.5, YES)
    ic += yazi(180, 52, "Peygamber kabrini 2 yıl 7 ay boyunca açlık ve kuşatmaya karşı savundu", 9.6, LAC)
    ic += yazi(180, 76, "Mukaddes emanetleri yağmadan kurtararak Topkapı Sarayı’na ulaştırdı", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Fahreddin Paşa Medine panosu.", 34)

def savunma_ve_yardim_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "OSMANLI SAVUNMA VE YARDIM CEPHELERİ AYRIMI", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, KIR_A, KIR)
    ic += yazi(92, 56, "Savunma Cepheleri", 10.0, KIR)
    ic += yazi(92, 74, "Kendi vatan topraklarımız", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Yardım Cepheleri", 10.0, YES)
    ic += yazi(267, 74, "Galiçya, Romanya, Makedonya", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Savunma ve yardım cepheleri şeması.", 34)

def savunma_kronoloji_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "SAVUNMA CEPHESİ GELİŞMELERİ KRONOLOJİSİ", 10.5, MAVI)
    adimlar = ["1915 Çanakkale", "1916 Kutü’l-Amare", "1916 Medine", "1918 Katma"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Savunma cephesi kronolojisi.", 34)

def suriye_katma_hatti_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "MUSTAFA KEMAL VE SURİYE KATMA SAVUNMA HATTI", 10.5, TUR)
    ic += yazi(180, 52, "Halep kuzeyinde kurulan çelik savunma hattı (Ekim 1918)", 10.0, LAC)
    ic += yazi(180, 76, "Düşmanın Anadolu’ya girmesini engelledi ve Millî Mücadele sınırını çizdi", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Suriye Katma hattı panosu.", 34)

def dort_savunma_komutani_karti():
    kartlar = [
        ('1. Halil Paşa', 'Kutül Amare', YES, YES_A),
        ('2. Fahreddin P.', 'Medine Müdafaası', TUR, TUR_A),
        ('3. M. Kemal', 'Katma Hattı', KIR, KIR_A),
        ('4. Cevat Paşa', '18 Mart Boğaz', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört savunma komutanı kartı.", 34)

def sifre_siper_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "SAVUNMA SAVAŞLARI KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "SİPER · İNGİLTERE · PAŞA · ERZURUM · RUSYA", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli savunma mevzisini (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre siper kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_savunma_cephesi_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = kutulamare_zafer_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = fahreddin_pasa_medine_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = savunma_ve_yardim_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = savunma_kronoloji_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = suriye_katma_hatti_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_savunma_komutani_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_siper_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True