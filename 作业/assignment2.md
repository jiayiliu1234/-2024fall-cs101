# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
for i in range(5):
    a = input().split()
    for j in range(5):
        if int(a[j]) == 1:
            m = i
            n = j
print(abs(m - 2) + abs(n - 2))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924150314861](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924150314861.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
n = int(input())
ans = []
for i in range(n):
    a = input().split()
    if int(a[0]) % int(a[1]) == 0:
        ans.append(0)
    else:
        x = int(a[0]) // int(a[1])
        ans.append((x + 1) * int(a[1]) - int(a[0]))
for i in ans:
    print(i)
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20240924150349855](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924150349855.png)

### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
n = int(input())
a = input().split()
sum = 0
num = 0
for i in a:
    if int(i) > 0:
        num += int(i)
    else:
        if num <= 0:
            sum += 1
            num = 0
        else:
            num -= 1
print(sum)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20240924150424440](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924150424440.png)

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
# l, m = map(int, input().split())
is_Tree = [0] * (l + 1)

# 标记区间
for _ in range(m):
    begin, end = map(int, input().split())
    is_Tree[begin] -= 1
    if end + 1 <= l:
        is_Tree[end + 1] += 1

# 计算前缀和，得到是否为树
count = 0
current = 0
for i in range(l + 1):
    current += is_Tree[i]
    if current == 0:
        count += 1

print(count)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924150450310](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924150450310.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
a, b = map(int, input().split())
ans = []
for i in range(a, b + 1):
    if (i // 100) ** 3 + ((i - 100 * (i // 100)) // 10) ** 3 + (i - 100 * (i // 100) - 10 * ((i - 100 * (i // 100)) // 10)) ** 3 == i:
        ans.append(i)
if len(ans) == 0:
    print('NO')
else:
    print(*ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924150512810](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924150512810.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：本题其实不需要研究查理运动的轨道，因为查理总是跟着其他人走，那么查理到达的时间就是其他人到达的时间，因此最终的答案就是查理能跟上的其他人中到达最快的。查理在t=0时到达，因此只要t>=0，查理都能跟上。如果t<0且速度比查理快，那么查理就碰不到，如果t<0且比查理慢，则没有必要跟着他走。



##### 代码

```python
import math
while True:
    min_time = float('inf')
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        arrive_time = (4500 * 3.6 / v) + t
        min_time = min(arrive_time, min_time)
    print(math.ceil(min_time))


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20240924160346762](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240924160346762.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==



### 总结与反思

1.在做题之前可以先手算几个例子，先大概想一想题目再进行作答，不要一上来就开始写代码，这样写代码效率反而不高。

2.写代码的时候一定要调整好心态，一道比较难的算法题写一个小时两个小时对现阶段而言很正常，一定不要心急。

3.善用gpt，代码有问题可以找gpt进行优化

4.在做题过程中，感觉很多算法题都涉及了很多看起来完全不会出现的后期知识以进行优化，似乎陷入了一个僵局——学简单的东西以后需要练习，但是练习往往会涉及更多更难的东西。这种情况：1.可以通过先刷简单的题目（刷晴问而非oj） 2.尽可能搞懂更难的知识（利用ai进行讲解）

### 收获

1. oj04144:畜栏保留问题：要对数组的规模和时间复杂度有个大概的认知，大概多大的数组会超，大概多大的复杂度时间会超。在贪心算法中要善用排序，排序在一些比大小题目中十分重要，用好了能起到意想不到的效果。本题涉及两个时间：开始时间和结束时间。我最开始的算法两个时间都没有进行排序，因此复杂度非常高，然后我对开始时间进行了排序，但还需要对结束时间进行遍历（没排序），时间复杂度依然不够=>引入一个叫最优队列的东西再对结束时间排序即可（因为开始时间和结束时间相对比较独立，所以可以这么干）。

2. 做题要难易结合（oj和晴问结合）

3. 对贪心来说，很重要的一点是贪心算法的选取，一定要选取到全局最优而非局部最优，有一个特征：对于某个项，它行的，另外一个项肯定也行，那么另一项肯定是更优解，这么进行下去，一定能找到最优解。比如区间不相交问题，对于逆序排布，任何一个次优项能适配的下一个区间，局域最优项都可以适配，因此局域最优项就是全局最优项。但是对于一般的正序排布就没有这样的性质。如果找不到这样的特征，就只能适当结合枚举进行证明（oj1042）

4. 感觉贪心的要点是要见很多种不同的算法才能在做题的时候有思路，做题一定要尽可能多想几种思路以当做练习




最后抱怨一句，题目做的好慢啊，而且还经常想不出来好的解决方案，崩溃捏
