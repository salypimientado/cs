a = input()

l = input()

i = []

r = []

for c in a:
    i.append(c)


def rev():

    if len(i) == 0:
        return 0
    else:
        if i[0] == l:
            r.append(i[0])
        else:
            r.append('*')
        i.pop(0)
        rev()


rev()


print(''.join(r))