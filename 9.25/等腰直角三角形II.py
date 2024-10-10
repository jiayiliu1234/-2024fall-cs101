n = int(input())
for i in range(n):
    if i == 0:
        print('*')
    elif i == n - 1:
        a = ['*']*(i + 1)
        a = ''.join(a)
        print(a)
    else:
        a = [' '] * (i - 1)
        a = ''.join(a)
        print('*' + a + '*')
