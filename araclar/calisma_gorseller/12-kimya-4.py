"""12. sınıf Kimya 4. hafta (Daniell Pili ve Pil Şeması) çalışma kâğıdı görselleri."""

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

def dort_daniell_terimi_karti():
    kartlar = [
        ('1. Anot (Zn)', 'Zn → Zn²⁺ + 2e⁻', KIR, KIR_A),
        ('2. Katot (Cu)', 'Cu²⁺ + 2e⁻ → Cu', YES, YES_A),
        ('3. Köprü (||)', 'Yük Denkliği', MAVI, MAVI_A),
        ('4. Faz Sınırı (|)', 'Katı / Çözelti', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört Daniell pili terimi kartı.", 34)

def pil_semasi_gosterim_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "STANDART PİL ŞEMASI KISA GÖSTERİMİ", 10.5, CAM)
    ic += yazi(180, 52, "Zn(k) | Zn²⁺(1 M)  ||  Cu²⁺(1 M) | Cu(k)", 10.2, LAC)
    ic += yazi(180, 76, "Anot Yarı Hücresi (Sol)  ||  Katot Yarı Hücresi (Sağ)", 9.2, CAM, ince=True)
    return svg(360, 110, ic, "Pil şeması gösterim panosu.", 34)

def elektrot_kutle_degisim_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "ELEKTROT KÜTLE DEĞİŞİMLERİ", 10.5, TUR)
    ic += yazi(90, 56, "Zn Anot Kütlesi: Azalır", 9.8, KIR)
    ic += yazi(90, 76, "Çinko metali aşınır", 9.0, LAC, ince=True)
    ic += yazi(270, 56, "Cu Katot Kütlesi: Artar", 9.8, YES)
    ic += yazi(270, 76, "Bakır metali toplanır", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Elektrot kütle değişim panosu.", 34)

def daniell_calisma_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "DANIELL PİLİ TEPKİME DENGESİ", 10.5, MOR)
    ic += yazi(180, 52, "Zn(k) + Cu²⁺(suda) ⇄ Zn²⁺(suda) + Cu(k) + Isı", 10.0, LAC)
    ic += yazi(180, 76, "Ekzotermiktir; soğutulduğunda pil potansiyeli artar", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Daniell pili çalışma şeması.", 34)

def sema_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "PİL ŞEMASI YAZIM KURALLARI SIRASI", 10.5, YES)
    adimlar = ["1. Zn(k)", "2. Zn²⁺(suda)", "3. Cu²⁺(suda)", "4. Cu(k)"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 40, 70, a, 9.0, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Pil şeması yazım sırası şeması.", 34)

def daniell_gerilim_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "DANIELL PİLİ STANDART GERİLİM HESABI", 10.5, MAVI)
    ic += yazi(180, 52, "E°_pil = E°(Cu²⁺/Cu) - E°(Zn²⁺/Zn)", 10.0, LAC)
    ic += yazi(180, 76, "= 0,34 - (-0,76) = +1,10 V", 10.2, YES)
    return svg(360, 110, ic, "Daniell gerilim hesap panosu.", 34)

def dort_mudahale_karti():
    kartlar = [
        ('1. Anota Su Ekle', 'E_pil Artar', YES, YES_A),
        ('2. Katota Su Ekle', 'E_pil Azalır', KIR, KIR_A),
        ('3. Sıcaklık Artışı', 'E_pil Düşer', TUR, TUR_A),
        ('4. Denge Hâli', 'E_pil = 0 V', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört kimyasal müdahale kartı.", 34)

def sifre_volta_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "ELEKTROKİMYA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "VOLTMETRE · OKSİTLENME · LİTYUM · TUZ · ANOT", 9.4, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli pil mucidi bilginin soyadını (5 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre Volta kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_daniell_terimi_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = pil_semasi_gosterim_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = elektrot_kutle_degisim_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = daniell_calisma_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = sema_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = daniell_gerilim_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_mudahale_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_volta_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True