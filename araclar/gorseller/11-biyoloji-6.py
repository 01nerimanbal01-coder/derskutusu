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
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Nöronun Yapısı ve İmpulsun İletim Yönü</text>'
        '<circle cx="85" cy="115" r="32" fill="#dbeafe" stroke="#2563eb" stroke-width="2.2"/>'
        '<circle cx="85" cy="115" r="10" fill="#1e40af"/>'
        '<line x1="40" y1="85" x2="60" y2="96" stroke="#2563eb" stroke-width="2.5"/>'
        '<line x1="35" y1="115" x2="53" y2="115" stroke="#2563eb" stroke-width="2.5"/>'
        '<line x1="40" y1="145" x2="60" y2="134" stroke="#2563eb" stroke-width="2.5"/>'
        '<line x1="117" y1="115" x2="275" y2="115" stroke="#2563eb" stroke-width="4"/>'
        '<rect x="132" y="103" width="35" height="24" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>'
        '<rect x="178" y="103" width="35" height="24" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>'
        '<rect x="224" y="103" width="35" height="24" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>'
        '<line x1="275" y1="115" x2="298" y2="98" stroke="#2563eb" stroke-width="2.5"/>'
        '<line x1="275" y1="115" x2="298" y2="132" stroke="#2563eb" stroke-width="2.5"/>'
        '<text x="85" y="165" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Dendrit &amp; Gövde</text>'
        '<text x="195" y="92" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#b45309" text-anchor="middle">Miyelin Kılıf &amp; Ranvier Boğumu</text>'
        '<text x="292" y="155" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Akson Ucu</text>'
        + _kart(330, 42, 330, 145, "Nöronun Kısımları ve Görevleri", [
            "• Dendrit: Uyartıları alıp hücre gövdesine iletir.",
            "• Hücre Gövdesi: Çekirdek, mitokondri ve Nissl",
            "  cisimciklerini (granüllü ER) bulundurur; sentrozom yoktur.",
            "• Akson: Uyartıyı diğer nörona/efektöre taşır.",
            "• Bir nöronda yön: Dendrit -> Gövde -> Akson"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Nöronda Elektriksel Değişimler ve Sinapsta Kimyasal İletim</text>'
        + _kart(25, 42, 300, 145, "Polarizasyon - Depolarizasyon", [
            "• Polarizasyon (Dinlenme): Dış (+), İç (-); Na+/K+",
            "  pompası ATP harcayarak K+’yı içeri, Na+’yı dışarı taşır.",
            "• Depolarizasyon (Uyartı): Na+ kapıları açılır, Na+",
            "  difüzyonla içeri girer; Dış (-), İç (+) olur.",
            "• Repolarizasyon: K+ kapıları açılır, K+ dışarı çıkar."
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Sinapsta İmpuls İletimi", [
            "• İletim yönü: Akson ucu -> Sinaps boşluğu -> Dendrit",
            "• Akson ucuna gelen impuls Ca2+ girişini sağlar.",
            "• Sinaptik keselerden nörotransmitter maddeler",
            "  ekzositozla (ATP harcanarak) boşluğa salgılanır.",
            "• İletim kimyasaldır ve aksona göre daha yavaştır."
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Duyu Reseptörlerinin Sınıflandırılması ve Duyu Organları</text>'
        + _kart(25, 42, 300, 145, "Uyaran Türüne Göre Reseptörler", [
            "• Fotoreseptör: Işığa duyarlıdır -> Göz (Retina)",
            "• Kemoreseptör: Kimyasal maddelere duyarlıdır ->",
            "  Burun (koku) ve Dil (tat)",
            "• Mekanoreseptör: Basınç, dokunma, ses, denge ->",
            "  Deri ve Kulak"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Diğer Reseptörler ve İmpuls Hızı", [
            "• Termoreseptör: Sıcaklık değişimi -> Deri, Hipotalamus",
            "• Nosiseptör (Ağrı reseptörü): Beyin hariç tüm vücut",
            "• İmpuls hızı yalnızca miyelin kılıf varlığına ve",
            "  akson çapına bağlıdır (Uyaran şiddeti hızı değiştirmez,",
            "  yalnızca impuls sayısını/frekansını artırır)."
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
}


def uygula(v):
    hedefler = [0, 1, 2]
    anahtarlar = ["b1", "b2", "b3"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]