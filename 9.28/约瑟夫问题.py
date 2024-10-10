while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    monkeys = [(i + 1) for i in range(n)]
    last = 0
    while len(monkeys) > 1:
        next = monkeys[(last + m) % len(monkeys)]
        del monkeys[(last + m) % len(monkeys) - 1]
        last = monkeys.index(next)
    print(monkeys[0])