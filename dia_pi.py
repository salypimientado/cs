

def dia_pi():
    steps = int(input())
    print(sum((-1.0) ** n / (2.0 * n + 1.0) for n in reversed(range(steps))) * 4)


dia_pi()