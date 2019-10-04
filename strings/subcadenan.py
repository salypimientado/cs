from typing import Any, Union

from pip._vendor.msgpack.fallback import xrange

a = input()
m = input()
i = []
sc = []
num = 0

for c in a:
    i.append(c) #Lista de la cadena

for b in m:
    sc.append(b) #Lista de la subcadena


def rev():
    v = 0
    tr = True #Si se encontro la subcadena en la cadena

    for x in range(len(i)):     #Un loop que se repite la candidad de letras que tiene la cadena
        while len(i) >= len(sc):   #Mientras la cadena sea mas grande que la subcadena compararlas entre si
            for n in range(len(sc)):   #Compara las primeras letras de la cadena contra las letras de la subcadena de uno por uno
                if n < len(i):
                    if sc[n] != i[n]:
                        tr = False     #Si alguna letra de las primeras de la cadena es diferente que las de la subcadena tr se vuelve falso

            if tr:
                v += 1     #Si no se encontro ninguna letra que no coincidiera se sube el numero de veces por uno

            if len(i) >=1:
                i.pop(0)     #Si la lista de la cadena tiene 1 valor o mas se destruye el primer valor de la cadena para poder comparar el resto de la cadena con la subcadena
            tr = True
    return v   #devolver la cantidad de veces
