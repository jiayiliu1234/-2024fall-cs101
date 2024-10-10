def count_number(n):
    count = 0
    while n >= 0:
        count += 1
        n -= 1 / (count + 1)
    return count

while True:
    a = float(input())
    if a == 0:
        break
    print(f'{count_number(a)} card(s)')
# 浮点数与0比较需要 用 math.isclose(....)，而不能直接用 == 0.00判断。