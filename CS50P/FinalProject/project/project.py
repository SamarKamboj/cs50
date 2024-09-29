from random import choice
import os
import platform
import time

def main():
    # Iterate until user is satisfied playing this game
    while True:
        print()
        print("Game of 5")
        print()

        # Winner of each game
        winner = playerWin()
        print(f"{winner[0]} by {winner[1]}-{winner[2]}")
        # Ask to play again
        quit = input("Do you want to play again (y/n): ").lower().strip()
        if quit == 'n':
            os.system("clear") if platform.system() == "Linux" else os.system("cls")
            break

        os.system("clear") if platform.system() == "Linux" else os.system("cls")

def playerWin():
    # Count how many times a player wins
    count1 = 0
    count2 = 0

    # Game of 5
    for _ in range(5):
        # User Output
        p1 = user()
        # Corresponding art of p1
        print(art(p1))

        # Computer Output
        p2 = com()
        # Corresponding art of p2
        print(art(p2))

        # Check for victory
        if (p1 == 'r' and p2 == 's') or (p1 == 'p' and p2 == 'r') or (p1 == 's' and p2 == 'p'):
            count1 += 1
            print("You Won!")
        elif (p1 == 's' and p2 == 'r') or (p1 == 'r' and p2 == 'p') or (p1 == 'p' and p2 == 's'):
            count2 += 1
            print("You Lost!")
        else:
            print("Draw!")

        time.sleep(1.5)
        os.system("clear") if platform.system() == "Linux" else os.system("cls")

        # Output score
        print(f"User:{count1} Computer:{count2}")
        print()

    # Check who wins at the end
    if count1 > count2:
        return ("Human Won", count1, count2)
    elif count1 < count2:
        return ("Computer Won", count1, count2)
    else:
        return ("Draw", count1, count2)


# User output
def user():
    # Iterate until user enter correct input
    while True:
        # Get user input
        rps = input("Type 'r' for Rock, 'p' for Paper and 's' for Scissor: ")
        # Check if input is valid
        if rps == 'r' or rps == 'p' or rps == 's':
            return rps
        print("Invalid input!")


# Computer output
def com():
    return choice(['r', 'p', 's'])


# Output the corresponding picture
def art(char):
    r = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    p = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    s = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    return eval(char)


if __name__ == "__main__":
    main()
