import math

for _ in range(int(input())):
    a = int(input())
    x = int(math.log2(a))
    count = a * (a + 1) // 2 - 2 * (2 ** (x + 1) - 1)
    print(count)