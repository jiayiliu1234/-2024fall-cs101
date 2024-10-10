def diviser(a):
    while a % 2 == 0:
        a = a // 2
    return(a)

ans = []
n = int(input())
for i in range(n):
    a = int(input())
    if diviser(a) == 1:
        ans.append('NO')
    else:
        ans.append('YES')

for i in ans:
    print(i)