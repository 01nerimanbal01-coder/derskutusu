"""Yayında üst çizgisiz kök kalmasını önleyen bağımsız, bağımlılıksız denetim."""
from pathlib import Path
import re,html,zipfile,sys
R=Path(__file__).resolve().parents[1];bad=[];count=0
def say(folder,n):
 # Klasör taşınır ya da boşalırsa denetim "0 hata" diye sessizce geçmesin.
 if not n:bad.append(folder+': taranacak dosya bulunamadı')
for folder,ext in [('araclar/kpss','json'),('araclar/ozetler','json'),('araclar/calisma','json'),('public','html'),('public','svg')]:
 n=0
 for p in (R/folder).rglob('*.'+ext):
  count+=1;n+=1
  s=p.read_text(encoding='utf-8')
  # JSON'da kaçışlı yazılmış kök (\u221a) de düz kök sayılır.
  if re.search('[√∛∜]',html.unescape(re.sub(r'\\u221[abc]','√',s,flags=re.I))):bad.append(str(p.relative_to(R))+': düz kök işareti')
  if ext=='html' and re.search(r'\{kok:',s):bad.append(str(p.relative_to(R))+': çözülmemiş kök')
 say(folder+'/*.'+ext,n)
n=0
for p in (R/'public/dosyalar/gunluk-plan').glob('*.docx'):
 count+=1;n+=1
 with zipfile.ZipFile(p) as z:
  for name in z.namelist():
   if name.startswith('word/') and name.endswith('.xml'):
    s=z.read(name).decode()
    if re.search('[√∛∜]',s):bad.append(str(p.relative_to(R))+': Word denklemine çevrilmemiş kök')
say('public/dosyalar/gunluk-plan/*.docx',n)
# Resmî JSON alıntıları değiştirilmez; bunları kullanan göstericiler kökü çizer.
say('public/veri/gunluk-plan/*.json',len(list((R/'public/veri/gunluk-plan').glob('*.json'))))
for p in [R/'public/veri/senaryolar.json',*(R/'public/veri/gunluk-plan').glob('*.json')]:
 text=p.read_text(encoding='utf-8')
 for root in re.findall(r'[√∛∜].{0,22}',text):
  if not re.match(r'[√∛∜](?:[a-zA-Z]|\d+)',root):bad.append(str(p.relative_to(R))+': alıntı kökü için yeni gösterim denetimi gerekli')
assert 'kokDugumu(c)' in (R/'public/ortak.js').read_text(encoding='utf-8')
assert 'kokParcalari(satir)' in (R/'public/planlar.js').read_text(encoding='utf-8')
print(f'{count} kaynak/web/Word dosyası; kök gösterimi hatası: {len(bad)}')
for x in bad:print(x)
sys.exit(bool(bad))
