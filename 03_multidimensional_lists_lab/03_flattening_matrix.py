flattened_matrix = []

for _ in range(int(input())):
    current_row = [int(x) for x in input().split(", ")]
    flattened_matrix.extend(current_row)

print(flattened_matrix)
