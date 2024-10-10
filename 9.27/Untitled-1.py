n, w = map(int, input().split())
candys = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    candys.append([x, y])
candys.sort(key=lambda x: x[0] / x[1], reverse=True)
index_of_candy = 0
value = 0
while w > 0 and index_of_candy < n:
    if candys[index_of_candy][1] < w:
        w -= candys[index_of_candy][1]
        value += candys[index_of_candy][0]
    else:
        value += candys[index_of_candy][0] / candys[index_of_candy][1] * w
        w = 0
    index_of_candy += 1

print(f'{value:.1f}')