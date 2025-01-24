# Assignment #A: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>刘家亦，物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：dp，但是直接写答案也可以



代码：

```python
n = int(input())
dp = [0] * n
if n == 1:
    print(1)
    exit(0)
dp[0] = 1; dp[1] = 2
for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202114408789](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114408789.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：一道数学题



代码：

```python
print(2 ** (int(input()) - 1))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241202114420984](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114420984.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：和某道每日选做很像



代码：

```python
t, k = map(int, input().split())
mod = 10 ** 9 + 7
dp = [1] * (10 ** 5 + 1)
dp[k - 1] = 2
for i in range(k, 10 ** 5 + 1):
    dp[i] = (dp[i - 1] + dp[i - k]) % mod
pre_sum = [0] * (10 ** 5 + 2)
for i in range(1, 10 ** 5 + 2):
    pre_sum[i] = (pre_sum[i - 1] + dp[i - 1]) % mod
ans = []
for _ in range(t):
    a, b = map(int, input().split())
    ans.append((pre_sum[b] - pre_sum[a - 1]) % mod)
print(*ans, sep='\n')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202114529126](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114529126.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：马拉车还是蛮难想的，算法实现的细节很多



代码：

```python
class Solution:
    def expand(self, s, i, j):
        while 0 <= i and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (j - i - 2) // 2
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        length = [0] * len(s)
        right = -1
        j = -1
        start = 0; end = 0
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                arm_len = min(right - i, length[i_sym])
                length[i] = self.expand(s, i - arm_len - 1, i + arm_len + 1)
            else:
                length[i] = self.expand(s, i, i)
            if i + length[i] > right:
                j = i
                right = i + length[i]
            if 2 * length[i] + 1 > end - start:
                end = i + length[i]
                start = i - length[i]
        return s[start + 1:end + 1:2]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202114622247](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114622247.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：卡在这个逆天输入上，矩阵的读取一直不对，还没发现。提交了28次



代码：

```python
from collections import deque
import sys
input = sys.stdin.read
idx = 1
input = input().split()
results = []
for _ in range(int(input[0])):
    m, n = map(int, input[idx:idx + 2]); idx += 2
    matrix = []
    for _ in range(m):
        matrix.append(list(map(lambda x:[int(x), 0], input[idx:idx + n])))
        idx += n
    X, Y = map(int, input[idx:idx + 2]); idx += 2
    flag = False
    p = int(input[idx]); idx += 1
    for i in range(p):
        a, b = map(int, input[idx:idx + 2]); idx += 2
        h = matrix[a - 1][b - 1][0]
        if h <= matrix[X - 1][Y - 1][0]:
            continue
        q = deque([[a - 1, b - 1]])
        if h > matrix[a - 1][b - 1][1]:
            matrix[a - 1][b - 1][1] = h
        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and\
                    matrix[i + di][j + dj][0] < h and matrix[i + di][j + dj][1] < h:
                    q.append([i + di, j + dj])
                    matrix[i + di][j + dj][1] = h
    results.append("Yes" if matrix[X - 1][Y - 1][0] < matrix[X - 1][Y - 1][1] else "No")
sys.stdout.write("\n".join(results) + "\n")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202114727042](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114727042.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：也可以用dijstra算法



代码：

```python
from collections import deque
idx = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while True:
    idx += 1
    case = 0
    w, h = map(int, input().split())
    if w == h == 0:
        break
    print(f'Board #{idx}:')
    board = [[' '] * (w + 2)] + [[' '] + list(input()) + [' '] for _ in range(h)] + [[' '] * (w + 2)]
    while True:
        x1, y1, x2, y2 = map(lambda x: int(x), input().split())
        case += 1; flag = False
        if x1 == y1 == x2 == y2 == 0:
            break
        visited = [[False] * (w + 2) for _ in range(h + 2)]
        board[y2][x2] = ' '
        
        q = deque([(x1, y1, -1, 0)])
        visited[y1][x1] = True
        while q:
            i, j, prediction, depth = q.popleft()
            if i == x2 and j == y2:
                flag = True
                break
            for _ in range(4):
                ni = i + directions[_][0]; nj = j + directions[_][1]
                if 0 <= ni < w + 2 and 0 <= nj < h + 2 and board[nj][ni] == ' ' and not visited[nj][ni]:
                    visited[nj][ni] = True
                    if _ != prediction:
                        q.append((ni, nj, _, depth + 1))
                    else:
                        q.append((ni, nj, _, depth))
        if flag:
            print(f'Pair {case}: {depth} segments.')
        else:
            print(f'Pair {case}: impossible.')
        board[y2][x2] = 'X'
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202114759772](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241202114759772.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

额外跟进每日选做以及leetcode



