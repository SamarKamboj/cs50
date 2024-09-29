import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(1[0-2]|0?[1-9])(:[0-5][0-9])? ([AP]M) to (1[0-2]|0?[1-9])(:[0-5][0-9])? ([AP]M)", s)
    if not matches:
        raise ValueError

    h1, min1, m1 = matches.group(1), matches.group(2) if matches.group(2) != None else ":00", matches.group(3)
    h2, min2, m2 = matches.group(4), matches.group(5) if matches.group(5) != None else ":00", matches.group(6)

    if int(h1) > 12 or int(h2) > 12:
        raise ValueError

    firstTime = newFormat(h1, min1, m1)
    secondTime = newFormat(h2, min2, m2)

    return firstTime + " to " + secondTime


def newFormat(hour, minute, meridiem):

    if meridiem == "PM" and hour != "12":
        hour = f"{int(hour) + 12}"

    if meridiem == "AM" and hour == "12":
        hour = "00"

    return f"{int(hour):02}" + minute


if __name__ == "__main__":
    main()
