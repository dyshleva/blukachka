import game

# Стрийська, вул. Козельницька, вул. І.Франка, пр.Т.Шевченка, вул. Краківська
stryyska = game.Room('Стрийська')
stryyska.set_description("вулиця, з якої починається подорож")

kozelnytska = game.Room('Козельницька')
kozelnytska.set_description("вулиця, на якій чомусь немає кіз")

secret = game.Room('secret street')
secret.set_description("вулиця secret, бо ніхто не знає, що там")

franka = game.Room('І.Франка')
franka.set_description("вулиця названа в честь відомого українського поета")

shevchenka = game.Room('пр.Т.Шевченка')
shevchenka.set_description("вулиця 4")

krakivska = game.Room('вул. Краківськаа')
krakivska.set_description("вулиця остання")

# керування
stryyska.link_room(kozelnytska, "next")

kozelnytska.link_room(franka, "next")
kozelnytska.link_room(stryyska, "previous")
kozelnytska.link_room(secret, "provulok")

franka.link_room(shevchenka, "next")
franka.link_room(kozelnytska, "previous")
secret.link_room(kozelnytska, "previous")

shevchenka.link_room(krakivska, "next")
shevchenka.link_room(franka, "previous")

krakivska.link_room(shevchenka, "previous")
krakivska.link_room(stryyska, "taxi")

# вороги
dave = game.Enemy("Dave", "An ordinary zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("book")
kozelnytska.set_character(dave)

crave = game.Strongenemy(
    "Crave", "Really strong enemy with unexpectable results after fight ")
crave.set_conversation("What's up, i`m CRave! I'm hungry.")
crave.set_weakness("knife")
franka.set_character(crave)

mave = game.Twicekilled("Mave", "you need 2 same objects to kill this enemy")
mave.set_conversation("What's up, i`m Mave! I'm hungry.")
mave.set_weakness("knife")
shevchenka.set_character(mave)


# допоміжні речі
knife = game.Item("knife")
knife.set_description("A big amnd dangerous knife")
krakivska.set_item(knife)
shevchenka.set_item(knife)

book = game.Item("book")
book.set_description("A really good book kills many zombies")
franka.set_item(book)

flowers = game.Item('flowers')
flowers.set_description(
    "Bright flowers (hint: what will cavalers gift to their lovely girlfriends?)")
stryyska.set_item(flowers)

juice = game.Support('juice')
juice.set_description("peach juice")
secret.set_item(juice)


# friends
cavaler = game.Cavaler(
    "cavaler", "A great guy that may gift you something special (try to please him)+")
cavaler.set_conversation("What's up, dude! I want to tell you a joke")
cavaler.set_please("flowers")
secret.set_character(cavaler)


current_room = stryyska
backpack = []

dead = False
win = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()
    if win == True and current_room == krakivska:
        print('Congratulations, you have won')
        dead = True
    else:
        command = input("> ")

        if command in ["next", "previous", 'provulok']:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()

        elif command == 'please':
            if isinstance(inhabitant, game.Enemy):
                print("It`s  an enemy, attack him")
            elif inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print(f"What will you give him?\n {(',').join(backpack)}")
                please_with = input()
                if please_with in backpack:
                    # print("Hooray, you pleased your Friend!")
                    if inhabitant.pleasure(please_with) == True:
                        # What happens if you win?
                        print(f"Hooray, you won the joke! {inhabitant.joke()}")
                        current_room.character = None
                        if inhabitant.get_defeated() >= 3:
                            if current_room == krakivska:
                                print(
                                    "Congratulations, you have vanquished the enemy horde and pleased your friends!")
                                dead = True
                            else:
                                win = True
                                print("go to the krakivska street to win!")
                    else:
                        # What happens if you lose?
                        print("Oh dear, that`s a bad surprise.")
                else:
                    print("You don't have a " + please_with)
            else:
                print("There is no one here to please")

        elif command == "fight":
            if isinstance(inhabitant, game.Friend):
                print("It`s not an enemy, don`t attack him")
            elif inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:
                    if isinstance(inhabitant, game.Twicekilled):
                        if backpack.count(fight_with) >= 2 and inhabitant.fight(fight_with) == True:
                            # What happens if you win Twicekilled?
                            print("Hooray, you won the fight with Twicekilled!")
                            current_room.character = None

                            if inhabitant.get_defeated() >= 3:
                                if current_room == krakivska:
                                    print(
                                        "Congratulations, you have vanquished the enemy horde and pleased your friends!")
                                    dead = True
                                else:
                                    win = True
                                    print(
                                        "go to the krakivska street to win!")
                    elif isinstance(inhabitant, game.Strongenemy):
                        if inhabitant.fight(fight_with) == True:
                            # What happens if you win?
                            print(
                                "Hooray, you won the fight! But this enemy was too strong, so your score remains stable")
                            current_room.character = None

                            if inhabitant.get_defeated() >= 3:
                                if current_room == krakivska:
                                    print(
                                        "Congratulations, you have vanquished the enemy horde and pleased your friends!")
                                    dead = True
                                else:
                                    win = True
                                    print(
                                        "go to the krakivska street to win!")

                    elif inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.character = None

                        if inhabitant.get_defeated() >= 3:
                            if current_room == krakivska:
                                print(
                                    "Congratulations, you have vanquished the enemy horde!")
                                dead = True
                            else:
                                win = True
                                print(
                                    "go to the krakivska street to win!")
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                if isinstance(item, game.Support):
                    print(
                        f'This item -{item.name}- has given you one more point')
                    if item.treat() >= 3:
                        if current_room == krakivska:
                            print(
                                "Congratulations, you have vanquished the enemy horde!")
                            dead = True
                        else:
                            win = True
                            print("go to the krakivska street to win!")

                else:
                    print("You put the " + item.get_name() + " in your backpack")
                    backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == 'taxi':
            print("Congratulations, you have won because you are smart!")
            dead = True

        else:
            print("I don't know how to " + command)
