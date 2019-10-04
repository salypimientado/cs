from tokenize import String


def sumatoria(iN):
    n = iN
    num = 0
    while n != 0:
        num += n
        n -=1
    print(num)


def cuenta_PNC(iN):
    cc = 0
    cp = 0
    cn = 0
    num = 0
    while num != iN:
        k = int(input())
        if k == 0:
            cc += 1
        if k <0:
            cn +=1
        if k > 0:
            cp +=1
        num+=1
    print("la cantidad de números positivos es ",cp,'\n',"la cantidad de números negativos es ",cn,'\n', "la cantidad de ceros es ",cc, sep='')

def tablaMultiplicar(iN):
    n = 10
    while n !=0:
        print(iN, "*", n, "=", iN*n,sep='')
        n -=1

def promedio(iN):
    pr = 0
    s = 0
    n = iN
    while n !=0:
        s += int(input())
        n-=1

    pr = s/iN
    print(pr)

def mayor(iN):
    n = iN
    m = 0
    i = 0
    while n != 0:
        i = int(input())
        if i > m :
            m = i

        n -= 1
    print('el mayor es ', m)

def menor(iN):
    n = iN
    m = 0
    i = 0
    while n != 0:
        i = int(input())
        if i < m :
            m = i

        n -= 1
    print('el mayor es ', m)

def fibo(iN):
    n1 =  0
    n2 = 1
    n = iN
    temp = 0
    while n != 0:
        print(n1)
        temp = n2
        n2 = n1 + n2
        n1 = temp
        n -=1
fibo()