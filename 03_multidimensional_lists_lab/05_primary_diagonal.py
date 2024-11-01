matrix_size = int(input())
matrix = []
diagonal_sum = 0

for _ in range(matrix_size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for i in range(matrix_size):
    for j in range(matrix_size):
        if i == j:
            diagonal_sum += matrix[i][j]

print(diagonal_sum)
