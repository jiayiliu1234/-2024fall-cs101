n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
for i in range(1, n):
    if numbers[i] != numbers [i - 1]:
        print(f'{numbers[i - 1]} {numbers.count(numbers[i - 1])}')
print(f'{numbers[n - 1]} {numbers.count(numbers[n - 1])}')