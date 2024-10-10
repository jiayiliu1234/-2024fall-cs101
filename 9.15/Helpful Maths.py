input_str = input().replace('+', '')
number = list(map(int, input_str))
number.sort()
print('+'.join(map(str, number)))