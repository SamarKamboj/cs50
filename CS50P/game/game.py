from random import randint

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
    except ValueError:
        pass
    else:
        num = randint(1, n)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                pass
            else:
                if guess > num:
                    print("Too Large!")
                elif guess < num:
                    print("Too Small!")
                else:
                    print("Just Right!")
                    break
        break
