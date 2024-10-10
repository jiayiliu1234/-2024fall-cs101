n = int(input())
dict = ['love', 'hate']
for i in range(n - 1, -1, -1):
    if i == 0:
        print(f'I {dict[abs(i - n) % 2]} it', end='')
        break
    print(f'I {dict[abs(i - n) % 2]} that ', end='')
