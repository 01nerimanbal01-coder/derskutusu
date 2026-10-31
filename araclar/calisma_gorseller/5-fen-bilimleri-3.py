"""5. sınıf Fen Bilimleri 3. hafta (Gökyüzündeki Komşumuz: Güneş — bilgiye ulaşma, Güneş Günlüğü, güvenli gözlem, Güneş lekeleri, görünen boyut, Parker) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = ' style="max-height:16mm"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10.5, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="1.8"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def bilgi_adimlari_sema():
    kutular = [
        ('1. Adım', 'Araç belirle', '(Basılı ve dijital)', MAVI, MAVI_A, False),
        ('2. Adım', 'K : ?', '(Toplama aşaması)', MAVI, '#fff', True),
        ('3. Adım', 'Bilgiyi doğrula', '(Öğretmen ve bilim)', TUR, TUR_A, False),
        ('4. Adım', 'L : ?', '(Sürekli güncelleme)', YES, '#fff', True),
    ]
    ic = ''
    for i, (adim, bas, alt, renk, arka, kesik) in enumerate(kutular):
        x = 8 + i * 148
        ek = ' stroke-dasharray="5 3"' if kesik else ''
        ic += f'<rect x="{x}" y="8" width="134" height="88" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"{ek}/>'
        ic += f'<rect x="{x}" y="8" width="134" height="24" rx="10" fill="{renk}"/><rect x="{x}" y="22" width="134" height="10" fill="{renk}"/>'
        ic += yazi(x + 67, 25, adim, 11.2, '#fff')
        ic += yazi(x + 67, 55, bas, 12 if kesik else 11.5, renk if kesik else LAC)
        ic += yazi(x + 67, 76, alt, 10.5, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="52" x2="{x + 146}" y2="52" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 142} 47 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 104, ic, 'Bilgiye ulaşmanın dört adımı şeması: 1. Araç belirle, 2. K (soru işareti), 3. Bilgiyi doğrula, 4. L (soru işareti).', 22)


def gozlem_guvenlik_panosu():
    kartlar = [
        ('1. Kart: Filtreli Teleskop', 'Özel güneş filtresi takılmış', 'teleskopla gözlem', YES, YES_A),
        ('2. Kart: Beyaz Perdeye Yansıtma', 'Görüntüyü ekrana düşürerek', 'dolaylı inceleme', MAVI, MAVI_A),
        ('3. Kart: Büyüteç ve Filtresiz Dürbün', 'Güneş ışığını doğrudan', 'mercekle göze odaklama', KIR, '#fdeaea'),
        ('4. Kart: Gün Batımına Yakın Saat', 'Işığın etkisinin azaldığı', 'saatleri tercih etme', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 11.2, renk, 'start')
        ic += yazi(x + 18, y + 36, s1 + ' — ' + s2, 10.5, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört Güneş gözlemi uygulama kartı: 1. Filtreli teleskop, 2. Beyaz perdeye yansıtma, 3. Büyüteç ve filtresiz dürbün, 4. Gün batımına yakın saat.', 23)


def kaynak_kartlari_tablo():
    kartlar = [
        ('1. Kart', 'Kütüphane kitabı ve', 'dijital içerik seçimi', MAVI, MAVI_A),
        ('2. Kart', 'Kaynaklardan Güneş', 'bilgilerini ayıklama', MOR, MOR_A),
        ('3. Kart', 'Bilgileri öğretmen ve', 'bilim kaynağıyla sınama', TUR, TUR_A),
        ('4. Kart', 'Doğru notları Güneş', 'Günlüğü’ne kaydetme', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="90" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.5, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.2, LAC, ince=True)
    return svg(600, 106, ic, 'Güneş araştırmasında dört çalışma kartı: 1. kaynak seçimi, 2. bilgi ayıklama, 3. bilimsel doğrulama, 4. günlüğe kaydetme.', 22)


def gunes_leke_gozlemi():
    gozlemler = [
        ('1. Gözlem (09.00)', -20, 'Sol kenara yakın'),
        ('2. Gözlem (3 gün sonra)', 0, 'Ortaya yakın'),
        ('3. Gözlem (6 gün sonra)', 20, 'Sağ kenara yakın'),
    ]
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    for i, (bas, dx, konum) in enumerate(gozlemler):
        x = 18 + i * 192
        cx, cy = x + 90, 62
        ic += yazi(cx, 22, bas, 11, LAC)
        ic += f'<circle cx="{cx}" cy="{cy}" r="30" fill="{TUR_A}" stroke="{TUR}" stroke-width="2"/>'
        # Üç koyu leke: X, Y, Z
        for lx, ly, ad in [(-6 + dx, -8, 'X'), (2 + dx, 2, 'Y'), (-5 + dx, 12, 'Z')]:
            ic += f'<circle cx="{cx + lx}" cy="{cy + ly}" r="3.2" fill="{KAHVE}"/>'
            ic += yazi(cx + lx + 8, cy + ly + 4, ad, 10, LAC)
        ic += yazi(cx, 108, konum, 10.5, TUR)
        if i < 2:
            ic += f'<line x1="{x + 174}" y1="{cy}" x2="{x + 194}" y2="{cy}" stroke="{TUR}" stroke-width="2"/>'
            ic += f'<path d="M{x + 190} {cy - 5} l5 5 l-5 5" fill="none" stroke="{TUR}" stroke-width="1.8"/>'
    return svg(600, 126, ic, 'Üç farklı günde yapılan Güneş gözlemi çizimi: X, Y ve Z koyu bölgeleri soldan sağa birlikte kayar.', 24)


def gunluk_hazirlama_sema():
    ic = f'<rect x="6" y="6" width="588" height="100" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    adimlar = [
        ('Üç A4 Kâğıdı', 'Katla ve kurdele bağla', MAVI, MAVI_A),
        ('İlk Sayfa', 'Tarih ve ön bilgiler', MOR, MOR_A),
        ('Süreç Boyunca', 'Yeni not ve çizim ekle', TUR, TUR_A),
        ('Doğrulama Sonu', 'Eksik tamamla ve düzelt', YES, YES_A),
    ]
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 16 + i * 144
        ic += f'<rect x="{x}" y="18" width="132" height="74" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 66, 44, ust, 11.2, renk)
        ic += yazi(x + 66, 68, alt, 10.5, LAC, ince=True)
    return svg(600, 112, ic, 'Güneş Günlüğü hazırlama ve kullanma aşamaları: üç A4 kâğıdı ve kurdele, ilk sayfa, süreç boyunca ekleme, doğrulama sonu düzeltme.', 22)


def gorunen_boyut_deneyi():
    ic = f'<rect x="6" y="6" width="368" height="108" rx="10" fill="#fbfcff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(190, 23, 'Üstten Görünüm (Aynı Doğrultu)', 11.2, MAVI)
    # X gözlem noktası
    ic += f'<line x1="28" y1="58" x2="40" y2="70" stroke="{KIR}" stroke-width="2.4"/><line x1="40" y1="58" x2="28" y2="70" stroke="{KIR}" stroke-width="2.4"/>'
    ic += yazi(34, 50, 'X', 12, KIR)
    ic += yazi(34, 88, 'Gözlem', 10.2, LAC, ince=True)
    ic += f'<line x1="46" y1="64" x2="108" y2="64" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="4 3"/>'
    ic += yazi(77, 56, '1 adım', 10, LAC, ince=True)
    ic += f'<circle cx="122" cy="64" r="9" fill="{MAVI}"/>'
    ic += yazi(122, 92, 'Küçük top', 10.5, MAVI)
    ic += f'<line x1="136" y1="64" x2="288" y2="64" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="4 3"/>'
    ic += yazi(212, 56, 'Çok uzak mesafe', 10, LAC, ince=True)
    ic += f'<circle cx="318" cy="64" r="22" fill="{TUR}"/>'
    ic += yazi(318, 102, 'Büyük top', 10.5, TUR)

    # Sağ kutu: Gözlemcinin gördüğü
    ic += f'<rect x="386" y="6" width="208" height="108" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(490, 23, 'X Noktasından Görünüm', 11.2, TUR)
    ic += f'<circle cx="446" cy="64" r="20" fill="{MAVI}"/>'
    ic += yazi(446, 100, 'Küçük top', 10.5, MAVI)
    ic += f'<circle cx="534" cy="64" r="11" fill="{TUR}"/>'
    ic += yazi(534, 100, 'Büyük top', 10.5, TUR)
    return svg(600, 120, ic, 'Görünen boyut etkinliği: X gözlem noktasında 1 adım uzaktaki küçük top, en uzaktaki büyük toptan daha büyük görünür.', 23)


def parker_uzay_karti():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    # Sol: Güneş ve Parker çizimi
    ic += f'<circle cx="64" cy="58" r="34" fill="{TUR}" stroke="{ALTIN}" stroke-width="2"/>'
    ic += yazi(64, 62, 'Güneş', 11.5, '#fff')
    ic += f'<path d="M110 26 Q160 58 110 90" fill="none" stroke="{MAVI}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += f'<rect x="132" y="48" width="28" height="20" rx="3" fill="{LAC}"/><line x1="124" y1="44" x2="124" y2="72" stroke="{ALTIN}" stroke-width="4"/>'
    ic += yazi(164, 98, 'Parker Aracı', 10.5, MAVI)
    # Sağ: Bilgi maddeleri
    ic += f'<rect x="216" y="16" width="364" height="84" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(232, 36, 'Görev Kartı: Parker Uzay Aracı', 11.5, MAVI, 'start')
    ic += yazi(232, 55, '- Fırlatılış yılı: 2018 (Özel Güneş araştırma görevi)', 10.8, LAC, 'start', ince=True)
    ic += yazi(232, 72, '- Özelliği: Güneş’e en fazla yaklaşan insan yapımı cisim', 10.8, LAC, 'start', ince=True)
    ic += yazi(232, 89, '- Amacı: Güneş’in yapısı ve dönmesi hakkında veri toplamak', 10.8, LAC, 'start', ince=True)
    return svg(600, 116, ic, 'Parker uzay aracı görev kartı: 2018’de fırlatılan ve Güneş’e en fazla yaklaşarak veri toplayan araştırma aracı.', 23)


def galileo_karsilastirma():
    ic = f'<rect x="8" y="8" width="268" height="96" rx="10" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.6"/>'
    ic += yazi(142, 26, '1. Durum: Tek Gözlem Çizimi', 11.5, LAC)
    ic += f'<circle cx="72" cy="64" r="24" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += f'<circle cx="64" cy="58" r="3" fill="{KAHVE}"/><circle cx="70" cy="68" r="3" fill="{KAHVE}"/>'
    ic += yazi(176, 58, 'Yalnızca lekelerin', 10.8, LAC, ince=True)
    ic += yazi(176, 74, 'o anki yerini gösterir.', 10.8, LAC, ince=True)

    ic += f'<rect x="296" y="8" width="296" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(444, 26, '2. Durum: Aralıklı Üç Gözlem Çizimi', 11.5, YESIL_K)
    for k, dx in enumerate([-8, 0, 8]):
        cx = 342 + k * 56
        ic += f'<circle cx="{cx}" cy="64" r="20" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
        ic += f'<circle cx="{cx + dx}" cy="60" r="2.8" fill="{KAHVE}"/><circle cx="{cx + dx + 3}" cy="68" r="2.8" fill="{KAHVE}"/>'
    ic += yazi(534, 58, 'Kayma yönünü', 10.5, YESIL_K)
    ic += yazi(534, 74, 've dönüşü kanıtlar.', 10.5, YESIL_K)
    return svg(600, 112, ic, '1. durumda tek gözlem çizimi, 2. durumda belirli zaman aralıklarıyla yapılmış üç gözlem çizimi karşılaştırması.', 22)


def dogrulama_tartisma_karti():
    ic = f'<rect x="6" y="6" width="284" height="96" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(148, 25, 'Kerem’in İlk Günlük Notu (Doğrulama Öncesi)', 11, KIR)
    ic += yazi(22, 48, '1. “Güneş gökyüzünde hareketsiz durur.”', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 68, '2. “Yüzeydeki koyu renkli bölgeler', 10.8, LAC, 'start', ince=True)
    ic += yazi(38, 84, 'Güneş’in katmanlarıdır.”', 10.8, LAC, 'start', ince=True)

    ic += f'<line x1="296" y1="54" x2="316" y2="54" stroke="{LAC}" stroke-width="2"/><path d="M311 49 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="322" y="6" width="272" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(458, 25, 'Bilimsel Kaynakla Doğrulama Sonrası', 11, YESIL_K)
    ic += yazi(458, 52, 'Eksikler tamamlanır, hatalı olan', 11, LAC, ince=True)
    ic += yazi(458, 72, '1 ve 2. ifadeler günlüğün yeni', 11, LAC, ince=True)
    ic += yazi(458, 90, 'sayfasında düzeltilir: ?', 11.2, YESIL_K)
    return svg(600, 110, ic, 'Kerem’in doğrulama öncesi hatalı günlük notu ve bilimsel kaynakla doğrulama sonrası düzeltme kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bilgi_adimlari_sema()
    s[4]['gorsel'] = gozlem_guvenlik_panosu()
    s[5]['gorsel'] = kaynak_kartlari_tablo()
    s[6]['gorsel'] = gunes_leke_gozlemi()
    s[7]['gorsel'] = gunluk_hazirlama_sema()
    s[8]['gorsel'] = gorunen_boyut_deneyi()
    s[9]['gorsel'] = parker_uzay_karti()
    s[10]['gorsel'] = galileo_karsilastirma()
    s[12]['gorsel'] = dogrulama_tartisma_karti()
