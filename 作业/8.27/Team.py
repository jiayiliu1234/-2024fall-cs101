def count(a):
    sum = 0
    for i in range(3):
        if int(a[i]) == 1:
            sum += 1
    if sum >= 2:
        return 1
    else:
        return 0
    
n = int(input())
num = 0
for i in range(n):
    line = input().split()
    num += count([int(x) for x in line])
print(num)