a = input()

i = []
o = True

for c in a:
    i.append(c)

def rev():
    tr = True
    global o

    if len(i) == 1:
        return 0
    elif len(i) == 0:
        return 0
    else:
        if i[0] != i[-1]:
            o = False
        i.pop(0)
        i.pop(-1)
        rev()

rev()


print(o)