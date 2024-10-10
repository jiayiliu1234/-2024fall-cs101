n = int(input())
ans = []
for i in range(n):
    a = input().split()
    if int(a[0]) % int(a[1]) == 0:
        ans.append(0)
    else:
        x = int(a[0]) // int(a[1])
        ans.append((x + 1) * int(a[1]) - int(a[0]))
for i in ans:
    print(i)
