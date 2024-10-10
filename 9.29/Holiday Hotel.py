while True:
    hotels = []
    num = 0
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        hotels.append(list(map(int, input().split())))
    hotels.sort(key = lambda x: (x[0], x[1]))
    min = 10 ** 9
    for i in range(n):
        if hotels[i][1] < min:
            min = hotels[i][1]
            num += 1
    print(num)