import csv
import sys


def main():
    # Exit if user hadn't given 2 command-line argument
    # one for reading and other for writing
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Read 1st command-line argument file
    data = readFile()

    # Write to 2nd command-line argument file even if it not exist
    writeToFile(data)


def readFile():
    # Empty list to store data from file
    before = []
    try:
        with open(sys.argv[1]) as file:
            # Read the file in Dictionary mode
            reader = csv.DictReader(file)
            # Iterate over list of dictionaries and append each one in 'before' list
            for line in reader:
                before.append(line)

    # Error handling if file not found or could not read
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    return before


def writeToFile(data):
    # Variable to store the File name in which we are going to write our data
    after = sys.argv[2]

    with open(after, 'w') as file:
        # Write to the file in Dictionary Mode
        writeTo = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        # Write the header to new file
        writeTo.writeheader()

        # Iterate over each dictionary of list 'data'
        for line in data:
            house = line["house"].strip()

            # Split and store the 'name' into 'first' and 'last'
            last, first = line["name"].split(',')
            # Strip off any whitespaces
            last, first = last.strip(), first.strip()

            # Write each row of data into new file with fieldnames
            writeTo.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()
