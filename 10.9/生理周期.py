num = 1
while True:
    p, e, i, d = map(int, input().split())
    if (p, e, i, d) == (-1, -1, -1, -1):
        break
    day = d + 1
    while True:
        if day % 23 == p % 23 and day % 28 == e % 28 and day % 33 == i % 33:
            break
        else:
            day += 1
    print(f'Case {num}: the next triple peak occurs in {day - d} days.')
    num += 1