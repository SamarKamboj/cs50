def main():
    # List of months in a year
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Run Loop infinitely
    while True:
        # Prompt user for Date
        date = input("Date: ")
        try:
            m, d, y = date.split('/')
            # Convert number string into number
            m, d, y = int(m), int(d), int(y)
            # If from outside of this planet, ask date again
            if (int(m) > len(month) or int(m) < 0) or (int(d) > 31 or int(d) < 0):
                continue
        except:
            try:
                m, d, y = date.split(' ')
                if ',' not in d:
                    continue

                # Replace comma from string with nothing
                d = d.replace(',', '')
                # Convert into integers if number string
                d, y = int(d), int(y)
                # Check month list for index of month
                m = month.index(m) + 1
                # If from outside of this planet, ask date again
                if (int(m) > len(month) or int(m) < 0) or (int(d) > 31 or int(d) < 0):
                    continue
            except:
                pass
            else:
                print(f"{y}-{m:02}-{d:02}")
                break

        else:
            print(f"{y}-{m:02}-{d:02}")
            break


main()