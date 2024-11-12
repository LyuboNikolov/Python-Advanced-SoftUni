size = int(input())
chessboard = [list(input()) for _ in range(size)]

pos_numbers = [-2, -1, 1, 2]
positions = [(x, y) for x in pos_numbers for y in pos_numbers if abs(x) != abs(y)]

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if chessboard[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row, pos_col = row + pos[0], col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if chessboard[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        chessboard[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
