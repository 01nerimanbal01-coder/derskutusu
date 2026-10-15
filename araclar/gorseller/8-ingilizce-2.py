from ozet_gorsel import svg


def g1():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-m"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">PERSONAL TRAITS: OLUMLU VE OLUMSUZ KİŞİLİK ÖZELLİKLERİ</text>'
        '<rect x="14" y="54" width="258" height="152" rx="8" class="g-ya"/>'
        '<text x="143" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">POSITIVE TRAITS (OLUMLU)</text>'
        '<rect x="26" y="88" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="143" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">Honest · Reliable · Trustworthy</text>'
        '<rect x="26" y="126" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="143" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">Supportive · Helpful · Loyal</text>'
        '<rect x="26" y="164" width="234" height="32" rx="6" class="g-s"/>'
        '<text x="143" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">Generous · Cheerful · Kind</text>'
        '<rect x="288" y="54" width="258" height="152" rx="8" class="g-ta"/>'
        '<text x="417" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">NEGATIVE TRAITS (OLUMSUZ)</text>'
        '<rect x="300" y="88" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="417" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-tf">Stingy (Cimri) · Selfish (Bencil)</text>'
        '<rect x="300" y="126" width="234" height="32" rx="6" class="g-l"/>'
        '<text x="417" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-lf">Stubborn (İnatçı) · Rude (Kaba)</text>'
        '<rect x="300" y="164" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="417" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-tf">Jealous · Pessimistic (Kötümser)</text>'
    )
    return svg(w, h, ic, "Olumlu ve olumsuz kişilik sıfatları karşılaştırma şeması")


def g2():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-t"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">MÜSAİTLİK SORMA VE DAVET KALIPLARI (GRAMMAR BOX)</text>'
        '<rect x="14" y="54" width="532" height="36" rx="6" class="g-sa"/>'
        '<text x="280" y="77" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">Uygunluk Sorma: "Are you busy tomorrow?" → "No, not at all. Why?"</text>'
        '<rect x="14" y="98" width="258" height="108" rx="8" class="g-ma"/>'
        '<text x="143" y="120" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">YALIN FİİL (V1) ALANLAR</text>'
        '<text x="143" y="144" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Would you like to + V1 ...?</text>'
        '<text x="143" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Why don\'t we + V1 ...?</text>'
        '<text x="143" y="188" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Shall we + V1 ...? / Let\'s + V1!</text>'
        '<rect x="288" y="98" width="258" height="108" rx="8" class="g-ya"/>'
        '<text x="417" y="120" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">FİİL + ING VEYA İSİM ALANLAR</text>'
        '<text x="417" y="144" text-anchor="middle" font-size="12" font-weight="600" class="g-y">How about + V-ing ...?</text>'
        '<text x="417" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-y">What about + V-ing ...?</text>'
        '<text x="417" y="188" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Would you like + some + İsim?</text>'
    )
    return svg(w, h, ic, "Müsaitlik sorma ve davet kalıpları dil bilgisi şeması")


def g3():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-y"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-yf">ACCEPTING (KABUL) VE REFUSING WITH REASONS (MAZERETLİ RET)</text>'
        '<rect x="14" y="54" width="258" height="152" rx="8" class="g-ya"/>'
        '<text x="143" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">ACCEPTING (KABUL İFADELERİ)</text>'
        '<rect x="26" y="88" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="143" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">Yes, I\'d love to. / Yeah, why not?</text>'
        '<rect x="26" y="126" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="143" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">Sure, it sounds good / awesome!</text>'
        '<rect x="26" y="164" width="234" height="32" rx="6" class="g-s"/>'
        '<text x="143" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">That would be nice. / Cool.</text>'
        '<rect x="288" y="54" width="258" height="152" rx="8" class="g-la"/>'
        '<text x="417" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">REFUSING + EXPLANATION</text>'
        '<rect x="300" y="88" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="417" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-tf">I\'m sorry / afraid, I can\'t.</text>'
        '<rect x="300" y="126" width="234" height="32" rx="6" class="g-l"/>'
        '<text x="417" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-lf">I\'d love to, but I have an exam.</text>'
        '<rect x="300" y="164" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="417" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">No, thanks. I\'m full / stuffed.</text>'
    )
    return svg(w, h, ic, "Kabul etme ve mazeret bildirerek reddetme kalıpları şeması")


def g4():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-l"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-lf">SITUATIONS &amp; OFFERS: DURUMA UYGUN TEKLİF EŞLEŞTİRME</text>'
        '<rect x="14" y="54" width="532" height="34" rx="6" class="g-ma"/>'
        '<text x="280" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">Your sister is thirsty. → "Would you like to drink some water?"</text>'
        '<rect x="14" y="96" width="532" height="34" rx="6" class="g-ta"/>'
        '<text x="280" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">Your friend is hungry. → "What about eating something?"</text>'
        '<rect x="14" y="138" width="532" height="34" rx="6" class="g-ya"/>'
        '<text x="280" y="160" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">You are tired. → "Let\'s have a rest!" | Bored → "How about the cinema?"</text>'
        '<rect x="14" y="180" width="532" height="34" rx="6" class="g-sa"/>'
        '<text x="280" y="202" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">Your fridge is empty. → "Why don\'t we go shopping?"</text>'
    )
    return svg(w, h, ic, "Duruma uygun İngilizce teklif eşleştirme şeması")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
