l = input().split()
m = int(l[0])
n = int(l[1])
a = int(l[2])
if m % a != 0 and n % a != 0:
    print((m // a + 1) * (n // a + 1))
elif m % a == 0 and n % a != 0:
    print((m // a) * (n // a + 1))
elif n % a == 0 and m % a != 0:
    print((m // a + 1) * (n // a))
else:
    print((m // a) * (n // a))