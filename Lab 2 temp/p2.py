def matrix_order():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    return row, col

def matrix_values(order):
    matrix = {}
    for i in range(order[0]):
        for j in range(order[1]):
            value = int(input(f"Enter value at position ({i}, {j}): "))
            if value != 0:
                matrix[(i, j)] = value
    return matrix

def add_matrices(matrix1, matrix2, order):
    result = {}
    for i in range(order[0]):
        for j in range(order[1]):
            value = matrix1.get((i, j), 0) + matrix2.get((i, j), 0)
            if value != 0:
                result[(i, j)] = value
    return result

def display_matrix(matrix, order):
    for i in range(order[0]):
        for j in range(order[1]):
            value = matrix.get((i, j), 0)
            print(value, end="\t")
        print()

def main():
    print("Matrix 1:")
    matrix1_order = matrix_order()
    matrix1 = matrix_values(matrix1_order)

    print("Matrix 2:")
    matrix2_order = matrix_order()
    matrix2 = matrix_values(matrix2_order)

    if matrix1_order == matrix2_order:
        result_matrix = add_matrices(matrix1, matrix2, matrix1_order)
        print("Resultant Matrix:")
        display_matrix(result_matrix, matrix1_order)
    else:
        print("order not equal cant add")

main()