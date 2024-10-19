odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_value = sum(ord(char) for char in input()) // row

    if ascii_value % 2 != 0:
        odd_set.add(ascii_value)
    else:
        even_set.add(ascii_value)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
