a = int(input())

if 0 <= a < 90:
    print('1')

if 90 < a < 180:
    print('2')

if 180 < a < 270:
    print('3')

if 270 < a < 360:
    print('4')

if a == 90 or a == 180 or a == 270 or a == 360:
    print('eje')

if a > 360 or a < 0:
    print('excede')

