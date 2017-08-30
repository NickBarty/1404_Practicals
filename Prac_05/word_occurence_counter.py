words_dict = {}
sentence = input("Enter a sentence: ")

words = sentence.split()
for word in words:
    occurrences = words_dict.get(word, 0)
    if occurrences is None:
        words_dict[word] = 1
    else:
        words_dict[word] = occurrences + 1

words = list(words_dict.keys())
words.sort()
longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, words_dict[word]))
