even_matrix = []

for _ in range(int(input())):
    row_data = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    even_matrix.append(row_data)

print(even_matrix)
