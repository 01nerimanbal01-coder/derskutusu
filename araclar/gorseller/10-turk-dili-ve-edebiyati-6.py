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
        'Masal Türünün Yapısal Bölümleri (Beş Bölüm Plânı)</text>'
        + _kart(16, 42, 124, 138, "1. Döşeme", [
            "• ”Bir varmış",
            "  bir yokmuş...”",
            "• Tekerleme ile",
            "  dinleyiciyi",
            "  kurguya hazırlar"
        ], "#2563eb", "#eff6ff")
        + _kart(147, 42, 124, 138, "2. Serim", [
            "• Kahramanların",
            "  ve belirsiz",
            "  zaman/mekânın",
            "  tanıtıldığı",
            "  başlangıç"
        ], "#059669", "#ecfdf5")
        + _kart(278, 42, 124, 138, "3. Düğüm", [
            "• Çatışmanın,",
            "  sınavların ve",
            "  olağanüstü",
            "  maceraların",
            "  geliştiği bölüm"
        ], "#d97706", "#fffbeb")
        + _kart(409, 42, 124, 138, "4. Çözüm", [
            "• İyilerin kazandığı,",
            "  kötülerin",
            "  cezalandırıldığı",
            "  ve düğümün",
            "  çözüldüğü sonuç"
        ], "#7c3aed", "#f5f3ff")
        + _kart(540, 42, 124, 138, "5. Dilek", [
            "• ”Gökten üç",
            "  elma düştü...”",
            "• İyi dileklerle",
            "  masalı bitiren",
            "  son kalıp söz"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 195, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Masal Türünün Temel Özellikleri ve Evrensel İletisi</text>'
        + _kart(25, 42, 300, 145, "Biçim, Dil ve Kurgu Özellikleri", [
            "• Anonim halk edebiyatı ürünüdür (sözlü gelenek)",
            "• Yer (Kafdağı) ve zaman (evvel zaman) belirsizdir",
            "• Öğrenilen geçmiş zaman (-mış) veya geniş zaman",
            "• Cin, peri, dev, Zümrüdüanka gibi olağanüstülükler",
            "• Kalıp sözler (tekerlemeler) ve ahenkli anlatım"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "İçerik, Karakterler ve Eğitici Amaç", [
            "• Evrensel değerleri (iyilik, doğruluk, sabır) işler",
            "• Dini ve millî motiflere yer vermez (evrenseldir)",
            "• Kişiler ”tip” özelliği gösterir (İyi-Kötü çatışması)",
            "• Keloğlan: Zekâ, şans ve halk tipi",
            "• Didaktik (öğretici) nitelik taşır; iyiler daima kazanır"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Çok Modlu Metinlerde Dinleme/İzleme Sürecini Yönetme</text>'
        + _kart(20, 42, 200, 138, "1. Dinleme Öncesi", [
            "• Dinleme/izleme amacını",
            "  belirleme",
            "• Başlık ve görsellerden",
            "  hareketle tahmin yapma",
            "• Uygun strateji seçme"
        ], "#d97706", "#fffbeb")
        + _kart(240, 42, 200, 138, "2. Dinleme Sırası", [
            "• Ön bilgilerle bağ kurma",
            "• Ses, müzik ve görsel",
            "  unsurları birlikte izleme",
            "• Neden-sonuç, koşul ve",
            "  örtük iletileri yakalama"
        ], "#7c3aed", "#f5f3ff")
        + _kart(460, 42, 200, 138, "3. Dinleme Sonrası", [
            "• Tahminlerle sonucu",
            "  karşılaştırma",
            "• Gerçek/kurgu, öznel/",
            "  nesnel ayrımı yapma",
            "• Metni özetleyip değerlendirme"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 195, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Dünya ve Türk Edebiyatında Önemli Masal/Fabl Kaynakları</text>'
        + _kart(25, 42, 300, 138, "Doğu ve Batı Klasikleri", [
            "• Hint: Pançatantra ve Beydeba (Kelile ve Dimne)",
            "• Arap/İran: Binbir Gece ve Binbir Gündüz Masalları",
            "• Yunan/Batı: Ezop, La Fontaine, Grimm Kardeşler,",
            "  Hans Christian Andersen (Yapma masallar)"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 138, "Türk Edebiyatında Masal Derleyicileri", [
            "• Uygur Dönemi: Kalyanamkara ve Papamkara",
            "• Osmanlı Dönemi: Billur Köşk Masalları",
            "• Cumhuriyet Dönemi: Eflatun Cem Güney (Masalcı",
            "  Baba), Naki Tezel, Pertev Naili Boratav, Ziya Gökalp"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


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
