commands_count = int(input())
parked_cars = set()

for _ in range(commands_count):
    direction, car = input().split(", ")
    if direction == "IN":
        parked_cars.add(car)
    elif direction == "OUT":
        if car in parked_cars:
            parked_cars.remove(car)

if parked_cars:
    print(*parked_cars, sep="\n")
else:
    print("Parking Lot is Empty")
