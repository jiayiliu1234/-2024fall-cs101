a = input().split()
# n = int(a[0])
# k = int(a[1])
# l = int(a[2])
# c = int(a[3])
# d = int(a[4])
# p = int(a[5])
# nl = int(a[6])
# np = int(a[7])
n, k, l, c, d, p, nl, np = map(int, input().split())
print(min(k * l // nl, c * d, p // np) // n)