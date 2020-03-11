# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def move_player(self, movement):
        if(getattr(self.currentRoom, f'{movement}_to') != None):
            self.currentRoom = getattr(self.currentRoom, f'{movement}_to')
        else:
            print('That move is not possible')

    def get_item(self, pickup_item):
        self.items.append(pickup_item)

    def drop_item(self, drop_item):
        self.items.remove(drop_item)
        self.currentRoom.items.append(drop_item)

    def __str__(self):
        return f'{self.name} is in the {self.currentRoom}. \n {self.currentRoom.description}'