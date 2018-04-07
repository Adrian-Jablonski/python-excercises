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

class Main_Menu(object):
    def __init__(self):
        self.name = "Main Menu"
        self.background_image = pygame.image.load("images/background_images/main_menu.png").convert_alpha()
        self.enemy_char = []
        self.level_border_x = [350, 400]
        self.level_border_y = [100, 400]

class Main_Menu2(object):
    def __init__(self):
        self.name = "Main Menu2"
        self.background_image = pygame.image.load("images/background_images/main_menu_2.png").convert_alpha()
        self.enemy_char = []
        self.level_border_x = [350, 400]
        self.level_border_y = [100, 400]

class Store(object): # level 0
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/store.png").convert_alpha()
        self.enemy_char = []
        self.healing_potion = {"price": 15, "description": "Heals 10 health"}
        self.helmet = {"price": 200, "description": "+ 3 Defense"} 
        self.sword = {"price": 260, "description": "+ 7 Attack"}
        self.shield = {"price": 500, "description": "+ 7 Defense"}
        self.chainmail = {"price": 800, "description": "+ 13 Defense"}
        self.zombie_axe = {"price": 5000, "description": "+ 1 Attack"}
        self.dragon_fire_shield = {"price": 10000, "description": "+ 2 Defense"}
        self.level_border_x = [350, 400]
        self.level_border_y = [100, 400]

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

# class Upgrade_Level_Store(object): # Level 0.1
#     def __init__(self, hero):
#         self.power_level = round(((hero.upgrades["Power_Level"] + 1) * (hero.upgrades["Power_Level"] + 1) + 20) * 2.3)
#         self.defense_level = round(((hero.upgrades["Defense_Level"] + 1) * (hero.upgrades["Defense_Level"] + 1) + 20) * 2.3)
#         self.health_level = round(((hero.upgrades["Health_Level"] + 1) * (hero.upgrades["Health_Level"] + 1) + 20) * 2.3)

#     def level_up(self, hero, item_bought):    
        
#         upgrade_price = {
#             "Power_Level": self.power_level,
#             "Defense_Level": self.defense_level,
#             "Health_Level" : self.health_level,
#         }

#         try:
#             if hero.coins < upgrade_price[item_bought]:
#                     return "Not enough coins"
#             else:
#                 hero.coins -= upgrade_price[item_bought]
#                 hero.upgrades[item_bought] += 1
#                 hero.upgrade_hero_levels(hero, item_bought)
#                 return True
#         except KeyError:
#             pass

class Area_98_100(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_100.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(300, 370), random.randint(150, 300), 290, 380, 140, 310)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, self.level_border_y[0], self.level_border_y[1]]

class Area_99_100(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_100.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, 220, 275]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, self.level_border_y[0] - 20, self.level_border_y[1] + 30]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]

class Area_99_101(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_101.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.west_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[0] + 30, self.level_border_y[0], self.level_border_y[1] - 30]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        
class Area_98_101(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_101.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290), 
        Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, self.level_border_y[0], self.level_border_y[1]]

class Area_100_100(object): # OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_100.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290), 
        Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]
        self.west_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[0] + 30, 220, 275]

class Area_100_101(object): #  OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_101.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290)]
        self.level_border_x = [20, 460]
        self.level_border_y = [20, 445]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, 220, 275]

class Area_101_101(object): #  OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_101_101.png").convert_alpha()
        self.enemy_char = [Goblin(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Goblin(random.randint(210, 280), random.randint(220, 280), 200, 290, 210, 290), 
        Goblin(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [20, 490]
        self.level_border_y = [20, 490]
        self.north_area_change_x_y = [215, 300, self.level_border_y[0], self.level_border_y[0] + 30]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, 220, 275]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, 220, 275]

class Area_102_101(object):  #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_102_101.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(90, 160), random.randint(70, 140), 80, 170, 60, 150), 
        Shadow(random.randint(70, 140), random.randint(220, 280), 60, 150, 210, 290), 
        Shadow(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180),
        Shadow(random.randint(200, 270), random.randint(300, 370), 190, 280, 290, 380)]
        self.level_border_x = [20, 430]
        self.level_border_y = [77, 415]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, 220, 275]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, 220, 275]

class Area_101_102(object):     #OK Characters
    def __init__(self):  
        self.background_image = pygame.image.load("images/background_images/area_101_102.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(90, 160), random.randint(70, 140), 80, 170, 60, 150), 
        Medic(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180), 
        Goblin(random.randint(200, 270), random.randint(200, 270), 190, 280, 190, 280)]
        self.level_border_x = [105, 420]
        self.level_border_y = [100, 440]
        self.west_area_change_x_y = [self.level_border_x[0], self.level_border_x[0] + 30, 220, 275]
        self.south_area_change_x_y = [215, 300, self.level_border_y[1] - 30, self.level_border_y[1] + 30]

class Area_100_102(object): #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_102.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(120, 200), random.randint(130, 210), 110, 210, 120, 220), 
        Medic(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180), 
        Medic(random.randint(200, 270), random.randint(260, 330), 190, 280, 250, 340)]
        self.level_border_x = [124, 404]
        self.level_border_y = [20, 472]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1] + 30, 220, 275]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1] + 30, self.level_border_y[0] - 20, self.level_border_y[0] + 30]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, 220, 275]

class Area_100_103(object):     #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_103.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(90, 160), random.randint(70, 140), 70, 170, 60, 150), 
        Shadow(random.randint(70, 140), random.randint(220, 280), 60, 150, 210, 290)]
        self.level_border_x = [124, 404]
        self.level_border_y = [20, 472]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]

class Area_100_104(object): #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_104.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(90, 160), random.randint(70, 140), 80, 170, 70, 150), 
        Shadow(random.randint(250, 320), random.randint(300, 370), 240, 310, 290, 380)]
        self.level_border_x = [80, 340]
        self.level_border_y = [20, 472]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]

class Area_100_105(object): #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_100_105.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(90, 160), random.randint(150, 220), 80, 170, 140, 230),  
        Shadow(random.randint(280, 340), random.randint(140, 210), 270, 350, 130, 220),
        Shadow(random.randint(150, 230), random.randint(380, 450), 140, 240, 370, 460)]
        self.level_border_x = [90, 370]
        self.level_border_y = [183, 472]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], 185, 255]

class Area_101_105(object): #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_101_105.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(40, 110), random.randint(190, 250), 30, 120, 185, 255),  
        Shadow(random.randint(300, 370), random.randint(200, 250), 290, 380, 190, 260)]
        self.level_border_x = [20, 460]
        self.level_border_y = [183, 255]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, 185, 255]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], 185, 255]

class Area_102_105(object): #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_102_105.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(40, 110), random.randint(190, 250), 30, 120, 185, 255),  
        Shadow(random.randint(300, 370), random.randint(200, 250), 290, 380, 190, 260)]
        self.level_border_x = [20, 380]
        self.level_border_y = [115, 280]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, 185, 255]
        self.north_area_change_x_y = [135, 280, self.level_border_y[0], self.level_border_y[0] + 30]

class Area_102_106(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_102_106.png").convert_alpha()
        self.enemy_char = [Shadow(random.randint(40, 110), random.randint(190, 250), 30, 120, 185, 255),  
        Shadow(random.randint(300, 370), random.randint(200, 250), 290, 380, 190, 260)]
        self.level_border_x = [198, 490]
        self.level_border_y = [20, 315]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]

class Area_99_102(object):  #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_102.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(270, 340), 60, 150, 260, 350), 
        Medic(random.randint(100, 170), random.randint(100, 170), 90, 180, 90, 180), 
        Medic(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [124, 404]
        self.level_border_y = [20, 472]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], 220, 275]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]
        self.west_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[0] + 30, self.level_border_y[0], self.level_border_y[1] - 30]

class Area_99_103(object):  #OK Characters
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_103.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380), 
        Medic(random.randint(300, 370), random.randint(100, 170), 290, 380, 90, 180)]
        self.level_border_x = [124, 404]
        self.level_border_y = [20, 472]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]

class Area_99_104(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_104.png").convert_alpha()
        self.enemy_char = []
        self.level_border_x = [20, 404]
        self.level_border_y = [20, 472]
        self.north_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]
        self.south_area_change_x_y = [215, 300, self.level_border_y[1] - 30, self.level_border_y[1]]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, self.level_border_y[0] - 20, self.level_border_y[1] + 30]

class Area_99_105(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_99_105.png").convert_alpha()
        self.enemy_char = []
        self.level_border_x = [124, 404]
        self.level_border_y = [20, 472]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.west_area_change_x_y = [self.level_border_x[0] - 20, self.level_border_x[0] + 30, self.level_border_y[0] - 20, self.level_border_y[1] + 30]

class Area_98_104(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_104.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380)]
        self.level_border_x = [40, 500]
        self.level_border_y = [20, 472]
        self.south_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1]]
        self.north_area_change_x_y = [self.level_border_x[0] - 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], self.level_border_y[0] - 20, self.level_border_y[1] + 30]

class Area_98_102(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_102.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380)]
        self.level_border_x = [40, 500]
        self.level_border_y = [20, 472]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], self.level_border_y[0] - 20, self.level_border_y[1] + 30]

class Area_98_103(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_103.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380)]
        self.level_border_x = [40, 500]
        self.level_border_y = [20, 472]
        self.north_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[0], self.level_border_y[0] + 30]

class Area_98_105(object):
    def __init__(self):
        self.background_image = pygame.image.load("images/background_images/area_98_105.png").convert_alpha()
        self.enemy_char = [Medic(random.randint(70, 140), random.randint(300, 370), 60, 150, 290, 380)]
        self.level_border_x = [40, 500]
        self.level_border_y = [20, 472]
        self.south_area_change_x_y = [self.level_border_x[0] + 30, self.level_border_x[1], self.level_border_y[1] - 30, self.level_border_y[1] + 20]
        self.east_area_change_x_y = [self.level_border_x[1] - 30, self.level_border_x[1], self.level_border_y[0] - 20, self.level_border_y[1] + 30]