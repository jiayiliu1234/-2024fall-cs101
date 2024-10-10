try:
    while True:
        n = int(input())
        a = list(map(int, input().split()))
        a_sorted = sorted(a)
        if 2 * a_sorted[-1] >= sum(a_sorted):
            print(f'{(sum(a_sorted) - a_sorted):.1f}')
        else:
            print(f'{(sum(a_sorted) / 2):.1f}')
except EOFError:
    pass