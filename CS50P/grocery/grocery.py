def main():
    grocery = dict()
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            if item not in grocery:
                grocery[item] = 0

            grocery[item] += 1

    for thing in sorted(grocery.keys()):
        print(grocery[thing], end=' ')
        print(thing)


main()
