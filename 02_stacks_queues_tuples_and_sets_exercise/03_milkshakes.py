from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))

chocolate_milkshakes = 0

while chocolate_milkshakes < 5 and chocolate and milk:
    current_choco = chocolate.pop()
    if current_choco <= 0:
        continue

    current_milk = milk.popleft()
    if current_milk <= 0:
        chocolate.append(current_choco)
        continue

    if current_choco == current_milk:
        chocolate_milkshakes += 1

    else:
        chocolate.append(current_choco + 5)
        milk.append(current_milk)

if chocolate_milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate:", end=" ")
    print(*chocolate, sep=", ")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk:", end=" ")
    print(*milk, sep=", ")
else:
    print("Milk: empty")
