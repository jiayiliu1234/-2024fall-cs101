n, q = map(int, input().split())
relations = []
flag = False
is_liked = [[False for i in range(n)] for j in range(n)]
for _ in range(q):
    x, y = map(int, input().split())
    is_liked[x - 1][y - 1] = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            if is_liked[i][j] and is_liked[j][k] and is_liked[k][i]:
                flag = True
if flag:
    print('Yes')
else:
    print('No')