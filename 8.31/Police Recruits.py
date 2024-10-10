n = int(input())
a = input().split()
sum = 0
num = 0
for i in a:
    if int(i) > 0:
        num += int(i)
    else:
        if num <= 0:
            sum += 1
            num = 0
        else:
            num -= 1
print(sum)