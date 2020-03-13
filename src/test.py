from PyInquirer import prompt
from colorama import Fore  # Fore is for foreground color of text
from colorama import init  # init is used to configure colorama
import os
"""
Docs:
PyInquirer: https://github.com/CITGuru/PyInquirer
Colorama: https://github.com/tartley/colorama
"""

# sets colorama autoreset to true
# prevents text color retention
init(autoreset=False)

# main menu configurations
main_menu = [
    {
        "type": "list",  # type of menu
        "name": "menu",
        "message": "What action would you like to take?",
        "choices": ["Move", "Quit"],
    }
]

# direction menu configurations
direction_menu = [
    {
        "type": "list", 
        "name": "direction",
        "message": "Which direction",
        "choices": ["North", "South", "East", "West", "Back to Menu"],
    }
]

# just a print function
def print_direction(direction):
    print(Fore.MAGENTA + "\nPlayer moved " + Fore.GREEN + f"{direction}\n")


cmd = ""
direction = ""

while not cmd == "Quit":
    # clears terminal after each loop
    os.system('cls') # windows

    # prints message at the start of each loop
    print_direction(direction)

    # this is where the menu gets rendered to the terminal and collects the input
    cmd = prompt(main_menu)[
        "menu" # menu at the end here refers to "name" in the config above
    ]  

    if cmd == "Move":
        # another menu prompt for the user to enter a cardinal direction
        direction = prompt(direction_menu)["direction"]

        if direction == "North":
            # TODO: Add game logic
            pass
        elif direction == "South":
            # TODO: Add game logic
            pass
        elif direction == "East":
            # TODO: Add game logic
            pass
        elif direction == "West":
            # TODO: Add game logic
            pass
    elif cmd == "Other Option":
        pass

os.system("cls")
print(Fore.RED + "Game over...")