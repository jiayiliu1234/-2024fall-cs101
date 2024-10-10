while True:
    win = 0
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    b = list(map(int, input().split()))
    b = sorted(b, reverse=True)
    while len(a) > 1:
        if a[0] > b[0]:
            del a[0]
            del b[0]
            win += 1
        elif a[0] < b[0]:
            del a[-1]
            del b[0]
            win -= 1
        elif a[-1] > b[-1]:
            del a[-1]
            del b[-1]
            win += 1
        elif a[-1] <= b[-1]:
            if a[-1] < b[0]:
                win -= 1
            del a[-1]
            del b[0]
    if a[0] > b[0]:
        win += 1
    elif a[0] < b[0]:
        win -= 1
    print(win * 200)