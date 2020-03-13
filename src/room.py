# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'{self.location}: {self.description}\n The possible choices include: North? {self.n_to}, East? {self.e_to}, South? {self.s_to}, West? {self.w_to} '