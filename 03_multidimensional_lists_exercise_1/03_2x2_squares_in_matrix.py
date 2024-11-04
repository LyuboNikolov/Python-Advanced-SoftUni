rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol != matrix[row][col + 1] or symbol != matrix[row + 1][col] or symbol != matrix[row + 1][col + 1]:
            continue

        equal_blocks += 1

print(equal_blocks)
