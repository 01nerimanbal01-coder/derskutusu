from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 230
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">REVISION 1: PERSONAL PROFILES, ROUTINES &amp; ADVERBS OF FREQUENCY</text>')
    # Sol: Aygül & Priya Profiles
    ic.append('<rect x="25" y="45" width="275" height="165" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>')
    ic.append('<text x="162" y="65" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">SOCIAL MEDIA PROFILES</text>')
    ic.append('<text x="38" y="84" font-size="10" font-weight="700" fill="#1e3a8a">• Aygül (Turkmenistan):</text>')
    ic.append('<text x="45" y="99" font-size="9.5" fill="#1e293b">Turkmen &amp; English | slim, wavy dark hair</text>')
    ic.append('<text x="45" y="114" font-size="9.5" fill="#1e293b">cheerful, sometimes forgetful | documentaries</text>')
    ic.append('<line x1="38" y1="124" x2="285" y2="124" stroke="#bfdbfe"/>')
    ic.append('<text x="38" y="142" font-size="10" font-weight="700" fill="#1e3a8a">• Priya (New Delhi, India):</text>')
    ic.append('<text x="45" y="157" font-size="9.5" fill="#1e293b">Native: Hindi | India Gate &amp; Lotus Temple</text>')
    ic.append('<text x="45" y="172" font-size="9.5" fill="#1e293b">Mother: biology teacher | Father: software eng.</text>')
    ic.append('<text x="45" y="187" font-size="9.5" font-weight="700" fill="#2563eb">Likes English &amp; history; group work → teamwork</text>')
    # Sağ: Adverbs of Frequency & Simple Present
    ic.append('<rect x="315" y="45" width="280" height="165" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="455" y="65" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">ROUTINES &amp; FREQUENCY</text>')
    bars = [
        ("always (100%)", 230, "#16a34a"),
        ("usually (80%)", 185, "#22c55e"),
        ("often (60%)", 140, "#4ade80"),
        ("sometimes (40%)", 95, "#f59e0b"),
        ("never (0%)", 25, "#ef4444"),
    ]
    for idx, (lbl, bw, col) in enumerate(bars):
        y = 78 + idx * 24
        ic.append(f'<rect x="330" y="{y}" width="{bw}" height="16" rx="4" fill="{col}" opacity="0.85"/>')
        ic.append(f'<text x="336" y="{y+12}" font-size="9" font-weight="700" fill="#ffffff">{lbl}</text>')
    ic.append('<text x="455" y="202" text-anchor="middle" font-size="9.5" font-weight="700" fill="#166534">He/She + V-s/es (walks, studies, watches)</text>')
    return svg(w, h, "".join(ic), "Revision 1 kişisel profiller ve sıklık zarfları şeması")


def _gorsel_2():
    w, h = 620, 220
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#fffbeb" stroke="#fcd34d"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">CULTURES, CITIES &amp; FESTIVALS IN "A QUICK LOOK INTO MY LIFE"</text>')
    cards = [
        (25, "INDIA (New Delhi)", "#eff6ff", "#3b82f6", "#1d4ed8", ["• Person: Priya (speaks Hindi)", "• Capital: New Delhi", "• Landmarks: India Gate,", "  Lotus Temple"]),
        (218, "JAPAN (Tokyo)", "#fdf2f8", "#ec4899", "#be185d", ["• School trip last summer", "• Places: Shibuya Crossing,", "  Tokyo Tower", "• Festival: Hanami (cherry blossom)"]),
        (411, "SPAIN (Barcelona)", "#f0fdf4", "#22c55e", "#15803d", ["• Person: Luis (speaks Spanish)", "• Famous for: beaches &amp; stadiums", "• Festival: Gracia Festival", "  (cuisines &amp; folk dancers)"]),
    ]
    for x, title, bg, st, tc, lines in cards:
        ic.append(f'<rect x="{x}" y="46" width="184" height="152" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+92}" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="{tc}">{title}</text>')
        for i, ln in enumerate(lines):
            ic.append(f'<text x="{x+12}" y="{92+i*22}" font-size="9.5" fill="#1e293b">{ln}</text>')
    return svg(w, h, "".join(ic), "Hindistan, Japonya ve İspanya kültürel öğeler ve festivaller tablosu")


def _gorsel_3():
    w, h = 620, 220
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">REVISION 2: HOME LIFE, FOOD PREFERENCES &amp; ENDANGERED WILDLIFE</text>')
    ic.append('<rect x="25" y="46" width="275" height="152" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="1.5"/>')
    ic.append('<text x="162" y="66" text-anchor="middle" font-size="11" font-weight="700" fill="#c2410c">HOME &amp; FOOD IDIOMS</text>')
    ic.append('<text x="38" y="88" font-size="9.5" font-weight="700" fill="#9a3412">• "Home sweet home":</text>')
    ic.append('<text x="45" y="104" font-size="9.5" fill="#1e293b">Sharing a homemade meal in a cosy house</text>')
    ic.append('<text x="38" y="126" font-size="9.5" font-weight="700" fill="#9a3412">• "Not my cup of tea":</text>')
    ic.append('<text x="45" y="142" font-size="9.5" fill="#1e293b">Disliking something (Carol → sushi)</text>')
    ic.append('<text x="38" y="166" font-size="9.5" font-weight="700" fill="#9a3412">• "Food brings people together"</text>')
    ic.append('<rect x="315" y="46" width="280" height="152" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>')
    ic.append('<text x="455" y="66" text-anchor="middle" font-size="11" font-weight="700" fill="#047857">PROTECTING SEA TURTLES</text>')
    ic.append('<text x="328" y="88" font-size="9.5" font-weight="700" fill="#065f46">• Problem: Sea turtles\' habitats are endangered</text>')
    ic.append('<text x="328" y="110" font-size="9.5" fill="#1e293b">1. Recycle waste materials regularly</text>')
    ic.append('<text x="328" y="130" font-size="9.5" fill="#1e293b">2. Use less plastic in daily life</text>')
    ic.append('<text x="328" y="150" font-size="9.5" fill="#1e293b">3. Join a wildlife / environmental club</text>')
    ic.append('<text x="455" y="178" text-anchor="middle" font-size="9.5" font-weight="700" fill="#047857">"Every little bit helps / makes a big difference!"</text>')
    return svg(w, h, "".join(ic), "Revision 2 ev deyimleri ve nesli tükenen deniz kaplumbağalarını koruma yolları")


def _gorsel_4():
    w, h = 620, 230
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">HOW SMART CAN A HOUSE BE? — GLOBAL SMART TECHNOLOGIES</text>')
    items = [
        (25, 48, "THE UNITED STATES", "Smart Mirrors", "Check health, show weather forecast &amp; schedule", "#eff6ff", "#3b82f6", "#1d4ed8"),
        (320, 48, "SINGAPORE", "Apartment Robots", "Clean the halls &amp; deliver packages", "#f0fdf4", "#22c55e", "#15803d"),
        (25, 132, "SWEDEN", "Colour-Changing Glass Walls", "Control indoor temperature &amp; adapt to climate", "#fef2f2", "#ef4444", "#b91c1c"),
        (320, 132, "DUBAI", "Smart Kitchens", "Cooker, oven &amp; dishwasher cook from a recipe", "#faf5ff", "#a855f7", "#7e22ce"),
    ]
    for x, y, country, tech, desc, bg, st, tc in items:
        ic.append(f'<rect x="{x}" y="{y}" width="275" height="72" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+14}" y="{y+20}" font-size="10" font-weight="700" fill="{tc}">{country} → {tech}</text>')
        ic.append(f'<text x="{x+14}" y="{y+42}" font-size="9.5" fill="#1e293b">{desc}</text>')
        ic.append(f'<text x="{x+14}" y="{y+59}" font-size="8.5" fill="#64748b">+ Voice assistants, smart wardrobe &amp; automatic hoover</text>')
    return svg(w, h, "".join(ic), "Ülkelere göre akıllı ev teknolojileri şeması")


def _gorsel_5():
    w, h = 620, 225
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">SMART HOUSES: ADVANTAGES, DISADVANTAGES &amp; LINKING WORDS</text>')
    ic.append('<rect x="25" y="46" width="235" height="156" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="142" y="66" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">ADVANTAGES (+)</text>')
    ic.append('<text x="36" y="88" font-size="9.5" fill="#1e293b">• Save energy and time</text>')
    ic.append('<text x="36" y="108" font-size="9.5" fill="#1e293b">• Make life easier &amp; comfortable</text>')
    ic.append('<text x="36" y="128" font-size="9.5" fill="#1e293b">• Control appliances remotely</text>')
    ic.append('<text x="36" y="148" font-size="9.5" fill="#1e293b">• Advanced security system</text>')
    ic.append('<rect x="36" y="162" width="212" height="28" rx="6" fill="#dcfce7"/>')
    ic.append('<text x="142" y="180" text-anchor="middle" font-size="9.5" font-weight="700" fill="#166534">Adding (+ → +): MOREOVER</text>')

    ic.append('<rect x="360" y="46" width="235" height="156" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>')
    ic.append('<text x="477" y="66" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b91c1c">DISADVANTAGES (-)</text>')
    ic.append('<text x="372" y="88" font-size="9.5" fill="#1e293b">• Expensive to install</text>')
    ic.append('<text x="372" y="108" font-size="9.5" fill="#1e293b">• Require the internet to work</text>')
    ic.append('<text x="372" y="128" font-size="9.5" fill="#1e293b">• Some devices are easy to hack</text>')
    ic.append('<text x="372" y="148" font-size="9.5" fill="#1e293b">• Can be difficult for some people</text>')
    ic.append('<rect x="372" y="162" width="212" height="28" rx="6" fill="#fee2e2"/>')
    ic.append('<text x="477" y="180" text-anchor="middle" font-size="9" font-weight="700" fill="#991b1b">Contrast (+ → -): HOWEVER / ON THE OTHER HAND</text>')

    ic.append('<line x1="265" y1="124" x2="355" y2="124" stroke="#64748b" stroke-width="2" stroke-dasharray="4,3"/>')
    ic.append('<text x="310" y="116" text-anchor="middle" font-size="9" font-weight="700" fill="#475569">vs.</text>')
    return svg(w, h, "".join(ic), "Akıllı evlerin avantaj ve dezavantajları ile bağlaç kullanımı")


def uygula(v):
    gorseller = [_gorsel_1(), _gorsel_2(), _gorsel_3(), _gorsel_4(), None, _gorsel_5()]
    for i, g in enumerate(gorseller):
        if g and i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
