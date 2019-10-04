w = float(input())
h = float(input())

i = w/(h*h)

if i < 20:
    print('PESO BAJO')

if 20 <i < 25:
    print('NORMAL')

if 25 <i < 30:
    print('SOBRE PESO')

if 30 <i < 40:
    print('OBESIDAD')

if i >= 40:
    print('OBESIDAD MORBIDA')
