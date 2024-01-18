def epit():
    s = int(input("s értéke: "))
    b = (int(input("b értéke: ")))
    w = int(input("w értéke: "))
    db_5x = w//5    # // -> pl.: 15 // 5 = 3 mert 3x van meg az 5 a 15-ben
    lehetFal = False

    # print(w % 5)
    if db_5x > b:
        if s >= w or b*5 + s >= w:
            lehetFal = True
    else:
        if w % 5 <= s:
            lehetFal = True

    # else:
    #     lehetFal = True
    # kulonbs1 = w - s
    # kulonbs2 = w - b
    # # if s >= w or b*5 == w or b*5 == kulonbs1 or s >= kulonbs2:
    # #     lehetFal = True
    # if s >= w:  # 12 >= 11 = True
    #     lehetFal = True
    # else:   # 9 >= 11 = False
    #     if b == w:  # b = 2 = 11 = False
    #         lehetFal = True
    #     else:   # 10 = b (1) -
    #         # w % b != 0
    #         if s >= kulonbs2:
    #             lehetFal = True

    return lehetFal

