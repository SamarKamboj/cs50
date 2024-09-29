def main():
    before = input("Input: ")
    after = twttr(before)

    print("Output: " + after)


def twttr(word):
    word = word.lower()
    
    new_word = ''
    for char in word:
        vowels = ['a', 'e', 'i', 'o', 'u']

        if char in vowels:
            continue
        new_word += char

    return new_word


if __name__ = "__main__":
    main()
