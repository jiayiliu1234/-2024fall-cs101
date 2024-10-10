n = int(input())
for _ in range(n):
    l = sorted(map(int, input().split()))
    if int(l[0]) + int(l[1]) == int(l[2]):
        print('YES')
    else:
        print('NO')
