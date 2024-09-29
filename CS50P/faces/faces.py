def main():
    # Take user input
    before = input()
    # Converting slightly smiling ':)' or/and frowning face ':('
    after = convert(before)
    # Printing the changed text
    print(after)


def convert(before):
    # Empty string
    after = ''
    # Iterating over text
    index = 0
    while index < len(before):
        # Change to slightly smiling face if found ':)'
        if before[index] == ':' and before[index + 1] == ')':
            after += "\N{slightly smiling face}"  # Add smiling face
            index += 2  # Add 2 to index for not checking next char, it's already added

        # Change to slightly frowning face if found ':('
        elif before[index] == ':' and before[index + 1] == '(':
            after += "\N{slightly frowning face}"  # Add frowning face
            index += 2  # Add 2 to index for not checking next char, it's already added
            
        # Add char without changing
        else:
            after += before[index]
            index += 1

    # Return new text
    return after


# Call the main function
main()
