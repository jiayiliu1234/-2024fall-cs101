a = list(input().lower())
ans = []
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for word in a:
    if word not in vowels:
        ans.append('.' + word)
ans_str = ''.join(ans)
print(ans_str)