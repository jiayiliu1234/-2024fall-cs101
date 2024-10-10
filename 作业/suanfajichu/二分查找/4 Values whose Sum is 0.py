# def BinarySearch(target):
#     left, right = 0, len(sum2) - 1
#     mid = (left + right) // 2
#     while left < right:
#         mid = (left + right) // 2
#         if sum2[mid] >= target:
#             right = mid
#         else:
#             left = mid + 1
#     num = 0
#     while left <= len(sum2) - 1 and sum2[left] == target:
#         num += 1
#         left += 1
#     return num

# n = int(input())
# A, B, C, D = [], [], [], []
# for _ in range(n):
#     a, b, c, d = map(int, input().split())
#     A.append(a)
#     B.append(b)
#     C.append(c)
#     D.append(d)
# sum1 = []
# sum2 = []
# for i in range(n):
#     for j in range(n):
#         sum1.append(A[i] + B[j])
#         sum2.append(C[i] + D[j])
# sum1.sort()
# sum2.sort()
# total = 0
# for a in sum1:
#     total += BinarySearch(-a)
# print(total)
n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())
dict = {}
for i in range(n):
    for j in range(n):
        if a[i] + b[j] not in dict:
            dict[a[i] + b[j]] = 0
        dict[a[i] + b[j]] += 1
num = 0
for i in range(n):
    for j in range(n):
        if -(c[i] + d[j]) in dict:
            num += dict[-(c[i] + d[j])]
print(num)