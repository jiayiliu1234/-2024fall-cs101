while True:
    total = 0
    n = int(input())
    if n == 0:
        break
    position = 0
    h = int(input()) * 12
    f = list(map(int , input().split()))
    d = list(map(int , input().split()))
    t = list(map(int, input().split()))
    time = [[0 for _ in range(n)] for _ in range(n)]
    ans = []
    for i in range(n):
        t_available = h - sum(t[:i])
        fish = f[:i + 1]
        total = 0
        while t_available >= 1:
            t_available -= 1
            num_of_fish = max(fish)
            index_of_lake = fish.index(num_of_fish)
            if fish[index_of_lake] > d[index_of_lake]:
                fish[index_of_lake] -= d[index_of_lake]
            else:
                fish[index_of_lake] = 0
            total += num_of_fish
            time[i][index_of_lake] += 5
        ans.append(total)
    max_ans = max(ans)
    index_of_ans = ans.index(max_ans)
    print(*time[index_of_ans], sep=', ')
    print(f'Number of fish expected: {max_ans}')
    print()