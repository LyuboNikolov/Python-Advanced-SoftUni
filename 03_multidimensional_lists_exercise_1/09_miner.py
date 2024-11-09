size = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0

directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

for row in range(size):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"

else:
    coal_left = total_coal - collected_coal
    print(f"{coal_left} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
