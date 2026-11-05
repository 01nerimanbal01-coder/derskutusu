"""7. sınıf Türkçe 12. hafta (Mustafa Kemal’in Kağnısı, Şiirde Ahenk, Anlam Kayması ve Birleşik Çekimli Fiiller) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def kagni_siir_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 24, 'Mustafa Kemal’in Kağnısı — Fazıl Hüsnü Dağlarca', TUR, kalin=True)
    ic += yazi(180, 50, '«Yediyordu Elif kağnısını, kara geceden geceden...', LAC)
    ic += yazi(180, 72, 'Kocabaş çok ihtiyardı, çok zayıftı, mahzundu bütün bütün,', LAC)
    ic += yazi(180, 94, 'Elif’cik boyunduruğun ucuna girdi, cephane gecikmesin diye!»', KIR, kalin=True)
    return svg(ic, 'Mustafa Kemal’in Kağnısı şiirinden dizeler ve tema kartı.')


def fiil_cekim_yapi_kartlari():
    kartlar = [
        (6, 6, '1. taşıyordu', 'taşı - yor - du (2 kip)', MAVI, MAVI_A),
        (184, 6, '2. koruyabiliriz', 'koru-y-abil-ir-iz (Yeterlilik)', YES, YES_A),
        (6, 60, '3. izlemişti', 'iz - le - miş - ti (Yapım + 2 kip)', TUR, TUR_A),
        (184, 60, '4. yardım ettiler', 'yardım + et-ti-ler (1 kip)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Fiilde çekim türü ve sözcük yapısı inceleme kartları.')


def siir_ahenk_dortlugu():
    ic = kutu(6, 6, 200, 103, MAVI_A, MAVI)
    ic += yazi(106, 24, 'Dörtlük İncelemesi', MAVI, kalin=True)
    ic += yazi(106, 46, 'Geçit verir dumanlı dağ-lar,', LAC, kalin=True)
    ic += yazi(106, 64, 'Yeşerir baharda bütün bağ-lar,', LAC, kalin=True)
    ic += yazi(106, 82, 'Güneş doğar güzel yurd-uma,', LAC, kalin=True)
    ic += yazi(106, 98, 'Selam olsun şanlı ord-uma.', LAC, kalin=True)
    ic += kutu(212, 6, 142, 103, YES_A, YES)
    ic += yazi(283, 28, 'Ahenk Unsurları', YES, kalin=True)
    ic += yazi(283, 56, 'Ekler: -lar / -uma', LAC)
    ic += yazi(283, 82, 'Sesler: -ağ / -rdu', KIR, kalin=True)
    return svg(ic, 'Dörtlükte redif ve kafiye çözümlemesi kartı.')


def anlam_kaymasi_kartlari():
    kartlar = [
        (6, 6, '1. Haftaya dönüyor.', 'Şimdiki → Gelecek', TUR, TUR_A),
        (184, 6, '2. Bir gün balıkçı görür.', 'Geniş → Duyulan Geçmiş', MOR, MOR_A),
        (6, 60, '3. Dün akşam ulaştı.', 'Geçmiş → Gerçek Geçmiş', YES, YES_A),
        (184, 60, '4. Düzenli çalışacaksın!', 'Gelecek → Gereklilik/Emir', KIR, KIR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Fiilde anlam (zaman/kip) kayması örnek kartları.')


def soz_sanati_dizeleri():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 26, 'Dize ve Dil Bilgisi Çözümlemesi', MOR, kalin=True)
    ic += yazi(180, 54, '«İnlerdi kağnının tekerlekleri,', LAC, kalin=True)
    ic += yazi(180, 76, 'Gecenin yıldızları Elif’e bakıp ağlardı.»', LAC, kalin=True)
    ic += yazi(180, 98, 'Fiiller: inle-r-di · ağla-r-dı   |   Sanat: ?', MAVI, kalin=True)
    return svg(ic, 'Kişileştirme sanatı ve birleşik çekimli fiil içeren dizeler.')


def kagni_olay_sirasi():
    adimlar = [
        (6, '1. Yola Çıkış', 'Gece Cephane Yükü', MAVI, MAVI_A),
        (94, '2. Engel', 'Kocabaş’ın Çökmesi', TUR, TUR_A),
        (182, '3. Fedakârlık', 'Elif Boyundurukta', KIR, KIR_A),
        (270, '4. Kararlılık', 'Cepheye İlerleyiş', YES, YES_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Mustafa Kemal’in Kağnısı şiirindeki olay örgüsü basamakları.')


def birlesik_yapi_cekim_tablosu():
    kartlar = [
        (6, 6, 'geliyordu', 'Basit Yapı · Birleşik Çekim', MAVI, MAVI_A),
        (184, 6, 'başarabilirsin', 'Birleşik Yapı · Basit Çekim', TUR, TUR_A),
        (6, 60, 'fark etmiştik', 'Birleşik Yapı · Birleşik Çekim', YES, YES_A),
        (184, 60, 'çalışmalıyız', 'Basit Yapı · Basit Çekim', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Birleşik yapılı ve birleşik çekimli fiillerin karşılaştırılması.')


def dusunceyi_gelistirme_karti():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 24, 'Millî Mücadele’de Cephe Gerisi (Bilgilendirici Metin)', CAM, kalin=True)
    ic += yazi(180, 50, 'Atatürk, «Dünyada hiçbir milletin kadını, Anadolu kadınından daha fazla', LAC)
    ic += yazi(180, 72, 'çalıştım diyemez.» demiştir. 1921-1922 yıllarında İnebolu’dan Ankara’ya', LAC)
    ic += yazi(180, 94, 'kağnılarla tam 300.000 ton cephane taşınarak zafer kazanılmıştır.', MAVI, kalin=True)
    return svg(ic, 'Tanık gösterme ve sayısal verilerden yararlanma içeren metin kartı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kagni_siir_karti()
    s[2]['gorsel'] = fiil_cekim_yapi_kartlari()
    s[5]['gorsel'] = siir_ahenk_dortlugu()
    s[6]['gorsel'] = anlam_kaymasi_kartlari()
    s[7]['gorsel'] = soz_sanati_dizeleri()
    s[8]['gorsel'] = kagni_olay_sirasi()
    s[9]['gorsel'] = birlesik_yapi_cekim_tablosu()
    s[11]['gorsel'] = dusunceyi_gelistirme_karti()
