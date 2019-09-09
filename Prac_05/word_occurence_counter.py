words_dict = {}
sentence = input("Enter a sentence: ")

words = sentence.split()
for word in words:
    frequency = words_dict.get(word, 0)
    words_dict[word] = frequency + 1

words = list(words_dict.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, words_dict[word]))
