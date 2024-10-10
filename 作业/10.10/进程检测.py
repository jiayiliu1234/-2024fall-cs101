k = int(input())
for _ in range(k):
    n = int(input())
    time = []
    for _ in range(n):
        time.append(list(map(int, input().split())))
    time.sort(key=lambda x: (-x[0], x[1]))
    left = time[0][0]
    num = 1
    for i in range(len(time)):
        if time[i][1] < left:
            left = time[i][0]
            num += 1
    print(num)
