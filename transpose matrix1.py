def get_matrix(rows, cols):
    
    matrix = []
    for i in range(rows):
    
        row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
        matrix.append(row)
    return matrix


def transpose_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    return transpose


def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    
    print("Enter the matrix values:")
    matrix = get_matrix(rows, cols)

    
    print("\nOriginal Matrix:")
    display_matrix(matrix)

    
    transposed = transpose_matrix(matrix)


    print("\nTranspose Matrix:")
    display_matrix(transposed)

if __name__ == "__main__":
    main()
