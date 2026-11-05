"""11. sınıf Matematik 4. hafta (İki Nicel Değişkenli Verileri İnceleme) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def veri_yanilgi_kartlari():
    kartlar = [
        ("1. Nedensellik", "Korelasyon ≠ Sebep", KIR, KIR_A),
        ("2. Örneklem Yanlılığı", "Temsil Edilmeyen Grup", TUR, TUR_A),
        ("3. Ekstrapolasyon", "Aralık Dışı Kör Tahmin", MAVI, MAVI_A),
        ("4. Aykırı Veri", "Saptıran Uç Noktalar", MOR, MOR_A),
    ]
    ic = ""
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, "#ffffff")
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, "İstatistiksel yanılgı türleri kartı.", 34)


def nedensellik_yanilgisi_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "KORELASYON VE NEDENSELLİK YANILGISI ŞEMASI", 9.8, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(92, 56, "Hatalı Çıkarım", 9.2, KIR)
    ic += yazi(92, 76, "Kahve içmek zengin yapar!", 8.2, LAC, ince=True)
    ic += yazi(92, 92, "Doğrudan sebep-sonuç sanısı", 8.2, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Gizli Üçüncü Değişken", 9.2, YESIL_K)
    ic += yazi(267, 76, "Eğitim ve Çalışma Alanı", 8.2, LAC, ince=True)
    ic += yazi(267, 92, "Her ikisini de artıran faktör", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Nedensellik yanılgısı karşılaştırması.", 34)


def ekstrapolasyon_tehlikesi_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "EKSTRAPOLASYON: ARALIK DIŞINA ÇIKMA HATASI", 9.8, MAVI)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "İnterpolasyon (0-10 Yaş)", 9.0, YESIL_K)
    ic += yazi(92, 76, "Gözlem aralığı içinde", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Güvenilir &amp; Geçerli Model", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(267, 56, "Ekstrapolasyon (50 Yaş)", 9.0, KIR)
    ic += yazi(267, 76, "Tahmin: Boy = 375 cm!", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Biyolojik Gerçekle Çelişir", 8.2, KIR, ince=True)
    return svg(360, 125, ic, "İnterpolasyon ve ekstrapolasyon kesiti.", 34)


def orneklem_taraflilik_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "ÖRNEKLEM YANLILIĞI VE TEMSİLİYET SORUNU", 10.0, YESIL_K)
    adımlar = [
        ("1. Hedef Evren", "Bütün ülke halkı", 16),
        ("2. Hatalı Seçim", "Sadece yazılımcılar", 102),
        ("3. Yanlı Sonuç", "Aşırı yüksek oran", 188),
        ("4. Genelleme", "Bilimsel hata doğar", 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Örneklem yanlılığı basamakları şeması.", 34)


def istatistik_denetim_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "VERİ VE MODEL DENETİMİ KONTROL LİSTESİ TABLOSU", 9.8, MOR)
    satirlar = [
        ("Kontrol Ölçütü", "Sorulacak Kritik Soru", "Doğrulama Amacı", MOR),
        ("Örneklem Temsili", "Veri kimlerden toplandı?", "Yanlılığı Tespit Etme", MAVI),
        ("Korelasyon Bağı", "Üçüncü bir etken var mı?", "Nedensellik Tuzağı", YESIL_K),
        ("Model Sınırı", "Tahmin aralık içinde mi?", "Ekstrapolasyonu Önleme", TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, "İstatistik denetim kontrol tablosu.", 34)


def aykiri_veri_saptirma_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "AYKIRI (UÇ) DEĞERİN MODELİ SAPTIRMA ETKİSİ", 10.0, CAM)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "Aykırı Değersiz Model", 9.0, YESIL_K)
    ic += yazi(92, 76, "r = +0,90 Güçlü İlişki", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Gerçekçi Doğrusal Eğilim", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(267, 56, "Tek Aykırı Değer Eklenince", 8.8, KIR)
    ic += yazi(267, 76, "r = +0,35 Yapay Düşüş", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Modeli Ciddi Yanıltır", 8.2, KIR, ince=True)
    return svg(360, 125, ic, "Aykırı değer sapma diyagramı.", 34)


def veri_okuma_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "ELEŞTİREL VERİ OKURYAZARLIĞI BASAMAKLARI", 9.8, TUR)
    kartlar = [
        ("1. Kaynak Doğrulama", "Veriyi kim üretti?", 16),
        ("2. Eksen Ölçeği", "Sıfırdan mı başlıyor?", 102),
        ("3. Değişken Bağı", "Mantıklı bir ilişki mi?", 188),
        ("4. Sonuç Analizi", "Abartılı genelleme var mı?", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Veri okuryazarlığı adımları kartı.", 34)


def elestirel_bakis_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "İSTATİSTİKSEL AKIL YÜRÜTME DÖNGÜSÜ", 10.0, YESIL_K)
    kutular = ["Veri İnceleme", "Yanlılık Arama", "Sebep Sorgulama", "Sağlam Sonuç"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"Aşama {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, "İstatistiksel akıl yürütme kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = veri_yanilgi_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = nedensellik_yanilgisi_semasi()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = ekstrapolasyon_tehlikesi_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = orneklem_taraflilik_semasi()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = istatistik_denetim_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = aykiri_veri_saptirma_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = veri_okuma_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = elestirel_bakis_kutulari()
    s[10]["en_fazla"] = 34
