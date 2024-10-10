for i in range(5):
    a = input().split()
    for j in range(5):
        if int(a[j]) == 1:
            m = i
            n = j
print(abs(m - 2) + abs(n - 2))
