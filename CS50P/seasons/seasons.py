# Import usefull module
from datetime import date
import re
import sys
import inflect



def main():
    # Take user Date of Birth
    dob = input("Date of Birth: ")
    # Check if user given input is in format yyyy-mm-dd or not
    check(dob)

    # Print the resulting minutes in words format
    print(convertToWords(minutes(dob)))


def check(s):
    matches = re.search(r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])", s)
    if not matches:
        sys.exit("Invalid date")


def minutes(dob):
    dob = date.fromisoformat(dob)
    # Import today's date month and year
    today = date.today()

    # Convert time difference of DOB and today into seconds
    seconds = (today - dob).total_seconds()
    # Convert seconds into minutes
    minutes = int(seconds / 60)

    return minutes

# Convert numeric value into words
def convertToWords(value):
    p = inflect.engine()
    words = p.number_to_words(value, andword='') + " minutes"

    # Return 'words' by capitalizing first word
    return words.capitalize()


if __name__ == "__main__":
    main()
