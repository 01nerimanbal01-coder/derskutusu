"""Yayında üst çizgisiz kök kalmasını önleyen bağımsız, bağımlılıksız denetim."""
from pathlib import Path
import re,json,html,zipfile,sys
from xml.etree import ElementTree as ET
R=Path(__file__).resolve().parents[1];bad=[];count=0
for folder,ext in [('araclar/kpss','json'),('araclar/ozetler','json'),('araclar/calisma','json'),('public','html'),('public','svg')]:
 for p in (R/folder).rglob('*.'+ext):
  count+=1
  if re.search('[√∛∜]',html.unescape(p.read_text())):bad.append(str(p.relative_to(R))+': düz kök işareti')
  if ext=='html' and re.search(r'\{kok:',p.read_text()):bad.append(str(p.relative_to(R))+': çözülmemiş kök')
for p in (R/'public/dosyalar/gunluk-plan').glob('*.docx'):
 count+=1
 with zipfile.ZipFile(p) as z:
  for name in z.namelist():
   if name.startswith('word/') and name.endswith('.xml'):
    s=z.read(name).decode()
    if re.search('[√∛∜]',s):bad.append(str(p.relative_to(R))+': Word denklemine çevrilmemiş kök')
# Resmî JSON alıntıları değiştirilmez; bunları kullanan göstericiler kökü çizer.
for p in [R/'public/veri/senaryolar.json',*(R/'public/veri/gunluk-plan').glob('*.json')]:
 text=p.read_text()
 for root in re.findall(r'[√∛∜].{0,22}',text):
  if not re.match(r'[√∛∜](?:[a-zA-Z]|\d+)',root):bad.append(str(p.relative_to(R))+': alıntı kökü için yeni gösterim denetimi gerekli')
assert 'kokDugumu(c)' in (R/'public/ortak.js').read_text()
assert 'kokParcalari(satir)' in (R/'public/planlar.js').read_text()
print(f'{count} kaynak/web/Word dosyası; kök gösterimi hatası: {len(bad)}')
for x in bad:print(x)
sys.exit(bool(bad))
