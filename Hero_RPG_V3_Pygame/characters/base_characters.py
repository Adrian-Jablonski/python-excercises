import pygame
import random
import time

red_color = (255, 0, 0)

class Character(object):
    def __init__(self, name, health, max_health, power, defense, special_desc, coins, x, items={}, bounty=[]):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.power = power
        self.defense = defense
        self.special_desc = special_desc
        self.coins = coins
        self.items = items
        self.x = x

    def attack(self, enemy, special_attack, screen):
        global damage 
        if self.health >= 0 or self.name == "Zombie":
            if enemy.name == "Shadow":      # shadow special
                if special_attack == True:
                    damage = 1   
                else:
                    damage = 0
                enemy.health -= damage
                print("\033[0;32;40m{} does \033[1;32;40m{}\033[0;32;40m damage to {}\033[0;37;40m.".format(self.name, damage, enemy.name))
            elif special_attack == True and self.name == "Hero":  # hero special
                damage = random.randint(0, self.power) * 2
                if damage > enemy.health:   # limits the damage to enemy health
                    damage = enemy.health
                enemy.health -= damage
                print("\033[5;37;42mSPECIAL ATTACK:\033[5;32;40m {} does {} damage to {}.\033[0;37;40m".format(self.name, damage, enemy.name))
            elif special_attack == True and self.name == "Medic":   # medic special
                damage = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                self.health += damage
                print("\033[0;37;41mSPECIAL ATTACK:\033[0;31;40m {} does {} damage to {} and restores {} health.\033[0;37;40m".format(self.name, damage, enemy.name, damage))
            elif special_attack == True and self.name == "Wizard":
                damage = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                print("\033[0;31;40m{} does {} damage to {}\033[0;37;40m.".format(self.name, damage, enemy.name))
                print("\033[1;37;44mSPECIAL ATTACK: Hero is FROZEN for one move. \033[0;37;40m")
            elif special_attack == True and self.name == "Ranger":
                damage = random.randint(0, self.power)
                damage2 = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                if damage2 > enemy.health:
                    damage2 = enemy.health
                enemy.health -= damage2
                print("\033[0;37;41mSPECIAL ATTACK:\033[1;31;40m {} does {} and {} damage to {}.\033[0;37;40m".format(self.name, damage, damage2, enemy.name))
            elif special_attack == True and self.name == "Dragon":
                if enemy.items["Dragon_Fire_Shield"] == 0:
                    damage = enemy.health
                    print("\033[0;37;41mSPECIAL ATTACK:\033[1;31;40m {} breathes fire and does {} damage to {}.\033[0;37;40m".format(self.name, damage, enemy.name))
                else:
                    damage = 0
                    print("\033[0;37;41mSPECIAL ATTACK:\033[1;31;40m {}'s Dragon Fire Shield protects him from the {}'s fire.\033[0;37;40m".format(enemy.name, self.name))
                enemy.health -= damage
            else:
                damage = random.randint(0, self.power)
                defense_benefit = round(enemy.defense * .3)
                defense_times = round(enemy.defense / 2)
                count = 0
                
                #print(damage, "-", count, "-", self.power - defense_benefit, "Max damage in", defense_times, "tries")
                while damage >= max((self.power - defense_benefit), 1) and count < defense_times:
                    damage = random.randint(0, self.power)
                    count += 1
                    #print(damage, "-", count, "-", self.power - defense_benefit, "Max damage in", defense_times, "tries")  # shows all numbers generated
                # If the enemy attacks within a certain number (number depends on defense level) of their max attack, another random number is generated. Number is generated half the enemies defense level times. This lowers the chance of high attacks on a higher defense oponent
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                if self.name == "Hero":
                    print("\033[0;32;40m{} does \033[1;32;40m{}\033[0;32;40m damage to {}.\033[0;37;40m".format(self.name, damage, enemy.name))
                else:
                    print("\033[0;31;40m{} does \033[1;31;40m{}\033[0;31;40m damage to {}.\033[0;37;40m".format(self.name, damage, enemy.name))
            enemy.damage = damage
            time.sleep(1)

    def alive(self):
        if self.health > 0 or self.name == "Zombie":
            return True
        else:
            return False

    def print_status(self):
        align = 7 - len(self.name) - 1
        print(" " * align, "\033[1;34;40m{} - \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}/{} \033[0;37;40m".format(self.name, self.power, self.defense, self.health, self.max_health))

    def update(self, width, height, rand_numb):
        rand_x = 0
        rand_y = 0

        if self.x > width - 50:    # Moves right
            #self.x = width - self.width
            self.speed_x *= -1
            #rand_numb = 1
        if self.y > height - 50:    # Moves Down
            #self.y = height - self.height
            self.speed_y *= -1
            #rand_numb = 3
        if self.x < 50:         # Moves Left
            #self.x = self.width + 3
            self.speed_x *= -1
            #rand_numb = 0
        if self.y < 50:         # Moves up
            #self.y = self.height + 3
            self.speed_y *= -1
            #rand_numb = 2
            
        if rand_numb == 0:      # Move right
            rand_x = self.speed_x
            rand_y = 0
        elif rand_numb == 1:    # Move left
            rand_x -= self.speed_x
            rand_y = 0
        elif rand_numb == 2:    # Move down
            rand_x = 0
            rand_y = self.speed_y
        elif rand_numb == 3:    # Move up
            rand_x = 0
            rand_y -= self.speed_y 
        elif rand_numb == 4:    # South East
            rand_x = self.speed_x / 2
            rand_y = self.speed_y / 2
        elif rand_numb == 5:    # North East
            rand_x = self.speed_x / 2
            rand_y -= self.speed_y / 2
        elif rand_numb == 6:    # North West
            rand_x -= self.speed_x / 2
            rand_y -= self.speed_y / 2
        elif rand_numb == 7:    # South West
            rand_x -= self.speed_x / 2
            rand_y = self.speed_y / 2
        elif rand_numb ==8:
            rand_x = 0
            rand_y = 0

        self.x += rand_x
        self.y += rand_y

    def health_bar(self):
        health_perc = float(self.health / self.max_health)
        if health_perc < .05 and health_perc > 0:
            return 1
        elif health_perc >=1:
            return 20
        else:
            health_bar_numb = int((health_perc) / 5 * 100)
            self.health_bar_numb = health_bar_numb
            return health_bar_numb
    
    def remove_dead_char(self, character_x, character_y, screen, background_image):
        x = character_x + 16
        y = character_y + 16
        
        screen.blit(background_image, (x, y), pygame.Rect(x, y, character_x - 16, character_y - 16))
