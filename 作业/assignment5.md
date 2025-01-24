# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>刘家亦 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：暴力枚举，还有一种用中国剩余定理的方法，没放上来



代码：

```python
num = 1
while True:
    p, e, i, d = map(int, input().split())
    if (p, e, i, d) == (-1, -1, -1, -1):
        break
    day = d + 1
    while True:
        if day % 23 == p % 23 and day % 28 == e % 28 and day % 33 == i % 33:
            break
        else:
            day += 1
    print(f'Case {num}: the next triple peak occurs in {day - d} days.')
    num += 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028204853780](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028204853780.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：很早以前写的屎山代码了



代码：

```python
from collections import deque

def can_make_v():
    if len(cost) == 1:
        return False
    if p + cost[-1] <= cost[0]:
        return False
    return True
p = int(input())
cost = deque(sorted(list(map(int, input().split()))))
narudo = 0
enemy = 0
while cost:
    if cost[0] > p:
        if can_make_v():
            if narudo <= enemy:
                break
            else:
                enemy += 1
                p += cost.pop()
        else:
            break
    else:
        p -= cost.popleft()
        narudo += 1
print(narudo - enemy)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241028205011542](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028205011542.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n = int(input())
a = [(int(ai), i) for i, ai in zip(range(n), input().split())]
a.sort()
wait = 0
for i in range(n):
    wait += a[i][0] * (n - i - 1)
for i in range(n):
    print(a[i][1] + 1, end=' ')
print()
print(f'{(wait / n):.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241028205110278](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028205110278.png)

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：相较于其他同学的代码显得有些臃肿



代码：

```python
n = int(input())
ans = []
Hmonths = {"pop":1,"no":2,"zip":3,"zotz":4,"tzec":5,"xul":6,"yoxkin":7,"mol":8,"chen":9,"yax":10,"zac":11,"ceh":12,"mac":13,"kankin":14,"muan":15,"pax":16,"koyab":17,"cumhu":18,"uayet":19}
Tnames = {1:"imix",2:"ik",3:"akbal",4:"kan",5:"chicchan",6:"cimi",7:"manik",8:"lamat",9:"muluk",10:"ok",11:"chuen",12:"eb",13:"ben",14:"ix",15:"mem",16:"cib",17:"caban",18:"eznab",19:"canac",0:"ahau"}
for _ in range(n):
    Hdays = input().split()
    Hdays[0] = Hdays[0].replace(".", "")
    Hday = int(Hdays[0])
    Hmonth = Hmonths[Hdays[1]]
    Hyear = int(Hdays[2])
    day = Hday + 1 + (Hmonth - 1) * 20 + Hyear * 365
    if day % 260 != 0:
        Tyear = day // 260
    else:
        Tyear = day // 260 - 1
    Tname = Tnames[(day - 260 * Tyear) % 20]
    Tnumber = (day - 260 * Tyear) % 13
    if Tnumber == 0:
        Tnumber = 13
    ans.append(f"{Tnumber} {Tname} {Tyear}")
print(n)
print(*ans, sep = "\n")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028205336839](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028205336839.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python
# n = int(input())
# trees = [[-float('inf'), 0]]
# for _ in range(n):
#     x, h = map(int, input().split())
#     trees.append([x, h])
# trees.append([float('inf'), 0])
# num = 0
# for i in range(1, n + 1):
#     if trees[i][0] - trees[i - 1][0] > trees[i][1]:
#         num += 1
#     elif trees[i + 1][0] - trees[i][0] > trees[i][1]:
#         num += 1
#         trees[i][0] += trees[i][1]

# dp做法
n = int(input())
trees = [[-float('inf'), 0]]
for _ in range(n):
    trees.append(list(map(int, input().split())))
trees.append([float('inf'), 0])
dp = [[0, 0, 0] for _ in range(n + 2)]
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    if trees[i - 1][0] < trees[i][0] - trees[i][1]:
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + 1
        if trees[i - 1][0] + trees[i - 1][1] < trees[i][0] - trees[i][1]:
            dp[i][1] = dp[i][0] + 1
    if trees[i][0] + trees[i][1] < trees[i + 1][0]:
        dp[i][2] = dp[i][0] + 1
ans = max(dp[n])
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028205543518](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028205543518.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：常规的区间贪心



代码：

```python
# pylint: skip-file
import math
def solve(n, d):
    num = 1
    flag = False
    radar = []
    for i in range(n):
        x, y = map(int, input().split())
        if y > d:
            flag = True
        else:
            radar.append((x - math.sqrt(d ** 2 - y ** 2), x + math.sqrt(d ** 2 - y ** 2)))
    input()
    if flag:
        return -1
    radar.sort(key = lambda x: (-x[0], x[1]))
    left = radar[0][0]
    for i in range(len(radar)):
        if radar[i][1] < left:
            num += 1
            left = radar[i][0]
    return num

i = 0
while True:
    i += 1
    n, d = map(int, input().split())
    if (n, d) == (0, 0):
        break
    print(f'Case {i}: {solve(n, d)}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028205618862](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241028205618862.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





自己通常会在一道题上面因为某些细节花上很久的时间，或者有了思路却没有很好的将它实现而白白增加时间复杂度和完成它的难度，因此完成题目的效率不高，有以下几点需要改进：

1. 对于条件语句的判断：自己通常会写出一堆又臭又长的条件判断，不仅花费的时间多，而且还容易把自己绕晕过去。在书写条件判断语句的时候，应该先写一遍草稿，然后自己再好好梳理一下逻辑的结构，以期得到对代码的简化。比方说有很多题目可能需要在某个特定的循环中不执行，这可以通过对条件语句的限制来实现。
2. 然后是Number Game，这是一道博弈的题目，花了不少时间，主要是因为自己的代码逻辑没有完全想清楚，在想自己代码逻辑的时候可以尝试着先举几个conner case并提炼出其中要点来帮助自己思考。然后是自己可能想到了一个正确的思路，但是实现起来比较麻烦，这时候可以先自己提炼要点，再想一想有没有什么等价的更好的方案。如本题中判断小于某个值的个数就可以用这个值与期待的极限值做对比，或者用bisect也不错。因为要点是寻找某个特定值在列表中应该出现的位置，这时候就可以用bisect
3. 以上问题的最主要原因是没有严谨思考的意识，经常想着先提交一下，看看错误样例再修改，这样的结果通常就是拆东墙补西墙，这个样例过了，那个样例就过不了。应该争取把题目彻底想明白再做，做到一次AC
