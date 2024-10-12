from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups.appendleft(current_cup)

if bottles:
    print(f"Bottles:", *bottles)
elif cups:
    print(f"Cups:", *cups)

print(f"Wasted litters of water:", wasted_water)
