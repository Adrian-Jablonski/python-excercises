from characters.base_characters import Character
import random
import math
import pygame

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.player_user_name = ""
        self.health = 12
        self.max_health = 12
        self.power_lv = 1
        self.defense_lv = 1
        self.health_exp = round((25 + (self.health)) * (self.health) / 1.13767) * (self.health - 1)
        self.next_health_level_exp = round(((25 + (self.health + 1)) * (self.health + 1) / 1.13767) * self.health)
        self.power_exp = round((25 + (self.power_lv)) * (self.power_lv) / 1.13767) * (self.power_lv - 1)
        self.next_power_level_exp = round(((25 + (self.power_lv + 1)) * (self.power_lv + 1) / 1.13767) * self.power_lv)
        self.defense_exp = round((25 + (self.defense_lv)) * (self.defense_lv) / 1.13767) * (self.defense_lv - 1)
        self.next_defense_level_exp = round(((25 + (self.defense_lv + 1)) * (self.defense_lv + 1) / 1.13767) * self.defense_lv)
        self.special_desc = "Generates 2x damage / 20%"
        self.coins = 100
        self.items = {
            "Healing_Potion": 2, 
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
        self.x_y = [250, 250]
        self.speed_x_y = [2.2, 2.2]
        self.width = 41
        self.height = 55
        self.damage = ""
        self.fight_status = False
        self.health_bar_numb = 20
        self.char_image = pygame.image.load("images/characters/hero.png").convert_alpha()
        self.attack_range = 70
        self.attack_time = 50
        self.attack_stance = "Aggressive"
        self.power_stance_bonus = 3
        self.defense_stance_bonus = -3
        self.power = max(self.power_lv + self.power_stance_bonus, 1)
        self.defense = max(self.defense_lv + self.defense_stance_bonus, 1)
        

    def bounty_earned(self, hero, enemy):
        randNumb = random.randint(0, len(enemy.bounty) - 1)    
        print("\033[1;33;40mYou receive {} coins\U0001F4B0 \033[0;37;40m".format(enemy.bounty[randNumb]))
        self.coins += enemy.bounty[randNumb]    # Receive coins from enemy
        return (enemy.bounty[randNumb])

    def restore_health(self):
        if (self.health + 10) > self.max_health:
            restore_amount = self.max_health - self.health
        else:
            restore_amount = 10
        self.health += restore_amount
        self.items["Healing_Potion"] -= 1
        print("\033[0;32;40m{} drank a Healing Potion and restored \033[1;32;40m{}\033[0;32;40m health.\033[0;37;40m".format(self.name, restore_amount))

    def equip_items(self, item):
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

    def movement(self, hero, mouse_position, enemy, frozen):

        distance = math.sqrt((math.pow(hero.x_y[0] - mouse_position[0], 2)) + (math.pow(hero.x_y[1] - mouse_position[1], 2)))
        
        if distance < 29:
            #hero.speed_x_y = [0, 0]
            return True
        else:
            # hero.speed_x_y = [1, 1]
            return False

    def hero_death(self, enemy):
        self.x_y = [90, 150]
        self.fight_status = False
        self.health = self.max_health
        self.coins -= int(round(self.coins * .80))
        self.items["Healing_Potion"] = 0 
        self.items["Helmet"] = 0
        self.items["Sword"] = 0 
        self.items["Shield"] = 0 
        self.items["Chainmail"] = 0 
        self.items["Zombie_Axe"] = 0 
        self.items["Dragon_Fire_Shield"] = 0
        self.health_bar_numb = 20
        self.damage = ""
        enemy.fight_status = False
        enemy.speed_x_y = [1, 1]
        enemy.damage = ""

    def hero_attack_stance(self, mouse_click_position):
        if mouse_click_position[0] >= 540 and mouse_click_position[0] <= 570 and mouse_click_position[1] >= 520 and mouse_click_position[1] <= 550:
            self.attack_stance = "Aggressive"
            self.power = self.power_lv + 3
            self.defense = max(self.defense_lv - 3, 1)
        elif mouse_click_position[0] >= 680 and mouse_click_position[0] <= 710 and mouse_click_position[1] >= 520 and mouse_click_position[1] <= 550:
            self.attack_stance = "Defensive"
            self.power = max(self.power_lv - 3, 1)
            self.defense = self.defense_lv + 3
        elif mouse_click_position[0] >= 540 and mouse_click_position[0] <= 570 and mouse_click_position[1] >= 562 and mouse_click_position[1] <= 595:
            self.attack_stance = "Normal"
            self.power = self.power_lv
            self.defense = self.defense_lv

    def load_hero_attack_stance(self):  # needed since attack stance bonus was not being counted without clicking on the attack stance
        if self.attack_stance == "Aggressive":
            self.power = self.power_lv + 3
            self.defense = max(self.defense_lv - 3, 1)
        elif self.attack_stance == "Defensive":
            self.power = max(self.power_lv - 3, 1)
            self.defense = self.defense_lv + 3
        elif self.attack_stance == "Normal":
            self.power = self.power_lv
            self.defense = self.defense_lv