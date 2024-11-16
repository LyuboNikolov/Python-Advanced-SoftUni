def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [num for num in args[:-1] if int(num) % 2 == 0]
    elif command == "odd":
        return [num for num in args[:-1] if int(num) % 2 != 0]
