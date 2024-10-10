from collections import Counter
n = int(input())
ans = []
for _ in range(n):
    s = int(input())
    a = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    c_list = [s - i for i in a_list]
    c_count = Counter(c_list)
    c_list_count = [list(pair) for pair in c_count.items()]
    b = int(input())
    b_list = list(map(int, input().split()))
    b_list.sort(reverse=True)
    b_count = Counter(b_list)
    b_list_count = [list(pair) for pair in b_count.items()]
    num = 0
    i, j = 0, 0
    while i < len(c_list_count) and j < len(b_list_count):
        if c_list_count[i][0] == b_list_count[j][0]:
            num += c_list_count[i][1] * b_list_count[j][1]
            i += 1
            j += 1
        elif c_list_count[i][0] > b_list_count[j][0]:
            i += 1
        else:
            j += 1
    ans.append(num)
print(*ans, sep='\n')