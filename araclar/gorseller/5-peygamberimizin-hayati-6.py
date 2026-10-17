def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Fil Vakası (M.S. 571): Olayın Sebebi, Gelişimi ve Sonucu</text>'
    ic += _kart(20, 45, 230, 185, "1. Olayın Sebebi", [
        "• Yemen Valisi Ebrehe\'nin San\'a",
        "  şehrinde Kulleys adlı kilise yapması",
        "• Arapların Kâbe ziyaretini kıskanıp",
        "  hac merkezini Yemen\'e çekme isteği",
        "• Başarısız olunca Kâbe\'yi yıkmak",
        "  için büyük bir ordu hazırlaması"
    ], "#be123c", "#fff1f2")
    ic += _kart(265, 45, 230, 185, "2. Abdülmuttalib\'in Tavrı", [
        "• Ordunun önünde Mamud adlı fil",
        "• Mekke yakınında (Muhassır Vadisi)",
        "  filin çöküp Kâbe\'ye yürümemesi",
        "• Abdülmuttalib\'in tarihi sözü:",
        "  \'Ben develerin sahibiyim, Kâbe\'nin",
        "   de onu koruyacak bir Rabbi vardır!\'"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "3. İlahi Mucize ve Sonuç", [
        "• Allah\'ın sürü sürü kuşlar",
        "  (Ebâbîl kuşları) göndermesi",
        "• Kuşların gagaları ve ayaklarıyla",
        "  pişkin taşlar (siccîl) atması",
        "• Ebrehe ordusunun yenik ekin",
        "  yaprağı gibi darmadağın olması"
    ], "#059669", "#ecfdf5")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'de Fil Vakası: Fil Suresi (105. Sure)</text>'
    ic += _kart(20, 45, 350, 175, "Fil Suresi\'nin Okunuşu", [
        "• Bismillâhirrahmânirrahîm",
        "• 1. Elem tera keyfe fe\'ale Rabbüke bi-ashâbi\'l-fîl.",
        "• 2. Elem yec\'al keydehüm fî tadlîl.",
        "• 3. Ve ersele \'aleyhim tayran ebâbîl.",
        "• 4. Termîhim bi-hicâratin min siccîl.",
        "• 5. Fece\'alehüm ke\'asfin me\'kûl."
    ], "#7c3aed", "#f5f3ff")
    ic += _kart(390, 45, 350, 175, "Fil Suresi\'nin Anlamı", [
        "• 1. Rabbinin Fil sahiplerine ne yaptığını görmedin mi?",
        "• 2. Onların tuzaklarını boşa çıkarmadı mı?",
        "• 3. Üzerlerine sürü sürü (ebâbîl) kuşlar gönderdi.",
        "• 4. Onlara pişirilmiş çamurdan (siccîl) taşlar atıyorlardı.",
        "• 5. Nihayet onları yenilmiş ekin yaprağı gibi yaptı."
    ], "#0f766e", "#f0fdfa")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Fil Vakası\'nın Tarihi Önemi ve Peygamberimizin Doğumu</text>'
    ic += _kart(20, 45, 350, 175, "Neden \'Fil Yılı\' (Âmü\'l-Fîl) Denilmiştir?", [
        "• O dönemde Araplarda sabit bir takvim başlangıcı yoktu",
        "• Yıllar o yıl yaşanan en büyük olayla adlandırılırdı",
        "• 571 yılında yaşanan bu mucizevi olaya \'Fil Yılı\' denildi",
        "• Kâbe\'nin ve Mekke\'nin saygınlığı tüm Arabistan\'da arttı",
        "• Son Peygamberin gelişine dair ilahi bir işaret oldu"
    ], "#d97706", "#fffbeb")
    ic += _kart(390, 45, 350, 175, "Fil Vakası\'ndan 50-55 Gün Sonra Kutlu Doğum", [
        "• Tarih: 20 Nisan 571 (12 Rebîülevvel Pazartesi, Fil Yılı)",
        "• Yer: Mekke-i Mükerreme (Haşimoğulları mahallesi)",
        "• Babası: Hz. Abdullah (Doğumdan önce vefat etmiştir)",
        "• Annesi: Hz. Âmine | Dedesi: Abdülmuttalib",
        "• Dedesi Kâbe\'ye götürüp \'Muhammed\' (Övülmüş) adını verdi"
    ], "#2563eb", "#eff6ff")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Fil Vakası\'на İlişkin Güvenilir Bilgi Kaynakları</text>'
    ic += _kart(20, 45, 230, 175, "1. Kur\'an-ı Kerim", [
        "• En temel ve kesin kaynağımız",
        "• 105. sure olan Fil Suresi",
        "• Olayın özetini ve ilahi mesajını",
        "  bizzat Allah Teâlâ haber verir",
        "• Tuzakların boşa çıktığını bildirir"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "2. Hadis ve Siyer Kaynakları", [
        "• Hz. Peygamber\'in hadisleri",
        "• Olaya şahit olan sahabilerin",
        "  ve Mekkeli büyüklerin anlatımları",
        "• İbn İshak ve İbn Hişam gibi",
        "  ilk Siyer (Peygamber tarihi) eserleri"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 175, "3. Çıkaracağımız Dersler", [
        "• Allah\'ın kudreti her şeyin üstündedir",
        "• Kâbe (Beytullah) Allah\'ın",
        "  koruması altındadır",
        "• Kibir ve zulüm sahiplerinin",
        "  planları mutlaka boşa çıkar"
    ], "#9333ea", "#faf5ff")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]
