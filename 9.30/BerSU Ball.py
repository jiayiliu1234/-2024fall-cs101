n = int(input())
boys = sorted(list(map(int, input().split())))
m = int(input())
girls = sorted(list(map(int, input().split())))
i, j = 0, 0
num = 0
while i < n and j < m:
    if abs(boys[i] - girls[j]) <= 1:
        i += 1
        j += 1
        num += 1
    elif boys[i] < girls[j]:
        i += 1
    elif boys[i] > girls[j]:
        j += 1
print(num)