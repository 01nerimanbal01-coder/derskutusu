"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 11. hafta (Misakımillî, İstanbul’un İşgali ve BMM’nin Açılışı) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def misakimilli_kapsar_kartlari():
    kartlar = [
        (6, 6, '1. Sınırlar', 'Mondros öncesi bütünlük', MAVI, MAVI_A),
        (184, 6, '2. Kapitülasyonlar', 'Siyasi/mali kısıtlama red', KIR, KIR_A),
        (6, 60, '3. Azınlık Hakları', 'Komşu Müslüman hakları denk', YES, YES_A),
        (184, 60, '4. Halk Oylaması', 'Kars, Ardahan, Batum oyu', TUR, TUR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Misakımillî kararlarının dört temel maddesini gösteren bilgi kartları.')


def onerge_24_nisan():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, '24 Nisan 1920 Önergesi', MAVI, kalin=True)
    ic += yazi(91, 52, '• Hükûmet kurmak zorunlu', LAC)
    ic += yazi(91, 74, '• Üstünde güç yoktur!', KIR, kalin=True)
    ic += yazi(91, 96, '• Geçici başkan atanmaz', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Meclis Yapısı ve İlke', YES, kalin=True)
    ic += yazi(269, 52, '• Kurucu ve Millî Meclis', LAC)
    ic += yazi(269, 74, '• Ulusal Egemenlik ilkesi', YES, kalin=True)
    ic += yazi(269, 96, '• Güçler Birliği sistemi', MAVI, kalin=True)
    return svg(ic, '24 Nisan 1920 önergesi kararları ve Birinci BMM nitelikleri şeması.')


def isgal_tedbirleri_panosu():
    ic = kutu(6, 6, 170, 103, KIR_A, KIR)
    ic += yazi(91, 26, '16 Mart 1920 İşgali', KIR, kalin=True)
    ic += yazi(91, 52, 'İstanbul resmen işgal edildi', LAC)
    ic += yazi(91, 74, 'Mebusan Meclisi basıldı', LAC)
    ic += yazi(91, 96, 'Manastırlı Hamdi bildirdi', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Alınan Stratejik Tedbir', TUR, kalin=True)
    ic += yazi(269, 52, 'Haberleşme kesildi;', LAC)
    ic += yazi(269, 74, 'Geyve ve Ulukışla demir', TUR, kalin=True)
    ic += yazi(269, 96, 'yolları tahrip edildi!', MAVI, kalin=True)
    return svg(ic, '16 Mart 1920 İstanbul’un işgali ve Geyve-Ulukışla demir yolu tedbiri.')


def mebuslardan_istekler():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Mustafa Kemal’in 3 İsteği', MAVI, kalin=True)
    ic += yazi(91, 52, '1. Başkan seçilmek (✗)', LAC)
    ic += yazi(91, 74, '2. Müdafaa-i Hukuk Grubu (✗)', LAC)
    ic += yazi(91, 96, '3. Misakımillî onayı (✓)', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Meclisteki Sonuç', YES, kalin=True)
    ic += yazi(269, 52, 'Felah-ı Vatan kuruldu;', LAC)
    ic += yazi(269, 74, '28 Ocak 1920’de', LAC)
    ic += yazi(269, 96, 'Misakımillî kabul edildi!', YES, kalin=True)
    return svg(ic, 'Mustafa Kemal’in mebuslardan üç isteği ve gerçekleşme durumu.')


def gucler_birligi_sema():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 26, 'Birinci BMM: Güçler Birliği İlkesi (23 Nisan 1920)', MOR, kalin=True)
    ic += yazi(180, 54, 'Yasama (Kanun) + Yürütme (Hükûmet) + Yargı (İstiklal Mahkemeleri)', LAC, kalin=True)
    ic += yazi(180, 82, 'Amaç: Olağanüstü savaş şartlarında hızlı karar alıp uygulamak!', KIR, kalin=True)
    return svg(ic, 'Birinci BMM’de yasama, yürütme ve yargının tek elde toplanması şeması.')


def kronoloji_1920_seridi():
    adimlar = [
        (6, '12 Ocak', 'Mebusan Açılışı', MAVI, MAVI_A),
        (94, '28 Ocak', 'Misakımillî', YES, YES_A),
        (182, '16 Mart', 'İstanbul İşgali', KIR, KIR_A),
        (270, '23 Nisan', 'BMM Açılışı', TUR, TUR_A),
    ]
    ic = ''
    for x, tarih, olay, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, tarih, r, kalin=True)
        ic += yazi(x + 42, 72, olay, LAC, kalin=True)
    return svg(ic, '1920 yılı Ocak-Nisan arası dört temel gelişmenin kronolojik şeridi.')


def misakimilli_bmm_karsilastirma():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Misakımillî (28 Ocak)', MAVI, kalin=True)
    ic += yazi(91, 54, 'Millî sınırları çizdi;', LAC)
    ic += yazi(91, 76, 'kapitülasyonları reddetti', LAC)
    ic += yazi(91, 98, '→ Tam Bağımsızlık', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'BMM Açılışı (23 Nisan)', YES, kalin=True)
    ic += yazi(269, 54, 'Millet iradesini yönetime', LAC)
    ic += yazi(269, 76, 'hâkim kıldı', LAC)
    ic += yazi(269, 98, '→ Ulusal Egemenlik', YES, kalin=True)
    return svg(ic, 'Misakımillî (Tam Bağımsızlık) ve BMM’nin açılışı (Ulusal Egemenlik) karşılaştırması.')


def bmm_uyeleri_milli_irade():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Birinci BMM’nin Oluşumu (23 Nisan 1920 - Ankara)', CAM, kalin=True)
    ic += yazi(180, 54, '1) Anadolu’da yeniden seçilen milletvekilleri', LAC)
    ic += yazi(180, 76, '2) İstanbul’dan kaçıp Ankara’ya gelen Mebusan Meclisi üyeleri', MAVI, kalin=True)
    ic += yazi(180, 98, 'Temel Gerekçe: Halkın seçtiği vekillerin iradesine saygı!', YES, kalin=True)
    return svg(ic, 'Birinci BMM üyelerinin iki kaynağı ve milli iradeye saygı ilkesi.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = misakimilli_kapsar_kartlari()
    s[2]['gorsel'] = onerge_24_nisan()
    s[5]['gorsel'] = isgal_tedbirleri_panosu()
    s[6]['gorsel'] = mebuslardan_istekler()
    s[7]['gorsel'] = gucler_birligi_sema()
    s[8]['gorsel'] = kronoloji_1920_seridi()
    s[9]['gorsel'] = misakimilli_bmm_karsilastirma()
    s[11]['gorsel'] = bmm_uyeleri_milli_irade()
