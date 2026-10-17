# -*- coding: utf-8 -*-
"""8. Sınıf Kur'an-ı Kerim — 5. Hafta Görselleri (Hz. Yusuf Kıssasında Sabır ve Affedicilik; Yâsîn Suresi 1-12)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hz. Yusuf (as) Kıssasının İkinci Bölümü: Zindandan Mısır Sultanlığına</text>',
        _kart(25, 50, 225, 215, "1. Zindanda Sabır ve Tebliğ", [
            "• İffetini korumak için suçsuz yere",
            "  atıldığı zindanda ümitsizliğe düşmedi.",
            "• Zindan arkadaşlarına tevhid inancını",
            "  anlattı ve onların rüyalarını yorumladı.",
            "• Güzel ahlakı sebebiyle zindanda",
            "  'Muhsin' (iyiliksever) olarak tanındı."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Kralın Rüyası ve Maliye Görevi", [
            "• Mısır Kralının gördüğü '7 besili inek",
            "  ve 7 zayıf inek ile 7 başak' rüyasını",
            "  7 bolluk ve 7 kıtlık yılı olarak tabir etti.",
            "• Suçsuzluğu kanıtlandıktan sonra zindandan",
            "  çıktı ve Mısır hazinelerinin başına geçti.",
            "• Adaletli planlamayla halkı kıtlıktan kurtardı."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Kardeşlerini Affetmesi ve Kavuşma", [
            "• Kıtlık sebebiyle Mısır'a erzak almaya",
            "  gelen kardeşlerine kendisini tanıttı.",
            "• İntikam almak yerine 'Bugün size kınama",
            "  yoktur, Allah sizi bağışlasın!' dedi.",
            "• Babası Hz. Yakup ve ailesiyle kavuştu;",
            "  çocukluk rüyası (Yusuf, 100) gerçekleşti."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hz. Yakup ve Hz. Yusuf Kıssasından Çıkarılan Evrensel İlkeler</text>',
        _kart(30, 50, 335, 215, "Sabr-ı Cemîl ve İffet Bilinci", [
            "• Sabr-ı Cemîl (Güzel Sabır): Hz. Yakup gibi",
            "  isyan etmeden yalnızca Allah'a sığınarak sabretmek.",
            "• İffet ve Hayâ: Hz. Yusuf gibi en zor şartlarda",
            "  bile harama yaklaşmamak ve Allah'tan korkmak.",
            "• 'Kim Allah'tan sakınır (takva) ve sabrederse,",
            "  Allah iyilik edenlerin ecrini zayi etmez!' (Yusuf, 90)"
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Hasetten Kaçınma ve Affedicilik", [
            "• Kıskançlık (haset) kardeşleri bile hataya",
            "  sürükleyebilir; mümin hasetten uzak durmalıdır.",
            "• Güç ve makam eline geçtiğinde intikam",
            "  almak yerine Hz. Yusuf gibi affedici olmak",
            "  ('Lâ tesrîbe aleykümü'l-yevm') en büyük erdemdir.",
            "• Allah'ın rahmetinden asla ümit kesilmez (Yusuf, 87)."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Yâsîn Suresi 1-12. Ayetleri Yüzünden Okuma ve Ana Mesajları</text>',
        _kart(30, 50, 335, 215, "1-6. Ayetler: Kur'an ve Peygamberlik", [
            "• Hurûf-u Mukattaa: 'Yâ-Sîn' ile başlar.",
            "• Hikmet dolu Kur'an'a (ve'l-Kur'âni'l-hakîm)",
            "  yemin edilerek Hz. Muhammed'in (sav)",
            "  dosdoğru yol (sırât-ı müstakîm) üzere",
            "  gönderilmiş bir peygamber olduğu vurgulanır.",
            "• Kur'an, gafletteki insanları uyarmak için inmiştir."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "7-12. Ayetler: Ahiret ve Amel Defteri", [
            "• Kibirle inkârda diretenlerin hakikati göremediği,",
            "  ancak Kur'an'a uyan ve görmeden Rahmân'dan",
            "  saygıyla korkanların bağışlanacağı müjdelenir.",
            "• 12. Ayet: 'Ölüleri biz diriltiriz; onların",
            "  yaptıklarını ve arkalarında bıraktıkları eserleri",
            "  (izleri) yazarız!' (Sorumluluk bilinci)."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Yâsîn Suresi 1-12. Ayetlerdeki Tecvit Uygulamaları</text>',
        _kart(30, 50, 335, 195, "Medd-i Lâzım ve Medd-i Munfasıl", [
            "• 'Yâ-Sîn': 'Yâ' harfi Medd-i Tabiî (1 elif),",
            "  'Sîn' harfi ise sonunda sükûn-u lâzım olduğu",
            "  için Medd-i Lâzım Harfî olarak 4 elif uzatılır!",
            "• 'İnnâ cealnâ', 'Mâ ünzira', 'Sevâün aleyhim'",
            "  ifadelerinde Medd-i Munfasıl ve Muttasıl uygulanır."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "İhfâ, İdgam ve Sekteli Okunuş Bilinci", [
            "• 'Tenzîle'l-azîzi'r-rahîm' ve 'li-tünzira kavmen'",
            "  ifadelerinde Sakin Nûn + Zây -> İhfâ kuralı vardır.",
            "• 'Kavmen mâ' ve 'Bi-mağfiratin ve ecrin kerîm'",
            "  ifadelerinde İdgam-ı Meal-Gunne uygulanır.",
            "• 'Mim-men' ifadesinde İdgam-ı Misleyn yapılır."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
