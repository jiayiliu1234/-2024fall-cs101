n, m = map(int, input().split())
numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
ans = []
for num in numbers2:
    ans.append(numbers1.count(num))
for i in range(len(ans) - 1):
    print(ans[i], end=' ')
print(ans[-1])