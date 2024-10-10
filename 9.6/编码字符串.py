a = list(input().lower())
num = 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        print(f'({a[i]},{num})', end='')
        num = 1
    else:
        num += 1
print(f'({a[len(a) - 1]},{num})')