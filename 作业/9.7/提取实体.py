def new_func(a):
    count = 0
    pre_has_hash = False
    for i in a:
        if i[:3] == '###':
            if pre_has_hash == False:
                count += 1
            pre_has_hash = True
        else:
            pre_has_hash = False
    return count

n = int(input())
result = 0
for i in range(n):
    result += new_func(input().split())
print(result)