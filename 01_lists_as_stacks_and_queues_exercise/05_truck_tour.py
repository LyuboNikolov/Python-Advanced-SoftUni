from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pumps_data_copy = pumps_data.copy()
fuel_in_tank = 0
index = 0

while pumps_data_copy:
    fuel, distance = pumps_data_copy.popleft()

    fuel_in_tank += fuel

    if fuel_in_tank >= distance:
        fuel_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        fuel_in_tank = 0

print(index)
