n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
a_dict = {}
for i in a:
    try:
        a_dict[i] += 1
    except KeyError:
        a_dict[i] = 1
a_list = list(a_dict.values())
print(max(a_list))