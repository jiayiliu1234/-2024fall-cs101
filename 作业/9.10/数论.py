def prime_factors(n):
    factor = []
    while n % 2 == 0:
        factor.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1):
        while n % i == 0:
            factor.append(i)
            n //= i
    if n > 2:
        factor.append(n)
    return factor

n = int(input())
num = 1
flag = False
factor = prime_factors(n)
factor.append(0)
for i in range(1, len(factor)):
    if factor[i] == factor[i - 1]:
        num += 1
    else:
        if num % 2 == 0:
            flag = True
            break
        num = 1
if flag:
    print(0)
else:
    if len(factor) % 2 == 0:
        print(-1)
    else:
        print(1)