from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('biyoloji')
    ic = []
    ic.append(P.baslik(400, 32, 'NÜKLEİK ASİTLERİN KEŞFİ VE GENETİK MATERYALİN ORGANİZASYONU', R['koyu']))

    # Sol panel: Griffith ve Avery Deneyleri (Kapsüllü / Kapsülsüz S. pneumoniae)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. NÜKLEİK ASİTLERİN KEŞİF SÜRECİ', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.kutu(35, 95, 335, 48, '#ffffff', R['orta']))
    ic.append(P.metin(202, 113, 'F. Miescher (1869): Akyuvar çekirdeğinde', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(202, 131, 'asidik yapılı "Nüklein" (DNA/RNA) molekülünü keşfetti.', '#334155', 11, 'normal', 'middle'))

    ic.append(P.kutu(35, 152, 335, 112, '#ffffff', R['orta']))
    ic.append(P.metin(202, 170, 'Griffith (1928) - Transformasyon Deneyi:', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(202, 188, '• Canlı Kapsüllü (S) → Fare Ölür | Kapsülsüz (R) → Yaşar', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(202, 206, '• Isıtılmış Ölü Kapsüllü (S) → Fare Yaşar', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(202, 224, '• Ölü Kapsüllü (S) + Canlı Kapsülsüz (R) → Fare ÖLÜR!', '#b91c1c', 11, 'bold', 'middle'))
    ic.append(P.metin(202, 245, '(Kalıtsal madde R bakterisine geçip onu S yapmıştır)', R['koyu'], 10, 'normal', 'middle'))

    ic.append(P.kutu(35, 273, 335, 58, '#fef3c7', '#d97706'))
    ic.append(P.metin(202, 292, 'Avery, MacLeod, McCarty (1944) & Hershey-Chase (1952):', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(202, 312, 'Kalıtsal bilgiyi taşıyan molekülün DNA olduğunu kanıtladılar!', '#334155', 10, 'bold', 'middle'))

    # Sağ panel: Genetik Materyalin Küçükten Büyüğe Organizasyonu
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. GENETİK MATERYALİN ORGANİZASYONU', '#1e40af', 13, 'bold', 'middle'))
    ic.append(P.metin(590, 100, '(Basitten Karmaşığa / Küçükten Büyüğe Sıralama)', '#334155', 11, 'bold', 'middle'))

    basamaklar = [
        (115, '1. Organik Baz + Şeker → Nükleozit'),
        (153, '2. Nükleozit + Fosfat → NÜKLEOTİT (Yapı Birimi)'),
        (191, '3. Üçlü Nükleotit Dizisi → KOD (Üçlü Şifre)'),
        (229, '4. Anlamlı DNA Bölgesi → GEN (Kalıtsal Birim)'),
        (267, '5. Genlerin Bütünü → DNA Molekülü'),
        (305, '6. DNA + Histon Proteini → KROMATİN / KROMOZOM'),
    ]
    for y, yazi in basamaklar:
        ic.append(P.kutu(420, y, 340, 30, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 19, yazi, '#1e40af', 11, 'bold', 'middle'))

    # Alt bant: Özet Kural
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KÜÇÜKTEN BÜYÜĞE: Baz < Nükleozit < Nükleotit < Kod < Gen < DNA < Kromozom < Çekirdek < Hücre', R['koyu'], 12, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Sadece DNAaz enzimi eklendiğinde transformasyon durur → Kalıtım materyali protein değil DNA’dır!', '#334155', 11, 'normal', 'middle'))

    kaydet('12-biyoloji-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic