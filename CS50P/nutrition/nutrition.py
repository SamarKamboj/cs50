nutrition = {
    "Apple": 130,
    "Pear": 100,
    "Avocado": 50,
    "Kiwifruit": 90,
    "Sweet Cherries": 100
}

fruit = input("Item: ").title()
if fruit in nutrition:
    print(f"Calories: {nutrition[fruit]}")