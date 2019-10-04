a = input()

i = []

r = []

for c in a:
    i.append(c)

def rev():

    if(len(i) == 0):
        return 0
    else:
        r.append(i[-1])
        i.pop()
        rev()

rev()


print(''.join(r))