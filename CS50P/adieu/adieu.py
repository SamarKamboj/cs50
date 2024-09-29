from inflect import engine


def main():
    # Class from a module called inflect
    p = engine()

    # Empty List to store new words
    words = []
    # Existing text and to add new text/word
    text = "Adieu, adieu, to "
    # Infinite Loop until work done
    while True:
        # Exceptions
        try:
            # Input word
            user_input = input("Name: ")
            # Add input word to 'words' list
            words.append(user_input)

        except EOFError:
            # If End of File (control-d) Join the words in "words" list
            text += p.join(words)
            # Return the new text
            return text


# Print the new text
print(main())
