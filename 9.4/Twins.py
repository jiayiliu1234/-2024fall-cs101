n = int(input())
coins = list(map(int, input().split()))
coins_sorted = sorted(coins, reverse = True)
total = 0
num = 0
for i in coins_sorted:
    if total > sum(coins_sorted) / 2:
        break
    total += i
    num += 1
print(num)