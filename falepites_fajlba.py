def epitEllenoriz(s: int, b: int, w: int):
    db_5x = w//5    # // -> pl.: 15 // 5 = 3 mert 3x van meg az 5 a 15-ben
    lehetFal = False

    if db_5x > b:
        if s >= w or b*5 + s >= w:
            lehetFal = True
    else:
        if w % 5 <= s:
            lehetFal = True

    return lehetFal


def teszt():
    fajlbol = open("tesztadat.txt")
    fajlbol.readline()
    sorok = fajlbol.readlines()
    fajlbol.close()

    for i in range(0, len(sorok)):
        sor = sorok[i].strip().split(", ")
        s = sor[0]
        b = sor[1]
        w = sor[2]
        eredmeny = sor[3].replace(" ", "")
        print(eredmeny)
        if bool(eredmeny) == (epitEllenoriz(int(s), int(b), int(w))):
            print(i, " Jó.")
        else:
            print(i, " Nem jó.")


teszt()


