import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:  # We change this to <= to handle the smallest correctly
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high):
    if low == high:
        return arr[low]
    
    pivot_index = random.randint(low, high)  # Random pivot selection
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element
    
    partition_index = partition(arr, low, high)
    
    # If partition index is at the first element, we return it (smallest element)
    if partition_index == 0:
        return arr[partition_index]
    else:
        return randomized_select(arr, low, partition_index - 1)

# Taking input from the user
input_list = input("Enter the list of numbers (comma separated): ").split(',')
arr = [int(num.strip()) for num in input_list]

# Finding the smallest element
smallest_element = randomized_select(arr, 0, len(arr) - 1)

# Display the result
print(f"The smallest element is: {smallest_element}")
