numbers = list(map(int, input().split()))
target_sum = int(input())

for index in range(len(numbers)):
    first_number = numbers[index]
    if index == len(numbers) - 1:
        break
    for idx in range(index + 1, len(numbers)):
        second_number = numbers[idx]
        if first_number + second_number == target_sum:
            print(f"{first_number} + {second_number} = {target_sum}")
            numbers.pop(idx)
            break
    if index == len(numbers) - 1:
        break
