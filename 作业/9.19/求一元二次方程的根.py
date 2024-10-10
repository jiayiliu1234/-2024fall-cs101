import math

for _ in range(int(input())):
    a, b, c = map(float, input().split())
    delta = b ** 2 - 4 * a * c
    if b == 0:
        b = - b
    if delta > 0:
        x_1 = (- b + math.sqrt(delta)) / (2 * a)
        x_2 = (- b - math.sqrt(delta)) / (2 * a)
        x_1 = format(x_1, '.5f')
        x_2 = format(x_2, '.5f')
        print(f'x1={x_1};x2={x_2}')
    elif delta == 0:
        x_1 = - b / (2 * a)
        x_1 = format(x_1, '.5f')
        print(f'x1=x2={x_1}')
    else:
        im = format(math.sqrt(-delta) / (2 * a), '.5f')
        re = format(- b / (2 * a), '.5f')
        print(f"x1={re}+{im}i;x2={re}-{im}i")