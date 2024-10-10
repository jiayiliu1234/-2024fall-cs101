def Euler_sieve(n):
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

n = int(input())
a = list(map(int, input().split()))

max_val = max(a)
is_prime = Euler_sieve(int(max_val ** 0.5) + 1)

ans = []

for num in a:
    if int(num**0.5)**2 != num or num < 4:
        ans.append('NO')
    elif is_prime[int(num**0.5)]:
        ans.append('YES')
    else:
        ans.append('NO')
# print(*ans, sep='\n')
print('\n'.join(ans))