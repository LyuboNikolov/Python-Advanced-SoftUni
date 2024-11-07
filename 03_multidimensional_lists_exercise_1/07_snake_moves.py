rows, cols = [int(x) for x in input().split()]
text = input()
current_text = text

for row in range(rows):
    difference = text[len(current_text):]
    current_text = current_text[:(cols - row)]
    new_text = difference + current_text

    print(new_text if row % 2 == 0 else new_text[::-1])
