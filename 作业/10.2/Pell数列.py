Pell_mod = [1, 2]
i = 2
while True:
    Pell_mod.append((Pell_mod[i - 1] * 2 + Pell_mod[i - 2]) % 32767)
    if Pell_mod[i] == 1 and ((Pell_mod[i] * 2 + Pell_mod[i - 1]) % 32767 == 2):
        break
    i += 1
cycle = len(Pell_mod) - 1
n = int(input())
for _ in range(n):
    k = int(input())
    print(Pell_mod[k % cycle - 1])