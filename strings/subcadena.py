from pip._vendor.msgpack.fallback import xrange

a = input()

l = input()

i = []

r = []

sc = []

mp = False

for c in a:
    i.append(c)

for b in l:
    sc.append(b)


def rev():
    if len(i) == 0:
        return 0
    else:
        if len(sc)>0:
            if i[0] != sc[0]:
                r.append(i[0])
                i.pop(0)
            else:
                while len(sc) > 0:
                    for m in xrange(len(sc)):
                        if i[int(m)] == sc[int(m)]:
                                 mp = True
                    if mp:
                        i.pop(0)
                        sc.pop(0)
                    else:
                        i.pop(0)
        else:
            r.append(i[0])
            i.pop(0)

        rev()


rev()


print(''.join(r))