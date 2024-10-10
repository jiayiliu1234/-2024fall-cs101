n, m, k = map(int, input().split())
matrix = [[False for j in range(m + 2)] for i in range(n + 2)]
step = 0
flag = False
for _ in range(k):
    i, j = map(int, input().split())
    matrix[i][j] = True
    for x in range(4):
        if (matrix[i][j]) and (matrix[i + (-1) ** (1 & (x >> 1))][j]) and (matrix[i][j + (-1) ** (1 & (x >> 0))]) and (matrix[i + (-1) ** (1 & (x >> 1))][j + (-1) ** (1 & (x >> 0))]) and not flag:
            step = _ + 1
            flag = True
print(step)