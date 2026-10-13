// Çevrimiçi test soru havuzu (veri/soru/*.json) bütünlük denetimi: tarayıcı gerekmez.
// Üretici: araclar/soru_havuzu_uret.py. Her ders dosyasının kimlikleri tekil, cevaplar geçerli, konu kodları ağaçta, dizin sayıları tutarlı olmalı.
const fs = require('node:fs');
const path = require('node:path');
const assert = (ok, message) => { if (!ok) throw new Error(message); };
const klasor = path.resolve(__dirname, '../public/veri/soru');
const dizin = JSON.parse(fs.readFileSync(path.join(klasor, 'dizin.json'), 'utf8'));
const OTOMATIK = new Set(['coktan', 'dy', 'bosluk', 'eslestir', 'siralama']);
const GORSEL = /görsel|resim|harita|grafi[kğ]|tablodaki|şekilde/i;
const cases = [];
let toplam = 0, otomatik = 0;
for (const [anahtar, ozet] of Object.entries(dizin.dersler)) {
  const d = JSON.parse(fs.readFileSync(path.join(klasor, `${anahtar}.json`), 'utf8'));
  assert(d.sinif === ozet.sinif && d.ders === ozet.ders, `${anahtar}: dizin ile dosya uyuşmuyor`);
  const kimlikler = new Set(), konular = new Set(d.uniteler.flatMap((u) => u.konular.map((k) => k.kod)));
  assert(d.sorular.length === ozet.toplam, `${anahtar}: soru sayısı ${d.sorular.length} ≠ dizin ${ozet.toplam}`);
  for (const s of d.sorular) {
    assert(!kimlikler.has(s.id), `${anahtar}: yinelenen kimlik ${s.id}`); kimlikler.add(s.id);
    assert(typeof s.soru === 'string' && s.soru.trim(), `${anahtar} ${s.id}: soru metni yok`);
    assert(!GORSEL.test(s.soru), `${anahtar} ${s.id}: görsele dayanan soru havuza girmiş`);
    assert(konular.has(s.konu), `${anahtar} ${s.id}: konu kodu ağaçta yok (${s.konu})`);
    assert(Array.isArray(s.cikti), `${anahtar} ${s.id}: cikti dizisi yok`);
    if (s.tur === 'coktan') assert(Array.isArray(s.secenekler) && s.secenekler.length >= 2 && Number.isInteger(s.dogru) && s.dogru >= 0 && s.dogru < s.secenekler.length, `${anahtar} ${s.id}: çoktan seçmeli cevabı geçersiz`);
    else if (s.tur === 'dy') assert(s.ifadeler?.length && s.ifadeler.every((f) => typeof f.dogru === 'boolean' && f.metin), `${anahtar} ${s.id}: doğru/yanlış ifadeleri geçersiz`);
    else if (s.tur === 'bosluk') assert(s.cumleler?.length && s.cumleler.every((c) => c.metin.includes('___') && c.cevap), `${anahtar} ${s.id}: boşluk cümleleri geçersiz`);
    else if (s.tur === 'eslestir') assert(s.ciftler?.length >= 2 && s.ciftler.every((c) => c.length === 2 && c[0] && c[1]), `${anahtar} ${s.id}: eşleştirme çiftleri geçersiz`);
    else if (s.tur === 'siralama') assert(s.ogeler?.length >= 3, `${anahtar} ${s.id}: sıralama ögeleri eksik`);
    else if (s.tur === 'acik') assert(typeof s.cevap === 'string' && s.cevap.trim(), `${anahtar} ${s.id}: açık uçlu cevap yok`);
    else throw new Error(`${anahtar} ${s.id}: bilinmeyen tür ${s.tur}`);
    toplam++; if (OTOMATIK.has(s.tur)) otomatik++;
  }
  assert(d.sorular.filter((s) => OTOMATIK.has(s.tur)).length === ozet.otomatik, `${anahtar}: otomatik sayısı dizinle uyuşmuyor`);
  for (const u of d.uniteler) for (const k of u.konular) assert(k.n === d.sorular.filter((s) => s.konu === k.kod).length, `${anahtar}: ${k.kod} konu sayısı yanlış`);
  for (const c of d.ciktilar) assert(c.n === d.sorular.filter((s) => s.cikti.includes(c.kod)).length, `${anahtar}: ${c.kod} çıktı sayısı yanlış`);
  cases.push({ name: anahtar, status: 'passed', sorular: d.sorular.length });
}
assert(Object.keys(dizin.dersler).length >= 90, 'Ders sayısı beklenenden az');
assert(otomatik >= 1000, `Otomatik puanlanan soru sayısı düşük: ${otomatik}`);
console.log(JSON.stringify({ status: 'passed', dersler: cases.length, sorular: toplam, otomatik }, null, 2));
