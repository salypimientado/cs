a = input()
i = []

r = []

for c in a:
    i.append(c)


def rev():

    if len(i) == 0:
        return 0
    else:
        if i[0] != ' ':
            r.append(i[0])
        i.pop(0)
        rev()


rev()


print(''.join(r))