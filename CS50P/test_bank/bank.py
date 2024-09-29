def main():
    user_greeting = input("Greeting: ")
    print(f"${value(user_greeting)}", end='')


def value(greeting):
    greeting = greeting.lower().strip()
    word = ''
    for i in greeting:
        if not i.isalpha():
            break
        word += i

    if word[0] == 'h' and word == 'hello':
        return 0
    elif word[0] == 'h' and word != 'hello':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
