from math import floor, ceil


def pastel():
    i = int(input())
    ia = int(input())
    st = ""

    for a in range(i):
        for x in range(ia):
            st += "|"

        print(st)
        st = ""

def esc():
    i = int(input())
    st = " *"
    space = " "
    for a in range(i):
        print(((i-a))*space, st)

        st += "**"


esc()