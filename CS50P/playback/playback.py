# Takes user input
before = input()
# Empty string
after = ''
# Iterate into user input
for i in before:
    # If ' ' (space) change it to '...' (three dots)
    if i == ' ':
        after += '...'
    else:
        after += i

print(after)