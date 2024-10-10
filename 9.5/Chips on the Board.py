def new_func():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_row = sum(a) + min(b) * n
    min_column = sum(b) + min(a) * n
    print(min(min_column, min_row))

t = int(input())
for i in range(t):
    new_func()