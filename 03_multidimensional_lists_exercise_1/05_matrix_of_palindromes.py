rows, cols = [int(x) for x in input().split()]

start_row = ord("a")

for row in range(start_row, start_row + rows):
    for col in range(row, row + cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()
