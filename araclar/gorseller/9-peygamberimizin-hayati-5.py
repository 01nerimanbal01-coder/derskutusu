def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#922b21"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Cahiliye Kavramı ve Oluşmasına Zemin Hazırlayan Etkenler (PH.9.1.2)</text>'
    c += _kart(18, 54, 314, 170, "Cahiliye Kavramının Anlamı", [
        "• Sözlükte \'bilgisizlik, taşkınlık, öfke ve",
        "  nefsine uyarak haddi aşmak\' demektir.",
        "• Terim anlamı: Arapların İslam\'dan önceki",
        "  inanç, ahlak ve toplumsal sapmalarını ifade",
        "  eden tarihsel dönem ve zihniyet yapısıdır."
    ], "#922b21", "#fdedec")
    c += _kart(348, 54, 314, 170, "Cahiliye Anlayışını Doğuran Etkenler", [
        "• Tevhid (Haniflik) inancından uzaklaşarak",
        "  putperestliğe ve şirke düşülmesi.",
        "• Merkezi bir devlet otoritesinin ve adil hukuk",
        "  düzeninin bulunmaması (güçlünün haklı sayılması).",
        "• Kabilecilik (asabiyet) ve ahiret inancının yokluğu."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">İslam Öncesi Mekke\'de Toplumsal Tabakalaşma ve Kabile Yapısı</text>'
    c += _kart(18, 54, 206, 175, "1. Hürler (Eşraf / Aristokrasi)", [
        "• Kabile reisleri, zengin",
        "  tüccarlar ve soylular.",
        "• Dâru\'n-Nedve\'de karar",
        "  alma yetkisine sahiptirler.",
        "• Tüm siyasi ve ekonomik",
        "  imtiyazları ellerinde tutarlar."
    ], "#1a5276", "#eaf2f8")
    c += _kart(237, 54, 206, 175, "2. Mevali (Azatlılar / Sığınanlar)", [
        "• Azat edilmiş köleler veya",
        "  kabilesinden kovulup başka",
        "  bir kabilenin himayesine",
        "  sığınan kimselerdir.",
        "• Hürlerle eşit haklara",
        "  sahip değillerdir."
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 175, "3. Köleler ve Cariyeler", [
        "• Savaş esirleri veya borcunu",
        "  ödeyemeyen insanlardır.",
        "• Hiçbir insani ve hukuki",
        "  hakları yoktur; eşya gibi",
        "  alınıp satılır ve ağır",
        "  işlerde çalıştırılırlar."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Cahiliye Kültürünün Genel Özellikleri (Olumsuz Uygulamalar)</text>'
    c += _kart(18, 54, 314, 170, "Ailede ve Kadına Bakışta Yozlaşma", [
        "• Kadına değer verilmemesi, mirastan pay",
        "  alamaması ve söz hakkının bulunmaması.",
        "• Kız çocuklarının diri diri toprağa gömülmesi",
        "  (Ve\'dü\'l-benât — Nahl, 16/58-59; Tekvîr, 81/8-9).",
        "• Sınırsız ve nikâhsız evlilik türlerinin yaygınlığı."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 170, "Toplumsal ve Ekonomik Yozlaşma", [
        "• Asabiyet (Kabile Taassubu): \'Zalim de olsa mazlum da",
        "  olsa kabile kardeşine yardım et!\' anlayışı.",
        "• Kan davaları (Eyyâmü\'l-Arab savaşları).",
        "• Tefecilik (riba/faiz), içki, kumar, fal okları,",
        "  büyücülük ve kâhinliğin yaygın olması."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Cahiliye Toplumundaki Olumlu Hasletler ve İslam\'ın Dönüşümü</text>'
    c += _kart(18, 54, 314, 165, "Korunan Olumlu Değerler (Mekarim-i Ahlak)", [
        "• Cömertlik ve misafirperverlik (İkramda yarışma).",
        "• Sözünde durma (ahde vefa) ve emaneti koruma.",
        "• Cesaret, yiğitlik ve mazlumu koruma (Hilfü\'l-Fudûl",
        "  — Erdemliler Topluluğu antlaşması).",
        "• Şiir, hitabet ve belagat (edebiyat) sevgisi."
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 165, "Hz. Peygamber\'in (sav) Cahiliye\'ye Karşı Tutumu", [
        "• Şirk, putperestlik, kan davası, faiz ve kız",
        "  çocuklarının öldürülmesi kesin olarak kaldırılmıştır.",
        "• Cömertlik, misafirperverlik ve Hilfü\'l-Fudûl gibi",
        "  adil uygulamalar ise tevhid ve ihlas temeline",
        "  oturtularak devam ettirilmiştir."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
