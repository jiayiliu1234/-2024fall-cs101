import math

while True:
    a = list(map(int, input().split()))
    if a == [0] * 6:
        break
    num = a[5]
    a[5] = 0
    available = [0] * 6

    num += a[4]
    available[0] += a[4] * 11
    a[4] = 0

    num += a[3]
    available[1] += a[3] * 5
    a[3] = 0

    num += math.ceil(a[2] / 4)
    if a[2] % 4 == 3:
        available[0] += 5
        available[1] += 1
    elif a[2] % 4 == 2:
        available[0] += 6
        available[1] += 3
    elif a[2] % 4 == 1:
        available[0] += 7
        available[1] += 5
    a[2] = 0

    if available[1] >= a[1]:
        available[1] -= a[1]
        a[1] = 0
        available[0] += 4 * available[1]
    else:
        num += math.ceil((a[1] - available[1]) / 9)
        available[0] += 36 - 4 * ((a[1] - available[1]) % 9)
        a[1] = 0
    
    if a[0] > available[0]:
        num += math.ceil((a[0] - available[0]) / 36)
    
    print(num)