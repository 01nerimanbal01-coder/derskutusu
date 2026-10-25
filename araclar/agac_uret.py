#!/usr/bin/env python3
"""Öğrenci ders ağacı: yıllık/günlük plandan hafta → ünite → konu.

Kaynak : public/veri/gunluk-planlar.json (plan ↔ sınıf/ders eşlemesi) ve public/veri/gunluk-plan/<plan>.json
Çıktı  : public/veri/agac/<sinif>-<ders>.json  {sinif, ders, plan, haftalar{no: {bas, ad}}, uniteler[{ad, konular[{kod, ad, haftalar[]}]}]}
         public/veri/agac/dizin.json           {"<sinif>-<ders>": {"unite": n, "konu": m}}
Bir haftada iki ünite ya da iki konu varsa (geçiş haftası) satırlara bölünür; konu yoksa hafta ünite adıyla anılır.
Türkçe planlarındaki "Metin: …" satırı konu adı olur; "İçerik çerçevesi", örnek cümle ve madde satırları atlanır.
Çalıştırma: python3 araclar/agac_uret.py   (plan dosyaları değişince; site sayfalarına dokunmaz)
"""
import datetime
import json
import re
from collections import Counter
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / 'public'
VERI = PUBLIC / 'veri'
CIKTI = VERI / 'agac'

KUCUK = {'ve', 'ile', 'veya', 'ya', 'da', 'de', 'ki', 'mi', 'için', 'gibi', 'and', 'or', 'of', 'the'}
KISALTMA = {'DNA', 'RNA', 'T.C.', 'TBMM', 'ABD', 'MEB', 'LGS', 'YKS', 'AB', 'BM', 'NATO', 'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'XI', 'XII', 'TV', 'ATP', 'AİHL', 'İHO'}
ATLA = re.compile(r'^(?:İçerik çerçevesi|Icerik cercevesi|[—–\-*•(“"])', re.I)
ON_EK = re.compile(r'^(?:Metin|Sub-?Themes?|Konu|Tema)\s*:\s*', re.I)
# Ünite sayılmayan plan satırları (okul temelli planlama, sosyal etkinlik, tatil ve sınav haftaları)
OZEL = re.compile(r'okul temelli|sosyal etkinlik|ara tatil|yarıyıl|yariyil|dönem sonu|sene sonu|bayram', re.I)
KOD = re.compile(r'^(?:[A-ZÇĞİÖŞÜ]{1,4}\.)?\d+(?:\.\d+)+\.?\s*')
DEVAM_SON = re.compile(r"(?:['’](?:in|ın|un|ün|nin|nın|nun|nün|e|a|ye|ya)|\b(?:ve|ile|veya|ile ilgili|Arasındaki|Dair|Yönelik|İçin|Olan))$", re.I)


def tr_kucuk(s):
    return s.replace('I', 'ı').replace('İ', 'i').lower()


def tr_buyuk_bas(s):
    return (s[:1].replace('i', 'İ').replace('ı', 'I').upper() + s[1:]) if s else s


def baslik_bicim(s, ingilizce=False):
    """BÜYÜK HARFLİ plan adlarını Türkçe başlık biçimine çevirir; karışık yazılmış adlara dokunmaz."""
    harfler = [c for c in s if c.isalpha()]
    if not harfler or sum(c.isupper() for c in harfler) / len(harfler) < 0.8:
        return s
    parcalar = re.split(r'(\s+|[-/(])', s)
    sonuc, ilk = [], True
    for p in parcalar:
        if not p or p.isspace() or p in '-/(':
            sonuc.append(p)
            continue
        if sonuc and ''.join(sonuc).rstrip().endswith(':'):             # "Destan: Ya İstiklal…"
            ilk = True
        cekirdek = p.strip('.,:;)')
        if sonuc and sonuc[-1] == '-' and len(cekirdek) == 1:      # "Kur'an-ı"
            sonuc.append(tr_kucuk(p))
            ilk = False
            continue
        if cekirdek.upper() in KISALTMA or re.fullmatch(r'[A-ZÇĞİÖŞÜ]\.(?:[A-ZÇĞİÖŞÜ0-9]+\.?)*', cekirdek) or re.fullmatch(r'[\d.]+', cekirdek):
            sonuc.append(p)
        else:
            k = p.lower() if ingilizce else tr_kucuk(p)
            kucuk = KUCUK | ({'in', 'on', 'at', 'to', 'a', 'an', 'for', 'with'} if ingilizce else set())
            if not ilk and cekirdek.lower() in kucuk:
                sonuc.append(k)
            else:
                sonuc.append(k[:1].upper() + k[1:] if ingilizce else tr_buyuk_bas(k))
        ilk = False
    return ''.join(sonuc)


def satirlar(deger):
    out = []
    for x in (deger or '').split('\n'):
        x = re.sub(r'[ \t]+', ' ', x).strip()
        if not x:
            continue
        x = re.sub(r'([a-zçğıöşü])([A-ZÇĞİÖŞÜ])', r'\1 \2', x)       # "SureÖğreniyorum" → "Sure Öğreniyorum"
        x = re.sub(r'(\d\.)([A-ZÇĞİÖŞÜa-zçğıöşü])', r'\1 \2', x)    # "8.4.6.Türkiye" → "8.4.6. Türkiye"
        out.append(x)
    return birlestir(out)


def birlestir(L):
    """Hücre içinde satır sonuna bölünmüş başlıkları birleştirir ("Dinin Mimarimize" + "Etkisi")."""
    out = []
    for x in L:
        if out:
            onceki = out[-1]
            if re.fullmatch(r'Bir (?:Sure|Dua) ?Öğreniyorum\s*:?', onceki, re.I) and not x.lower().startswith('bir '):
                out[-1] = f'{onceki.rstrip(" :")}: {x}'
                continue
            tek = len(x.split()) == 1 and len(onceki.split()) >= 2 and not re.match(r'^[\d(]', x)
            acik = onceki.count('(') > onceki.count(')') or onceki.count('[') > onceki.count(']')
            ek = re.match(r'^\w+(?:arak|erek|madan|meden|ılan|ilen|ulan|ülen)\b', x)
            if x[:1].islower() or DEVAM_SON.search(onceki) or tek or acik or ek or onceki.endswith(','):
                out[-1] = f'{onceki} {x}'
                continue
        out.append(x)
    return out


def unite_temiz(s, ingilizce=False):
    s = re.sub(r'(\S)\(', r'\1 (', s)                 # "NİCELİKLER(2)" → "NİCELİKLER (2)"
    s = KOD.sub('', s)                                   # "M.8.1. SAYILAR…" → "SAYILAR…"
    s = re.sub(r'^\d+\s*[.)]?\s*(?:ÜNİTE|TEMA|THEME|UNIT)\s*[:.\-]?\s*', '', s, flags=re.I)   # "1. ÜNİTE: …", "THEME 1: …" önce
    s = re.sub(r'^(?:ÜNİTE|TEMA|THEME|UNIT)\s*\d+\s*[:.\-]?\s*', '', s, flags=re.I)
    s = re.sub(r'^\d+\s*[.)]\s*|^\d+\s+(?=[A-ZÇĞİÖŞÜa-z])', '', s)   # "1. Allah İnancı", "2 Sports"
    return baslik_bicim(s.strip(' :*'), ingilizce)


def bol_egik(metin):
    """Parantez dışındaki boşluklu eğik çizgiden böler ("Konu A / Konu B"; "(Dinleme/ İzleme)" bölünmez)."""
    parca, derin, out = '', 0, []
    for i, c in enumerate(metin):
        derin += (c in '([') - (c in ')]')
        if c == '/' and derin <= 0 and (metin[i - 1:i].isspace() or metin[i + 1:i + 2].isspace()):
            out.append(parca)
            parca = ''
            continue
        parca += c
    return [x.strip() for x in out + [parca] if x.strip()]


YABANCI = {'Lıvıngston': 'Livingston'}


def konu_satirlari(deger, ders=''):
    deger = deger or ''
    if re.search(r'[\u0600-\u06FF]', deger):                            # Arapça satırlar konu adı olmaz
        deger = '\n'.join(x for x in deger.split('\n') if not re.search(r'[\u0600-\u06FF]', x))
    if '•' in deger:                                                     # beceri listesi (Edebiyat): ünite adı yeter
        return []
    duz = re.sub(r'\s+', ' ', deger)
    if len(bol_egik(duz)) > 1:                                           # "Konu A / Konu B": satır sonları sarma
        ham = [p for x in bol_egik(duz) for p in birlestir(satirlar(x))]
    else:
        ham = satirlar(deger)
    if any(re.match(r'^Metin\s*:', x, re.I) for x in ham):          # Türkçe: yalnız okuma metinleri konu olur
        ham = [x for x in ham if re.match(r'^Metin\s*:', x, re.I)]
    if ders == 'ingilizce':                                            # işlev satırları ve alt temalar; örnek cümle/kelime değil
        ham = [x for x in ham if re.match(r'^Sub-?Themes?\s*:', x, re.I) or re.match(r'^\(?[A-Z][a-z]+ing\b', x)]
    out = []
    for x in ham:
        if ATLA.match(x) and not x.startswith('('):
            continue
        if x.startswith('(') and x.endswith(')'):
            x = x[1:-1]
        x = ON_EK.sub('', x).strip(' :;*')
        if x.count('(') > x.count(')'):
            x += ')'
        x = KOD.sub('', x)
        x = re.sub(r'\s*İçerik çerçevesi\s*:.*$', '', x, flags=re.I).strip()
        if len(x) < 3:
            continue
        if len(x) > 90:                                      # İngilizce alt temalar gibi uzun satırlar
            x = x[:90].rsplit(' ', 1)[0].rstrip(',;') + '…'
        x = baslik_bicim(x, ders == 'ingilizce')
        for a, b in YABANCI.items():
            x = x.replace(a, b)
        out.append(tr_buyuk_bas(x) if ders != 'ingilizce' else x[:1].upper() + x[1:])
    return out


def anahtar(s):
    return re.sub(r'[^a-z0-9çğıöşü]+', ' ', tr_kucuk(s)).strip()


def kod_yap(s, kullanilan):
    a = tr_kucuk(s)
    for x, y in zip('çğıöşüâîû', 'cgiosuaiu'):
        a = a.replace(x, y)
    a = re.sub(r'[^a-z0-9]+', '-', a).strip('-')[:48].strip('-') or 'konu'
    k, n = a, 2
    while k in kullanilan:
        k, n = f'{a}-{n}', n + 1
    kullanilan.add(k)
    return k


def alanlar(h):
    d = {}
    for _, satir in h.get('bolumler', []):
        for k, v in satir:
            d[k] = v
    return d


AYLAR = 'Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık'.split()
HAFTA_ADI = re.compile(r'^(\d{1,2})(?: (' + '|'.join(AYLAR) + r'))?-(\d{1,2}) (' + '|'.join(AYLAR) + r')$')


def hafta_adi(ad, bas):
    """Hafta etiketi ("14-18 Eylül", "28 Eylül-2 Ekim"). Plandaki yazım bozuksa ya da başlangıç gününe uymuyorsa
    (ör. "29-Mart-2 Nisan", "21-25 Eylü", "5 9 Ekim", yıl eki) etiket başlangıç tarihinden (pazartesi-cuma) yeniden yazılır.
    Kısa haftalar ("28-31 Aralık", "20-21 Mayıs") geçerli yazımda olduğu için korunur."""
    ad = re.sub(r'\s*-\s*', '-', re.sub(r'\s+\d{4}$', '', str(ad or '').strip().strip('"')))
    try:
        b = datetime.date.fromisoformat(bas)
    except (TypeError, ValueError):
        return ad
    m = HAFTA_ADI.match(ad)
    if m and int(m.group(1)) == b.day and (m.group(2) or m.group(4)) == AYLAR[b.month - 1]:
        return ad
    c = b + datetime.timedelta(days=4)
    return f'{b.day}-{c.day} {AYLAR[c.month - 1]}' if b.month == c.month else f'{b.day} {AYLAR[b.month - 1]}-{c.day} {AYLAR[c.month - 1]}'


def ortak_takvim(takvimler):
    """Hafta no → {bas, ad}: planların çoğunluğundaki başlangıç tarihi (hafta numarası farklı sayılan planlar,
    ör. ara tatili hafta sayan Arapça planları, planı olmayan derslerin takvimini kaydırmasın diye)."""
    oylar = {}
    for t in takvimler:
        for no, h in t.items():
            if h.get('bas'):
                oylar.setdefault(no, Counter())[h['bas']] += 1
    sonuc = {}
    for no in sorted(oylar, key=int):
        bas = oylar[no].most_common(1)[0][0]
        adlar = Counter(h['ad'] for t in takvimler for n, h in t.items() if n == no and h.get('bas') == bas)
        sonuc[no] = {'bas': bas, 'ad': adlar.most_common(1)[0][0]}
    return sonuc


def agac(plan_json, ders=''):
    uniteler, sira_u, haftalar, onceki_u = {}, [], {}, None
    for h in plan_json['haftalar']:
        no = h['no']
        a = alanlar(h)
        ad = re.sub(r'^\d+\.\s*Hafta:\s*', '', h.get('hafta', '')).strip()
        haftalar[str(no)] = {'bas': h.get('tarih', ''), 'ad': hafta_adi(ad, h.get('tarih', ''))}
        U = [u for u in (unite_temiz(u, ders == 'ingilizce') for u in satirlar(a.get('Ünite / Tema', ''))) if u]
        K = konu_satirlari(a.get('Konu (içerik çerçevesi)') or a.get('Konu') or '', ders)
        if U and all(OZEL.search(u) for u in U):
            continue
        U = [u for u in U if not OZEL.search(u)]
        K = [k for k in K if not OZEL.search(k)]
        if ders == 'turk-dili-ve-edebiyati':                                # Edebiyat planı beceri/metin listesi: ünite düzeyi
            K = []
        if not U and not K:
            continue
        if not U:
            U = [onceki_u] if onceki_u else ['Genel']
        if not K:
            K = [U[-1]]
        if len(U) == 1:
            eslesme = [(U[0], k) for k in K]
        elif len(K) == len(U):
            eslesme = list(zip(U, K))
        else:
            eslesme = [(U[0], K[0])] + [(U[-1], k) for k in K[1:]]
        for u, k in eslesme:
            ua = anahtar(u)
            if ua not in uniteler:
                uniteler[ua] = {'ad': u, 'konular': {}, 'sira': []}
                sira_u.append(ua)
            kn = uniteler[ua]
            ka = anahtar(k)
            if ka not in kn['konular']:
                kn['konular'][ka] = {'ad': k, 'haftalar': []}
                kn['sira'].append(ka)
            if no not in kn['konular'][ka]['haftalar']:
                kn['konular'][ka]['haftalar'].append(no)
        onceki_u = U[-1]
    kullanilan = set()
    cikti = []
    for ua in sira_u:
        u = uniteler[ua]
        cikti.append({'ad': u['ad'], 'konular': [{'kod': kod_yap(u['konular'][ka]['ad'], kullanilan), **u['konular'][ka]} for ka in u['sira']]})
    return haftalar, cikti


def plan_sec(adaylar):
    def puan(p):
        a = p['ad']
        return (any(x in a for x in ('-aihl', '-iho', '-hazirlik')), '-2-saat' in a, len(a))
    return sorted(adaylar, key=puan)[0]


def ozetlerden_agac(sinif, ders, referans_haftalar):
    ozet_klasor = Path(__file__).resolve().parent / 'ozetler'
    dosyalar = sorted(
        ozet_klasor.glob(f'{sinif}-{ders}-*.json'),
        key=lambda p: int(p.stem.rsplit('-', 1)[-1]) if p.stem.rsplit('-', 1)[-1].isdigit() else 999
    )
    if not dosyalar:
        return None, None
    uniteler, sira_u, haftalar = {}, [], {}
    for p in dosyalar:
        o = json.loads(p.read_text(encoding='utf-8'))
        no = int(o['hafta'])
        ref = referans_haftalar.get(str(no), {})
        # Etiket ortak takvimden; özetteki tarih yazısı yalnız takvimde o hafta yoksa kullanılır
        haftalar[str(no)] = {'bas': ref.get('bas', ''), 'ad': ref.get('ad') or hafta_adi(o.get('tarih') or f'{no}. Hafta', ref.get('bas', ''))}
        u_ham = o.get('unite') or 'Genel'
        u = unite_temiz(u_ham, ders == 'ingilizce') or u_ham
        k = (o.get('konu') or u).strip()
        ua = anahtar(u)
        if ua not in uniteler:
            uniteler[ua] = {'ad': u, 'konular': {}, 'sira': []}
            sira_u.append(ua)
        kn = uniteler[ua]
        ka = anahtar(k)
        if ka not in kn['konular']:
            kn['konular'][ka] = {'ad': k, 'haftalar': []}
            kn['sira'].append(ka)
        if no not in kn['konular'][ka]['haftalar']:
            kn['konular'][ka]['haftalar'].append(no)
    kullanilan = set()
    cikti = []
    for ua in sira_u:
        u = uniteler[ua]
        cikti.append({
            'ad': u['ad'],
            'konular': [{'kod': kod_yap(u['konular'][ka]['ad'], kullanilan), **u['konular'][ka]} for ka in u['sira']]
        })
    return haftalar, cikti


def main():
    gp = json.loads((VERI / 'gunluk-planlar.json').read_text(encoding='utf-8'))
    dersler = json.loads((VERI / 'dersler.json').read_text(encoding='utf-8'))
    gruplar = {}
    for p in gp['planlar']:
        for s in p['siniflar']:
            gruplar.setdefault((s, p['ders']), []).append(p)
    CIKTI.mkdir(parents=True, exist_ok=True)
    dizin, yazilan = {}, set()
    takvimler = []
    for (s, d), adaylar in sorted(gruplar.items()):
        if d not in dersler['dersler']:
            continue
        p = plan_sec(adaylar)
        yol = VERI / 'gunluk-plan' / f'{p["ad"]}.json'
        if not yol.exists():
            print('PLAN YOK:', yol.name)
            continue
        haftalar, uniteler = agac(json.loads(yol.read_text(encoding='utf-8')), d)
        if haftalar:
            takvimler.append(haftalar)
        ad = f'{s}-{d}'
        o = {'sinif': s, 'ders': d, 'plan': p['ad'], 'haftalar': haftalar, 'uniteler': uniteler}
        metin = json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '\n'
        hedef = CIKTI / f'{ad}.json'
        if not hedef.exists() or hedef.read_text(encoding='utf-8') != metin:
            hedef.write_text(metin, encoding='utf-8')
        yazilan.add(hedef.name)
        dizin[ad] = {'unite': len(uniteler), 'konu': sum(len(u['konular']) for u in uniteler)}

    referans_haftalar = ortak_takvim(takvimler)
    # Günlük planı olmayan ama dersler.json ve araclar/ozetler içinde bulunan dersler (ör. 9-12 İngilizce)
    for s_str, d_list in sorted(dersler.get('siniflar', {}).items(), key=lambda x: int(x[0])):
        s = int(s_str)
        for d in d_list:
            ad = f'{s}-{d}'
            if ad in dizin or d not in dersler['dersler']:
                continue
            haftalar, uniteler = ozetlerden_agac(s, d, referans_haftalar)
            if not uniteler:
                continue
            o = {'sinif': s, 'ders': d, 'plan': f'{ad}-ozet', 'haftalar': haftalar, 'uniteler': uniteler}
            metin = json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '\n'
            hedef = CIKTI / f'{ad}.json'
            if not hedef.exists() or hedef.read_text(encoding='utf-8') != metin:
                hedef.write_text(metin, encoding='utf-8')
            yazilan.add(hedef.name)
            dizin[ad] = {'unite': len(uniteler), 'konu': sum(len(u['konular']) for u in uniteler)}

    for f in CIKTI.glob('*.json'):
        if f.name not in yazilan and f.name != 'dizin.json':
            f.unlink()
    (CIKTI / 'dizin.json').write_text(json.dumps(dizin, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    print(len(dizin), 'ders ağacı;', sum(v['konu'] for v in dizin.values()), 'konu')


if __name__ == '__main__':
    main()
