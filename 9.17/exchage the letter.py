a = list(input())
big_letter = range(65, 91)
small_letter = range(97, 123)
for i in range(len(a)):
    if ord(a[i]) in big_letter:
        a[i] = chr(ord(a[i]) + 32)
    elif ord(a[i]) in small_letter:
        a[i] = chr(ord(a[i]) - 32)
print(''.join(a))