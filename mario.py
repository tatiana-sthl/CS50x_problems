from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height <= 0 or height > 8:
        continue

    else:   
        for i in range(height):
            print(' ' * (height - i - 1) + '#' * (1 * i + 1))
        break