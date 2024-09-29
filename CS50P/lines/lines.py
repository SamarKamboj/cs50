import sys

def main():
    length = len(sys.argv)
    if length <= 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

    lines_of_code = lines()
    print(lines_of_code)

def lines():
    count = 0
    try:
        with open(sys.argv[1], "r") as file:
            for row in file:
                row = row.strip()
                if row == '':
                    continue
                elif row[0] == '#':
                    continue
                count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return count


main()
