n = int(input())
binary_rep = bin(n)[2:]
check = True
for i in range(len(binary_rep)):
    if binary_rep[i] != binary_rep[- i - 1]:
        check = False
if check:
    print('Yes')
else:
    print('No')