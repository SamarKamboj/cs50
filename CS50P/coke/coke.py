def main():
    due = 50
    while True:
        print(f"Amount due: {due}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            due -= coin

        if due <= 0:
            print(f"Change owed: {abs(due)}")
            break


main()
