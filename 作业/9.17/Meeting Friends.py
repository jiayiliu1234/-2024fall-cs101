situation = map(int, input().split())
situation_sorted = sorted(situation)
print(situation_sorted[2] - situation_sorted[0])