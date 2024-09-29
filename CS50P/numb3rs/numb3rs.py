import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    ip_list = [i for i in ip.split('.') if '0' <= i <= "255"]

    if len(ip_list) != 4:
        return False

    return True


if __name__ == "__main__":
    main()