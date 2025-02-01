def binary_search(arr, low, high, target):
    if low > high:
        return -1  # Base case: Element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Found the target
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)  # Search in left half
    else:
        return binary_search(arr, mid + 1, high, target)  # Search in right half

# Taking input from user
numbers = list(map(int, input("Enter sorted numbers (comma-separated): ").split(',')))
target = int(input("Enter the number to find: "))

# Performing binary search
result = binary_search(numbers, 0, len(numbers) - 1, target)

# Display result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
