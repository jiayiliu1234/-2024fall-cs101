#逆序列表：.reverse()

def func(n, k):
    ans = []
    while n != 0:
        ans.append(n % k)
        n = n // k
    ans.reverse()
    return ans

n, k = map(int, input().split())
num = func(n, k)
ans = []
dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
for i in num:
    if i <= 9:
        ans.append(i)
    else:
        ans.append(dict[i])
print(*ans, sep='')