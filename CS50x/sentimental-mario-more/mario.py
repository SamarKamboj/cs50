# TODO
while True:
    height = input("Height: ")
    if height.isdigit():
        height = int(height)
        if height >= 1 and height <= 8:
            break

for i in range(height):
    for j in range(height-1-i):
        print(" ", end="")

    for k in range(i+1):
        print("#", end="")

    print("  ", end="")

    for l in range(i+1):
        print("#", end="")

    print()
