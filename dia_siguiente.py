import string
from tokenize import String

da = int(input())
mo = int(input())
ye = int(input())
stro = []


def nd(d, m, y):
    if d < 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        d = d+1
    elif d == 31 and (m == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        if m == 12:
            y = y+1
            m = 0
            d = 1

        else:
            m = m + 1
            d = 1

    elif d < 30 and (m == 2 or 4 or 6 or 9 or 11):
        d = d + 1
    elif d == 30 and (m == 2 or 4 or 6 or 9 or 11):
        if m == 12:
            y = y + 1
            m = 1
            d = 1

        else:
            m = m + 1
            d = 1

    a = [d,m,y]

    return a


stro = [str(nd(da,mo,ye)[0]), str(nd(da,mo,ye)[1]), str(nd(da,mo,ye)[2])]


print('/'.join(stro))