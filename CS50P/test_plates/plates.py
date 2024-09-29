def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if s.isalpha():
        return True

    if in_between(s):
        return False

    return True


def in_between(plate):
    d = 0
    if plate.isalnum():
        for char in plate:
            if d == 0 and char == '0':
                return True
            if char.isdigit():
                d += 1
            if d > 0 and char.isalpha():
                d = 0
                break
    if d == 0:
        return True

    return False


if __name__ == "__main__":
    main()
    