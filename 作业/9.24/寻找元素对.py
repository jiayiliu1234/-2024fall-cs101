n = int(input())
a = list(map(int, input().split()))
k = int(input())
num = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            num += 1
print(num)