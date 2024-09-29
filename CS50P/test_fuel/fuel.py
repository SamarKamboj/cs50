def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)

    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)

            if x / y <= 1:
                return round(x * 100 / y)
            else:
                fraction = input("Fraction: ")
                pass
        except ValueError or ZeroDivisionError:
            raise


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return str(percentage) + '%'


if __name__ == "__main__":
    main()
