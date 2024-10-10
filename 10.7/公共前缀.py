n = int(input())
s = []
for _ in range(n):
    s.append(list(input()))
length = [len(i) for i in s]
flag = True
for i in range(min(length)):
    for j in range(n):
        if s[j][i] != s[0][i]:
            flag = False
    if not flag:
        i = i - 1
        break
if i == 0:
    print()
else:
    print(*s[0][:i + 1:], sep='')