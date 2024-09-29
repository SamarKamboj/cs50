def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Return after removing first char and converting into float
    return float(d[1:])


def percent_to_float(p):
    # TODO
    # Return after removing last char, convert into float and then divide it by 100
    return float(p[:-1]) / 100


main()