"""7. sınıf Türkçe 6. hafta (Motivasyon, Zaman Yönetimi, Metin Karşılaştırma ve Özetleme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def iki_metin_karsilastirma():
    """Soru 1: Adını Göklere Yazdıran Çocuk ve Bayrağımızın Altında karşılaştırması."""
    ic = kutu(4, 4, 172, 90, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, '1. Metin: Göklere Yazdıran', MAVI)
    ic += yazi(90, 44, 'Tür: Biyografik Hikâye', LAC, 'middle', True)
    ic += yazi(90, 63, 'Değer: Azim ve kararlılık', LAC, 'middle', True)
    ic += yazi(90, 81, 'Tema: Başarı ve vatan sevgisi', MAVI)

    ic += kutu(184, 4, 172, 90, KIR_A, KIR, 8, 1.4)
    ic += yazi(270, 22, '2. Metin: Bayrağımızın Altında', KIR)
    ic += yazi(270, 44, 'Tür: Destansı Şiir / Anlatı', LAC, 'middle', True)
    ic += yazi(270, 63, 'Değer: Bağımsızlık ve fedakârlık', LAC, 'middle', True)
    ic += yazi(270, 81, 'Tema: Bayrak ve vatan sevgisi', KIR)
    return svg(360, 98, ic, 'İki farklı metnin tür ve tema bakımından metinler arası karşılaştırması.', 12)


def cumle_ve_fiil_fisleri():
    """Soru 2: Motivasyon, zaman yönetimi ve fiil anlam özellikleri fişleri."""
    fisler = [
        ('1. Fiş · Planlama', '«...önem sırasına göre planladı.»', MAVI, MAVI_A),
        ('2. Fiş · Merak', '«...merakla gökyüzünü inceledi.»', YES, YES_A),
        ('3. Fiş · Dinlenme', '«...uçuşun ardından dinlendi.»', TUR, TUR_A),
        ('4. Fiş · Değişim', '«...bahçedeki yapraklar sarardı.»', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Dört cümle fişi ve çekimli fiil örnekleri.', 12)


def ozetleme_kontrol_listesi():
    """Soru 4: Özetleme kuralları kontrol listesi."""
    ic = kutu(4, 4, 352, 90, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Hikâye Özetleme Kontrol Panosu', KAHVE)
    maddeler = [
        ('1. Kronolojik Sıra', 'Olay sırası korundu', YES, YES_A, 10, 28),
        ('2. Ayıklama', 'Betimlemeler çıkarıldı', MAVI, MAVI_A, 184, 28),
        ('3. Öznel Yorum (!)', '«Bence çok yanlıştı»', KIR, KIR_A, 10, 60),
        ('4. Özgün İfade', 'Kendi cümleleriyle yazıldı', MOR, MOR_A, 184, 60),
    ]
    for bas, alt, r, z, x, y in maddeler:
        ic += kutu(x, y, 166, 28, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 18, f'{bas}: {alt}', LAC, 'middle', True)
    return svg(360, 98, ic, 'Özetleme yaparken doğru ve yanlış uygulamalar panosu.', 12)


def metin_ici_degisim_karti():
    """Soru 5: Metin içi karşılaştırma (önceki ve sonraki durum) kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Metin İçi Karşılaştırma: Önceki ve Sonraki Durum', MAVI)
    ic += kutu(14, 28, 158, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(93, 46, 'İlk Tasarım (Önce)', TUR)
    ic += yazi(93, 66, 'Kanat kırıldı · Deneyim kazandı', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Yeni Tasarım (Sonra)', YESIL_K)
    ic += yazi(267, 66, '«Eskisinden DAHA sağlam planör»', LAC, 'middle', True)
    return svg(360, 94, ic, 'Mühendisin ilk ve yeni planör tasarımının metin içi karşılaştırması.', 12)


def hikaye_unsurlari_haritasi():
    """Soru 7: Bayrağımızın Altında hikâye haritası."""
    ic = kutu(4, 4, 352, 92, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, 'Hikâye Çözümleme Haritası · «Bayrağımızın Altında»', KIR)
    ic += kutu(12, 28, 162, 60, '#fff', KIR, 6, 1.2)
    ic += yazi(93, 45, 'Anlatım Cümlesi:', KIR)
    ic += yazi(93, 64, '«Elimdeki al bayrağı tepeye', LAC, 'middle', True)
    ic += yazi(93, 80, 'diktikçe gururla yürüdüm.»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 60, '#fff', MAVI, 6, 1.2)
    ic += yazi(267, 45, 'Yapı Unsurları:', MAVI)
    ic += yazi(267, 64, 'Kişi: Ben (1. Kişi) · Yer: Tepe', LAC, 'middle', True)
    ic += yazi(267, 80, 'Duygu: Bağımsızlık ve bayrak', LAC, 'middle', True)
    return svg(360, 100, ic, 'Birinci kişi ağzıyla anlatılan bayrak temalı hikâye çözümleme kartı.', 12)


def ozetleme_adimlari_sema():
    """Soru 8: 4 adımlı metin çözümleme ve özetleme kılavuzu."""
    adimlar = [
        ('1. Çözümle', 'Ana olayı bul', MAVI, MAVI_A, 6),
        ('2. Ayıkla', 'Ayrıntıyı çıkar', TUR, TUR_A, 94),
        ('3. Sırala', 'Oluş sırasını koru', MOR, MOR_A, 182),
        ('4. Özetle', 'Kendi cümlenle yaz', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Metin çözümleme ve özetleme dört aşamalı akış şeması.', 12)


def dusunceyi_gelistirme_kartlari():
    """Soru 9: Düşünceyi geliştirme yolları 4 kart."""
    kartlar = [
        ('1. Kart · Tanım + Kıyas', '«...EN verimli kullanma sanatıdır.»', YES, YES_A),
        ('2. Kart · Örnekleme', '«Vecihi Hürkuş, Sabiha Gökçen...»', MAVI, MAVI_A),
        ('3. Kart · Tanık Gösterme', '«Atatürk’ün ‘İstikbal...’ sözü»', MOR, MOR_A),
        ('4. Kart · Doğrudan Anlatım', '«Motor testlerine sabah başlandı.»', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Düşünceyi geliştirme yolları dört cümle kartı.', 12)


def zaman_yonetimi_plan_karti():
    """Soru 12: Zaman yönetimi ve öncelik matrisi kartı."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Elif’in Haftalık Zaman Yönetimi ve Hedef Çizelgesi', YESIL_K)
    kutular = [
        ('1. Öncelik Sırası', 'Önemli işler ilk sırada', MAVI, '#fff', 10),
        ('2. Planlı Çalışma', 'Erteleme alışkanlığı yok', TUR, '#fff', 126),
        ('3. Kazanım', 'Yüksek içsel motivasyon', YESIL_K, '#fff', 242),
    ]
    for bas, alt, r, z, x in kutular:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Öncelik sıralaması ve zaman yönetiminin motivasyona etkisi kartı.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = iki_metin_karsilastirma()
    s[1]['gorsel'] = cumle_ve_fiil_fisleri()
    s[3]['gorsel'] = ozetleme_kontrol_listesi()
    s[4]['gorsel'] = metin_ici_degisim_karti()
    s[6]['gorsel'] = hikaye_unsurlari_haritasi()
    s[7]['gorsel'] = ozetleme_adimlari_sema()
    s[8]['gorsel'] = dusunceyi_gelistirme_kartlari()
    s[11]['gorsel'] = zaman_yonetimi_plan_karti()
