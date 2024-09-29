import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^<iframe.*https?://(www.)?youtube.com/embed/(\w*).*></iframe>$", s)

    if not matches:
        return None

    return (f"https://youtu.be/{matches.group(2)}")


if __name__ == "__main__":
    main()