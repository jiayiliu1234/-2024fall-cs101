# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by 刘家亦 物理学院



**说明：**

1）Oct⽉考： AC6。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：



代码

```python
k = int(input())
s_list = list(input())
ans = []
for letter in s_list:
    if ord(letter) < 97:
        ans.append(chr(65 + (ord(letter) - k - 65) % 26))
    else:
        ans.append(chr(97 + (ord(letter) - k - 97) % 26))
print(*ans, sep='')

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012135732449](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012135732449.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：



代码

```python
s = input().split()
num1 = int(str(list(s[0])[0])+str(list(s[0])[1]))
num2 = int(str(list(s[1])[0])+str(list(s[1])[1]))
print(num1+num2)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012135827041](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012135827041.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：



代码

```python

for _ in range(int(input())):
    s = list(input())
    s_list = list(map(int, s[0:17]))
    a = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    jioayan = ['1','0','X','9','8','7','6','5','4','3','2']
    x = 0
    for i in range(len(a)):
        x += s_list[i] * a[i]
    x = x % 11
    if s[17] == jioayan[x]:
        print('YES')
    else:
        print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012135855041](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012135855041.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python

n = int(input())
while True:
    if n == 1:
        print('End')
        break
    if n % 2 == 1:
        print(f'{n}*3+1={3*n+1}')
        n = 3 * n + 1
    else:
        print(f'{n}/2={n//2}')
        n = n // 2
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012135932106](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012135932106.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：这个代码太丑了，数字转罗马可以再用字典优化



##### 代码

```python
# n = input()
lm = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
try:
    n = int(n)
    flag = True
except ValueError:
    n = list(n)
    flag = False
if flag:
    ans = []
    ans += ['M'] * (n // 1000)
    n = n % 1000
    ans += ['CM'] * (n // 900)
    n = n % 900
    ans += ['D'] * (n // 500)
    n = n % 500
    ans += ['CD'] * (n // 400)
    n = n % 400
    ans += ['C'] * (n // 100)
    n = n % 100
    ans += ['XC'] * (n // 90)
    n = n % 90
    ans += ['L'] * (n // 50)
    n = n % 50
    ans += ['XL'] * (n // 40)
    n = n % 40
    ans += ['X'] * (n // 10)
    n = n % 10
    ans += ['IX'] * (n // 9)
    n = n % 9
    ans += ['V'] * (n // 5)
    n = n % 5
    ans += ['IV'] * (n // 4)
    n = n % 4
    ans += ['I'] * (n)
    print(*ans, sep='')
else:
    num = 0
    for i in range(len(n) - 1):
        if lm[n[i]] >= lm[n[i+1]]:
            num += lm[n[i]]
        else:
            num -= lm[n[i]]
    num += lm[n[-1]]
    print(num)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012135954637](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012135954637.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python
n, d = map(int, input().split())
h = []
ans = []
for _ in range(n):
    h.append(int(input()))

while h != []:
    inlist = []
    other = []
    max = h[0]
    min = h[0]
    for i in range(len(h)):
        if abs(h[i] - max) <= d and abs(h[i] - min) <= d:
            inlist.append(h[i])
        else:
            other.append(h[i])
        if h[i] < min:
            min = h[i]
        if h[i] > max:
            max = h[i]
    ans += sorted(inlist)
    h = other
print(*ans, sep='\n')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012140126588](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20241012140126588.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==



额外在刷晴问，以及跟着算法实践在oj上面刷题。

感觉这周投入在计概上面的时间有所下降，有点懈怠了，应该反思。应该保持工作日每天花至少2小时在计概上，休息日为3小时。

计概月考考的不错，原因有以下几点：

1. 心态比较好，状态比较好，将tough难度的题目做出来了
2. 对于基本的语法比较熟悉，能够留出大量的时间用来做tough难度的题目
3. 思路比较好，这是做了比较多高难度的题目，思维得到训练以后的结果
4. 要大胆一点，把自己想到的算法实现

基于以上总结，接下来应该做到：

1. 继续学习新的知识和语法，按照胡凡的算法笔记以及其他资料进行学习，同时复习以前学过的语法知识，例如优先队列，最小堆等知识，不要懈怠
2. 以每日选做为基本语法知识的复习
3. **保持谦卑的心态**，这次能考好很大程度上是运气好，自己在知识层次和做的题目数量上都不如人
4. **要保证做题的质量**，鉴于现在的情况，可以选择多做一点难题，多学一点有用的语法/数据结构/算法等，平时做的题目一定要搞懂，千万不能模棱两可，比如贪心的题目中的贪心策略自己一定要有一个证明（不要求多严谨，但是一定要把握到这种证明策略的思想，在学习其他数据结构和算法的时候也要注意）
5. 重在对知识的理解和应用上，不是知识越多越好的，知识多了，如果不能灵活的应用，其实也不太好。

目标：

1. 熟练掌握python的基本语法和常用的函数，适当了解一点c的内容
2. 多学习一点数据结构和算法，但是一定要注意不能好高骛远，囫囵吞枣，要学就要学扎实，学透
3. 多刷一点难题，尽可能保证能稳定做出排队这种难度的题目

下来看了一下线段树的做法，看崩了，写出这个代码的邮电部诗人，每个部分环环相扣，各种默认值的设置与判断，光看懂就很困难了，更别提空间复杂度和时间复杂度的分析。感觉自己一边看，一遍照着这个代码打一遍能帮助自己理解。另外，在Python中看到面向对象编程还是分外亲切的。
