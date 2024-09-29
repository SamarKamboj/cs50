def main():
    greeting = input("Greeting: ").lower().strip()
    if greeting[:5] == "hello":
        return 0
    elif greeting[0] == 'h' and greeting[1:5] != "ello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    print(f"${main()}", end='')
