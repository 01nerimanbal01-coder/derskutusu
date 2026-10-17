# -*- coding: utf-8 -*-
"""12. Sınıf Din Kültürü ve Ahlak Bilgisi — 4. Hafta görsel modülü: İslam Medeniyetinde Öne Çıkan Eğitim ve Bilim Kurumları."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">İLK DÖNEM EĞİTİM KURUMLARI: MESCİT, SUFFE VE MEKTEP</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Dârülerkam, Mescit ve Ashâb-ı Suffe", [
        "• Mekke döneminde ilk eğitim merkezi: Dârülerkam",
        "• Medine'de Mescid-i Nebevî ibadet ve ilim merkezi oldu",
        "• Suffe: Mescid-i Nebevî bitişiğindeki ilk yatılı",
        "  İslam üniversitesi; öğrencilerine Ashâb-ı Suffe denir",
        "• En meşhur Suffe talebesi: Hz. Ebû Hüreyre (r.a.)",
        "• Camilerde 'ders halkaları' (halaka) geleneği doğdu"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Mektep (Küttâb) ve Sıbyan Mektepleri", [
        "• İlköğretim düzeyindeki temel eğitim kurumlarıdır",
        "• Okuma-yazma, Kur'an-ı Kerim, temel dini bilgiler,",
        "  güzel ahlak ve matematik (hesap) öğretilmiştir",
        "• Osmanlı'da 'Sıbyan Mektebi' veya 'Mahalle Mektebi'",
        "  adıyla her caminin yanında açılmıştır",
        "• Çocukların okula başlaması 'Âmin Alayı' ile kutlanmıştır"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">YÜKSEKÖĞRETİM VE İHTİSAS KURUMLARI: MEDRESE, DÂRÜLKURRÂ, DÂRÜLHADİS</text>'
    )
    ic += _kart(25, 50, 225, 175, "#d97706", "Medrese (Yükseköğretim)", [
        "• Nizamiye Medreseleri (1067,",
        "  Alparslan ve Nizamülmülk)",
        "  ilk büyük üniversite ağıdır",
        "• Osmanlı'da ilk medrese:",
        "  İznik Medresesi (1331)",
        "• Sahn-ı Seman ve Süleymaniye",
        "  Medreseleri zirve kurumlarıdır"
    ])
    ic += _kart(268, 50, 225, 175, "#8b5cf6", "Dârülkurrâ (Kur'an İhtisas)", [
        "• Kur'an-ı Kerim'i güzel okuma,",
        "  hafızlık ve 'Kıraat İlmi'",
        "  alanında uzman yetiştiren",
        "  ihtisas medreseleridir",
        "• Tecvit, mahreç ve aşere-takrib",
        "  eğitimi verilmiştir"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Dârülhadis (Hadis İhtisas)", [
        "• Hadis ilimlerinde uzman",
        "  (muhaddis) yetiştiren yüksek",
        "  ihtisas kurumlarıdır",
        "• İlk Dârülhadis: Şam'da",
        "  Nûreddin Zengî tarafından",
        "  kurulan Nûriye Dârülhadisi'dir"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">BİLİM VE ARAŞTIRMA MERKEZLERİ: BEYTÜLHİKME, RASATHANE VE KÜTÜPHANE</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Beytülhikme (Bilgelik Evi)", [
        "• Abbasîler döneminde Bağdat'ta",
        "  (Harun Reşid ve Me'mûn)",
        "  kurulan bilim akademisidir",
        "• Yunanca, Süryanice, Farsça",
        "  ve Sanskritçe eserler",
        "  Arapçaya tercüme edilmiştir"
    ])
    ic += _kart(268, 50, 225, 175, "#14b8a6", "Rasathane (Gözlemevi)", [
        "• Astronomi gözlemlerinin",
        "  yapıldığı bilim merkezleridir",
        "• Bağdat Şemmâsiye, Merâga",
        "  (Nasîrüddin Tûsî), Semerkant",
        "  (Uluğ Bey) ve İstanbul",
        "  (Takıyyüddin) rasathaneleri"
    ])
    ic += _kart(510, 50, 225, 175, "#0ea5e9", "Kütüphane (Beytülkütüb)", [
        "• Kurtuba, Bağdat, Kahire,",
        "  Semerkant ve İstanbul'da",
        "  yüz binlerce ciltlik",
        "  vakıf kütüphaneleri kuruldu",
        "• Beytülhikme, Dârülilim",
        "  ve Süleymaniye Kütüphanesi"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">TIP EĞİTİMİ VE SAĞLIK KURUMLARI: ŞİFAHANE (BÎMÂRİSTAN / DÂRÜŞŞİFA)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Şifahane (Bîmâristan / Dârüşşifa / Mâristan)", [
        "• Hem hastaların ücretsiz tedavi edildiği hastane",
        "  hem de uygulamalı tıp eğitimi verilen tıp fakültesidir",
        "• İlk kapsamlı bîmâristan Emevî Halifesi Velîd b.",
        "  Abdülmelik tarafından 706'da Şam'da kurulmuştur",
        "• Ruh ve akıl hastaları su sesi, kuş sesi ve",
        "  musiki makamlarıyla şefkatle tedavi edilmiştir"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "Anadolu'da Öne Çıkan Tarihi Şifahaneler", [
        "• Kayseri Gevher Nesibe Dârüşşifası (1206 - Dünyanın",
        "  ilk müstakil tıp fakültesi ve hastanesi)",
        "• Sivas İzzeddin Keykâvus ve Divriği Turan Melek",
        "• Amasya Dârüşşifası ve Edirne II. Bayezid Dârüşşifası",
        "• İstanbul Fatih ve Süleymaniye Dârüşşifaları",
        "• Vakıf kültürüyle tüm insanlara hizmet vermiştir"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]