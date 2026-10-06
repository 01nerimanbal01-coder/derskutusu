"""Günlük planlardaki basit kökleri Word'ün gerçek denklem nesnesine dönüştürür."""
from copy import deepcopy
import re
from lxml import etree as ET
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M='http://schemas.openxmlformats.org/officeDocument/2006/math'
# Kökten sonra harf/rakam sürüyorsa (√ab, √2x) kök içi belirsizdir: eşleşmez, aşağıda ValueError verir.
ROOT=re.compile(r'([√∛∜])((?:\d+(?:[.,]\d+)?|[a-zA-Z])(?:[²³⁴⁵⁶⁷⁸⁹⁰¹]+)?)(?![A-Za-z\d])')

def ele(ns,name,text=None):
 e=ET.Element('{'+ns+'}'+name)
 if text is not None:e.text=text
 return e

def kokleri_duzelt(doc):
 adet=0
 for run in list(doc.iter('{'+W+'}r')):
  ts=list(run.findall('{'+W+'}t'))
  if len(ts)!=1 or not any(c in (ts[0].text or '') for c in '√∛∜'):continue
  text=ts[0].text
  if any(c in ROOT.sub('',text) for c in '√∛∜'):raise ValueError('Kapsamı desteklenmeyen Word kökü: '+text)
  if not all(isinstance(x.tag,str) and ET.QName(x).localname in ('rPr','t') for x in run):raise ValueError('Kök koşusunda başka nesne var: '+text)
  parent=run.getparent();pos=parent.index(run);out=[];start=0
  def normal(t):
   if t:
    r=deepcopy(run);r.find('{'+W+'}t').text=t;r.find('{'+W+'}t').set('{http://www.w3.org/XML/1998/namespace}space','preserve');out.append(r)
  for m in ROOT.finditer(text):
   normal(text[start:m.start()]);o=ele(M,'oMath');rad=ele(M,'rad');pr=ele(M,'radPr');hide=ele(M,'degHide');hide.set('{'+M+'}val','1' if m[1]=='√' else '0');pr.append(hide);rad.append(pr)
   deg=ele(M,'deg')
   if m[1]!='√':
    rr=ele(M,'r');rr.append(ele(M,'t',{'∛':'3','∜':'4'}[m[1]]));deg.append(rr)
   rad.append(deg);body=ele(M,'e');r=ele(M,'r');rpr=run.find('{'+W+'}rPr')
   if rpr is not None:r.append(deepcopy(rpr))
   r.append(ele(M,'t',m[2]));body.append(r);rad.append(body);o.append(rad);out.append(o);start=m.end();adet+=1
  normal(text[start:]);parent.remove(run)
  for node in out:parent.insert(pos,node);pos+=1
 return adet

if __name__=='__main__':
 import os,sys,zipfile
 from pathlib import Path
 for filename in sys.argv[1:]:
  p=Path(filename)
  with zipfile.ZipFile(p) as z:entries=[(i,z.read(i.filename)) for i in z.infolist()]
  root=ET.fromstring(dict((i.filename,b) for i,b in entries)['word/document.xml']);n=kokleri_duzelt(root)
  if n:
   tmp=p.with_name(p.name+'.tmp')  # önce yanına yazılır; kaynak .docx yarım kalmaz
   with zipfile.ZipFile(tmp,'w') as z:
    for i,b in entries:z.writestr(i,ET.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True) if i.filename=='word/document.xml' else b)
   os.replace(tmp,p)
  print(p.name,n,'OMML kök')
