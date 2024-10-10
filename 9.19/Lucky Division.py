n = int(input())
others = ['1', '2', '3', '5', '6', '8', '9', '0']
find = False
for i in range(1, n + 1):
    if n % i == 0:
        flag = False
        for num in others:
            if num in str(i):
                flag = True
                break
        if flag:
            continue
        else:
            find = True
            break
if find:
    print('YES')
else:
    print('NO')
