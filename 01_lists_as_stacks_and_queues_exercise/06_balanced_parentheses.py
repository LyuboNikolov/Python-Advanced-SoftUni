from collections import deque

parentheses = deque(input())
opening_closing = {"{": "}", "(": ")", "[": "]"}
opened = []

while parentheses:
    current = parentheses.popleft()
    if current in opening_closing:
        opened.append(current)
    elif current in opening_closing.values():
        if opened and current == opening_closing[opened[-1]]:
            opened.pop()
        else:
            print("NO")
            break
else:
    print("YES")
