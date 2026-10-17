from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'HİTABET VE MESLEKİ UYGULAMA: DİN HİZMETLERİNDE ETKİLİ HİTABET', R['koyu']))

    # Sol panel: Hitabetin Unsurları, Ses ve Beden Dili
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. DİNÎ HİTABETTE SES, DİKSİYON VE BEDEN DİLİ', R['koyu'], 11.2, 'bold', 'middle'))

    sol = [
        (100, 'Hitabet ve Dinî Hitabet Tanımı', 'İkna edici güzel söz söyleme sanatı; dini hakikatleri hikmet ve güzel öğütle gönüllere ulaştırma.'),
        (150, 'Diksiyon, Boğumlama ve Nefes Kontrolü', 'Diyafram nefesi kullanma, harfleri (özellikle Arapça ayet/hadisleri) mahrecine uygun telaffuz etme.'),
        (200, 'Vurgu, Tonlama ve Konuşma Hızı', 'Tekdüze (monoton) sesten kaçınma; dua, müjde ve uyarı bölümlerine uygun ses tonu ayarlama.'),
        (250, 'Beden Dili: Göz Teması, Jest ve Mimikler', 'Kürsüde/minberde tüm cemaati kucaklayan göz teması, doğal el-kol (jest) ve yüz (mimik) uyumu.'),
        (300, 'Dış Görünüş ve Temsil (Vakar ve Tevazu)', 'Temiz ve sünnete uygun kıyafet (sarık/cübbe düzeni), vakur duruş ve samimi tebessüm.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.0, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Muhatap Analizi, Hazırlık Aşamaları ve Nebevî Üslup
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. MUHATAP ANALİZİ VE NEBEVÎ HİTABET İLKELERİ', '#92400e', 11.2, 'bold', 'middle'))

    sag = [
        (100, 'Muhatap Kitlesini Tanıma (Müktezâ-yı Hâl)', 'Cemaatin yaş, eğitim, kültür ve güncel ihtiyaçlarına uygun konu ve dil düzeyi seçme.'),
        (150, 'Hitabet Planı: Giriş - Gelişme - Sonuç', 'Hamdele ve salvele ile giriş; sahih ayet/hadislerle gelişme; özet ve samimi duayla sonuç.'),
        (200, 'Nebevî Hitabet: Cevâmiu’l-Kelim ve İtidâl', 'Az sözle derin anlam ifade etme; sözü uzatıp cemaati usandırmama (“Namazı uzun, hutbeyi kısa tutma”).'),
        (250, 'Tebşîr (Müjdeleme) ve Teysîr (Kolaylaştırma)', '“Kolaylaştırınız, zorlaştırmayınız; müjdeleyiniz, nefret ettirmeyiniz!” (Buhârî, İlim, 11).'),
        (300, 'Temsil Gücü ve İhlas (Kalpten Kalbe Yol)', 'Söylediğini önce kendi hayatında yaşama (Saf, 2-3); şöhret ve riyadan uzak ihlaslı üslup.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.0, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'HZ. PEYGAMBER’İN HUTBE SÜNNETİ: “Kişinin namazını uzun, hutbesini kısa tutması onun fıkhından (dini anlayış ve ferasetinden)dir!” (Müslim, Cum’a, 47)', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Dinî hitabette uydurma (mevzû) rivayetlerden ve kişileri hedef alan kırıcı üsluptan sakınılmalı; “Mâ bâlü akvâmin (Bazı kimselere ne oluyor ki...)” metodu izlenmelidir.', '#334155', 9.6, 'normal', 'middle'))

    kaydet('11-hitabet-ve-mesleki-uygulama-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
