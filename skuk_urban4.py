beseda = input('vnesi število z besedo:   ')

enice = {
    "nič": 0, "ena": 1, "dva": 2, "dve": 2,
    "tri": 3, "štiri": 4, "pet": 5, "šest": 6,
    "sedem": 7, "osem": 8, "devet": 9,
    "deset": 10, "enajst": 11, "dvanajst": 12,
    "trinajst": 13, "štirinajst": 14, "petnajst": 15,
    "šestnajst": 16, "sedemnajst": 17,
    "osemnajst": 18, "devetnajst": 19
}

desetice = {
    "dvajset": 20, "trideset": 30, "štirideset": 40,
    "petdeset": 50, "šestdeset": 60,
    "sedemdeset": 70, "osemdeset": 80,
    "devetdeset": 90
}

stotice = {
    "sto": 100, "dvesto": 200, "tristo": 300,
    "štiristo": 400, "petsto": 500,
    "šeststo": 600, "sedemsto": 700,
    "osemsto": 800, "devetsto": 900
}

deli = beseda.split()
rezultat = 0

if deli[0] in stotice:
    rezultat += stotice[deli[0]]
    deli = deli[1:]

if len(deli) > 0:
    b = deli[0]

    if b in enice:
        rezultat += enice[b]
    elif b in desetice:
        rezultat += desetice[b]
    else:
        for d in desetice:
            if d in b:
                rezultat += desetice[d]
                en = b.replace("in" + d, "")
                rezultat += enice[en]
                break

print(rezultat)