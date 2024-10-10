import heapq #用来实现最小堆的库

n = int(input())
cows = []
for _ in range(n):
    cows.append(list(map(int, input().split())))
for i in range(n):
    cows[i].append(i) #用来标记初始的位置，这样在排序后就能轻松找到原来的位置，而这个又显然不影响排序

cows.sort(key=lambda x: (x[0], x[1])) #进行排序，按x[0]从小到大进行排序，若x[0]相同，则按x[1]进行排序

barn = []
schedule = [0] * n
maxnum = 1
heapq.heappush(barn, [cows[0][1], 0]) #把第一头牛的结束时间按入最小堆中
schedule[cows[0][2]] = 1 #记录编号

for i in range(1, n):
    k = heapq.heappop(barn) #弹出现在的堆头(最有可能空闲的畜栏)
    if k[0] < cows[i][0]: #判断是否空闲
        heapq.heappush(barn, [cows[i][1], k[1]])
        schedule[cows[i][2]] = k[1] + 1
    else: #不空闲：加新的一个畜栏
        heapq.heappush(barn, k)
        heapq.heappush(barn, [cows[i][1], maxnum])
        schedule[cows[i][2]] = maxnum + 1
        maxnum += 1

print(len(barn))
for i in range(n):
    print(schedule[i])