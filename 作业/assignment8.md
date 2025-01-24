# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：原本是一个dfs，但是由于图只会遍历一次，所以就转化成了一个普通的遍历问题



代码：

```python
n,m = map(int,input().split())
l = [[0]*(m+2)] +[[0] +list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
ans = 0
for i in range(1,n+1):
    for j in range(1, m + 1):
        if l[i][j] == 1:
            ans += 4-l[i+1][j]-l[i][j+1]-l[i-1][j]-l[i][j-1]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117225040919](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241117225040919.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：模版题



代码：

```python
import math
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
num = 1
col = 0; row = 1
for i in range(math.ceil(n / 2)):
    x, y = i, i
    if n == 2 * i + 1:
        matrix[x][y] = n ** 2
        break
    for row, col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        for j in range(n - 2 * i - 1):
            matrix[x][y] = num
            num += 1
            x += row
            y += col
for i in range(n):
    print(*matrix[i])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241117224910489](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241117224910489.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d = int(input())
n = int(input())
city = [[0 for _ in range(1025)] for _ in range(1025)]

for _ in range(n):
    x, y, i = map(int, input().split())
    for dx in range(-d, d + 1):
        for dy in range(-d, d + 1):
            if 0 <= x + dx < 1025 and 0 <= y + dy < 1025:
                city[x + dx][y + dy] += i

MAX = max(max(row) for row in city)
num = sum(1 for row in city for value in row if value == MAX)

print(f'{num} {MAX}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117224736843](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241117224736843.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：原来是个greedy，学dp入脑了，这可不太好。以后遇到题目还是先想一想greedy做法吧



代码：

```python
# 原来是个greedy，学dp入脑了
n = int(input())
a = list(map(int, input().split()))
dp_pos = [1] * n
dp_neg = [1] * n
for i in range(n):
    for j in range(i):
        if (dp_pos[j] % 2 == 0 and a[i] < a[j]) or (dp_pos[j] % 2 == 1 and a[i] > a[j]):
            dp_pos[i] = max(dp_pos[i], dp_pos[j] + 1)
        if (dp_neg[j] % 2 == 0 and a[i] > a[j]) or (dp_neg[j] % 2 == 1 and a[i] < a[j]):
            dp_neg[i] = max(dp_neg[i], dp_neg[j] + 1)
print(max(max(dp_pos), max(dp_neg)))
# greedy的思路是：如果一个元素不能加到这个序列中，那么就将序列的最后一个元素改为这个新的元素，这样下一个元素就更可能加入这个序列
# 这种方法能行的根本原因：dp_neg和dp_pos是有关系的，用dp就把它们割裂开了
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241113202232670](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241113202232670.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：dp



代码：

```python
n = int(input())
a = sorted(list(map(int, input().split())))
dic = [0] * (max(a) + 1)
for i in range(n):
    dic[a[i]] += a[i]
dp = [0] * len(dic)
dp[0] = dic[0]; dp[1] = dic[1]
for i in range(2, len(dic)):
    dp[i] = max(dic[i] + dp[i - 2], dic[i] + dp[i - 3], dp[i - 1])
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241113202351921](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241113202351921.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：贪心



代码：

```python
from collections import deque
while True:
    n = int(input())
    ans = 0
    if n == 0:
        break
    a = deque(sorted(list(map(int, input().split())), reverse=True))
    b = deque(sorted(list(map(int, input().split())), reverse=True))
    while a:
        if b[0] > a[0]:
            b.popleft()
            a.pop()
            ans -= 1
        elif b[0] < a[0]:
            a.popleft()
            b.popleft()
            ans += 1
        elif b[-1] > a[-1]:
            a.pop()
            b.popleft()
            ans -= 1
        elif b[-1] < a[-1]:
            a.pop()
            b.pop()
            ans += 1
        elif a[-1] == b[-1]:
            if b[0] > a[-1]:
                ans -= 1
            a.pop()
            b.popleft()
    print(ans * 200)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117225102116](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241117225102116.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉自己有点太追求代码的完美了，希望能一次性写出既简洁性能又好的代码，这就导致了自己摘抉择思路和写代码时的犹豫不决，反而导致自己没有办法做题。现在的思路是先写出一个不那么完美的代码，再参照答案或者使用AI进行修改。

