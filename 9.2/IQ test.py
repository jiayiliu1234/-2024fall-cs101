n = int(input())
a = input().split()
ans = []
for i in range(n):
    ans.append(int(a[i]) % 2)
if ans[n - 1] != ans[n - 2] and ans[n - 1] != ans[0]:
    print(n)
else:
    for i in range(n - 1):
        if ans[i] != ans[i - 1] and ans[i] != ans[i + 1]:
            print(i + 1)
            break
