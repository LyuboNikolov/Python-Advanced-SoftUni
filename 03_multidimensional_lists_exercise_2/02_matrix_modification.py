size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":

    operation, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")

    elif operation == "Add":
        matrix[row][col] += value

    elif operation == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]
