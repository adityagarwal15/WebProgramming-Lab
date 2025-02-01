class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        index_map = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(self.numbers):
            complement = self.target - num  # Find the required pair value
            
            if complement in index_map:
                return index_map[complement], i  # Return indices of the pair

            index_map[num] = i  # Store the index of the current number
        
        return None  # Return None if no pair is found

# Example Usage
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

finder = PairFinder(numbers, target)
result = finder.find_pair()

# Print the output
if result:
    print(result[0] + 1, result[1] + 1)  # Convert 0-based index to 1-based index
else:
    print("No pair found")
