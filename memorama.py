import math
import random


def matrix_c(s1, s2):
    matrix = [[0 for x in range(s1)] for y in range(s2)]
    return matrix

def matrix2_c(s1, s2):
    matrix = [["-" for x in range(s1)] for y in range(s2)]
    return matrix

def matrixv_rand(matrix):

    ebic = []

    li = list(range(1, 19))
    for x in range(1,19):
        li.append(x)
    random.shuffle(li)

    for x in range(len(matrix)):
        for m in range(len(matrix[x-1])):
            matrix[x-1][m-1] =  li[0]
            li.pop(0)
        matrix[x-1].append("\n")


    '''  while len(li) !=0:

        col = nri[m] % 6
        ren = math.floor(nri[m] / 6)
        matrix[ren][col-1] = li[a]
        print("a", a ,"len li", len(li), "m", m, "nri len", len(nri))
        li.pop(a)
        nri.pop(m-1)
        
        



        while len(lii) != 0:
        
            a = random.choice(range(0,len(lii)))
            m = random.choice(range(0, len(nrii)))
            col = nrii[m] % 6
            ren = math.floor(nrii[m] / 6)
            matrix[ren-1][col] = lii[a]
            lii.pop(a)
            nrii.pop(m-1)

         if len(l) == 1:

            matrix[math.floor(l[0] / 6)][l[0] % 6 - 1] = l[0]
            l.pop(0)
        else:
            temp = random.randint(0, len(l))
            print("temp: ", temp)
            print(len(l))
            num = l[temp-1]
            col = num % 6
            ren = math.floor(num / 6)
            print("a", temp, "l", len(l), "r", ren,"c", col)
            matrix[ren-1][col-1] = num
            if len(l) == 1:
                l.pop(0)
            else:
                l.pop(temp-1)'''
    return matrix




print(matrixv_rand(matrix_c(6, 6)))
print(matrix2_c(6,6))