def fabonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)
    
for _ in range(int(input())):
    print(fabonacci(int(input())))