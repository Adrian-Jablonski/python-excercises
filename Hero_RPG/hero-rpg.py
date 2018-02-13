# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import time

fight_mode = False
enemy = ""

class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        if self.health >= 0 or self.name == "Zombie":
            enemy.health -= self.power
            print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
            time.sleep(1)

    def alive(self):
        if self.health > 0 or self.name == "Zombie":
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = "Goblin"
        self.health = 6
        self.power = 2
    
class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 10
        self.power = 2

hero = Hero()
goblin = Goblin()
zombie = Zombie()

while fight_mode == False:
    print("A goblin and zombie appears. Which do you fight?")
    print("1. Goblin")
    print("2. Zombie")
    print("3. Flee")
    print("> ", end=" ")
    raw_input = input()
    if raw_input == "1":
        enemy = goblin
        fight_mode = True
    elif raw_input == "2":
        enemy = zombie
        fight_mode = True
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

if fight_mode == True:
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            hero.attack(enemy)
            if enemy.health <= 0 and enemy.name != "Zombie":
                print("The enemy is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive:
            # enemy attacks hero
            enemy.attack(hero)
            if hero.health <= 0:
                print("You are dead.")