def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Allah (cc) - İnsan İletişimi: Vahiy, İbadet ve Dua Döngüsü</text>'
        + _kart(20, 42, 195, 130, "1. İlahi Hitap (Vahiy)", [
            "• Allah’tan (cc) insana",
            "• Peygamberler ve kitaplar",
            "• Doğru yolu gösterme",
            "• Emir, öğüt ve müjde"
        ], "#2563eb", "#eff6ff")
        + _kart(242, 42, 195, 130, "2. İnsanın Cevabı: İbadet", [
            "• İnsandan Allah’a (cc)",
            "• Kulluk, itaat ve saygı",
            "• Bedenî ve malî ibadetler",
            "• Şükür ve bağlılık"
        ], "#059669", "#ecfdf5")
        + _kart(465, 42, 195, 130, "3. Samimi Yakınlık: Dua", [
            "• Kalpten gelen yakarış",
            "• İsteme, sığınma ve tövbe",
            "• Her an ve her yerde",
            "• İbadetin özü ve ruhu"
        ], "#d97706", "#fffbeb")
        + '<rect x="20" y="184" width="640" height="32" rx="6" fill="#f1f5f9" stroke="#cbd5e1"/>'
        '<text x="340" y="205" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">'
        'Kur’an-ı Kerim’i okumak Allah’ı (cc) dinlemek; ibadet ve dua etmek ise O’na içtenlikle cevap vermektir.</text>'
    )
    return _svg(680, 228, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'İslam’da İbadet Kavramı: Dar ve Geniş Anlamı</text>'
        + _kart(25, 42, 300, 145, "Özel (Dar) Anlamda İbadet", [
            "• Belirli vakit, şart ve kuralları vardır",
            "• Namaz kılmak (Günde 5 vakit)",
            "• Oruç tutmak (Ramazan ayında)",
            "• Zekât vermek ve Hacca gitmek",
            "• Abdest, niyet ve rükünlerle eda edilir"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Genel (Geniş) Anlamda İbadet", [
            "• Allah’ın (cc) rızasını kazanma niyetiyle",
            "• Yapılan her güzel, faydalı ve salih amel",
            "• Ailesinin rızkı için dürüstçe çalışmak",
            "• İlim öğrenmek, canlılara merhamet etmek",
            "• İnsanlara tebessüm etmek ve yardım"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Dua Türleri: Kavli (Sözlü) Dua ve Fiili (Eylemsel) Dua</text>'
        + _kart(25, 42, 300, 145, "1. Fiili Dua (Sebeplere Sarılmak)", [
            "• Gayret, emek ve tedbir göstermek",
            "• Çiftçinin tarlayı sürüp tohum ekmesi",
            "• Öğrencinin düzenli ders çalışması",
            "• Hastanın doktora gidip ilaç kullanması",
            "• Sünnetullah (evren yasaları) gereğidir"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "2. Kavli Dua (Dil ve Kalp ile Yakarış)", [
            "• Sonucu Yüce Allah’tan (cc) dilemek",
            "• ”Rabbim! Bereketli ürün nasip eyle”",
            "• ”Rabbim! İlmimi ve başarımı artır”",
            "• ”Ey Şâfî olan Allah’ım! Şifa ver”",
            "• Tevekkül ve teslimiyetin göstergesidir"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'İbadet ve Duanın Birey ve Toplum Hayatına Katkıları</text>'
        + _kart(20, 42, 200, 135, "Ruhsal Huzur", [
            "• Yalnızlık hissini giderir",
            "• Ümit ve güven aşılar",
            "• Stres ve kaygıyı azaltır",
            "• Sabır ve metanet kazandırır"
        ], "#ea580c", "#fff7ed")
        + _kart(240, 42, 200, 135, "Ahlaki Olgunluk", [
            "• Kötülüklerden alıkoyar",
            "• Sorumluluk bilinci verir",
            "• Zamanı planlamayı öğretir",
            "• İhlas ve samimiyeti artırır"
        ], "#0284c7", "#f0f9ff")
        + _kart(460, 42, 200, 135, "Toplumsal Dayanışma", [
            "• Cemaatle birlik ruhu",
            "• Zekât ve infakla paylaşma",
            "• Kardeşlik ve empati bağı",
            "• Hayırda yardımlaşma"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 190, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
