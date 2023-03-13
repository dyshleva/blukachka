class Room:
    '''
    class to describe a room
    '''

    def __init__(self, name):
        self.name = name
        self.linked_rooms = []
        self.character = None
        self.item = None

    def set_description(self, description):
        '''
        description of the room
        '''
        self.description = description

    def link_room(self, linked_room, side):
        '''
        linked rooms to the main room
        '''
        self.linked_rooms += [[linked_room, side]]

    def set_character(self, character):
        '''
        add a character to the room
        '''
        self.character = character

    def set_item(self, item):
        '''
        add a item to the room
        '''
        self.item = item

    def get_details(self):
        '''
        get full information about the room

        Kitchen
        --------------------
        A dank and dirty room buzzing with flies.
        The Dining Hall is south
        '''
        print(
            f'{self.name}\n--------------------\n{self.description}')
        for room in self.linked_rooms:
            print(f'The {room[0].name} is {room[1]}')

    def get_character(self):
        '''
        find which character is in the room
        '''
        return self.character

    def get_item(self):
        '''
        find which item is in the room
        '''
        return self.item

    def move(self, command):
        '''
        move to another linked room
        '''
        for room in self.linked_rooms:
            if room[1] == command:
                return room[0]


class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Mycharacter:
    '''
    class for main characrter
    '''

    def __init__(self):
        self.counter = 0

    def fought(self):
        '''
        fight calculate
        '''
        self.counter += 1
        return self.counter


my = Mycharacter()


class Enemy(Person):
    '''
    class for main characrters enemies
    '''

    def set_conversation(self, conversation):
        '''
        enemies words
        '''
        self.conversation = conversation

    def set_weakness(self, weakness):
        '''
        enemies weakness
        '''
        self.weakness = weakness

    def describe(self):
        '''
        description of the enemy
        '''
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        '''
        print enemies words
        '''
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, fight_with):
        '''
        fight method
        '''
        return fight_with == self.weakness

    def get_defeated(self):
        '''
        find out info about our winnings
        '''
        return my.fought()


class Item:
    '''
    class for all items
    '''

    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        '''
        description of an item
        '''
        self.description = description

    def describe(self):
        '''
        print the description
        '''
        print(f'The [{self.name}] is here -{self.description}')

    def get_name(self):
        '''
        Find out the name of the item
        '''
        return self.name
