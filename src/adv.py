from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. To the west lies a dark cave"""),

    'narrow':   Room("Narrow Passage", """The room seems empty, but there is hole on
the floor the size of a rock."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! """),

    'darkroom': Room("Dark Room", """Its very dark, you cant see anything"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = room['darkroom']
room['darkroom'].e_to = room['overlook']
room['narrow'].w_to = room['foyer']
#room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['outside'].items = [Item(
    'rock', 'A heavy rock, I wonder what I could use this for...')]
room['foyer'].items = [Item(
    'torch', 'Its already lit, how strange')]
room['narrow'].items = [Item(
    'pickaxe', 'Its broken, but still good')]
room['treasure'].items = [Item(
    'old_chest', 'Gold'),
    Item(
    'shiny_chest', 'Curse')]  

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerName = input(f"What is your name adventurer?\n\n")
newplayer = Player(str(playerName), room['outside'])
completion = False
foundItem = False
backpackOpen = False
secretPassage = False
roomLit = False

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while completion == False:
    #This controls if the secret passage conditions have been met, only runs once
    if secretPassage == False and newplayer.currentRoom.location == 'Narrow Passage' and any(item.name == 'rock' for item in newplayer.currentRoom.items):
        print('\nYou place the rock into the hole, a secret passage to the north opens')
        secretPassage = True
        room['narrow'].n_to = room['treasure']
        room['narrow'].description = 'The room has revelead a secret passage to the north.'

    print(f'\n\n{newplayer.name} is now in the {newplayer.currentRoom.location}. {newplayer.currentRoom.description}\n')

   #This controls if the dark room conditions have been met, only runs once
    if roomLit == False and newplayer.currentRoom.location == 'Dark Room' and any(item.name == 'torch' for item in newplayer.items):    
        print('\nYou hold your torch ahead of you, you see written in blood on the wall "drop a rock and pick the old treasure to live')
        roomLit = True
        room['darkroom'].description = 'In the light you see written in blood on the wall "drop a rock and pick the old treasure to live'

    if(len(newplayer.currentRoom.items) > 0):
        print(
            f'The following items are observed in this room: {[item.name for item in newplayer.currentRoom.items]}\n')
    else:
        print('There are no items left in this room.\n')
    movement = input(
        f"What would you like to do? \nn, e, s, w to move \nType 'get' and the name of the item to add the item to player inventory.\nI to view your inventory.\nType 'drop' and the name of the item to remove the item from the player inventory.\nPress Q to exit.\n\n")
    result = movement.split(' ')
    if result[0] == 'get':
        for item in newplayer.currentRoom.items:
            if(item.name == result[1]):
                foundItem = True
                newplayer.get_item(item)
                newplayer.currentRoom.items.remove(item)
                for x in newplayer.items:
                    if(x.name == 'old_chest'):
                        print('\n\n\nCongratulations! You got the treasure! You win!')
                        completion = True
                    if(x.name == 'shiny_chest'): 
                        print('\n\n\nYou pick up the chest and hear a rumble, the door collapses behind you, you are trapped forever, you lose...')
                        completion = True   
        if foundItem == False:
            print('\n\n\nThat item is not in this room.')

    elif result[0] == 'drop':
        if any(item.name == result[1] for item in newplayer.items):
            for item in newplayer.items:
                if(item.name == result[1]):
                    newplayer.drop_item(item)
        else:
            print(f'You do not have a {result[1]} to drop in here.')

    elif movement.lower() == 'q':
        completion = True
        print('Thanks for playing. Try again later!')

    elif movement.lower() == 'n' or movement.lower() == 'e' or movement.lower() == 's' or movement.lower() == 'w':
        newplayer.move_player(movement)

    elif movement.lower() == 'i':
        if(len(newplayer.items) > 0):
            print(f'\nThe items in your inventory are as followed: {[item.name for item in newplayer.items]} \n')
            backpackOpen = True
            while backpackOpen == True:    
                print('\nInspect item by typing name or b to back\n')
                choice = input()
                if any(item.name == choice for item in newplayer.items):
                    for item in newplayer.items:
                        if(item.name == choice):
                            print(f'\n {[item.description]} \n')
                elif(choice.lower() == 'b'):
                    backpackOpen = False
                else:
                    print("\nPlease input the name of an item\n")     
        else:
            print("\nYou have no items currently\n")     
    else:
        print('Please choose a valid movement or action.')
