def count(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count % 2 == 1:
        return True
    else:
        return False

list_of_num = []
for i in range(1, 110):
    list_of_num.append(count(i))

n = int(input())
for _ in range(n):
    a = int(input())
    print(sum(list_of_num[:a]))