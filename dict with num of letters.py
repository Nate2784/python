file = open('sample.txt')
words = file.read().split()
word_length_dict = {word: len(word) for word in words}

# Create a reverse dictionary
length_word_dict = {}
for word, length in word_length_dict.items():
    if length not in length_word_dict:
        length_word_dict[length] = []  # Create a new list for this length
    length_word_dict[length].append(word)

#search for words by their length
length_to_search = 2
if length_to_search in length_word_dict:
    print(f"Words of length {length_to_search}: {length_word_dict[length_to_search]}")
else:
    print(f"No words of length {length_to_search} found.")