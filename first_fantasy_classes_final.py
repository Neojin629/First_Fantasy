import random
from time import sleep
from art import castle, title, the_end, production


# prints imported ASCII art from art.py
print(castle)

print(title)

# Building out Classes for Characters,Weapons, Obstacles and Villains


class Player_Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


black_knight = Player_Character("Black Knight", 100, 100)
king_arthur = Player_Character("King Arthur", 120, 100)
merlin = Player_Character("Merlin", 80, 100)


class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


sword = Weapons("Sword", 110)
spear = Weapons("Spear", 90)
mace = Weapons("Mace", 80)
magic = Weapons("Magic", 200)


class Villains:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


goblin = Villains("Goblin", 400, 20)
werewolf = Villains("Werewolf", 550, 22)
vampire = Villains("Vampire", 600, 25)
dragon = Villains("Dragon", 1000, 50)


class Obstacles:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


volcano = Obstacles("Volcano", 1000)
flood = Obstacles("Flood", 90)
earthquake = Obstacles("Earthquake", 500)


# Dictionary of characters player can choose from
characters = [black_knight.name, black_knight.hp,
              king_arthur.name, king_arthur.hp, merlin.name, merlin.hp]

# Dictionary of weapons player can choose from
weapons = [sword.name, spear.name, mace.name, magic.name]


print("Welcome to First Fantasy!\n")

print("The time has come...our World is in danger and only YOU can save it!\n")

# Asks the player if the would like to play the game
player_choice = input("Are you ready to save the world? Yes or No? ").lower()
if player_choice == "yes":
    print("\nExcellent!  Let's get started!\n")
else:
    print("See you next time!")
    exit()


# While loop that asks the player for their character, updates character_strength for chosen character
while True:
    character_selection = input(
        f"Select your character by typing their name, their HP is dictated by the number next to their name: {characters} ").lower()
    if character_selection == "black knight":
        print("\nA fearsome fighter, feared by many, excellent choice! You are now, the Black Knight!\n")
        character_hp = black_knight.hp
        break
    elif character_selection == "king arthur":
        print("\nMy king!  We bow to you!  You are now King Arthur!\n")
        character_hp = king_arthur.hp
        break
    elif character_selection == "merlin":
        print(
            "\nAhh a powerful Wizard!  The enemies will meet their match! You are now Merlin!\n")
        character_hp = merlin.hp
        break
    else:
        print("\nPlease select a character from the list in order to save our World\n")


# While loop that asks the player for their weapon, updates weapon_damage for chosen weapon
while True:
    weapon_selection = input(
        f"Select your weapon by typing its name: {weapons} ").lower()
    if weapon_selection == "sword":
        print("\nA powerful weapon, heavy but dangerous in the right hands.  You now have Sword equipped.\n")
        weapon_damage = sword.damage
        break
    elif weapon_selection == "spear":
        print(
            "\nFast, agile and great against multiple enemies. You now have Spear equipped\n")
        weapon_damage = spear.damage
        break
    elif weapon_selection == "mace":
        print("\nA truly dangerous weapon, terrifying and quite frankly, very pointy.  You now have Mace equipped.\n")
        weapon_damage = mace.damage
        break
    if weapon_selection == "magic" and character_selection == "merlin":
        print("\nYears of training are required for this weapon...however, super powerful in the right hands.  You now have Magic equipped.\n")
        weapon_damage = magic.damage
        break
    # Only Merlin can use magic, so it forces other characters to use another weapon
    elif weapon_selection == "magic" and character_selection != "merlin":
        print("\nOnly Wizards can use Magic...Please select another weapon!\n")
    # Prints if option chosen not inside the dictionary
    else:
        print("\nPlease select a weapon, there's no time to waste!\n")


# While loop to determine what player would like to do when facing the obstacles. Having it loop 5 times to help build Character HP before the Boss Battle

adventure = 0

while adventure < 5:

    input("\nAdventure Awaits...Press Enter To Continue Your Quest!")

    # List of obstacles that the player can run into during their adventure
    obstacles = [goblin.name, werewolf.name, vampire.name,
                 flood.name, volcano.name, earthquake.name]

    # Ramdomizes the obstacles so that every playthrough is different.
    current_obstacles = random.choice(obstacles)

    print(f"\nYou have encountered a {current_obstacles}!")

    while True:
        if current_obstacles == "Goblin":
            goblin.hp = goblin.hp - weapon_damage
            print("\nYou damaged the Goblin!")
            print("The Goblin's hitpoints are now:", goblin.hp)
            sleep(2)
            if goblin.hp <= 0:
                character_hp = character_hp + 100
                goblin.hp = 500
                print("\nYou have defeated the Goblin, Impressive!")
                print(f"\nYour Character now has {character_hp} hp! ")
                break
            character_hp = character_hp - goblin.damage
            print("\nThe Goblin strikes back!")
            print("Your hitpoints are now:", character_hp)
            sleep(2)
            if character_hp <= 0:
                print("You have lost the battle.  Game Over")
                exit()
        elif current_obstacles == "Werewolf":
            werewolf.hp = werewolf.hp - weapon_damage
            print("\nYou damaged the Werewolf!")
            print("The Werewolf's hitpoints are now:", werewolf.hp)
            sleep(2)
            if werewolf.hp <= 0:
                character_hp = character_hp + 100
                werewolf.hp = 550
                print("\nYou have defeated the Werewolf, Impressive!")
                print(f"\nYour Character now has {character_hp} hp! ")
                break
            character_hp = character_hp - werewolf.damage
            print("\nThe Werewolf strikes back!")
            print("Your hitpoints are now:", character_hp)
            sleep(2)
            if character_hp <= 0:
                print("\nYou have lost the battle.  Game Over")
                exit()
        elif current_obstacles == "Vampire":
            vampire.hp = vampire.hp - weapon_damage
            print("\nYou damaged the Vampire!")
            print("The Vampire's hitpoints are now:", vampire.hp)
            sleep(2)
            if vampire.hp <= 0:
                character_hp = character_hp + 100
                vampire.hp = 600
                print("\nYou have defeated the Vampire, Impressive!")
                print(f"\nYour Character now has {character_hp} hp! ")
                break
            character_hp = character_hp - vampire.damage
            print("\nThe Vampire strikes back!")
            print("Your hitpoints are now:", character_hp)
            sleep(2)
            if character_hp <= 0:
                print("\nYou have lost the battle.  Game Over")
                exit()
        elif current_obstacles == "Flood":
            print("\nThe plains are rapidly flooding!  You have to make a choice!")
            choice = input(
                "Do you want to turn back or keep going? Enter Back or Forward: ").lower()
            if choice == "back":
                print(
                    "\nYou have avoided the Flood and you have received no damage, whew!")
                print(f"\nYour Character has {character_hp} hp! ")
                break
            elif choice == "forward":
                character_hp = character_hp - flood.damage
                if character_hp <= 0:
                    print("\nYou have drowned.  Game Over")
                    exit()
                else:
                    print("\nYou survived...barely...")
                    print(f"\nYour Character has {character_hp} hp! ")
                break
        elif current_obstacles == "Volcano":
            print("\nA Volcano has just erupted!  You have to make a choice!")
            choice = input(
                "Do you want to turn back or keep going? Enter Back or Forward: ").lower()
            if choice == "back":
                print(
                    "\nYou have avoided the Volcano and you have received no damage, whew!")
                print(f"\nYour Character has {character_hp} hp! ")
                break
            elif choice == "forward":
                character_hp = character_hp - volcano.damage
                if character_hp <= 0:
                    print("\nYou were burned alive.  Ouch...  Game Over")
                    exit()
                else:
                    print("\nYou survived...barely...")
                    print(f"\nYour Character has {character_hp} hp! ")
                break
        elif current_obstacles == "Earthquake":
            print(
                "\nAn Earthquake is destroying the ground around you!  You have to make a choice!")
            choice = input(
                "Do you want to turn back or keep going? Enter Back or Forward: ").lower()
            if choice == "back":
                print(
                    "\nYou have avoided the massive hole in the ground and you have received no damage, whew!")
                print(f"\nYour Character has {character_hp} hp! ")
                break
            elif choice == "forward":
                character_hp = character_hp - earthquake.damage
                if character_hp <= 0:
                    print("\nYou fell into the hole...  Ouch...  Game Over")
                    exit()
                else:
                    print("\nYou survived...barely...")
                    print(f"\nYour Character now has {character_hp} hp! ")
                break

    adventure += 1

# Dragon Boss Battle. HINT: Magic always beats dragon

input(
    f"\nSomething MASSIVE approaches over the horizon!  Get ready!  This won't be easy! It's a Dragon!!!  Press Enter When Ready... ")
while True:

    current_obstacles = "Dragon"

    if current_obstacles == "Dragon":
        dragon.hp = dragon.hp - weapon_damage
        print("\nYou damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon.hp)
        sleep(2)
        if dragon.hp <= 0:
            character_hp = character_hp + 100
            dragon.hp = 1000
            print("\nYou have defeated the Dragon and saved the Kingdom!")
            print(f"\nThank you for playing! ")
            print(the_end)
            sleep(2)
            print(production)
            exit()
        character_hp = character_hp - dragon.damage
        print("\nThe Dragon strikes back, HARD!")
        print("Your hitpoints are now:", character_hp)
        sleep(2)
        if character_hp <= 0:
            print("You have lost the battle.  The Kingdom Falls...")
            exit()
