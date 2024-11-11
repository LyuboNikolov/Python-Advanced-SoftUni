def check_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command = input()

    if command == "END":
        break

    operation, r, c, value = [int(x) if x.lstrip("-").isdigit() else x for x in command.split()]

    if not check_valid_index(r, c):
        print("Invalid coordinates")
        continue

    elif operation == "Add" and check_valid_index(r, c):
        matrix[r][c] += value

    elif operation == "Subtract" and check_valid_index(r, c):
        matrix[r][c] -= value

[print(*row) for row in matrix]
