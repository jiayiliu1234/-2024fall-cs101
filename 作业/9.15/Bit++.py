x = 0
for i in range(int(input())):
    a = input()
    if '++' in a:
        x += 1
    elif '--' in a:
        x -= 1
print(x)