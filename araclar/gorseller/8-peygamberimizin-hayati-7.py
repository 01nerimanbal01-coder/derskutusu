from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'MÜŞRİKLERLE MÜCADELE: BEDİR (624), UHUD (625) VE HİNDEK (627)', R['koyu']))

    # Sol panel: Bedir Savaşı (624) ve Uhud Savaşı (625)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. BEDİR (624) VE UHUD (625) SAVAŞLARI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Bedir Savaşı (624) — Müslümanların İLK ZAFERİ!', '305 Müslüman vs. 1000 Müşrik -> Hubâb bin Münzir’in görüşüyle kuyular tutuldu.'),
        (150, 'Bedir Esirlerine Uygulanan Eğitim Politikası', 'Okuma yazma bilen esirler 10 Müslümana okuma yazma öğreterek özgür kaldı!'),
        (200, 'Uhud Savaşı (625) — İstişare ve Okçular Tepesi', 'Peygamberimiz şehir savunması istese de gençlerin görüşüne (istişare) uydu.'),
        (250, 'Ayneyn (Okçular) Tepesi ve İtaatin Önemi', '50 okçunun "Savaş bitti" diyerek tepeyi terk etmesiyle Halid bin Velid arkadan saldırdı.'),
        (300, 'Hz. Hamza’nın Şehadeti ve Peygamberimizin Sabrı', 'Amcası Hz. Hamza şehit oldu; Peygamberimiz yaralansa da sabırla ordusunu topladı.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Hendek Savaşı (627) ve Savaş Ahlakı İlkeleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HENDEK SAVAŞI (627) VE SAVAŞ AHLAKI', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'Hendek (Ahzâb) Savaşı (627) — Son Savunma Savaşı!', 'Müşriklerin 10.000 kişilik birleşik ordusu Medine’yi kuşattı.'),
        (150, 'Selmân-ı Fârisî’nin (r.a.) Hendek Fikri (İstişare)', 'Medine’nin açık olan kuzey cephesine derin hendekler kazıldı.'),
        (200, 'Hendek Savaşı’nın Sonucu', 'Şiddetli fırtına ile müşrikler çekildi; müşriklerin saldırı gücü kırıldı!'),
        (250, 'Peygamberimizin Savaş Ahlakı ve Merhameti', 'Kadınlara, çocuklara, yaşlılara, din adamlarına ve ağaçlara dokunulmaz!'),
        (300, 'Çıkarılacak Üç Temel İlke', '1) İstişare (Danışma)  2) Peygamberin emrine itaat  3) Sabır ve Tevekkül.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'SAHABİ ÖNERİLERİ (İSTİŞARE): Bedir’de Hubâb bin Münzir (su kuyuları) | Hendek’te Selmân-ı Fârisî (hendek kazılması)!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Uhud Savaşı’nda Ayneyn (Okçular) Tepesi olayı, Peygamberimizin sözüne ve emrine itaatin ne kadar hayati olduğunu göstermiştir.', '#334155', 10, 'normal', 'middle'))

    kaydet('8-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
