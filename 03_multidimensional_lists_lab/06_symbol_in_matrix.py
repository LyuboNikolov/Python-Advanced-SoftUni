matrix_size = int(input())
matrix = []

for row in range(matrix_size):
    current_row = list(input())
    matrix.append(current_row)

searched_symbol = input()

for row in matrix:
    if searched_symbol in row:
        print((matrix.index(row), row.index(searched_symbol)))
        break
else:
    print(f"{searched_symbol} does not occur in the matrix")
