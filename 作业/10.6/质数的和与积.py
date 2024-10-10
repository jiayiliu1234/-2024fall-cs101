def Euler_sieve(n):
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

s = int(input())
is_prime = Euler_sieve(s)
for i in range(s // 2, 1, -1):
    if is_prime[i] and is_prime[s - i]:
        ans = i * (s - i)
        break

print(ans)