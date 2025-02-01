class ParenthesisValidator:
    def __init__(self):
        # A dictionary to map opening brackets to their corresponding closing brackets
        self.bracket_pairs = { '(': ')', '{': '}', '[': ']' }
        
    def is_valid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it to the stack
            if char in self.bracket_pairs:
                stack.append(char)
            # If the character is a closing bracket
            elif char in self.bracket_pairs.values():
                # If the stack is empty or the top of the stack does not match the closing bracket
                if not stack or self.bracket_pairs[stack.pop()] != char:
                    return False
        # The stack should be empty if all brackets are properly closed
        return not stack

# Taking input from the user
input_string = input("Enter the string of parentheses: ")

# Create an instance of the ParenthesisValidator class
validator = ParenthesisValidator()

# Check if the parentheses are valid
if validator.is_valid(input_string):
    print("The parentheses are valid.")
else:
    print("The parentheses are invalid.")
