# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>刘家亦、物理学院</mark>



**说明：**

1）⽉考： <mark>AC6</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：考到了timesort的稳定性，不算很难



代码：

```python
n = int(input())
young = []
old = []
for _ in range(n):
    s, y = input().split()
    y = int(y)
    if y >= 60:
        old.append([s, y])
    else:
        young.append([s, y])
old.sort(key=lambda x: -x[1])
ans = old + young
for i in old:
    print(i[0])
for i in young:
    print(i[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108194252176](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108194252176.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：字典的经典应用



代码：

```python
n, m1, m2 = map(int, input().split())
a = {}
for i in range(m1):
    s, x, y = map(int, input().split())
    a[(s, x)] = y
b = {}
for i in range(m2):
    s, x, y = map(int, input().split())
    b[(s, x)] = y
ans = {}
for i in range(n):
    for j in range(n):
        for d in range(n):
            if (i, d) in a and (d, j) in b:
                if (i, j) not in ans:
                    ans[(i, j)] = 0
                ans[(i, j)] += a[(i, d)] * b[(d, j)]
for i in range(n):
    for j in range(n):
        if (i, j) in ans:
            print(f'{i} {j} {ans[(i, j)]}')
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241108194330831](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108194330831.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：一个相当暴力的算法，但是表现的还可以，可能是因为数据量比较小的原因



代码：

```python
t = int(input())
for _ in range(t):
    n, m, b = map(int, input().split())
    a = {}
    time = []
    for i in range(n):
        t, x = map(int, input().split())
        if t not in a:
            a[t] = []
            time.append(t)
        a[t].append(x)
    time.sort()
    for i in range(len(time)):
        b -= sum(sorted(a[time[i]], reverse=True)[:m])
        if b <= 0:
            print(time[i])
            break
    else:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108194520360](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108194520360.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：经典的完全背包问题



代码：

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] + [float('inf')] * m
for i in range(len(a)):
    for j in range(a[i], m + 1):
        dp[j] = min(dp[j - a[i]] + 1, dp[j])
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108194601961](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108194601961.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：本题感觉可以采用单调栈的方法，结果被坑了，是个字符串的题目(qwq)。此题耗费1h进行调试，不然能做到在1h之内ak。

实在没绷住，我用单调栈写了好长一堆屎山代码代码（其实主要原因还有考试的时候比较紧张，没心情控制码风了）



代码：

```python
# 屎山代码就不拿出来给大伙品鉴了，这个是自己下来写的代码
english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million']
number = list(range(21)) + [30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000]
english_number = dict(zip(english, number))
s = input().split()
num = 0
ans = 0
flag = 1
if s[0] == 'negatiange(len(s)):
    if s[i] == 'hundred':
        num *= 100
    elif s[i] == 'million' or s[i] == 'thousand':
        ans += num * english_number[s[i]]
        num = 0
    else:
        num += english_number[s[i]]
ans += num
print(flag * ans)
'''
利用单调栈写的代码，性能相较于直接判断要好，而且代码的复杂度并没有高到哪里去。其实这段代码有一个地方的逻辑还可以再优化，但是引用著名厨师于涛的话：“我故意保留了一点代码的本味，让你知道我是在写单调栈”
'''
english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million']
number = list(range(21)) + [30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000]
english_number = dict(zip(english, number))
s = input().split()
ans = 0
sign = 1
if s[0] == 'negative':
    sign = -1
    s = s[1:]
num = []
for i in range(len(s)):
    if english_number[s[i]] >= 100:
        if num[0][1] < english_number[s[i]] and (len(num) > 1 or num[-1][1] > 1):
            while num and num[-1][1] < english_number[s[i]]:
                ans += num[-1][0] * num[-1][1] * english_number[s[i]]
                num.pop()
        else:
            num[-1][1] = english_number[s[i]]
    else:
        num.append([english_number[s[i]], 1])
for i in range(len(num)):
    ans += num[i][0] * num[i][1]
print(sign * ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108201601698](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108201601698.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：经典greedy，没什么好说的



代码：

```python
n = int(input())
vac = []
for i in range(n):
    vac.append(list(map(int, input().split())))
vac.sort(key = lambda x: (-x[0], x[1]))
left = 61
num = 0
for i in range(0, n):
    if vac[i][1] < left:
        num += 1
        left = vac[i][0]
print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108201655429](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241108201655429.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

本次考试还可以，至少AK6了，但是自我感觉发挥的不太好，没能做到自己的最好水平。有部分原因是自己疏于练习，有一部分原因是机房的电脑太难用了，还有一部分原因是考试的心态问题。同时感觉***自己的思路有点僵化了，要及时改正***

T5是重灾区，花了整整一小时调试自己的屎山代码，评价为用单调栈用的。对单调栈的知识点掌握不够熟练，导致考试只会套模版，而且考试的时候心态也占了很重要的一个因素，如果能再多想一会/多观察一下数据的范围，说不定就能想到字符串的用法了。再多提一嘴，T5的字符串解法其实就是单调栈解法在数据范围比较小的时候的简化（这个时候单调栈只对hundred发力，所以可以简化为同学们用的方法）T6是经典区间问题，结果排序的时候0,1搞反了，导致没能一遍过，值得反思。
