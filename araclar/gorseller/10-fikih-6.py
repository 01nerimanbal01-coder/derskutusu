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
        'Fıkıh İlminin Tarihi Dönemleri (Kronolojik Gelişim Şeması)</text>'
        + _kart(16, 42, 124, 142, "1. Hz. Peygamber", [
            "• (610 - 632)",
            "• Vahiy ve Sünnet",
            "  dönemi",
            "• Tedricilik ve",
            "  kolaylık ilkesi"
        ], "#2563eb", "#eff6ff")
        + _kart(147, 42, 124, 142, "2. Sahabe Dönemi", [
            "• (632 - ~710)",
            "• Hulefâ-yi Râşidîn",
            "• İlk icma ve kıyas",
            "  uygulamaları",
            "• Hicaz ve Irak"
        ], "#059669", "#ecfdf5")
        + _kart(278, 42, 124, 142, "3. Tâbiîn ve Tedvin", [
            "• (8. - 10. Yüzyıl)",
            "• Ehl-i Hadis (Medine)",
            "  ve Ehl-i Rey (Kûfe)",
            "• Mezheplerin",
            "  teşekkülü (Altın Çağ)"
        ], "#d97706", "#fffbeb")
        + _kart(409, 42, 124, 142, "4. İstikrar/Taklit", [
            "• (10. - 19. Yüzyıl)",
            "• Mezhep içi içtihat",
            "• Muhtasar, şerh ve",
            "  fetva mecmuaları",
            "  dönemi"
        ], "#7c3aed", "#f5f3ff")
        + _kart(540, 42, 124, 142, "5. Kanunlaştırma", [
            "• (19. Yüzyıl - Gün.)",
            "• Mecelle-i Ahkâm-ı",
            "  Adliyye (1869-1876)",
            "• Fıkıh akademileri",
            "  ve çağdaş meseleler"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Dört Büyük Amelî Fıkıh Mezhebi ve Kurucu Müçtehit İmamları</text>'
        + _kart(25, 42, 300, 145, "1. Hanefî ve 2. Mâlikî Mezhepleri", [
            "• Hanefî: İmam-ı Âzam Ebû Hanîfe (Nu’man b. Sâbit)",
            "  - Kûfe (Irak) / Ehl-i Rey ekolü",
            "  - Öğrencileri: İmam Ebû Yûsuf ve İmam Muhammed",
            "• Mâlikî: İmam Mâlik b. Enes (el-Muvatta yazarı)",
            "  - Medine (Hicaz) / Ehl-i Hadis ve Medine ehli ameli"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "3. Şâfiî ve 4. Hanbelî Mezhepleri", [
            "• Şâfiî: İmam Muhammed b. İdrîs eş-Şâfiî",
            "  - İlk fıkıh usulü eseri ”er-Risâle”nin müellifi",
            "  - Hicaz (Hadis) ve Irak (Rey) ekollerini birleştirdi",
            "• Hanbelî: İmam Ahmed b. Hanbel (el-Müsned yazarı)",
            "  - Bağdat / Hadis ve sahabe kavli ağırlıklı usul"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Ehl-i Hicaz (Ehl-i Hadis) ve Ehl-i Irak (Ehl-i Rey) Ekollerinin Karşılaştırması</text>'
        + _kart(25, 42, 300, 142, "Hicaz (Medine) Ekolü -> Ehl-i Hadis", [
            "• Merkezi: Medine-i Münevvere (Sünnetin vatanı)",
            "• Öncüleri: Saîd b. Müseyyeb, İmam Mâlik",
            "• Zengin hadis birikimi ve sade toplumsal yapı",
            "• Ayet, hadis ve sahabe uygulamasına sıkı bağlılık",
            "• Gerçekleşmemiş farazi meselelere girmezler"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 142, "Irak (Kûfe) Ekolü -> Ehl-i Rey", [
            "• Merkezi: Kûfe ve Bağdat (Kozmopolit kültür merkezi)",
            "• Öncüleri: Abdullah b. Mes’ûd, İbrâhim en-Nehaî,",
            "  Hammâd b. Ebû Süleyman ve Ebû Hanîfe",
            "• Yeni karşılaşılan karmaşık sorunlarda kıyas,",
            "  istihsan ve illet araştırmasına geniş yer verir"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Kanunlaştırma Dönemi: Mecelle-i Ahkâm-ı Adliyye ve Hukuk Mirası</text>'
        + _kart(25, 42, 300, 138, "Mecelle-i Ahkâm-ı Adliyye (1869-1876)", [
            "• Ahmet Cevdet Paşa başkanlığındaki ilim heyeti",
            "  tarafından hazırlanan ilk İslam Medeni Kanunu",
            "• 16 kitap ve 1851 maddeden oluşur",
            "• İlk 99 maddesi ”Kavâid-i Külliyye” (Genel Hukuk",
            "  İlkeleri) olup evrensel hukuk kurallarıdır"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 138, "Hukuki Aile Kararnamesi ve Çağdaş Kurumlar", [
            "• 1917 Hukuk-ı Aile Kararnamesi: Aile hukukunu",
            "  farklı mezheplerden yararlanarak kanunlaştırdı",
            "• Günümüzde DİB Din İşleri Yüksek Kurulu ve",
            "  İslam Fıkıh Akademileri ortak (kolektif) içtihat yapar"
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
