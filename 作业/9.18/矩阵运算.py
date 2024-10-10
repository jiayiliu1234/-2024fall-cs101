r = []
c = []
matrix = []
for i in range(3):
    a, b = map(int, input().split())
    r.append(a)
    c.append(b)
    matrix.append([])
    for j in range(a):
        matrix[i].append(list(map(int, input().split())))
if c[0] != r[1] or r[0] != r[2] or c[1] != c[2]:
    print('Error!')
else:
    for i in range(r[0]):
        for j in range(c[1]):
            x = matrix[2][i][j]
            for k in range(c[0]):
                x += matrix[0][i][k] * matrix[1][k][j]
            print(x, end=' ')
        print()

# A=[];B = [];C=[]
# a,b= map(int,input().split())
# for _ in range(a):
#     A.append(list(map(int,input().split())))

# c,d=map(int,input().split())
# for _ in range(c):
#     B.append(list(map(int,input().split())))

# e,f=map(int,input().split())
# for _ in range(e):
#     C.append(list(map(int,input().split())))

# if a!=e or d!=f or b!=c:print('Error!')
# else:
#     for i in range(e):
#         for j in range(f):
#             C[i][j]+=sum(A[i][p]*B[p][j]for p in range(b))
#     for i in range(e):
#         print(*C[i])