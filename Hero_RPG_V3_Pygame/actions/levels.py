import random
import math
import pygame


from characters.hero import Hero
from characters.enemies import Fake
from characters.enemies import Goblin
from characters.enemies import Medic
from characters.enemies import Ranger
from characters.enemies import Wizard
from characters.enemies import Shadow
from characters.enemies import Zombie
from characters.enemies import Dragon


class Store(object): # level 0
    def __init__(self):
        self.background_image = pygame.image.load("images/store.png").convert_alpha()
        self.enemy_char = []
        self.healing_potion = {"price": 8, "description": "Heals 10 health"}
        self.helmet = {"price": 150, "description": "+ 3 Defense"} 
        self.sword = {"price": 200, "description": "+ 7 Attack"}
        self.shield = {"price": 225, "description": "+ 7 Defense"}
        self.chainmail = {"price": 750, "description": "+ 13 Defense"}
        self.zombie_axe = {"price": 2000, "description": "+ 1 Attack"}
        self.dragon_fire_shield = {"price": 5000, "description": "+ 2 Defense"}
        
# Make price list its own class so that the prices could show up in the store
    def shopping(self, hero, item_bought):
        price_list = {
            "Healing_Potion": self.healing_potion["price"], 
            "Helmet": self.helmet["price"],
            "Sword": self.sword["price"], 
            "Shield": self.shield["price"],
            "Chainmail": self.chainmail["price"],
            "Zombie_Axe": self.zombie_axe["price"],
            "Dragon_Fire_Shield": self.dragon_fire_shield["price"],
        }
        try:
            if hero.coins < price_list[item_bought]:
                return "Not enough coins"
            elif hero.items[item_bought] == 1 and item_bought != "Healing_Potion":
                return "Already own", item_bought
            else:
                hero.coins -= price_list[item_bought]
                hero.items[item_bought] += 1
                return True
        except KeyError:
            pass

class Upgrade_Level_Store(object): # Level 0.1
    def __init__(self, hero):
        self.power_level = round(((hero.upgrades["Power_Level"] + 1) * (hero.upgrades["Power_Level"] + 1) + 20) * 2.3)
        self.defense_level = round(((hero.upgrades["Defense_Level"] + 1) * (hero.upgrades["Defense_Level"] + 1) + 20) * 2.3)
        self.health_level = round(((hero.upgrades["Health_Level"] + 1) * (hero.upgrades["Health_Level"] + 1) + 20) * 2.3)

    def level_up(self, hero, item_bought):    
        
        upgrade_price = {
            "Power_Level": self.power_level,
            "Defense_Level": self.defense_level,
            "Health_Level" : self.health_level,
        }

        try:
            if hero.coins < upgrade_price[item_bought]:
                    return "Not enough coins"
            else:
                hero.coins -= upgrade_price[item_bought]
                hero.upgrades[item_bought] += 1
                hero.upgrade_hero_levels(hero, item_bought)
                return True
        except KeyError:
            pass


class Level1(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_north_and_west_exit.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290), 
        Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]

class Level2(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_S_E_exits.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290), 
        Medic(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180),
        Medic(random.randint(300, 370), random.randint(300, 370), 290, 380, 290, 380)]
