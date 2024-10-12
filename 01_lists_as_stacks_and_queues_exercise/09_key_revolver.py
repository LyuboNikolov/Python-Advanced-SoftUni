from collections import deque

bullet_price = int(input())
gun_barrel_capacity = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())

gun_barrel = gun_barrel_capacity

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    intelligence -= bullet_price
    gun_barrel -= 1

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    if bullets and not gun_barrel:
        gun_barrel = gun_barrel_capacity
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")
