size = int(input())
territory = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

alice_pos = []
bags_of_tea = 0

for row in range(size):
    territory.append(input().split())

    if "A" in territory[row]:
        alice_pos = [row, territory[row].index("A")]

alice_row, alice_col = alice_pos[0], alice_pos[1]

while bags_of_tea < 10:

    command = input()

    territory[alice_row][alice_col] = "*"
    alice_row += directions[command][0]
    alice_col += directions[command][1]

    if not (0 <= alice_row < size and 0 <= alice_col < size):
        break

    new_pos = territory[alice_row][alice_col]

    if new_pos.isdigit():
        bags_of_tea += int(territory[alice_row][alice_col])
        territory[alice_row][alice_col] = "*"
    elif new_pos == "R":
        territory[alice_row][alice_col] = "*"
        break

if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

[print(*row) for row in territory]
