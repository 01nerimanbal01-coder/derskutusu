// Sosyal medya kuyruğu ve afiş kartlarının tutarlılık denetimi (bağımlılıksız).
// sosyal/kuyruk.json, sosyal/bilgiler.json, public/sosyal/*.png ve araclar/ozetler/*.json birbirini tutmalı.
const fs = require('node:fs');
const path = require('node:path');

function runSocialChecks(root) {
  const assert = (ok, message) => { if (!ok) throw new Error(message); };
  const cases = [];
  const read = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
  const queue = read('sosyal/kuyruk.json');
  const cards = fs.existsSync(path.join(root, 'sosyal/bilgiler.json')) ? read('sosyal/bilgiler.json') : [];
  const images = new Set(fs.readdirSync(path.join(root, 'public/sosyal')).filter(f => f.endsWith('.png')));
  const summaries = new Set(fs.readdirSync(path.join(root, 'araclar/ozetler')).map(f => f.replace(/\.json$/, '')));

  const ids = queue.gonderiler.map(g => g.kimlik);
  assert(new Set(ids).size === ids.length, 'kuyrukta yinelenen kimlik var');
  cases.push('kuyruk kimlikleri tekil');

  for (const g of queue.gonderiler) {
    assert(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+03:00$/.test(g.zaman), `${g.kimlik}: zaman TSİ ISO biçiminde değil`);
    assert(Array.isArray(g.hedef) && g.hedef.every(h => ['instagram', 'facebook'].includes(h)), `${g.kimlik}: hedef hatalı`);
    assert(typeof g.durum === 'object', `${g.kimlik}: durum nesnesi yok`);
    const m = g.gorsel.match(/^https:\/\/derskutusu\.com\/sosyal\/([a-z0-9-]+\.png)$/);
    assert(m && images.has(m[1]), `${g.kimlik}: görsel public/sosyal içinde yok (${g.gorsel})`);
    assert(g.metin.length > 20 && g.metin.length <= 2200, `${g.kimlik}: metin uzunluğu Instagram sınırı dışında`);
    assert(g.metin.includes('#derskutusu'), `${g.kimlik}: #derskutusu etiketi yok`);
  }
  cases.push(`kuyruktaki ${queue.gonderiler.length} gönderinin görseli, zamanı ve metni geçerli`);

  const cardIds = cards.map(k => k.kimlik);
  assert(new Set(cardIds).size === cardIds.length, 'bilgiler.json içinde yinelenen kimlik var');
  for (const k of cards) {
    assert(/^bilgi-[a-z0-9-]+$/.test(k.kimlik), `${k.kimlik}: kimlik biçimi`);
    assert(summaries.has(k.dosya), `${k.kimlik}: özet dosyası yok (${k.dosya})`);
    assert(k.baslik.length >= 20 && k.baslik.length <= 52, `${k.kimlik}: başlık ${k.baslik.length} karakter (20-52 olmalı)`);
    assert(Array.isArray(k.metin) && k.metin.length === 2, `${k.kimlik}: metin iki paragraf olmalı`);
    assert(k.metin.join(' ').length <= 300, `${k.kimlik}: paragraflar toplam 300 karakteri aşıyor`);
    assert(k.ozet.length >= 20 && k.ozet.length <= 240, `${k.kimlik}: özet ${k.ozet.length} karakter`);
    assert(!/[؀-ۿ]/.test(k.baslik + k.metin.join('')), `${k.kimlik}: afiş metninde Arap harfi var`);
    assert(images.has(k.kimlik + '.png'), `${k.kimlik}: afiş çizilmemiş (python3 araclar/sosyal_uret.py)`);
  }
  cases.push(`${cards.length} afiş kartının özeti, görseli ve uzunlukları uygun`);
  return { ok: true, cases };
}

if (typeof module !== 'undefined') module.exports = { runSocialChecks };
if (typeof require !== 'undefined' && require.main === module) {
  try {
    console.log(JSON.stringify(runSocialChecks(path.resolve(__dirname, '..')), null, 2));
  } catch (error) {
    console.error(error.stack);
    process.exitCode = 1;
  }
}
