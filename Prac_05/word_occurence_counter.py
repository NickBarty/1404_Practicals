words_dict = {}
sentence = input("Enter a sentence: ")

words = sentence.split()

# word is the value of the Key: Value pairs
for word in words:
    frequency = words_dict.get(word, 0)
    words_dict[word] = frequency + 1

words = sorted(words_dict.keys())

# Using longest word for .format to format nicely
longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {words_dict[word]}")
