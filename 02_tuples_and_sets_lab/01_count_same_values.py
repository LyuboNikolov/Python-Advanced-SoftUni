numbers = tuple([float(x) for x in input().split()])

numbers_count = {}

for num in numbers:
    if num not in numbers_count:
        numbers_count[num] = numbers.count(num)

for number, occ in numbers_count.items():
    print(f"{number} - {occ} times")
