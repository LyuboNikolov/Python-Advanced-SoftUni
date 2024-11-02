rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for col in range(cols):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][col]
    print(total_sum)
