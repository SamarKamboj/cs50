expression = input("Expression: ").split(' ')

first_num = float(expression[0])
second_num = float(expression[2])
operator = expression[1]

match operator:
    case '/':
        print(f"{(first_num / second_num):.1f}")
    case '+':
        print(f"{(first_num + second_num):.1f}")
    case '-':
        print(f"{(first_num - second_num):.1f}")
    case '*':
        print(f"{(first_num * second_num):.1f}")


# Use this line to shorten the code
# print(f"{eval(expression):.1f}")