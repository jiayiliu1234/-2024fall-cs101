def BinarySearch(word, dict):
    left, right = 0, len(dict) - 1
    Target = word[0]
    while left <= right:
        mid = (left + right) // 2
        if Target == dict[mid][1]:
            return mid
        elif Target < dict[mid][1]:
            right = mid - 1
        else:
            left = mid + 1
    return None

dict = []
while True:
    s = input().split()
    if s:
        dict.append(s)
    else:
        break
dict.sort(key=lambda x: x[1])
while True:
    try:
        word = input().split()
        result = BinarySearch(word, dict)
        if result:
            print(dict[result][0])
        else:
            print('eh')
    except EOFError:
        break