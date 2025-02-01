class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums
        self.result = []

    def generate_subsets(self, index=0, current_subset=[]):
        # Add the current subset to the result
        self.result.append(current_subset[:])

        # Iterate through the remaining elements
        for i in range(index, len(self.nums)):
            # Include nums[i] in the current subset
            current_subset.append(self.nums[i])
            # Recursively call for the next index
            self.generate_subsets(i + 1, current_subset)
            # Backtrack: Remove the last element to explore the next possibility
            current_subset.pop()

    def get_subsets(self):
        self.generate_subsets()
        return self.result

# Example Usage
nums = [4, 5, 6]  # Input set
subset_gen = SubsetGenerator(nums)
unique_subsets = subset_gen.get_subsets()

# Print the output
print(unique_subsets)
