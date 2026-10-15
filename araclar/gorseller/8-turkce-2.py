"""8. sınıf Türkçe — 2. hafta konu özeti görselleri.
1. Tema: Okuma Kültürü — Öğrencilerin Dijital Okuma Kültürü (s. 16-21)."""

from ozet_gorsel import svg


def gorsel_dijital_okuma():
    """Basılı metinden dijital metne geçiş ve dijital okuryazarlık şeması."""
    W, H = 700, 286
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Basılı Metinden Dijital Metne Geçiş ve Dijital Okuma Kültürü</text>',

        '<rect x="24" y="42" width="302" height="176" rx="10" class="g-ma g-ms" stroke-width="1.5"/>',
        '<text x="175" y="66" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">'
        'GELENEKSEL (BASILI) METİN</text>',
        '<line x1="42" y1="78" x2="308" y2="78" class="g-c" stroke-width="1"/>',
        '<text x="175" y="104" text-anchor="middle" font-size="12" class="g-y">'
        '• Bilgi kâğıt sayfalar üzerindedir.</text>',
        '<text x="175" y="128" text-anchor="middle" font-size="12" class="g-y">'
        '• Yazı ve durağan resimle sınırlıdır.</text>',
        '<text x="175" y="152" text-anchor="middle" font-size="12" class="g-y">'
        '• Çoğunlukla bireysel ve tek yönlü</text>',
        '<text x="175" y="172" text-anchor="middle" font-size="12" class="g-y">'
        'bilişsel bir okuma etkinliğidir.</text>',

        '<line x1="334" y1="130" x2="364" y2="130" class="g-c" stroke-width="2"/>',
        '<polygon points="372,130 362,125 362,135" class="g-y"/>',

        '<rect x="374" y="42" width="302" height="176" rx="10" class="g-ta g-ts" stroke-width="1.5"/>',
        '<text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">'
        'DİJİTAL VE ETKİLEŞİMLİ METİN</text>',
        '<line x1="392" y1="78" x2="658" y2="78" class="g-c" stroke-width="1"/>',
        '<text x="525" y="104" text-anchor="middle" font-size="12" class="g-y">'
        '• Bilgisayar, tablet ve telefonda sunulur.</text>',
        '<text x="525" y="128" text-anchor="middle" font-size="12" class="g-y">'
        '• Video, animasyon, film ve simge içerir.</text>',
        '<text x="525" y="152" text-anchor="middle" font-size="12" class="g-y">'
        '• Toplumla etkileşim ve paylaşım içeren</text>',
        '<text x="525" y="172" text-anchor="middle" font-size="12" class="g-y">'
        'sosyo-bilişsel bir etkinliktir.</text>',

        '<rect x="24" y="232" width="652" height="40" rx="8" class="g-ya g-ys" stroke-width="1.5"/>',
        '<text x="350" y="257" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">'
        'İlkemiz: Okuma tutumunu geliştirmek için basılı ve dijital materyaller birlikte kullanılır.</text>',
    ]
    return svg(W, H, "".join(ic), "Basılı metinden dijital metne geçiş ve dijital okuma kültürü")


def gorsel_ipuclarindan_kelime():
    """1. Etkinlik: İpuçlarından hareketle metindeki kelimeleri bulma."""
    W, H = 700, 290
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'İpuçlarından Anahtar Sözcüğe Ulaşma ve TDK Sözlük Kontrolü</text>',
    ]
    satirlar = [
        (42, "ahlak bilimi  ·  ahlakî  ·  törel", "ETİK", "g-ma g-ms", "g-mf"),
        (102, "araç  ·  gereç  ·  belge", "MATERYAL", "g-ta g-ts", "g-tf"),
        (162, "canlandırmak  ·  film  ·  aktarmak", "ANİMASYON", "g-ya g-ys", "g-yf"),
        (222, "işaret  ·  sembol  ·  nesne", "SİMGE", "g-ma g-ms", "g-mf"),
    ]
    for y, ipucu, kelime, k_cls, y_cls in satirlar:
        ok_y = y + 24
        ic.extend([
            f'<rect x="24" y="{y}" width="386" height="48" rx="8" class="g-z g-c" stroke-width="1.2"/>',
            f'<text x="217" y="{y+29}" text-anchor="middle" font-size="13" class="g-y">{ipucu}</text>',

            f'<line x1="418" y1="{ok_y}" x2="458" y2="{ok_y}" class="g-c" stroke-width="2"/>',
            f'<polygon points="466,{ok_y} 456,{ok_y-5} 456,{ok_y+5}" class="g-y"/>',

            f'<rect x="474" y="{y}" width="202" height="48" rx="8" class="{k_cls}" stroke-width="1.5"/>',
            f'<text x="575" y="{y+30}" text-anchor="middle" font-size="14" font-weight="700" class="{y_cls}">{kelime}</text>',
        ])
    return svg(W, H, "".join(ic), "İpuçlarından anahtar sözcüğe ulaşma: etik, materyal, animasyon, simge")


def gorsel_makale_olcutleri():
    """3. Etkinlik: Metin türünü (makale) ayırt etme ölçütleri."""
    W, H = 700, 310
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Metin Türü Değerlendirme Tablosu: Makaleyi Ayırt Eden Özellikler</text>',
    ]
    olcutler = [
        (42, "1. Öne sürülen düşünce kanıtlanmaya çalışılmıştır.", "VAR (X)", "g-ya g-ys", "g-yf"),
        (86, "2. Olaya dayalı kurmaca bir anlatım yapılmıştır.", "YOK (—)", "g-z g-c", "g-s"),
        (130, "3. Doğrulanabilir, nesnel ifadeler kullanılmıştır.", "VAR (X)", "g-ya g-ys", "g-yf"),
        (174, "4. Belli bir makam, kurum veya kişiye yazılmıştır.", "YOK (—)", "g-z g-c", "g-s"),
        (218, "5. İçerik, bilimsel bir yaklaşımla ele alınmıştır.", "VAR (X)", "g-ya g-ys", "g-yf"),
    ]
    for y, metin, durum, k_cls, y_cls in olcutler:
        ic.extend([
            f'<rect x="24" y="{y}" width="500" height="36" rx="7" class="g-z g-c" stroke-width="1.2"/>',
            f'<text x="42" y="{y+23}" text-anchor="start" font-size="12" class="g-y">{metin}</text>',
            f'<rect x="536" y="{y}" width="140" height="36" rx="7" class="{k_cls}" stroke-width="1.5"/>',
            f'<text x="606" y="{y+23}" text-anchor="middle" font-size="12" font-weight="700" class="{y_cls}">{durum}</text>',
        ])
    ic.extend([
        '<rect x="24" y="264" width="652" height="36" rx="8" class="g-ma g-ms" stroke-width="1.5"/>',
        '<text x="350" y="287" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">'
        'Sonuç: 1, 3 ve 5. ölçütleri birlikte sağlayan bilgilendirici metin türü MAKALEDİR.</text>',
    ])
    return svg(W, H, "".join(ic), "Metin türü değerlendirme tablosu: makalenin özellikleri")


def gorsel_fiilimsiler_uygulama():
    """6. Etkinlik: Cümlede fiilimsileri bulma ve görevlerine göre ayırma."""
    W, H = 700, 286
    ic = [
        '<text x="350" y="25" text-anchor="middle" font-size="14" font-weight="700" class="g-y">'
        'Cümlede Fiilimsileri Bulma: Üç Tür ve Kitaptaki Örnekleri</text>',
    ]
    gruplar = [
        (
            42, "1. İSİM-FİİL (Eylem Adı)",
            "• “Türkçemizi zenginleştirmek hepimizin görevidir.”",
            "• “Farklı yazarlara ait eserler okuması onu zenginleştiriyor.”",
            "g-ma g-ms", "g-mf",
        ),
        (
            122, "2. SIFAT-FİİL (İsmi Niteleyen)",
            "• “Abone olunan dergiler okuyucuların adresine gönderilir.”",
            "• “Her kitap, ufkumuzu genişletecek bir fırsattır.”",
            "g-ta g-ts", "g-tf",
        ),
        (
            202, "3. ZARF-FİİL (Durum ve Zaman Belirten)",
            "• “Elindeki kitabı bana göstererek bir şeyler söylüyordu.” (Nasıl?)",
            "• “Kütüphaneye girdiğinde kendini çok mutlu hissediyor.” (Ne zaman?)",
            "g-ya g-ys", "g-yf",
        ),
    ]
    for y, baslik, o1, o2, k_cls, y_cls in gruplar:
        ic.extend([
            f'<rect x="24" y="{y}" width="652" height="68" rx="9" class="{k_cls}" stroke-width="1.5"/>',
            f'<text x="44" y="{y+22}" text-anchor="start" font-size="13" font-weight="700" class="{y_cls}">{baslik}</text>',
            f'<text x="44" y="{y+42}" text-anchor="start" font-size="12" class="g-y">{o1}</text>',
            f'<text x="44" y="{y+60}" text-anchor="start" font-size="12" class="g-y">{o2}</text>',
        ])
    return svg(W, H, "".join(ic), "Cümlede fiilimsileri bulma: isim-fiil, sıfat-fiil ve zarf-fiil örnekleri")


GORSELLER = {
    "Basılı Sayfadan Ekrana: Dijital Okuma Kültürü ve Dijital Okuryazarlık": gorsel_dijital_okuma,
    "İpuçlarından Kelimeye Ulaşma ve Sözlükten Doğrulama": gorsel_ipuclarindan_kelime,
    "Metin Türünü Ayırt Etme: Makalenin Özellikleri": gorsel_makale_olcutleri,
    "Cümlede Fiilimsileri Bulma ve Görevlerini Çözümleme": gorsel_fiilimsiler_uygulama,
}


def uygula(o):
    for b in o.get("bolumler", []):
        fn = GORSELLER.get(b.get("baslik"))
        if fn:
            b["gorsel"] = fn()
