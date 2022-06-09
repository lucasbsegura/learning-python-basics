#List Comprehensions is a very powerful tool, which creates a new list based on 
# another list, in a single, readable line.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

print(words)
print(word_lengths)

#Using a list comprehension, we could simplify this process to this notation:
word_lengths_w_comprehensions = [len(word) for word in words if word != "the"]
print(word_lengths_w_comprehensions)
