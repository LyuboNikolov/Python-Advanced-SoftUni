clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
clothes_sum = 0

while clothes:
    cloth = clothes.pop()
    if cloth <= (rack_capacity - clothes_sum):
        clothes_sum += cloth
    else:
        clothes.append(cloth)
        racks += 1
        clothes_sum = 0

print(racks)
