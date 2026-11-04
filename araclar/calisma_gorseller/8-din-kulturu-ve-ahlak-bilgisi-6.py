"""8. sınıf Din Kültürü ve Ahlak Bilgisi 6. hafta (Bir Peygamber Tanıyorum: Hz. Musa (a.s.)) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı font-size="12" Noto Sans; eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, KUM = '#9aa6bd', '#eef1f6', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def mekan_olay_semasi():
    kartlar = [
        ('Nil ve Saray', 'Sandıkla Nil’e', 'Hz. Asiye himayesi', MAVI, MAVI_A, 6),
        ('Medyen Kuyusu', 'İki kıza yardım', 'Hz. Şuayb ile bağ', YES, YES_A, 152),
        ('Tûr Dağı', 'Tuvâ Vadisi vahyi', 'Hz. Harun desteği', TUR, TUR_A, 298),
        ('Kızıldeniz', 'Asâ ile 12 yol', 'Tevekkül zaferi', MOR, MOR_A, 444),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 70
        ic += kutu(x, 6, 140, 86, z, r, 8, 1.3)
        ic += yazi(cx, 26, bas, r)
        ic += f'<line x1="{x + 12}" y1="34" x2="{x + 128}" y2="34" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 56, s1, LAC, 'middle', True)
        ic += yazi(cx, 76, s2, LAC, 'middle', True)
    return svg(590, 98, ic, 'Hz. Musa hayatındaki dört temel mekân ve olay şeması.', 22)


def kader_saray_sureci():
    ic = kutu(6, 6, 282, 86, KIR_A, KIR, 8, 1.3)
    ic += yazi(147, 26, 'Firavun’un Aldığı Tedbir', KIR)
    ic += yazi(147, 50, 'Saltanatını koruma hırsıyla', LAC, 'middle', True)
    ic += yazi(147, 72, 'doğan erkek bebekleri öldürttü.', LAC, 'middle', True)

    ic += kutu(302, 6, 282, 86, YES_A, YES, 8, 1.3)
    ic += yazi(443, 26, 'Yüce Allah’ın Takdiri (Kader)', YES)
    ic += yazi(443, 50, 'Hz. Musa’yı bizzat Firavun’un', LAC, 'middle', True)
    ic += yazi(443, 72, 'sarayında öz annesiyle büyüttü.', LAC, 'middle', True)
    return svg(590, 98, ic, 'Firavun tuzağına karşı Yüce Allah takdirinin gerçekleşmesi şeması.', 22)


def kissa_bilgi_panosu():
    ic = kutu(6, 6, 282, 92, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(147, 26, 'Unvan ve Özellikleri', MAVI)
    ic += yazi(147, 48, 'Ulu’l-Azm · Kelîmullah unvanı', LAC, 'middle', True)
    ic += yazi(147, 68, 'Öz annesinin sütünü emmesi', LAC, 'middle', True)
    ic += yazi(147, 88, 'Hata sonrası samimi tövbe', MAVI)

    ic += kutu(302, 6, 282, 92, TUR_A, TUR, 8, 1.3)
    ic += yazi(443, 26, 'Mucize ve İmtihanlar', TUR)
    ic += yazi(443, 48, 'Asâ · Yed-i beyzâ mucizeleri', LAC, 'middle', True)
    ic += yazi(443, 68, 'Sihirbazların secdeye varması', LAC, 'middle', True)
    ic += yazi(443, 88, 'Sâmirî’nin altın buzağı imtihanı', TUR)
    return svg(590, 104, ic, 'Hz. Musa kıssası unvanlar, mucizeler ve imtihanlar panosu.', 22)


def taha_dua_karti():
    ic = kutu(6, 6, 578, 92, MOR_A, MOR, 8, 1.4)
    ic += yazi(295, 26, 'Hz. Musa’nın (a.s.) Tebliğ Öncesi Duası (Tâhâ, 25–30)', MOR)
    ic += yazi(295, 50, '“Rabbim! Göğsüme genişlik ver, işimi bana kolaylaştır,', LAC, 'middle', True)
    ic += yazi(295, 70, 'dilimdeki düğümü çöz ki sözümü iyi anlasınlar;', LAC, 'middle', True)
    ic += yazi(295, 88, 'ailemden kardeşim Harun’u da bana yardımcı (vezir) yap.”', MOR)
    return svg(590, 104, ic, 'Tâhâ Suresi 25-30. ayetlerdeki Hz. Musa duası kartı.', 22)


def zaman_seridi_musa():
    adimlar = [
        ('1. Evre', 'Nil Nehri', 've Saray', MAVI, MAVI_A, 6),
        ('2. Evre', 'Medyen’e', 'Yolculuk', YES, YES_A, 152),
        ('3. Evre', 'Tûr Dağı', 'İlk Vahiy', TUR, TUR_A, 298),
        ('4. Evre', 'Kızıldeniz', 've Tevrat', MOR, MOR_A, 444),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in adimlar:
        cx = x + 70
        ic += kutu(x, 6, 140, 78, z, r, 8, 1.3)
        ic += yazi(cx, 25, bas, r)
        ic += yazi(cx, 48, s1, LAC, 'middle', True)
        ic += yazi(cx, 68, s2, LAC, 'middle', True)
    return svg(590, 90, ic, 'Hz. Musa hayatının dört kronolojik evresi şeması.', 21)


def sihir_mucize_karti():
    ic = kutu(6, 6, 282, 86, GRI_A, GRI, 8, 1.3)
    ic += yazi(147, 26, 'Sihirbazların Gösterisi (Sihir)', LAC)
    ic += yazi(147, 50, 'Göz yanıltmaya dayalı geçici hile', LAC, 'middle', True)
    ic += yazi(147, 72, 'İpler ve sopalar yılan gibi göründü', LAC, 'middle', True)

    ic += kutu(302, 6, 282, 86, CAM_A, CAM, 8, 1.3)
    ic += yazi(443, 26, 'Hz. Musa’nın Asâsı (Mucize)', CAM)
    ic += yazi(443, 50, 'Yüce Allah’ın kudretiyle hakikat', LAC, 'middle', True)
    ic += yazi(443, 72, 'Hileleri yutunca secdeye kapandılar', CAM)
    return svg(590, 98, ic, 'Sihir ile ilahi mucize arasındaki farkı gösteren karşılaştırma kartı.', 22)


def kizildeniz_tevekkul_panosu():
    ic = kutu(6, 6, 578, 88, YES_A, YES, 8, 1.4)
    ic += yazi(295, 26, 'Kızıldeniz Kıyısında Sarsılmaz Tevekkül (Şuarâ, 61–62)', YES)
    ic += yazi(295, 50, 'İsrailoğulları: “İşte yakalandık!” · Hz. Musa (a.s.):', LAC, 'middle', True)
    ic += yazi(295, 72, '“Asla! Şüphesiz Rabbim benimledir; bana mutlaka bir kurtuluş yolu gösterecektir!”', YES)
    return svg(590, 100, ic, 'Kızıldeniz kıyısında Hz. Musa tevekkül sözü panosu.', 22)


def dort_bilgi_fisi():
    fisler = [
        ('1. Fiş · Tebliğ Dili', 'Tâhâ 44: Yumuşak söz emri', MAVI, MAVI_A),
        ('2. Fiş · Yardımseverlik', 'Medyen kuyusunda yardım', YES, YES_A),
        ('3. Fiş · İlahi Kitap', 'Tûr Dağı’nda Tevrat ve On Emir', MOR, MOR_A),
        ('4. Fiş · Son Nefes', 'Boğulurken imanı kabul edildi', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, acik, r, z) in enumerate(fisler):
        x, y = 6 + (i % 2) * 294, 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, z, r, 7, 1.3)
        ic += yazi(x + 144, y + 17, bas, r)
        ic += yazi(x + 144, y + 34, acik, LAC, 'middle', True)
    return svg(590, 102, ic, 'Dört bilgi fişi: 4. fişteki son nefes imanı bilgisi hatalıdır.', 22)


def kasas_dua_karti():
    ic = kutu(6, 6, 578, 86, TUR_A, TUR, 8, 1.4)
    ic += yazi(295, 26, 'Medyen’de Yardımseverlik ve Kulluk Duası (Kasas, 24)', TUR)
    ic += yazi(295, 50, 'Hz. Musa (a.s.), kuyuda hayvanlarını sulayamayan iki genç kıza karşılıksız yardım etti;', LAC, 'middle', True)
    ic += yazi(295, 72, 'ardından gölgeye çekilip: “Rabbim! Bana indireceğin her hayra muhtacım.” diye dua etti.', TUR)
    return svg(590, 98, ic, 'Kasas Suresi 24. ayet yardımseverlik ve tevazu duası kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = mekan_olay_semasi()
    s[1]['gorsel'] = kader_saray_sureci()
    s[3]['gorsel'] = kissa_bilgi_panosu()
    s[5]['gorsel'] = taha_dua_karti()
    s[6]['gorsel'] = zaman_seridi_musa()
    s[7]['gorsel'] = sihir_mucize_karti()
    s[8]['gorsel'] = kizildeniz_tevekkul_panosu()
    s[9]['gorsel'] = dort_bilgi_fisi()
    if len(s) > 11:
        s[11]['gorsel'] = kasas_dua_karti()
