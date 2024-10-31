rows, cols = [int(x) for x in input().split(", ")]

sum_of_cols = [0] * cols
index = 0

for _ in range(rows):
    current_row = [int(x) for x in input().split()]
    while index < cols:
        sum_of_cols[index] += current_row[index]
        index += 1
    index = 0

print(*sum_of_cols, sep="\n")
