first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(int(x)) for x in data],
    "Add Second": lambda x: [second_set.add(int(x)) for x in data],
    "Remove First": lambda x: [first_set.discard(int(x)) for x in data],
    "Remove Second": lambda x: [second_set.discard(int(x)) for x in data],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set))
}

for _ in range(int(input())):
    first_word, second_word, *data = input().split()

    command = first_word + " " + second_word

    functions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
