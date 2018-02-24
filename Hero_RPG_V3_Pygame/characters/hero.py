from characters.base_characters import Character
import random
import math

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.health = 50
        self.max_health = 50
        self.power = 10
        self.defense = 8
        self.special_desc = "Generates 2x damage / 20%"
        self.coins = 100
        self.items = {
            "Tonic": 0, 
            "Helmet": 0, 
            "Sword": 0, 
            "Shield": 0, 
            "Chainmail": 0,
            "Zombie_Axe": 0,
            "Dragon_Fire_Shield": 0

        }
        self.upgrades = {
            "Power_Level": 0,
            "Defense_Level": 0,
            "Health_Level" : 0,
        }
        self.x = 512 / 2
        self.y = 480 / 2
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.fight_status = False
        self.health_bar_numb = 20

    def hero_status(self, hero):
        print("", "-" * 42)
        print(" \033[1;34;40m{} - \033[1;33;40mCoins: {} \U0001F4B0 \033[0;37;40m ".format(hero.name, hero.coins), " " * 20)
        print("  \033[1;32;40mPower: {}\u2694\uFE0F  \033[1;36;40mDefense: {}\U0001F6E1  \033[1;31;40mHealth: {}/{} \u2764\uFE0F  \033[0;37;40m".format(hero.power, hero.defense, hero.health, hero.max_health))
        print("", "-" * 42)

    def bounty_earned(self, hero, enemy):
        randNumb = random.randint(0, len(enemy.bounty) - 1)    
        print("\033[1;33;40mYou receive {} coins\U0001F4B0 \033[0;37;40m".format(enemy.bounty[randNumb]))
        self.coins += enemy.bounty[randNumb]    # Receive coins from enemy

    def restore_health(self, hero):
        if (hero.health + 10) > self.max_health:
            restore_amount = self.max_health - self.health
        else:
            restore_amount = 10
        self.health += restore_amount
        self.items["Tonic"] -= 1
        print("\033[0;32;40m{} drank a Tonic and restored \033[1;32;40m{}\033[0;32;40m health.\033[0;37;40m".format(self.name, restore_amount))

    def equip_items(self, hero, item):
        if item == "Helmet":
            self.defense += 3
        elif item == "Sword":
            self.power += 7
        elif item == "Shield":
            self.defense += 7
        elif item == "Chainmail":
            self.defense += 13
        elif item == "Zombie_Axe":
            self.power += 1
        elif item == "Dragon_Fire_Shield":
            self.defense += 2

    def upgrade_hero_levels(self, hero, upgrade):
        if upgrade == "Power_Level":
            self.power += 1
        elif upgrade == "Defense_Level":
            self.defense += 1
        elif upgrade == "Health_Level":
            self.health += 1
            self.max_health += 1

    def movement(self, hero, mouse_position):

        distance = math.sqrt((math.pow(hero.x - mouse_position[0], 2)) + (math.pow(hero.y - mouse_position[1], 2)))
        if distance < 32:
            hero.speed_x = 0
            hero.speed_y = 0
            return True
        else:
            hero.speed_x = 1
            hero.speed_y = 1
            return False

        
