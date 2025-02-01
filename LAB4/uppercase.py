class StringManipulator:
    def __init__(self):
        self.input_string = ""

    # Method to accept string input from the user
    def get_String(self):
        self.input_string = input("Enter a string: ")

    # Method to print the string in uppercase
    def print_String(self):
        print(self.input_string.upper())

# Example Usage
string_manipulator = StringManipulator()
string_manipulator.get_String()  # Get string input from user
string_manipulator.print_String()  # Print the string in uppercase
