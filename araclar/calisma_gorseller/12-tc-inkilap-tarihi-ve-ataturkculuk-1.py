"""12. sınıf İnkılap Tarihi 1. hafta (Mustafa Kemal'in Yetiştiği Ortam) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

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


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_sehir_karti():
    sehirler = [
        ('1. Selanik', 'Liman &amp; Çok Kültürlü', MAVI, MAVI_A),
        ('2. Manastır', 'Askerî İdadi &amp; Tarih', YES, YES_A),
        ('3. İstanbul', 'Harp Okulu &amp; Başkent', TUR, TUR_A),
        ('4. Şam', '5. Ordu &amp; İlk Görev', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(sehirler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Mustafa Kemal fikir hayatını şekillendiren dört şehir kartı.', 34)


def selanik_harita_kroki():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'SELANİK LİMANI VE DEMİR YOLU BAĞLANTILARI', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(95, 54, 'Ege Limanı Ticareti', 10.0, MAVI)
    ic += yazi(95, 74, 'Batı basını ve gazete akışı', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, 'Belgrad - Manastır Hattı', 10.0, YES)
    ic += yazi(265, 74, 'Avrupa ile doğrudan ulaşım', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Selanik şehri ve coğrafi konumu krokisi.', 34)


def okul_zaman_seridi():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Şemsi Efendi Mektebi', 10.2, YES)
    ic += yazi(91, 50, 'Modern eğitim yöntemleri', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Yenilikçi pedagojik temel', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Mahalle Mektebi', 10.2, TUR)
    ic += yazi(269, 50, 'Geleneksel eğitim usulü', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'Kısa süreli ilk başlangıç', 9.4, TUR)
    return svg(360, 110, ic, 'Mustafa Kemal ilk eğitim kurumları karşılaştırma kartı.', 34)


def aydinlar_etki_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'FİKİR DÜNYASINI BESLEYEN AYDINLAR', 10.6, MOR)
    ic += kutu(16, 38, 98, 56, MAVI_A, MAVI)
    ic += yazi(65, 56, 'Namık Kemal', 9.8, MAVI)
    ic += yazi(65, 74, 'Vatan şairi', 9.0, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, YES_A, YES)
    ic += yazi(180, 56, 'Tevfik Fikret', 9.8, YES)
    ic += yazi(180, 74, 'İnkılap &amp; akıl', 9.0, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, TUR_A, TUR)
    ic += yazi(295, 56, 'J.J. Rousseau', 9.8, TUR)
    ic += yazi(295, 74, 'Halk iradesi', 9.0, LAC, ince=True)
    return svg(360, 110, ic, 'Fikir dünyasını besleyen düşünürler panosu.', 34)


def egitim_kurumlari_siralamasi():
    okullar = [
        ('1. Şemsi Efendi', 'Selanik İlkokul', YES, YES_A),
        ('2. Askerî Rüştiye', 'Kemal adını aldı', MAVI, MAVI_A),
        ('3. Askerî İdadi', 'Manastır Lise', TUR, TUR_A),
        ('4. Harp Akademisi', 'İstanbul Kurmay', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(okullar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Mustafa Kemal eğitim basamakları sıralaması kartı.', 34)


def kitaplik_dusunur_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'GENÇLİK YILLARI OKUMA KİTAPLIĞI', 10.6, TUR)
    ic += yazi(180, 52, 'Namık Kemal · Tevfik Fikret · Ziya Gökalp · J.J. Rousseau · Montesquieu', 9.8, LAC)
    ic += yazi(180, 76, 'Ortak Vizyon: Millî egemenlik, adalet, vatan sevgisi ve hürriyet.', 9.3, TUR, ince=True)
    return svg(360, 110, ic, 'Mustafa Kemal okuma ve düşünce kitaplığı kartı.', 34)


def dort_sahsiyet_karti():
    sahsiyetler = [
        ('Ömer Naci', 'Hitabet &amp; Edebiyat', MAVI, MAVI_A),
        ('M. Tevfik Bey', 'Tarih Şuuru', YES, YES_A),
        ('Montesquieu', 'Kanun &amp; Kuvvetler', TUR, TUR_A),
        ('M. Emin Yurdakul', 'Millî Şiirler', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(sahsiyetler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört önemli şahsiyet ve etki alanı kartı.', 34)


def sifre_tarih_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'VATAN VE HÜRRİYET FİKRİNİN DOĞUŞU', 10.8, CAM)
    ic += yazi(180, 50, 'VOLTAIRE · AKADEMİ · TEVFİK · ASKER · NAMIK', 9.8, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli tarih terimini (5 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre tarih kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_sehir_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = selanik_harita_kroki()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = okul_zaman_seridi()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = aydinlar_etki_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = egitim_kurumlari_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = kitaplik_dusunur_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_sahsiyet_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_tarih_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
