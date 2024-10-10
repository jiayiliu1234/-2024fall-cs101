#非常简洁的代码，使我的大脑旋转
s = list(input())
series = [0]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        series.append(0)
    else:
        series[-1] += 1
print(max(series) + 1)