sum = [0]*3 
for i in range(int(input())):
    a, b, c = map(int, input().split())
    sum[0] += a
    sum[1] += b
    sum[2] += c
if sum[0] == sum[1] == sum[2] == 0:
    print('YES')
else:
    print('NO')