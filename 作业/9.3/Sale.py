n, m = map(int, input().split())
numbers = sorted(list(map(lambda x: - int(x), input().split())), reverse = True)
total = sum(a for a in numbers[:m] if a > 0)
print(total)