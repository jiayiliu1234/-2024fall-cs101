# l, m = map(int, input().split())
# is_Tree = [True for i in range(l + 1)]
# sum = 0
# for i in range(m):
#     begin, end = map(int, input().split())
#     for i in range(begin, end + 1):
#         is_Tree[i] = False
# for i in is_Tree:
#     if i:
#         sum += 1
# print(sum)

l, m = map(int, input().split())
is_Tree = [0] * (l + 1)

# 标记区间
for _ in range(m):
    begin, end = map(int, input().split())
    is_Tree[begin] -= 1
    if end + 1 <= l:
        is_Tree[end + 1] += 1

# 计算前缀和，得到是否为树
count = 0
current = 0
for i in range(l + 1):
    current += is_Tree[i]
    if current == 0:
        count += 1

print(count)
