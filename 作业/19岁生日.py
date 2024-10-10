n = int(input())
for _ in range(n):
    a = int(input())
    a_str = str(a)
    if a % 19 == 0 or '19' in a_str:
        print('Yes')
    else:
        print('No')