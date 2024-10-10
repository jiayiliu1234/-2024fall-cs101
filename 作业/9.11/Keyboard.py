# keyboard = [list('qwertyuiop'), list('asdfghjkl;'), list('zxcvbnm,./')]
# def find_element(key):
#     for i, row in enumerate(keyboard):
#         for j, element in enumerate(row):
#             if element == key:
#                 return (i, j)

# x = input()
# msg = list(input())
# if x == 'R':
#     shift = 1
# else:
#     shift = -1
# for key in msg:
#     i, j = find_element(key)[0], find_element(key)[1]
#     print(keyboard[i][j-shift],end='')
d = input()
s = input()
kb = 'qwertyuiopasdfghjkl;zxcvbnm,./'

if d=='R':
        for c in s:
                print(kb[kb.index(c) - 1], end='')
else:
        for c in s:
                print(kb[kb.index(c) + 1], end='')

print()