def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to compare them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

# Taking input from the user
input_list = input("Enter the list of numbers (comma separated): ").split(',')
arr = [int(num.strip()) for num in input_list]

# Sorting the array using bubble sort
sorted_array = bubble_sort(arr)

# Display the sorted array
print(f"Sorted array: {sorted_array}")
