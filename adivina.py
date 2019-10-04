def adivina():
    n = int(input())
    x = 0
    num = 8
    l = []
    r = False
    while n != 0 and n >0:
        l.append(str(num + x))
        num = num + x
        x += 1
        n -= 1
    l.append("?")
    print(", ".join(l))

    while not r:
        if int(input()) == num + x:
            r = True
    print("Felicidades")


adivina()
