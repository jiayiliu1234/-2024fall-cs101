day = list(map(int, input().split('-')))
n = int(input())
month = {1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:31, 7:30, 8:31, 9:30, 10:31, 11:30, 12:31}
while n > 0:
    if day[1] > 12:
        day[1] -= 12
        day[0] += 1
    if day[1] == 2 and ((day[0] % 4 == 0 and day[0] % 100 != 0) or day[0] % 400 == 0):
        month[2] = 29
    else:
        month[2] = 28
    if n > (month[day[1]] - day[2]):
        n -= (month[day[1]] - day[2] + 1)
        day[1] += 1
        day[2] = 1
    else:
        day[2] += n
        n = 0
if day[1] < 10:
    day[1] = '0'+str(day[1])
if day[0] < 10:
    day[0] = '0'+str(day[0])
print(f'{day[0]}-{day[1]}-{day[2]}')