a = input()
b = input()
a_int = int(a)
b_int = int(b)
if a_int == 0 and b_int == 0:
    print(0)
else:
    a_list = [0] * (1000 - len(a)) + list(map(int, list(a)))
    b_list = [0] * (1000 - len(b)) + list(map(int, list(b)))
    c_list = [0] * 1000
    a_list.reverse()
    b_list.reverse()
    r = 0
    for i in range(1000):
        c_list[i] = (a_list[i] + b_list[i] + r) % 10
        r = (a_list[i] + b_list[i] + r) // 10
    flag = False
    c_list.reverse()
    for num in c_list:
        if num != 0:
            flag = True
        if flag:
            print(int(num), end='')