# -*- coding: utf-8 -*-
"""11. Sınıf Türk Dili ve Edebiyatı - 3. Hafta Görselleri (Karagöz, Mektup ve Dilekçe)"""


def _svg(g, y, icerik):
    return (
        f'<svg viewBox="0 0 {g} {y}" width="100%" xmlns="http://www.w3.org/2000/svg" '
        f'style="max-width:{g}px;display:block;margin:14px auto;background:#fff;'
        f'border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _baslik(g, metin, renk="#1e293b"):
    return (
        f'<rect x="0" y="0" width="{g}" height="38" rx="10" fill="{renk}"/>'
        f'<rect x="0" y="20" width="{g}" height="18" fill="{renk}"/>'
        f'<text x="{g//2}" y="25" font-family="Arial,sans-serif" font-size="14" '
        f'font-weight="bold" fill="#ffffff" text-anchor="middle">{metin}</text>'
    )


def _kutu(x, y, g, yk, r_ark, r_ken, baslik, satirlar, r_bas="#0f172a"):
    ic = f'<rect x="{x}" y="{y}" width="{g}" height="{yk}" rx="8" fill="{r_ark}" stroke="{r_ken}" stroke-width="1.8"/>'
    ic += f'<text x="{x+g//2}" y="{y+22}" font-family="Arial,sans-serif" font-size="12.5" font-weight="bold" fill="{r_bas}" text-anchor="middle">{baslik}</text>'
    ic += f'<line x1="{x+10}" y1="{y+30}" x2="{x+g-10}" y2="{y+30}" stroke="{r_ken}" stroke-width="1"/>'
    for i, s in enumerate(satirlar):
        ic += f'<text x="{x+g//2}" y="{y+48+i*18}" font-family="Arial,sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s}</text>'
    return ic


def gorsel_1():
    """Karagöz Gölge Oyununun Yapısal Bölümleri (Mukaddime, Muhavere, Fasıl, Bitiş)"""
    g, y = 740, 260
    s = _baslik(g, "KARAGÖZ GÖLGE OYUNUNUN DÖRT TEMEL BÖLÜMÜ", "#b91c1c")
    s += _kutu(16, 52, 168, 190, "#fef2f2", "#ef4444", "1. MUKADDİME (Giriş)", [
        "• Kamış düdük (nâreke) çalınır.",
        "• Göstermelik perdeden",
        "  kaldırılır.",
        "• Hacivat 'Semai' okuyarak",
        "  perdeye gelir ve",
        "  'Perde Gazeli'ni söyler.",
        "• 'Yâr bana bir eğlence!'"
    ], "#991b1b")
    s += _kutu(196, 52, 168, 190, "#fff7ed", "#f97316", "2. MUHAVERE (Söyleşme)", [
        "• Karagöz ile Hacivat'ın",
        "  karşılıklı atışma bölümüdür.",
        "• Asıl olaydan bağımsızdır.",
        "• Yanlış anlamalara (alaka",
        "  ve tekerlemelere) dayalı",
        "  dil komiği ön plandadır."
    ], "#9a3412")
    s += _kutu(376, 52, 168, 190, "#fefce8", "#eab308", "3. FASIL (Asıl Oyun)", [
        "• Oyunun adını aldığı asıl",
        "  konunun işlendiği bölümdür.",
        "• Yardımcı tipler (Çelebi,",
        "  Zenne, Tuzsuz Deli Bekir,",
        "  Beberuhi, Tiryaki vb.)",
        "  bu bölümde perdeye çıkar."
    ], "#854d0e")
    s += _kutu(556, 52, 168, 190, "#f0fdf4", "#22c55e", "4. BİTİŞ", [
        "• Oyunun en kısa bölümüdür.",
        "• Karagöz: 'Yıktın perdeyi",
        "  eyledin viran...' der.",
        "• Hacivat: 'Her ne kadar",
        "  sürçülisan ettikse affola!'",
        "  diyerek oyunu kapatır."
    ], "#166534")
    return _svg(g, y, s)


def gorsel_2():
    """Karagöz ile Hacivat Tiplerinin Karşılaştırması"""
    g, y = 740, 260
    s = _baslik(g, "BAŞAT TİPLERİN KARŞILAŞTIRMASI: KARAGÖZ VE HACİVAT", "#0f766e")
    s += _kutu(20, 52, 340, 192, "#fef2f2", "#ef4444", "KARAGÖZ (Halkın Temsilcisi)", [
        "• Eğitim Durumu: Okumamış, halk kültürüyle yetişmiş.",
        "• Dil ve Üslup: Sade, açık, halk Türkçesiyle konuşur;",
        "  Hacivat'ın yabancı kelimelerini ters/yanlış anlar.",
        "• Karakteri: Dobra, saf, patavatsız, hazırcevap, samimi.",
        "• Geçim Durumu: Sürekli işsizdir; Hacivat'ın bulduğu",
        "  geçici işlerde çalışır ve komik durumlara düşer."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 192, "#eff6ff", "#3b82f6", "HACİVAT (Aydın / Yarı Aydın Temsilcisi)", [
        "• Eğitim Durumu: Medrese tahsili görmüş, görgü kurallarını bilir.",
        "• Dil ve Üslup: Arapça-Farsça tamlamalarla dolu,",
        "  süslü, seci'li (iç uyaklı) ve sanatlı bir dille konuşur.",
        "• Karakteri: İçten pazarlıklı, arabulucu, nabza göre şerbet verir.",
        "• Geçim Durumu: Çevresi geniştir; Karagöz'e iş bulur",
        "  ve bundan komisyon / pay almaya çalışır."
    ], "#1e40af")
    return _svg(g, y, s)


def gorsel_3():
    """Mektup Türleri ve Yapısal Unsurları"""
    g, y = 740, 260
    s = _baslik(g, "İLETİŞİM ARACI OLARAK MEKTUP TÜRLERİ VE BİÇİMSEL UNSURLARI", "#4338ca")
    s += _kutu(20, 52, 340, 192, "#eef2ff", "#6366f1", "MEKTUP TÜRLERİ (Amacına Göre)", [
        "1. Özel Mektup: Akraba ve dostlar arasında samimi dille.",
        "2. Edebî (Sanat) Mektup: Sanatçıların sanat/edebiyat",
        "   görüşlerini estetik bir dille tartıştığı mektuplar.",
        "3. Resmî ve İş Mektupları: Kurumlar veya ticari",
        "   işletmeler arasında ciddi ve nesnel dille yazılır.",
        "4. Açık Mektup: Gazete/dergi yoluyla kamuoyuna seslenir."
    ], "#3730a3")
    s += _kutu(380, 52, 340, 192, "#f8fafc", "#64748b", "MEKTUBUN BİÇİMSEL (YAPISAL) PLANI", [
        "• Sağ Üst Köşe: YER ve TARİH (Örn: Ankara, 30.09.2026)",
        "• Satır Başı: HİTAP SÖZÜ (Sevgili Dostum, / Sayın Müdürüm,)",
        "• Gövde: GİRİŞ (yazılış amacı), GELİŞME (asıl mesaj)",
        "  ve SONUÇ (iyi dilek ve selam ifadeleri).",
        "• Sağ Alt Köşe: AD - SOYAD ve İMZA",
        "• Sol Alt Köşe: Göndericinin ADRESİ"
    ], "#334155")
    return _svg(g, y, s)


def gorsel_4():
    """Standart Dilekçe Şeması ve Yazım Kuralları"""
    g, y = 740, 275
    s = _baslik(g, "RESMÎ İLETİŞİM METNİ: STANDART DİLEKÇE YAZIM ŞEMASI", "#1e293b")
    # Dilekçe kağıdı simülasyonu
    s += '<rect x="140" y="48" width="460" height="214" rx="6" fill="#ffffff" stroke="#475569" stroke-width="2"/>'
    s += '<text x="370" y="72" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">... ANADOLU LİSESİ MÜDÜRLÜĞÜNE</text>'
    s += '<text x="560" y="90" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="end">ÇANKAYA / ANKARA</text>'
    s += '<text x="165" y="116" font-family="Arial,sans-serif" font-size="11" fill="#1e293b">Okulunuz 11/A sınıfı 412 numaralı öğrencisiyim. ... tarihinde yapılan</text>'
    s += '<text x="165" y="134" font-family="Arial,sans-serif" font-size="11" fill="#1e293b">Türk Dili ve Edebiyatı sınav kağıdımın yeniden incelenmesini istiyorum.</text>'
    s += '<text x="165" y="156" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">Gereğini bilgilerinize saygılarımla arz ederim.</text>'
    s += '<text x="530" y="176" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">30/09/2026</text>'
    s += '<text x="530" y="194" font-family="Arial,sans-serif" font-size="11" font-style="italic" fill="#1d4ed8" text-anchor="middle">[İmza]</text>'
    s += '<text x="530" y="212" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Adı SOYADI</text>'
    s += '<text x="165" y="196" font-family="Arial,sans-serif" font-size="10.5" font-weight="bold" fill="#15803d">ADRES:</text>'
    s += '<text x="165" y="212" font-family="Arial,sans-serif" font-size="10.5" fill="#334155">Cumhuriyet Mah. ... Sok. No: 5</text>'
    s += '<text x="165" y="228" font-family="Arial,sans-serif" font-size="10.5" font-weight="bold" fill="#15803d">EK: 1 Adet Belge  |  TEL: 05xx...</text>'
    return _svg(g, y, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for k, sv in GORSELLER.items():
        idx = int(k[1:]) - 1
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = sv
    return v
