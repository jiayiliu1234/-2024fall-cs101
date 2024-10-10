n = int(input())
a = input().split()
length = 0
for i in range(len(a)):
    length += len(a[i]) + 1
    try:
        if length + len(a[i + 1]) > 80:
            print(a[i])
            length = 0
        else:
            print(a[i], end=' ')
    except IndexError:
        print(a[i])