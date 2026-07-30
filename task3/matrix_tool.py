import numpy as np

# -----------------------------
# Function to Input Matrix
# -----------------------------
def input_matrix(matrix_name):
    print(f"\nEnter details for {matrix_name}")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print(f"\nEnter elements row-wise for {matrix_name}:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))

        matrix.append(row)

    return np.array(matrix)

# -----------------------------
# Display Matrix
# -----------------------------
def display_matrix(title, matrix):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)
    print(matrix)

# -----------------------------
# Main Program
# -----------------------------
print("=" * 60)
print("      MATRIX OPERATIONS TOOL USING NUMPY")
print("=" * 60)

A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

while True:

    print("\n")
    print("=" * 50)
    print("Choose Matrix Operation")
    print("=" * 50)

    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Determinant of Matrix A")
    print("7. Determinant of Matrix B")
    print("8. Display Matrices")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        if A.shape == B.shape:
            display_matrix("Addition Result", A + B)
        else:
            print("Addition not possible. Matrix sizes must be equal.")

    elif choice == "2":

        if A.shape == B.shape:
            display_matrix("Subtraction Result", A - B)
        else:
            print("Subtraction not possible. Matrix sizes must be equal.")

    elif choice == "3":

        if A.shape[1] == B.shape[0]:
            display_matrix("Multiplication Result", np.matmul(A, B))
        else:
            print("Multiplication not possible.")
            print("Columns of Matrix A must equal Rows of Matrix B.")

    elif choice == "4":

        display_matrix("Transpose of Matrix A", A.T)

    elif choice == "5":

        display_matrix("Transpose of Matrix B", B.T)

    elif choice == "6":

        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of Matrix A =", np.linalg.det(A))
        else:
            print("Determinant exists only for square matrices.")

    elif choice == "7":

        if B.shape[0] == B.shape[1]:
            print("\nDeterminant of Matrix B =", np.linalg.det(B))
        else:
            print("Determinant exists only for square matrices.")

    elif choice == "8":

        display_matrix("Matrix A", A)
        display_matrix("Matrix B", B)

    elif choice == "9":

        print("\nThank you for using Matrix Operations Tool.")
        break

    else:

        print("Invalid Choice. Please try again.")