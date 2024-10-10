a = list(map(int, list(input())))
flag = False
sum = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        sum = 1
    else:
        sum += 1
    if sum >= 7:
        flag = True
if flag == False:
    print('NO')
else:
    print('YES')