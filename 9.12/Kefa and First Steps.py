n = int(input())
a = list(map(int, input().split()))
length_of_a = []
length = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        length += 1
    else:
        length_of_a.append(length)
        length = 1
length_of_a.append(length)
print(max(length_of_a))