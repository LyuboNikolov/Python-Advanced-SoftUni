flattened_matrix = []

for _ in range(int(input())):
    current_row = [int(x) for x in input().split(", ")]
    for num in current_row:
        flattened_matrix.append(num)

print(flattened_matrix)
