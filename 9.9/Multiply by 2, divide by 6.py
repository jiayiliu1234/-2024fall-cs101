def divided_by_k(n, k):
    a = 0
    while n % k == 0:
        n = n // k
        a += 1
    return a

l = int(input())
for i in range(l):
    n = int(input())
    twos = divided_by_k(n ,2)
    threes = divided_by_k(n, 3)
    if n != 2 ** twos * 3 ** threes:
        print(-1)
    elif threes < twos:
        print(-1)
    else:
        print(2 * threes - twos)
