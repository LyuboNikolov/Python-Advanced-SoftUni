first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_word, second_word, *data = input().split()

    command = first_word + " " + second_word

    if command == "Add First":
        [first_set.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_set.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_set.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_set.discard(int(x)) for x in data]
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
