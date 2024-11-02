matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

diagonal_sum = 0
for index in range(matrix_size):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)
