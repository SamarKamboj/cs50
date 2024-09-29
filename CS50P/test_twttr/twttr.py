def main():
    before = input("Input: ")
    after = shorten(before)

    print("Output: " + after)


def shorten(word):
    new_word = ''
    for char in word:
        vowels = "aeiouAEIOU"

        if char in vowels:
            continue
        new_word += char

    return new_word


if __name__ == "__main__":
    main()
