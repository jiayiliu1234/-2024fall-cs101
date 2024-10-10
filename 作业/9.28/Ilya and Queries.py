s = list(input())
a = [1 if s[i] == s[i + 1] else 0 for i in range(len(s) - 1)]
a.append(0)
total = [a[0]]
for i in range(1, len(a)):
    total.append(total[i - 1] + a[i])
total.insert(0, 0)
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(total[r - 1]- total[l - 1])