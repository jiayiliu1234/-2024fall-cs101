for _ in range(int(input())):
    angle = int(input())
    angle1 = 180 - angle
    if (360 / angle1).is_integer():
        print('YES')
    else:
        print('NO')