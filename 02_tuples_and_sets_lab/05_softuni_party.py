guests_number = int(input())
guest_list = set()

for _ in range(guests_number):
    guest = input()
    guest_list.add(guest)

command = input()
while command != "END":
    if command in guest_list:
        guest_list.remove(command)

    command = input()

guest_list_sorted = sorted(guest_list)
print(len(guest_list_sorted))
print(*guest_list_sorted, sep="\n")
