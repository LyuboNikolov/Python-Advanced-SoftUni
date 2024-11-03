rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_sum, secondary_sum = 0, 0

for row in range(rows):
    primary_sum += matrix[row][row]
    secondary_sum += matrix[row][rows - row - 1]

print(abs(primary_sum - secondary_sum))
