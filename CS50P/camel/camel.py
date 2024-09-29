camelCase = input("camelCase: ")
snake_case = ''
for char in camelCase:
    if char.isupper():
        snake_case += '_'
    snake_case += char.lower()

print(snake_case)