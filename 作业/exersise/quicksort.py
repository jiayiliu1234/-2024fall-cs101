def quicksort(arr):
    if len(arr) <= 1:
        return arr #基线条件
    else:
        pivot = arr[0]
        less = [a for a in arr[1:] if a <= pivot]
        larger = [a for a in arr[1:] if a > pivot]
        return quicksort(less) + [pivot] + quicksort(larger)
    
array = list(map(int, input().split()))
print(quicksort(array))