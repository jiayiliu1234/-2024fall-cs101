n = int(input())
a = list(input())
num = 0
for i in range(1, n):
    if a[i] == a[i - 1]:
        num += 1
print(num)