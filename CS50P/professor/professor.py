from random import randint


def main():
    # Get the user level
    level = get_level()

    # Maximum Score
    s = 0
    for i in range(10):
        # Generate 2 integers X and Y
        x = generate_integer(level)
        y = generate_integer(level)

        # Add correct answers
        s += ques(x, y)

    # Output the total score
    print(s)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            # Prompt again if level is less than 1 or more than 3
            if n < 1 or n > 3:
                continue
        except ValueError:
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        value = randint(0, 9)
    elif level == 2:
        value = randint(10, 99)
    elif level == 3:
        value = randint(100, 999)

    return value


def ques(x, y):
    # Variable to check 3 consecutive wrong answers
    check = 0
    while check <= 3:
        if check == 3:
            # Output correct answer after 3 consecutive incorrect answer
            print(f"{x} + {y} = {x + y}")
            # Return 0 if answer is wrong 3 consecutive times
            return 0

        # Prompt user for answer
        ans = input(f"{x} + {y} = ")

        # Check if answer is not a number or is incorrect
        if not ans.isdigit() or ans != str(x + y):
            print("EEE")
            check += 1
        else:
            # Return 1 if answer is correct
            return 1


if __name__ == "__main__":
    main()
    