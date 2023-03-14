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

    def set_conversation(self, conversation):
        '''
        his words
        '''
        self.conversation = conversation

    def describe(self):
        '''
        description of the person
        '''
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        '''
        print enemies words
        '''
        print(f'[{self.name} says]: {self.conversation}')

    def get_defeated(self):
        '''
        find out info about our winnings
        '''
        return my.fought()


class Mycharacter:
    '''
    class for main characrter
    '''

    def __init__(self):
        self.counter = 0

    def fought(self):
        '''
        winnings counter
        '''
        self.counter += 1
        print(f'your score {self.counter}')
        return self.counter


my = Mycharacter()


class Friend(Person):
    def joke(self):
        '''
        tell a random joke
        '''
        import random
        jokes = ["Complaining about the lack of smoking shelters, the nicotine addicted Python programmers said there ought to be 'spaces for tabs'.",
                 "Ubuntu users are apt to get this joke.",
                 "Obfuscated Reality Mappers (ORMs) can be useful database tools.",
                 "Asked to explain Unicode during an interview, Geoff went into detail about his final year university project. He was not hired.",
                 "Triumphantly, Beth removed Python 2.7 from her server in 2030. 'Finally!' she said with glee, only to see the announcement for Python 4.4.",
                 "An SQL query goes into a bar, walks up to two tables and asks, 'Can I join you?'",
                 "When your hammer is C++, everything begins to look like a thumb."]
        return random.choice(jokes)

    def set_please(self, please):
        '''
        friends please
        '''
        self.please = please

    def pleasure(self, please_with):
        '''
        fight method
        '''
        return please_with == self.please


class Cavaler(Friend):
    '''
    If you meet a cavaler the game ends with winning
    '''
    def get_defeated(self):
        '''
        win automatically
        '''
        return 3


class Enemy(Person):
    '''
    class for main characrters enemies
    '''

    def set_weakness(self, weakness):
        '''
        enemies weakness
        '''
        self.weakness = weakness

    def fight(self, fight_with):
        '''
        fight method
        '''
        return fight_with == self.weakness

    def get_defeated(self):
        '''
        find out info about our winnings
        '''
        return super().get_defeated()


class Strongenemy(Enemy):
    def get_defeated(self):
        '''
        find out info about our winnings
        '''
        print(f'your score {my.counter}')
        return my.counter


class Twicekilled(Enemy):
    '''
    you need 2 same elements to kill him
    '''

    def fight(self, fight_with):
        '''
        fight method
        '''
        print('you want to fight twicekilled type of enemy')
        return fight_with == self.weakness


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


class Support(Item):
    def treat(self):
        '''
        gives you 1 additional point
        '''
        return my.fought()
