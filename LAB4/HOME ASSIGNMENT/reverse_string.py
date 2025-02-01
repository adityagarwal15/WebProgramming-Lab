class StringReverser:
    def __init__(self, input_string):
        # Initialize the string that needs to be reversed
        self.input_string = input_string
    
    def reverse_words(self):
        # Split the input string into words
        words = self.input_string.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words into a single string
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string

# Taking input from the user
input_string = input("Enter a string to reverse word by word: ")

# Create an instance of the StringReverser class
reverser = StringReverser(input_string)

# Get the reversed string and print it
reversed_string = reverser.reverse_words()
print("Reversed string:", reversed_string)
