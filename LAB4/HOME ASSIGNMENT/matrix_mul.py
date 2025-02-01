# Function to multiply two matrices
def multiply_matrices(A, B):
    # Number of rows and columns in A
    rows_A = len(A)
    cols_A = len(A[0])

    # Number of rows and columns in B
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible (columns of A must equal rows of B)
    if cols_A != rows_B:
        raise ValueError("Matrix multiplication is not possible. The number of columns in A must be equal to the number of rows in B.")

    # Initialize the result matrix with zero values
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or k in range(rows_B)
                result[i][j] += A[i][k] * B[k][j]

    return result

# Taking input from the user for matrix A
rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
print("Enter the elements of matrix A row by row:")
A = []
for i in range(rows_A):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    A.append(row)

# Taking input from the user for matrix B
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))
print("Enter the elements of matrix B row by row:")
B = []
for i in range(rows_B):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    B.append(row)

# Multiplying matrices A and B
try:
    result = multiply_matrices(A, B)
    # Printing the result
    print("The product of the matrices is:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
