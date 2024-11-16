from typing import List


def print_nums(nums: List[int]) -> None:
    negative_sum = sum(num for num in nums if num < 0)
    positive_sum = sum(num for num in nums if num > 0)

    print(negative_sum)
    print(positive_sum)

    if positive_sum > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
print_nums(numbers)
