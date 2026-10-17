from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kimya')
    ic = []
    ic.append(P.baslik(400, 32, 'ATOM ORBİTALLERİ VE ELEKTRON DİZİLİMİ KURALLARI', R['koyu']))

    # Sol panel: Elektron Dizilimi Kuralları (Aufbau, Pauli, Hund)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TEMEL ELEKTRON DİZİLİM İLKELERİ', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Aufbau (İnşa) Kuralı — Düşük Enerjiden Yükseğe', 'Elektronlar önce en düşük enerjili orbitale yerleşir: 1s 2s 2p 3s 3p 4s 3d...'),
        (150, 'Madelung-Kletchkowski (n + ℓ) Enerji Sıralaması', 'n+ℓ değeri küçük olanın enerjisi düşüktür; eşitse n’si küçük olan düşüktür.'),
        (200, 'Pauli Dışlama İlkesi (En Fazla 2 Elektron)', 'Bir orbitalde zıt spinli (↑↓) en fazla 2 elektron bulunabilir.'),
        (250, 'Hund Kuralı (Eş Enerjili Orbitallere Yerleşim)', 'Elektronlar eş enerjili orbitallere önce tek tek aynı yönlü (↑ ↑ ↑), sonra zıt yerleşir.'),
        (300, 'Orbital Kapasiteleri (s, p, d, f)', 's: 1 orb. (2 e⁻) | p: 3 orb. (6 e⁻) | d: 5 orb. (10 e⁻) | f: 7 orb. (14 e⁻).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Küresel Simetri, Değerlik Elektronu ve İyonlar
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KÜRESEL SİMETRİ, DEĞERLİK e⁻ VE İYONLAR', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Temel Hâl ve Uyarılmış Hâl Ayrımı', 'Elektron dışarıdan enerji alıp üst orbitale çıkarsa atom uyarılmış (kararsız) olur.'),
        (150, 'Küresel Simetri (Yarı Dolu / Tam Dolu Kararlılık)', 'Son orbitalin s¹, s², p³, p⁶, d⁵, d¹⁰ ile bitmesi atomu ekstra kararlı yapar.'),
        (200, '₂₄Cr ve ₂₉Cu Özel Küresel Simetri Dizilimi!', '₂₄Cr: [Ar] 4s¹ 3d⁵ (4s² 3d⁴ değil!)  |  ₂₉Cu: [Ar] 4s¹ 3d¹⁰ (4s² 3d⁹ değil!).'),
        (250, 'İyonlarda Elektron Dizilimi ve İzoelektroniklik', 'Katyonlarda (n > 20) elektron önce en dış katmandan (4s’den, 3d’den önce!) kopar.'),
        (300, 'Soygaz Kısa Gösterimi ve Değerlik Elektronları', 'En yüksek baş kuantum (en dış katman) elektronları kimyasal bağı belirler.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ENERJİ SIRASI (AUFBAU): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶... (4s orbitali 3d’den önce dolar ve iyonlaşmada önce 4s’den elektron kopar!)', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '₂₄Cr ve ₂₉Cu atomlarının 4s¹ 3d⁵ ve 4s¹ 3d¹⁰ dizilimleri kendiliğinden gerçekleştiği için UYARILMIŞ HÂL DEĞİL, TEMEL HÂLDİR!', '#334155', 9.8, 'normal', 'middle'))

    kaydet('9-kimya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
