def decompasitions(n, factor):
    count = 0
    if n == 1:
        return 1
    for i in range(factor, n + 1):
        if n % i == 0:
            count += decompasitions(n // i, i)
    return count

for _ in range(int(input())):
    a = int(input())
    print(decompasitions(a, 2))