num_of_case = int(input())
for _ in range(num_of_case):
    l, n = map(int, input().split())
    ants = list(map(int, input().split()))
    lenghth_min = []
    lenghth_max = []
    for ant in ants:
        lenghth_min.append(min(ant, l - ant))
        lenghth_max.append(max(ant, l - ant))
    print(f'{max(lenghth_min)} {max(lenghth_max)}')