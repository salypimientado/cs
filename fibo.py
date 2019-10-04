
def fibo():
    x = int(input())
    n1 = 0
    n2 = 1
    n = x
    l = []
    temp = 0
    while n != 0:
        l.append(str(n1))
        temp = n2
        n2 = n1 + n2
        n1 = temp
        n -=1
    m = ",".join(l)
    print(m)


fibo()