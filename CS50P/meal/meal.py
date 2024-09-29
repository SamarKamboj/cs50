def main():
    user_time = input("What time is it? ")
    time = convert(user_time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(':')
    minute = int(time[1]) / 60

    return int(time[0]) + minute


if __name__ == "__main__":
    main()