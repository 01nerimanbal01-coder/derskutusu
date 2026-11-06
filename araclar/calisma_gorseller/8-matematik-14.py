"""8-matematik-14 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma; K155/K208 uyumlu)."""

GORSELLER = {
    0: '<svg viewBox="0 0 350 118" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Olasılık temel kuralları kartları">'
       '<rect x="4" y="3" width="167" height="52" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/>'
       '<text x="87.5" y="21.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Eş Olasılıklı Olay</text>'
       '<text x="87.5" y="41.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">n çıktı → Eşit şans</text>'
       '<rect x="179" y="3" width="167" height="52" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/>'
       '<text x="262.5" y="21.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Değer Aralığı</text>'
       '<text x="262.5" y="41.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">0 (İmkânsız) .. 1 (Kesin)</text>'
       '<rect x="4" y="61" width="167" height="52" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/>'
       '<text x="87.5" y="79.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Tümleyen Kuralı</text>'
       '<text x="87.5" y="99.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">P(A) + P(A’) = 1 tam</text>'
       '<rect x="179" y="61" width="167" height="52" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/>'
       '<text x="262.5" y="79.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Olasılık Değeri</text>'
       '<text x="262.5" y="99.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">İstenilen ÷ Tüm durum</text></svg>',
    1: '<svg viewBox="0 0 350 86" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Torbadaki renkli toplar dağılımı">'
       '<rect x="4" y="3" width="342" height="80" rx="5" fill="#f8fafc" stroke="#2451d6" stroke-width="0.75"/>'
       '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Torbadaki Özdeş Toplar (Toplam = 12 Adet)</text>'
       '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d63a3a">Kırmızı Top: ● ● ● ● (4 adet)</text>'
       '<text x="12.0" y="58.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Mavi Top: ● ● ● ● ● (5 adet)</text>'
       '<text x="12.0" y="77.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Sarı Top: ● ● ● (3 adet)</text></svg>',
    2: '<svg viewBox="0 0 350 66" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hilesiz zar deneyi olası durumları">'
       '<rect x="4" y="3" width="342" height="60" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/>'
       '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Hilesiz Zar Deneyi (6 Eş Olasılıklı Yüz)</text>'
       '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Tüm Olası Çıktılar: { 1 , 2 , 3 , 4 , 5 , 6 }</text>'
       '<text x="12.0" y="57.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#475569">Örnek Uzay Eleman Sayısı: n(E) = 6 durum</text></svg>',
    5: '<svg viewBox="0 0 350 66" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MATEMATİK kelimesi harf kartları">'
       '<rect x="4" y="3" width="342" height="60" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/>'
       '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Özdeş Harf Kartları (Toplam 9 Kart)</text>'
       '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">[M] · [A] · [T] · [E] · [M] · [A] · [T] · [İ] · [K]</text>'
       '<text x="12.0" y="57.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#475569">M: 2 kart · A: 2 kart · T: 2 kart · E, İ, K: 1’er kart</text></svg>',
    6: '<svg viewBox="0 0 350 86" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kurs dağılımı daire grafiği merkez açıları">'
       '<rect x="4" y="3" width="342" height="80" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/>'
       '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Kurs Dağılımı Daire Grafiği (Tam Açı = 360°)</text>'
       '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. Dilim — Robotik Kursu: Merkez açı = 150°</text>'
       '<text x="12.0" y="58.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">2. Dilim — Satranç Kursu: Merkez açı = 120°</text>'
       '<text x="12.0" y="77.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">3. Dilim — Kodlama Kursu: Merkez açı = 90°</text></svg>',
    7: '<svg viewBox="0 0 350 66" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Okçuluk hedefi vurma ve vuramama tümleyen olayı">'
       '<rect x="4" y="3" width="342" height="60" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/>'
       '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Tümleyen Olay Analizi: P(A) + P(A’) = 1 Tam</text>'
       '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">A Olayı: Hedefi vurma (10 eş bölmeden 7’si)</text>'
       '<text x="12.0" y="57.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#475569">A’ Olayı: Hedefi vuramama olasılığı = ?</text></svg>',
    8: '<svg viewBox="0 0 350 116" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Basit olay olasılığı hesaplama adımları">'
       '<rect x="4" y="3" width="342" height="25" rx="5" fill="#f8fafc" stroke="#2451d6" stroke-width="0.75"/>'
       '<text x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. Adım: Tüm olası durum sayısını bul → Payda</text>'
       '<rect x="4" y="31" width="342" height="25" rx="5" fill="#f8fafc" stroke="#12a150" stroke-width="0.75"/>'
       '<text x="11.0" y="47.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">2. Adım: İstenilen çıktı sayısını bul → Pay</text>'
       '<rect x="4" y="59" width="342" height="25" rx="5" fill="#f8fafc" stroke="#d97706" stroke-width="0.75"/>'
       '<text x="11.0" y="75.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">3. Adım: İstenilen ve tüm durum oranını kur</text>'
       '<rect x="4" y="87" width="342" height="25" rx="5" fill="#f8fafc" stroke="#7c3aed" stroke-width="0.75"/>'
       '<text x="11.0" y="103.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">4. Adım: Kesri EBOB ile en sade hâline getir</text></svg>',
    11: '<svg viewBox="0 0 350 66" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="1’den 20’ye kadar numaralı kartlar">'
        '<rect x="4" y="3" width="342" height="60" rx="5" fill="#e0f4f8" stroke="#0e8fa8" stroke-width="0.75"/>'
        '<text x="12.0" y="20.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0e8fa8">Numaralı Kart Çekilişi (1’den 20’ye Kadar)</text>'
        '<text x="12.0" y="39.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Kartlar: [1] , [2] , [3] , [4] , ... , [19] , [20]</text>'
        '<text x="12.0" y="57.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#475569">Toplam 20 özdeş kart · İstenilen: Tam kare sayı</text></svg>',
}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
