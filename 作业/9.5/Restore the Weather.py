def new_func():
    m, n = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())
    enumerate_a = enumerate(a)
    a_sorted = sorted(enumerate_a, key = lambda x: x[1])
    b_sorted = sorted(b)
    ans = [(a_sorted[i][0], b_sorted[i]) for i in range(m)]
    ans_sorted = sorted(ans, key = lambda x: x[0])
    for x in ans_sorted:
        print(x[1], end = ' ')
    print()

t = int(input())
for i in range(t):
    new_func()
