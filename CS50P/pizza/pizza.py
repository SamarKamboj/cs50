import sys
from tabulate import tabulate
import csv

def main():
    length = len(sys.argv)
    if length <= 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

    print(format())


def format():
    menu = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    table = menu[1:]
    header = menu[0]

    return tabulate(table, header, tablefmt="grid")


main()
