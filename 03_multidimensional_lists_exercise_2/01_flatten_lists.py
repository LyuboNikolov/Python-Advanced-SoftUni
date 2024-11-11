sub_lists = input().split("|")
nums = []

for sub_list in sub_lists[::-1]:
    nums.extend(sub_list.split())

print(*nums)
