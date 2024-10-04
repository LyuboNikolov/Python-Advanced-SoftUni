expression = input()
parenthesis = []

for index in range(len(expression)):
    if expression[index] == "(":
        parenthesis.append(index)
    elif expression[index] == ")":
        start_index = parenthesis.pop()
        print(expression[start_index:index + 1])
