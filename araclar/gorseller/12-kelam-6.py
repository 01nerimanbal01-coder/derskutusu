from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kelam')
    ic = []
    ic.append(P.baslik(400, 32, 'KELAM İLMİNİN DİĞER İSLAMİ İLİMLERLE İLİŞKİSİ', R['koyu']))

    # Merkezdeki Küllî İlim: KELAM ("Eşrefü’l-Ulûm" / Usûlü’d-Dîn)
    ic.append(P.kutu(230, 56, 340, 68, R['acik'], R['koyu']))
    ic.append(P.metin(400, 80, 'MERKEZÎ (KÜLLÎ) İLİM: KELAM (USÛLÜ’D-DÎN)', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(400, 100, 'İslam’ın inanç esaslarını (Akaid) aklî ve naklî delillerle', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(400, 116, 'ispat ederek diğer tüm İslami ilimlere temel oluşturur.', R['koyu'], 10, 'bold', 'middle'))

    # Dört Köşede Kelam ile İlişkili İslami İlimler
    kutular = [
        (20, 140, 365, 96, '#ffffff', R['orta'],
         '1. KELAM — TEFSİR İLİŞKİSİ',
         '• Kelam, Allah’ın kelam sıfatını ve vahyin imkânını ispatlar.',
         '• Tefsir, kelamcılara naklî delil (ayetlerin anlamını) sunar;',
         '  kelam ilkeleri de müteşâbih ayetlerin te’viline rehberlik eder.'),
        (400, 140, 380, 96, '#ffffff', R['orta'],
         '2. KELAM — HADİS İLİŞKİSİ',
         '• Kelam, nübüvveti (Hz. Peygamber’in peygamberliğini) ispatlar.',
         '• Hadis ilmi sahih/mütevatir rivayetleri tespit ederek kelama',
         '  malzeme verir; kelam ise hadisleri inanç ilkeleriyle yorumlar.'),
        (20, 248, 365, 96, '#eff6ff', '#2563eb',
         '3. KELAM — FIKIH (USÛL-İ FIKIH) İLİŞKİSİ',
         '• Kelam "Asıl" (Usûlü’d-Dîn), Fıkıh ise "Fer’" (Fürûu’d-Dîn)dir.',
         '• Şâri (Hüküm Koyucu Allah) ve mükellef (akıl-irade) kelamda',
         '  ispatlanmadan fıkhî hükümlerin bağlayıcılığı kurulamaz!'),
        (400, 248, 380, 96, '#fef3c7', '#d97706',
         '4. KELAM — TASAVVUF / AHLAK İLİŞKİSİ',
         '• Kelam inancı akıl ve delille (tahkiki iman) temellendirir;',
         '  Tasavvuf ise bu inancı kalbî tecrübe ve ihlasla yaşatır.',
         '• Sahih tasavvuf, kelamın tevhid ve tenzih ölçülerine tabidir.'),
    ]
    for x, y, w, h, bg, kenar, b, s1, s2, s3 in kutular:
        ic.append(P.kutu(x, y, w, h, bg, kenar))
        ic.append(P.metin(x + w // 2, y + 20, b, R['koyu'], 12, 'bold', 'middle'))
        ic.append(P.metin(x + w // 2, y + 42, s1, '#334155', 10, 'normal', 'middle'))
        ic.append(P.metin(x + w // 2, y + 60, s2, '#334155', 10, 'normal', 'middle'))
        ic.append(P.metin(x + w // 2, y + 78, s3, '#1e40af', 10, 'bold', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 358, 760, 50, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 378, 'GAZZÂLÎ VE TAFTÂZÂNÎ’YE GÖRE: Kelam "Küllî (Tümel) İlim"dir; Tefsir, Hadis ve Fıkıh ise "Cüz’î (Tikel) İlimler"dir.', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 396, 'İmam-ı Âzam Ebû Hanîfe: İnanç esaslarını inceleyen Kelam’a "el-Fıkhu’l-Ekber" (En Büyük Fıkıh) adını vermiştir.', '#334155', 11, 'normal', 'middle'))

    kaydet('12-kelam-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
