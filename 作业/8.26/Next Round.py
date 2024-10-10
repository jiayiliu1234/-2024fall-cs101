l = input().split()
n = int(l[0])
k = int(l[1])
a = input().split()
if int(a[0]) == 0:
    print(0)
else:
    for i in range(n):
        if int(a[i]) >= int(a[k - 1]) and int(a[i]) != 0:
            m = i
        else:
            break
    print(m + 1)