def check_ans(ans):
    for i in range(2, 6):
        for j in range(1, 7):
            ans[i][j] = (matrix[i - 1][j] + ans[i - 2][j] + ans[i - 1][j - 1] + ans[i - 1][j + 1] + ans[i - 1][j]) % 2 #ans：是否按灯=>上面的灯是否亮着 亮着：按 不亮：不按
    for i in range(1, 7):
        if (matrix[5][i] + ans[5][i] + ans[4][i] + ans[5][i - 1] + ans[6][i] + ans[5][i + 1]) % 2 == 1:
            return False
    return True
                
def solve():
    for i in range(64):
        ans = [[0 for _ in range(8)] for _ in range(7)]
        for j in range(1, 7):
            if i & (1 << (j - 1)):
                ans[1][j] = 1
        if check_ans(ans):
            break
    for i in range(1, 6):
        for j in range(1, 7):
            print(f'{ans[i][j]}', end=' ')
        print()

matrix = [[0 for _ in range(8)] for _ in range(7)]
for i in range(1, 6):
    a = list(map(int, input().split()))
    for j in range(1, 7):
        matrix[i][j] = a[j - 1]
solve()
