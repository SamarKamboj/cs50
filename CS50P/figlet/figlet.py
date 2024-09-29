from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(argv) != 3 and len(argv) != 1:
    exit("Invalid Usage")
elif argv[1] != '-f' and argv[1] != "--font":
    exit("Invalid Usage")
elif argv[2] not in fonts:
    exit("Invalid Usage")

user_input = input("Input: ")

if len(argv) == 3:
    f = argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(user_input))

else:
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(user_input))
