def sum(arr):
    if arr != []:
        a = arr.pop()
        return a + sum(arr)
    else:
        return 0
    
array = list(map(int, input().split()))
print(sum(array))