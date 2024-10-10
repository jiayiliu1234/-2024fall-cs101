def Fabonaci(n):
    Fabonaci = [1, 1]
    for i in range(1, n):
        Fabonaci.append(Fabonaci[i] + Fabonaci[i - 1])
    return Fabonaci

n = int(input())
fabonaci = Fabonaci(25)
for _ in range(n):
    a = int(input())
    print(fabonaci[a - 1])