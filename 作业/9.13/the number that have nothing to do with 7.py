n = int(input())
sum = 0
for i in range(n + 1):
    if i % 7 != 0 and '7' not in str(i):
        sum += i ** 2
print(sum)