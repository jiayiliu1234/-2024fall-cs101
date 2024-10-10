n, m = map(int, input().split())
bulbs = set()
for i in range(n):
    Input = list(map(int, input().split()))
    bulb = Input[1:]
    bulbs.update(bulb)
if len(bulbs) == m:
    print('YES')
else:
    print('NO')