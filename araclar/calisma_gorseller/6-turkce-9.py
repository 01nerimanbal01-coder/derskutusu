"""6. sınıf Türkçe 9. hafta (Vatan Metni: Metin İçi ve Metinler Arası Karşılaştırma, Özetleme ve İsim Çekim Ekleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def iyelik_belirtme_kartlari():
    kartlar = [
        ('1. Kart: anı-y-ı', 'Neyi anlattı? → Belirtme', MAVI, MAVI_A),
        ('2. Kart: şiir-i', 'Onun şiiri → İyelik (Aitlik)', YES, YES_A),
        ('3. Kart: kürsü-y-ü', 'Neyi süsledi? → Belirtme', TUR, TUR_A),
        ('4. Kart: roman-ı', 'Neyi bitirdim? → Belirtme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'İyelik eki ile belirtme hâl ekini ayırt etme kartları.', 16)


def cokluk_eki_anlam_panosu():
    kartlar = [
        ('1. Sinan-lar', 'Benzerlik anlamı', MAVI, MAVI_A),
        ('2. Dayım-lar-a', 'Aile anlamı (?)', YES, YES_A),
        ('3. Dünya-lar', 'Abartma anlamı (?)', TUR, TUR_A),
        ('4. Bey-ler', 'Saygı anlamı (?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Çokluk ekinin cümleye kattığı farklı anlamlar panosu.', 15)


def iki_metin_karsilastirma():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 21, 'I. Metin · Şiir (Dörtlük)', 10.1, MAVI)
    ic += yazi(91, 42, '“Dalgalan göklerde al bayrağım,', 9.3, LAC, ince=True)
    ic += yazi(91, 61, 'Sensin benim huzurlu ocağım.”', 9.3, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 21, 'II. Metin · Anı (Düzyazı)', 10.1, YESIL_K)
    ic += yazi(269, 42, '“Vatan toprağını korumak için', 9.3, LAC, ince=True)
    ic += yazi(269, 61, 'bayrağımız altında kenetlendik.”', 9.3, LAC, ince=True)
    return svg(360, 88, ic, 'Şiir ve düzyazı türündeki iki vatan metninin karşılaştırma kartı.', 15)


def cekim_ekleri_cozumleme():
    kartlar = [
        ('A Kartı', 'Kahraman - lar - ımız', MAVI, MAVI_A),
        ('B Kartı', 'Vatan - ımız - dan', TUR, TUR_A),
        ('C Kartı', 'Toprak - lar - ımız - da', YES, YES_A),
        ('D Kartı', 'Bayrağ - ın - a', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ekler, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, ekler, 9.5, LAC)
    return svg(360, 94, ic, 'İsim çekim eklerinin dizilişini gösteren dört kelime kartı.', 16)


def ust_uste_iki_ek_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'EK ÇÖZÜMLEME KARTI · “ESERİNİ YARIŞMAYA GÖNDERDİ”', 10.1, CAM)
    ic += yazi(180, 45, 'Kök: eser   +   1. Ek: -i (Onun eseri = ?)   +   n   +   2. Ek: -i (Neyi? = ?)', 9.5, LAC)
    ic += yazi(180, 66, 'İpucu: İsimde üst üste gelen iki “-i” ekinden ilki aitlik, ikincisi durum bildirir.', 9.1, LAC, ince=True)
    return svg(360, 88, ic, 'Eserini kelimesindeki iyelik ve belirtme hâl eklerinin analizi.', 15)


def ozetleme_adimlari_panosu():
    adimlar = [
        ('1. Okuma', 'Ana fikri belirle', MAVI, MAVI_A),
        ('2. Seçme', 'Önemliyi ayıkla', YES, YES_A),
        ('3. Sıralama', 'Akışa göre diz', TUR, TUR_A),
        ('4. Yazma', 'Kendi cümlenle yaz', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Metin özetleme sürecinin dört temel adımı.', 15)


def soru_eki_yazim_kartlari():
    kartlar = [
        ('1. Kart (!)', 'Bahar geldimi açar (Yanlış)', KIR, KIR_A),
        ('2. Kart', 'Geniş mi geniş (Pekiştirme)', MAVI, MAVI_A),
        ('3. Kart', 'Araştırdın mı? (Soru)', MOR, MOR_A),
        ('4. Kart', 'Güneş doğdu mu... (Zaman)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Soru ekinin yazımı ve cümleye kattığı anlamlar kartı.', 16)


def vatan_metin_ici_sema():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Bölüm (İlk Dörtlükler)', 10.1, YESIL_K)
    ic += yazi(91, 44, 'Yemyeşil ovalar, yüksek dağlar', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 've coşkun akan ırmaklar', 9.5, YESIL_K)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Bölüm (Son Dörtlükler)', 10.1, TUR)
    ic += yazi(269, 44, 'Toprağı vatan yapan şehitler,', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'kahramanlık ve bağımsızlık', 9.5, TUR)
    return svg(360, 88, ic, 'Vatan şiirinin birinci ve ikinci bölümlerinin metin içi karşılaştırma şeması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = iyelik_belirtme_kartlari()
    s[2]['gorsel'] = cokluk_eki_anlam_panosu()
    s[5]['gorsel'] = iki_metin_karsilastirma()
    s[6]['gorsel'] = cekim_ekleri_cozumleme()
    s[7]['gorsel'] = ust_uste_iki_ek_karti()
    s[8]['gorsel'] = ozetleme_adimlari_panosu()
    s[9]['gorsel'] = soru_eki_yazim_kartlari()
    s[11]['gorsel'] = vatan_metin_ici_sema()
