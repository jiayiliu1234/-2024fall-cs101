n = int(input())
weekday = {0:'Sunday', 1: 'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
for _ in range(n):
    days = input()
    c = int(days[0:2])
    y = int(days[2:4])
    if (int(days[4:6]) == 1 or int(days[4:6])== 2) and y % 100 != 0:
        m = int(days[4:6]) + 12
        y -= 1
    elif (int(days[4:6]) == 1 or int(days[4:6])== 2) and y % 100 == 0:
        m = int(days[4:6]) + 12
        y = 99
        c -= 1
    else:
        m = int(days[4:6])
    d = int(days[6:8])
    print(weekday[(y + int(y / 4) + int(c / 4) - 2*c + int(26 * (m + 1) / 10) + d - 1) % 7])
