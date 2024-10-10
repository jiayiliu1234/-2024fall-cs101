# n = int(input())
# for i in range(n):
#     a, b, c, d = map(int, input().split())
#     flag = False
#     for i in range(15):
#         if (-1) ** ((i >> 0) & 1) * a + (-1) ** ((i >> 1) & 1) * b + (-1) ** ((i >> 2) & 1) * c + ((i >> 3) & 1) * d == 24:
#             flag = True
#             break
#     if flag == True:
#         print('YES')
#     else:
#         print('NO')
n = int(input())
for i in range(n):
    flag = False
    a, b, c, d = map(int, input().split())
    flag = False
    for i in range(15):
        if (-1) ** ((i >> 0) & 1) * a + (-1) ** ((i >> 1) & 1) * b + (-1) ** ((i >> 2) & 1) * c + ((i >> 3) & 1) * d == 24:
            flag = True
            break
    if flag == True:
        print('YES')
    else:
        print('NO')