while True:
    n, p, m = map(int, input().split())
    if (n, p, m) == (0, 0, 0):
        break
    cycle = list(range(n))
    begin = cycle[p - 1]
    ans = []
    while len(cycle) > 0:
        position = (cycle.index(begin) + m) % len(cycle)
        begin = cycle[position]
        ans.append(cycle[position - 1] + 1)
        del cycle[position - 1]
    print(*ans, sep=',')