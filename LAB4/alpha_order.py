# Take input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Sort the words in alphabetical order
words.sort()

# Display the sorted words
print("Sorted words:", " ".join(words))
