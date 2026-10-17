def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">School Clubs, Countries and National Days Vocabulary</text>'
    ic += _kart(20, 45, 230, 185, "School Clubs (Okul Kulüpleri)", [
        "• science club : fen/bilim kulübü",
        "• maths club : matematik kulübü",
        "• technology club : teknoloji kulübü",
        "• chess club : satranç kulübü",
        "• drama &amp; art club : tiyatro ve resim",
        "• folk dance club : halk oyunları"
    ], "#2563eb", "#eff6ff")
    ic += _kart(265, 45, 230, 185, "Countries (Ülkeler)", [
        "• Türkiye, Azerbaijan, Kazakhstan",
        "• Uzbekistan, Turkmenistan, Kyrgyzstan",
        "• the UK, the USA, Canada, Australia",
        "• France, Italy, Spain, Germany",
        "• Japan, South Korea, China",
        "• Brazil, Argentina, Mexico"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 185, "National Days (Milli Günler)", [
        "• 29 October Republic Day",
        "  (29 Ekim Cumhuriyet Bayramı)",
        "• 23 April National Sovereignty",
        "  and Children\'s Day",
        "• 19 May Youth and Sports Day",
        "• 30 August Victory Day"
    ], "#dc2626", "#fef2f2")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Expressing Preferences: Do you like + V-ing? (Like / Love / Enjoy)</text>'
    ic += _kart(20, 45, 350, 175, "Asking &amp; Answering About Preferences", [
        "• Do you like reading books in your free time?",
        "  -> Yes, I do. / No, I don\'t.",
        "• Does she like doing experiments in the science club?",
        "  -> Yes, she does. / No, she doesn\'t.",
        "• What do you like doing at school?"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Verbs Followed by -ing (Gerund)", [
        "• I like playing chess. (Satranç oynamayı severim.)",
        "• He loves solving maths problems. (Çözmeyi çok sever.)",
        "• We enjoy organising club events. (Düzenlemekten hoşlanırız.)",
        "• She hates making noise in the library.",
        "• Kural: like / love / enjoy / hate + Fiil-ing!"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">School Rules &amp; Prohibitions: Mustn\'t, Can\'t and Imperatives</text>'
    ic += _kart(20, 45, 350, 175, "Prohibition: Mustn\'t &amp; Can\'t (Yasaklar)", [
        "• You mustn\'t run in the corridors! (Koridorda koşmamalısın!)",
        "• You mustn\'t shout or fight at school! (Bağırmamalısın!)",
        "• You can\'t eat or drink in the library or science lab.",
        "• Students mustn\'t be late for classes.",
        "• Kural: Özne + mustn\'t / can\'t + Yalın Fiil (V1)"
    ], "#be123c", "#fff1f2")
    ic += _kart(390, 45, 350, 175, "Imperatives &amp; Social Language (Yönergeler)", [
        "• Olumlu Emir: Listen to your teacher! / Wear your uniform!",
        "• Olumsuz Emir: Don\'t make a noise! / Don\'t fight!",
        "• Line up, nice and straight! (Güzel ve düzgün sıraya girin!)",
        "• Follow the rules and play safe! (Kurallara uy, güvenli oyna!)",
        "• Let\'s get started! (Haydi başlayalım!)"
    ], "#0f766e", "#f0fdfa")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Wh- Questions (Who / What / Where) &amp; Articles (a / an / the)</text>'
    ic += _kart(20, 45, 350, 175, "Wh- Questions at School", [
        "• What is your favourite school club? -> The chess club.",
        "• Who is the coach of the sports club? -> Mr. Demir.",
        "• Where is the notice board? -> Next to the canteen.",
        "• Where are you from? -> I am from Türkiye.",
        "• When is Republic Day? -> It is on 29th October."
    ], "#d97706", "#fffbeb")
    ic += _kart(390, 45, 350, 175, "Using a / an / the with Countries &amp; Places", [
        "• a uniform, a lab, a coach (ünsüz sesle başlayan tekil)",
        "• an assistant, an art club, an environment club (ünlü ses)",
        "• the library, the Eiffel Tower, the Anıtkabir (belirli yerler)",
        "• Ülkeler: Türkiye, France, Japan (the ALMAZ!)",
        "• İstisna: the UK, the USA, the Turkish Republic of Northern Cyprus"
    ], "#1d4ed8", "#eff6ff")
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
