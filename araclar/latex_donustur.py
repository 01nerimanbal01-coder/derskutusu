#!/usr/bin/env python3
"""Konu özeti JSON'larındaki LaTeX formüllerini ($\\frac{a}{b}$ …) sitenin gösterimine çevirir (21.10.2026).

Site LaTeX çözmez; `$…$` sayfada dolar işaretleriyle bozuk görünür. Çeviri ozet_uret.e() gösterimiyle:
kesir {kesir:pay|payda} (K155 dikey), üs {us:|n}, alt simge {alt:n}, vektör {vektor:L}, devirli ondalık {devir:43}, \\text{} düz metin, Yunan harfleri ve
işaretler Unicode. Fiyat yazan dolar ($25/day, $15 olup) korunur.
Kullanım: python3 latex_donustur.py [--yaz] [dosya.json …]   (dosya verilmezse ozetler/*.json; --yaz yoksa yalnız rapor)
"""
import json, re, sys
from pathlib import Path

OZETLER = Path(__file__).resolve().parent / 'ozetler'
SEMBOL = {
    'cdot': ' · ', 'times': ' × ', 'div': ' ÷ ', 'pm': '±', 'mp': '∓',
    'le': ' ≤ ', 'leq': ' ≤ ', 'ge': ' ≥ ', 'geq': ' ≥ ', 'neq': ' ≠ ', 'ne': ' ≠ ', 'approx': ' ≈ ', 'equiv': ' ≡ ',
    'infty': '∞', 'emptyset': '∅', 'varnothing': '∅', 'circ': '°', 'degree': '°', 'parallel': '//', 'perp': '⊥',
    'mid': '|', 'dots': '…', 'ldots': '…', 'cdots': '⋯', 'sum': 'Σ', 'in': '∈', 'notin': '∉',
    'subset': '⊂', 'subseteq': '⊆', 'cup': '∪', 'cap': '∩', 'forall': '∀', 'exists': '∃',
    'rightarrow': ' → ', 'to': ' → ', 'leftarrow': ' ← ', 'longrightarrow': ' ⟶ ', 'longleftarrow': ' ⟵ ',
    'leftrightarrow': ' ↔ ', 'longleftrightarrow': ' ⟷ ', 'Rightarrow': ' ⇒ ', 'implies': ' ⇒ ', 'Leftarrow': ' ⇐ ',
    'Leftrightarrow': ' ⇔ ', 'iff': ' ⇔ ', 'rightleftharpoons': ' ⇌ ',
    'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ', 'epsilon': 'ε', 'varepsilon': 'ε', 'theta': 'θ',
    'lambda': 'λ', 'mu': 'μ', 'pi': 'π', 'rho': 'ρ', 'sigma': 'σ', 'tau': 'τ', 'phi': 'φ', 'varphi': 'φ',
    'omega': 'ω', 'Delta': 'Δ', 'Gamma': 'Γ', 'Theta': 'Θ', 'Lambda': 'Λ', 'Sigma': 'Σ', 'Phi': 'Φ', 'Omega': 'Ω',
    'left': '', 'right': '', ',': ' ', ';': ' ', ' ': ' ', '!': '', '%': '%', '&': '&', '#': '#', '_': '_',
}
MATHBB = {'N': 'ℕ', 'Z': 'ℤ', 'Q': 'ℚ', 'R': 'ℝ', 'C': 'ℂ'}
SADECE_ICERIK = {'text', 'mathrm', 'textbf', 'mathbf', 'textit', 'mathit', 'operatorname', 'mbox'}
# Fiyat yazan dolar: $25/day, $60 Full Pass, $15 olup — matematik değil, korunur.
FIYAT = re.compile(r'\$(?=\d+(?:\.\d\d)?(?:/|\)| [A-Za-z]{3,}|, [a-z]{3,}))')   # $25/day, $80), $15 olup, $15, and; Türkçe ondalık ($2,43$) değil
MATEMATIK = re.compile(r'\$\$(.+?)\$\$|\$([^$\n]+?)\$', re.S)   # önce $$…$$ (ayrı satır formül), sonra $…$


class Cozumleyici:
    def __init__(self, metin):
        self.s, self.i, self.bilinmeyen = metin, 0, []

    def grup(self):
        """Sıradaki argüman: {…} ya da tek simge."""
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1
        if self.i >= len(self.s):
            return ''
        if self.s[self.i] == '{':
            self.i += 1
            ic = self.ifade(kapanis='}')
            self.i += 1
            return ic
        if self.s[self.i] == '\\':
            return self.komut()
        self.i += 1
        return self.s[self.i - 1]

    def komut(self):
        self.i += 1
        m = re.match(r'[A-Za-z]+|.', self.s[self.i:])
        ad = m.group(0)
        self.i += len(ad)
        if ad.isalpha():   # LaTeX'te harfli komuttan sonraki boşluk sayılmaz: \Delta t → Δt
            while self.i < len(self.s) and self.s[self.i] == ' ':
                self.i += 1
        if ad in ('frac', 'dfrac', 'tfrac'):
            pay, payda = self.grup(), self.grup()
            return '{kesir:' + pay.strip() + '|' + payda.strip() + '}'
        if ad in SADECE_ICERIK:
            return self.grup()
        if ad == 'vec':
            return '{vektor:' + self.grup() + '}'
        if ad == 'overline':
            return '{devir:' + self.grup() + '}'
        if ad == 'mathbb':
            ic = self.grup()
            return MATHBB.get(ic, ic)
        if ad == 'sqrt':
            return '{kok:' + self.grup() + '}'
        if ad in SEMBOL:
            return SEMBOL[ad]
        self.bilinmeyen.append(ad)
        return ad

    def ifade(self, kapanis=None):
        cikti = []
        while self.i < len(self.s):
            c = self.s[self.i]
            if kapanis and c == kapanis:
                break
            if c == '\\':
                cikti.append(self.komut())
            elif c == '{':
                cikti.append(self.grup())
            elif c in '^_':
                self.i += 1
                arg = self.grup().strip()
                if c == '^':
                    cikti.append('°' if arg == '°' else '{us:|' + arg + '}')
                else:
                    cikti.append('{alt:' + arg + '}')
            else:
                cikti.append(c)
                self.i += 1
        return ''.join(cikti)


def cevir(metin, bilinmeyen):
    metin = metin.replace('\x0bec{', '\\vec{')   # JSON'da kaçışsız \vec → dikey sekme + 'ec{'
    korunan = FIYAT.sub('\ue001', metin)

    def bir(m):
        c = Cozumleyici(m.group(1) if m.group(1) is not None else m.group(2))
        sonuc = c.ifade()
        bilinmeyen.extend(c.bilinmeyen)
        return re.sub(r' {2,}', ' ', sonuc).strip()

    return MATEMATIK.sub(bir, korunan).replace('\ue001', '$')


def gez(x, bilinmeyen):
    if isinstance(x, str):
        return cevir(x, bilinmeyen) if '$' in x else x
    if isinstance(x, list):
        return [gez(v, bilinmeyen) for v in x]
    if isinstance(x, dict):
        return {k: gez(v, bilinmeyen) for k, v in x.items()}
    return x


def main():
    yaz = '--yaz' in sys.argv
    dosyalar = [Path(a) for a in sys.argv[1:] if not a.startswith('--')] or sorted(OZETLER.glob('*.json'))
    for p in dosyalar:
        ham = p.read_text(encoding='utf-8')
        if '$' not in ham:
            continue
        bilinmeyen = []
        yeni = gez(json.loads(ham), bilinmeyen)
        kalan = json.dumps(yeni, ensure_ascii=False).count('$')
        print(f'{p.name}: kalan $ {kalan}' + (f' · bilinmeyen komut {sorted(set(bilinmeyen))}' if bilinmeyen else ''))
        if yaz:
            p.write_text(json.dumps(yeni, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
