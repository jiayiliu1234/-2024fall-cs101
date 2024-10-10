def Hanoi(n, l, m, r): #多传一点参数也没问题
    if n == 1:
        print(f'{l} -> {r}')
        return
    Hanoi(n - 1, l, r, m) 
    print(f'{l} -> {r}')
    Hanoi(n - 1, m, l, r)

n = int(input())
Hanoi(n, 'A', 'B', 'C')