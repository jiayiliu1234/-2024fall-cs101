n = int(input())
moneys = [100, 20, 10, 5, 1]
sum = 0
for money in moneys:
    sum += n // money
    n = n % money
print(sum)