# blukachka
# TASK 5
CLASSES:

- class Room: 

(describes different types of locations in the game)

you may set description of it, add character or item, linked rooms to wich you may move further. And get all the information about your current location

    def __init__(self, name):
    
    def set_description(self, description):
    def link_room(self, linked_room, side):
    def set_character(self, character):

    def set_item(self, item):
    def get_details(self):
    def get_character(self):
    def get_item(self):
    def move(self, command):
    
- class Person:

(it contains all the basic information about people we may meet in the rooms - name, description)

    def __init__(self, name, description)

- class Mycharacter: 

(to get the score of the game)
    
    def __init__(self):
    
    def fought(self):
    
- class Enemy(Person): 

(child class of Person. you should fight these characters to get a point)
    
    def set_weakness(self, weakness):
    
    def fight(self, fight_with):
    
    def get_defeated(self):
    
    def describe(self):
    
    def talk(self):
    
- class Item: 

(class for all items that help you to fight . Contains descriptions.)
    
    def __init__(self, name):
    
    def set_description(self, description):
        
    def describe(self):
    
    def get_name(self):

    

# TASK 6
Game in which you need to collect 3 points by winning different type of enemies or finding support items

CLASSES:

- class Room: 

(describes different types of locations in the game)

you may set description of it, add character or item, linked rooms to wich you may move further. And get all the information about your current location
    
  
    def __init__(self, name):
    
    def set_description(self, description):
    def link_room(self, linked_room, side):
    def set_character(self, character):

    def set_item(self, item):
    def get_details(self):
    def get_character(self):
    def get_item(self):
    def move(self, command):
        
                
- class Person:

(it contains all the basic information about people we may meet in the rooms - name, description, conversation, battle score)

    def __init__(self, name, description)

    def set_conversation(self, conversation):
    
    def describe(self):
    
    def talk(self):
    
    def get_defeated(self):
    
    

- class Mycharacter: 

(to get the score of the game)

    def __init__(self):
    
    def fought(self):
        
        

- class Friend(Person): 

(child class of Person. you should please these characters to get a point. Additionally they give you a joke)

    def joke(self):
        
    def set_please(self, please):
        
    def pleasure(self, please_with):
    
- class Cavaler(Friend): 

(child class of Friend. Brings auto winning)
    
    def get_defeated(self):
      
      
- class Enemy(Person): 

(child class of Person. you should fight these characters to get a point)
    
    def set_weakness(self, weakness):
    
    def fight(self, fight_with):
    
    def get_defeated(self):

- class Strongenemy(Enemy):

(Enemy class child. Doesn`t bring you a point, even if you win)
    
    def get_defeated(self):
       
- class Twicekilled(Enemy):

(Enemy class child.you need 2 same elements to kill him)
    
    def fight(self, fight_with):
        
        
- class Item: 

(class for all items that help you to fight or to win faster. Contains descriptions.)
    
    def __init__(self, name):
    
    def set_description(self, description):
        
    def describe(self):
    
    def get_name(self):
       
 - class Support(Item):
 
 (Item class child.Give you 1 additional point)
    
    def treat(self):
       
