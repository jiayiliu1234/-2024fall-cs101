n = int(input())
v = list(map(int, input().split()))
sum_v = [v[0]]
for i in range(1, n):
    sum_v.append(sum_v[i - 1] + v[i])
sum_v = [0] + sum_v
u = sorted(v)
sum_u = [u[0]]
for i in range(1, n):
    sum_u.append(sum_u[i - 1] + u[i])
sum_u = [0] + sum_u
m = int(input())
ans = []
for _ in range(m):
    Type, l, r = map(int, input().split())
    if Type == 1:
        ans.append(sum_v[r] - sum_v[l - 1])
    else:
        ans.append(sum_u[r] - sum_u[l - 1])
print(*ans, sep='\n')