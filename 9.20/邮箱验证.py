def check(a_str):
    a = list(a_str)
    if '@' in [a[0], a[-1]] or '.' in [a[0], a[-1]]:
        return False
    try:
        position = a.index('@')
        if a[position + 1] == '.' or a[position - 1] == '.':
            return False
        a_sliced = a[position + 1:]
        if '@' in a_sliced:
            return False
        elif '.' not in a_sliced:
            return False
        else:
            return True
    except ValueError:
        return False

try:
    while True:
        a = input()
        if check(a):
            print('YES')
        else:
            print('NO')
except EOFError:
    pass