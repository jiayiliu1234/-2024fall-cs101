r, c = map(int, input().split())
n = int(input())
points = []
max_step = -1
for i in range(n): #读取稻田，将点添加到points中
    x, y = map(int, input().split())
    points.append([x - 1, y - 1])
points.sort()
for i in range(n):
    for j in range(i + 1, n): #遍历每一对点
        dy = points[j][0] - points[i][0]
        dx = points[j][1] - points[i][1]

        if [2 * points[i][0] - points[j][0], 2 * points[i][1] - points[j][1]] in points:
            continue
        elif points[i][0] + max(max_step, 2) * dy >= r or points[i][1] + max(max_step, 2) * dx >= c:
            break
        if (points[i][0] - dy > 0) and (points[i][1] - dx > 0):
            continue
        step = 0
        while [points[i][0] + step * dy, points[i][1] + step * dx] in points:
            step += 1
        if step > max_step:
            max_step = step

if max_step >= 3:
    print(max_step)
else:
    print(0)