n = int(input())
t = list(map(int, input().split()))
t.sort()
total_time = 0
num = 0
for i in range(n):
    if t[i] >= total_time:
        num += 1
        total_time += t[i]
print(num)