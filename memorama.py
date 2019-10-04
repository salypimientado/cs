import math
import random






def juego():

    nums = matrixv_rand(matrix_c(6,6))

    noc = matrix2_c(6,6)

    for line in noc:
        print(*line)
    for a in range(len(noc)):
        while "-" in noc[a]:
            presbut(nums, noc)

    print("Ganaste!")

def matrix_c(s1, s2):
    matrix = [[0 for x in range(s1)] for y in range(s2)]
    return matrix

def matrix2_c(s1, s2):
    matrix = [["-" for x in range(s1)] for y in range(s2)]
    return matrix

def matrixv_rand(matrix):

    v1 = 0
    v2 = 1

    li = list(range(1, 19))
    for x in range(1,19):
        li.append(x)
    random.shuffle(li)

    for x in range(len(matrix)):
        for m in range(len(matrix[x-1])):
            matrix[x-1][m-1] =  li[0]
            li.pop(0)
    return matrix

def presbut(m1, m2):
    x1 = int(input("Introduzca la columna de su eleccion\n"))
    y1 = int(input("Introduzca la fila de su eleccion\n"))
    n1 = m1[y1-1][x1-1]
    m2[y1-1][x1-1] = m1[y1-1][x1-1]
    for line in m2:
        print(*line)
    x2 = int(input("Introduzca la columna de su segunda eleccion\n"))
    y2 = int(input("Introduzca la columna de su secunda eleccion\n"))
    n2 = m1[y2-1][x2-1]
    if n1 == n2:
        m2[y2-1][x2-1] = m1[y2-1][x2-1]
        for line in m2:
            print(*line)

    else:

        m2[y2 - 1][x2 - 1] = m1[y2 - 1][x2 - 1]
        for line in m2:
            print(*line)
        print("\n")
        m2[y1 - 1][x1 - 1] = "-"
        m2[y2 - 1][x2 - 1] = "-"


    return m2


juego()