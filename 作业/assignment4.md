# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>刘家亦、物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
# n, m = map(int, input().split())
numbers = sorted(list(map(lambda x: - int(x), input().split())), reverse = True)
total = sum(a for a in numbers[:m] if a > 0)
print(total)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241020204317625](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020204317625.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python
n = int(input())
coins = list(map(int, input().split()))
coins_sorted = sorted(coins, reverse = True)
total = 0
num = 0
for i in coins_sorted:
    if total > sum(coins_sorted) / 2:
        break
    total += i
    num += 1
print(num)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241020204342815](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020204342815.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：



代码

```python

def new_func():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_row = sum(a) + min(b) * n
    min_column = sum(b) + min(a) * n
    print(min(min_column, min_row))

t = int(input())
for i in range(t):
    new_func()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241020204419490](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020204419490.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：



代码

```python
from collections import Counter
n = int(input())
s = list(map(int, input().split()))
ans = 0
available = 0
s_dict = Counter(s)
ans += s_dict[4]
ans += s_dict[3]
ans += s_dict[2] // 2 + s_dict[2] % 2
available += s_dict[3] + (s_dict[2] % 2) * 2
if s_dict[1] > available:
    if (s_dict[1] - available) % 4 == 0:
        ans += (s_dict[1] - available) // 4
    else:
        ans += (s_dict[1] - available) // 4 + 1
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241020204500419](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020204500419.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：



代码

```python
def Euler_sieve(n):
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

n = int(input())
a = list(map(int, input().split()))

max_val = max(a)
is_prime = Euler_sieve(int(max_val ** 0.5) + 1)

ans = []

for num in a:
    if int(num**0.5)**2 != num or num < 4:
        ans.append('NO')
    elif is_prime[int(num**0.5)]:
        ans.append('YES')
    else:
        ans.append('NO')
# print(*ans, sep='\n')
print('\n'.join(ans))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241020204523680](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020204523680.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：



代码

```python
n = int(input())
nums = list(map(lambda x: (x, len(x)), input().split()))
nums_max = sorted(nums, reverse=True, key=lambda x: int(x[0]) / (10 ** x[1] - 1))
nums_min = sorted(nums, key=lambda x: int(x[0]) / (10 ** x[1] - 1))
MAX = [];MIN = []
for x in nums_max:
    MAX.append(x[0])
for x in nums_min:
    MIN.append(x[0])
print(f'{"".join(MAX)} {"".join(MIN)}')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241020211643931](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241020211643931.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



本周练习了一点深搜广搜的题目，然后学习了正则表达式，由于这周末有一些事情，所以未能进行计概的学习，导致学习内容略显单薄

做题感想：

1. 贪心算法的选择&print的耗时&合理选择排序，有的需要用最大最小值的题目在逆序排序以后就不用了，而且这样能做到剪枝&剪枝很重要
2. 缺少了对conner case的训练，可能要吃大亏。取模，数据范围容易出问题 
3. 一定要把数据读完！不能中间跳过！否则会RE
4. 做题前一定要先想一想
5. 一些有趣的函数/方法的使用能给做题带来一些遍历，如正则表达式等

