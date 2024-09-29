from cs50 import get_int

# TODO
credit_num = get_int("Number: ")

card_len = len(str(credit_num))
if card_len != 15 and card_len != 13 and card_len != 16:
    print("INVALID")

f = 0
s = 0
x = credit_num
while True:
    # Remove last digit and add to f
    mod1 = x % 10
    x //= 10
    f += mod1

    # Remove second last digit
    mod2 = x % 10
    x //= 10

    # Double second last digit and add digits to s
    mod2 *= 2
    d1 = mod2 % 10
    d2 = mod2 // 10
    s += d1 + d2

    if x == 0:
        break

total_sum = f + s
# Check if card number is valid
if total_sum % 10 != 0:
    print("INVALID")
else:
    n = credit_num
    while True:
        n //= 10
        if n < 100:
            break

    if n >= 51 and n <= 55:
        print("MASTERCARD")
    elif n // 10 == 3 and (n % 10 == 4 or n % 10 == 7):
        print("AMEX")
    elif n // 10 == 4:
        print("VISA")
    else:
        print("INVALID")