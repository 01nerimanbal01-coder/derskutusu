"""12. sınıf Din Kültürü 3. hafta (İslam Medeniyetinde Bilim ve Düşünce) çalışma kâğıdı görselleri."""

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

def dort_islam_kurumu_karti():
    kartlar = [
        ('1. Suffe', 'Mescid-i Nebi · İlk Yatılı Okul', MAVI, MAVI_A),
        ('2. Beytülhikme', 'Bağdat · Tercüme Merkezi', YES, YES_A),
        ('3. Nizamiye', 'Selçuklu · İlk Üniversite', TUR, TUR_A),
        ('4. Bimaristan', 'Tıp Eğitimi · Şifahane', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört İslam ilim ve eğitim kurumu kartı.", 34)

def beytulhikme_sema_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "BEYTÜLHİKME (BİLGELİK EVİ) BAĞDAT KURUMSAL ŞEMASI", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Tercüme Odaları", 10.0, YES)
    ic += yazi(95, 74, "Grekçe, Süryanice, Farsça metinler", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(265, 54, "Kütüphane &amp; Rasathane", 10.0, MAVI)
    ic += yazi(265, 74, "Özgün araştırma ve tahlil meclisleri", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Beytülhikme kurumsal şeması panosu.", 34)

def suffe_egitim_mekani_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "MESCİD-İ NEBİ VE SUFFE MEKTEBİ (MEDİNE)", 10.6, YES)
    ic += yazi(180, 52, "Hz. Peygamber'in gözetiminde ilk yatılı talebe mektebi", 9.8, LAC)
    ic += yazi(180, 76, "Kur'an öğretimi, hadis rivayeti ve çevre kabilelere muallim yetiştirme", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Suffe mektebi eğitim mekânı panosu.", 34)

def ilim_tarihi_asamalari_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "İSLAM BİLİM TARİHİ TEMEL AŞAMALARI", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "1. Doğuş &amp; Tercüme", 10.0, MAVI)
    ic += yazi(92, 74, "Vahiy temeli ve kaynak aktarımı", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "2. Özgün Keşifler", 10.0, YES)
    ic += yazi(267, 74, "Cebir, optik ve tıp ekolleri", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "İslam bilim tarihi temel aşamaları şeması.", 34)

def egitim_kurumlari_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "İSLAM EĞİTİM KURUMLARI TARİHSEL GELİŞİMİ", 10.5, MAVI)
    adimlar = ["1. Darülerkâm", "2. Suffe", "3. Beytülhikme", "4. Nizamiye"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 38, 70, a, 9.4, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Eğitim kurumları tarihsel gelişim sıralaması.", 34)

def ilimlerin_tasnifi_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "İSLAM ÂLİMLERİNİN İLİMLERİ TASNİFİ (TASNİF-İ ULÛM)", 10.5, MOR)
    ic += yazi(180, 52, "Farabi (İhsâü’l-Ulûm) · Gazali (İhyâ)", 10.0, LAC)
    ic += yazi(180, 76, "Akli İlimler (Matematik, Fizik, Felsefe) + Nakli İlimler (Tefsir, Hadis, Fıkıh)", 9.2, YES, ince=True)
    return svg(360, 110, ic, "İlimlerin tasnifi panosu.", 34)

def dort_alim_tasnif_karti():
    kartlar = [
        ('1. Farabi', 'İhsâül-Ulûm · Felsefe', MAVI, MAVI_A),
        ('2. Gazali', 'Farz-ı Kifaye · Ahlak', YES, YES_A),
        ('3. Hârizmî', 'Cebir &amp; Sıfır Rakamı', TUR, TUR_A),
        ('4. İbn Heysem', 'Optik &amp; Deney Yöntemi', MOR, MOR_A),
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
        elif ' &amp; ' in alt:
            ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört İslam âlimi ve katkıları kartı.", 34)

def sifre_hikmet_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "İSLAM DÜŞÜNCESİ KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "HİKMET · İLİM · KÜTTAB · MEDRESE · ERKÂM · TERCÜME", 9.4, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli bilgelik kavramını (6 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre hikmet kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_islam_kurumu_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = beytulhikme_sema_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = suffe_egitim_mekani_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = ilim_tarihi_asamalari_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = egitim_kurumlari_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = ilimlerin_tasnifi_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_alim_tasnif_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_hikmet_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True