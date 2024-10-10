import matplotlib.pyplot as plt

def cal_cycle(k):
    a, b = [1, 1]
    Pell = [a, b]
    i = 1
    while True:
        Pell.append((2*Pell[i]+Pell[i-1]) % k)
        if [Pell[i - 1], Pell[i]] == [a, b] and i != 1:
            cycle = i
            break
        i += 1
    return (cycle - 1)

cycles = []
n = int(input())
for i in range(3, n + 1):
    cycles.append(cal_cycle(i))

y_values = cycles
x_values = list(range(len(cycles)))

plt.plot(x_values, y_values, marker='o', linestyle='', markersize=2)

plt.title("List Plot")
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()