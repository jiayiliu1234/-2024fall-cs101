import math
while True:
    min_time = float('inf')
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        arrive_time = (4500 * 3.6 / v) + t
        min_time = min(arrive_time, min_time)
    print(math.ceil(min_time))