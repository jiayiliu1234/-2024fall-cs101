def calculate(a, b):
    if b != 0:
        return calculate(b, a % b)
    else:
        return a

try:
    while True:
        a, b = map(int, input().split())
        print(calculate(a, b))
except EOFError:
    pass