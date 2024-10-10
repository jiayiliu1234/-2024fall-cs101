n = int(input())
ans = []
num = []
for i in range(n):
    a = list(input())
    ans.append([])
    sum = 0
    for j in range(len(a)):
        if (int(a[j]) != 0):
            ans[i].append(str(int(a[j]) * 10 ** (len(a) - j - 1)))
            sum += 1
    num.append(sum)
    # ans.append([str(int(a[j]) * 10 ** (len(a) - j - 1)) for j in range(len(a))])
for i in range(n):
    print(num[i])
    print(" ".join(ans[i]))