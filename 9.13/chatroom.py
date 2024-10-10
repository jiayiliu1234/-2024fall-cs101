a = list(input())
try:
    i_1 = a.index('h')
    i_2 = a[i_1 + 1:].index('e')
    i_3 = a[i_1 + i_2 + 2:].index('l')
    i_4 = a[i_1 + i_2 + i_3 + 3:].index('l')
    i_5 = a[i_1 + i_2 + i_3 + i_4 + 4:].index('o')
    print('YES')
except ValueError:
    print('NO')