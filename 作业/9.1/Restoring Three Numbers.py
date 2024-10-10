a = input().split()
a = [int(i) for i in a]
x = max(a[0], a[1], a[2], a[3])
a.remove(x)
print(x - a[0], x - a[1], x - a[2])