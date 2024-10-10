# def check(line, coin):
#     left, right, flag = line.split()
#     left = list(map(lambda x: ord(x) - 65, list(left)))
#     right = list(map(lambda x: ord(x) - 65, list(right)))
#     if flag == 'up':
#         flag = 1
#     elif flag == 'down':
#         flag = -1
#     else:
#         flag = 0
#     if flag == sum([coin[i] for i in left]) - sum([coin[i] for i in right]):
#         return True
#     else:
#         return False

# n = int(input())
# for _ in range(n):
#     result = [input() for _ in range(3)]
#     coin = [0]*12
#     for i in range(12):
#         coin[i] = 1
#         if check(result[0], coin) and check(result[1], coin) and check(result[2], coin):
#             h = 'heavy'
#             break
#         coin[i] = -1
#         if check(result[0], coin) and check(result[1], coin) and check(result[2], coin):
#             h = 'light'
#             break
#         coin[i] = 0
#     print(f'{chr(i + 65)} is the counterfeit coin and it is {h}.')
balToRes = {"up": 1, "even": 0, "down": -1}

for _ in range(int(input())):
    a = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [],
         'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []}
    res = []
    reverse_res = []

    for _ in range(3):
        left, right, bal = input().split(" ")

        for k in a:
            if k in left:
                a[k].append(1)
            elif k in right:
                a[k].append(-1)
            else:
                a[k].append(0)
        res.append(balToRes[bal])
        reverse_res.append(-balToRes[bal])

    for k, v in a.items():
        if v == res:
            print(f"{k} is the counterfeit coin and it is heavy.")
            break
        elif v == reverse_res:
            print(f"{k} is the counterfeit coin and it is light.")
            break