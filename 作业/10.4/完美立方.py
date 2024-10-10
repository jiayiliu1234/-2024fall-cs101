n = int(input())
cube = [i ** 3 for i in range(n + 1)]

for m in range(2, n + 1):
    for i in range(2, m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if cube[m] == cube[i] + cube[j] + cube[k]:
                    print(f'Cube = {m}, Triple = ({i},{j},{k})')