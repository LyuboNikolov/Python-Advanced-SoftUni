from collections import deque


def fill_the_box(height, length, width, *cubes):
    box_volume = height * length * width
    cubes = deque(cubes)

    while cubes[0] != "Finish":
        box_volume -= cubes.popleft()

        if box_volume < 0:
            cubes_left = abs(box_volume) + sum(c for c in cubes if c != "Finish")
            return f"No more free space! You have {cubes_left} more cubes."

    return f"There is free space in the box. You could put {box_volume} more cubes."
