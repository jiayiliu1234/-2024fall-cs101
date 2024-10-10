for _ in range(int(input())):
    word = input()
    word_list = list(word)
    if len(word_list) <= 10:
        print(word)
    else:
        print(f'{word_list[0]}{len(word_list) - 2}{word_list[-1]}')