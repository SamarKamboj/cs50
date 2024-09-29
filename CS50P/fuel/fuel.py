def main():
    while True:
        try:
            fuel_frac = input("Fraction: ").split('/')
            x = int(fuel_frac[0])
            y = int(fuel_frac[1])

            convert_percentage = round(x * 100 / y)
            if convert_percentage > 100:
                continue
        except ValueError or ZeroDivisionError:
            pass
        else:
            if 99 <= convert_percentage <= 100:
                return 'F'
            elif 0 <= convert_percentage <= 1:
                return 'E'
            else:
                return str(convert_percentage) + '%'


print(main())