import pygame
import random
import time

red_color = (255, 0, 0)

class Character(object):
    def __init__(self, name, health, max_health, power, defense, special_desc, coins, x_y,  min_walk_x, max_walk_x, min_walk_y, max_walk_y, items={}, bounty=[]):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.power = power
        self.defense = defense
        self.special_desc = special_desc
        self.coins = coins
        self.items = items
        self.x_y = [x, y]
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_x = max_walk_x

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
                if damage > enemy.health and enemy.name != "Zombie":   # limits the damage to enemy health
                    damage = enemy.health
                elif damage >= enemy.health and enemy.name == "Zombie":
                    damage = enemy.health - 1
                enemy.health -= damage
                print("\033[5;37;42mSPECIAL ATTACK:\033[5;32;40m {} does {} damage to {}.\033[0;37;40m".format(self.name, damage, enemy.name))
            elif special_attack == True and self.name == "Medic":   # medic special
                damage = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                self.health += damage
                self.special_attack_text = "{} does {} damage to hero and restores {} health".format(self.name, damage, damage)
            elif special_attack == True and self.name == "Wizard":
                damage = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                self.special_attack_text = "{} does {} damage and freezes hero".format(self.name, damage)
            elif special_attack == True and self.name == "Ranger":
                damage = random.randint(0, self.power)
                damage2 = random.randint(0, self.power)
                if damage > enemy.health:
                    damage = enemy.health
                enemy.health -= damage
                if damage2 > enemy.health:
                    damage2 = enemy.health
                enemy.health -= damage2
                self.special_attack_text = "{} shoots two arrows doing {} and {} damage to hero".format(self.name, damage, damage2)
            elif special_attack == True and self.name == "Dragon":
                if enemy.items["Dragon_Fire_Shield"] == 0:
                    damage = enemy.health
                    self.special_attack_text = "{} breathes fire doing {} damage and kills hero".format(self.name, damage)
                else:
                    damage = 0
                    self.special_attack_text = "Dragon Fire Shield protects hero from {} fire".format(self.name)
                enemy.health -= damage
            else:
                damage = random.randint(0, self.power)
                defense_benefit = round(enemy.defense * .3)
                defense_times = round(enemy.defense / 2)
                count = 0
                
                print(damage, "-", count, "-", max(self.power - defense_benefit, 1), "Max damage in", defense_times, "tries")
                while damage > max((self.power - defense_benefit), 1) and count < defense_times:
                    damage = random.randint(0, self.power)
                    count += 1
                    print(damage, "-", count, "-", max(self.power - defense_benefit, 1), "Max damage in", defense_times, "tries")  # shows all numbers generated
                # If the enemy attacks within a certain number (number depends on defense level) of their max attack, another random number is generated. Number is generated half the enemies defense level times. This lowers the chance of high attacks on a higher defense oponent
                if damage > enemy.health and enemy.name != "Zombie":   # limits the damage to enemy health
                    damage = enemy.health
                elif damage >= enemy.health and enemy.name == "Zombie":
                    damage = enemy.health - 1
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

    def walking(self, rand_numb, hero_char):
        rand_x = 0
        rand_y = 0
        if self.fight_status == False:
            if self.x_y[0] > self.max_walk_x:    # Moves right
                self.speed_x_y[0] *= -1
            if self.x_y[1] > self.max_walk_y:    # Moves Down
                self.speed_x_y[1] *= -1
            if self.x_y[0] < self.min_walk_x:         # Moves Left
                self.speed_x_y[0] *= -1
            if self.x_y[1] < self.min_walk_y:         # Moves up
                self.speed_x_y[1] *= -1
                
            if rand_numb == 0:      # Move right
                rand_x = self.speed_x_y[0]
                rand_y = 0
            elif rand_numb == 1:    # Move left
                rand_x -= self.speed_x_y[0]
                rand_y = 0
            elif rand_numb == 2:    # Move down
                rand_x = 0
                rand_y = self.speed_x_y[1]
            elif rand_numb == 3:    # Move up
                rand_x = 0
                rand_y -= self.speed_x_y[1]
            elif rand_numb == 4:    # South East
                rand_x = self.speed_x_y[0] / 2
                rand_y = self.speed_x_y[1] / 2
            elif rand_numb == 5:    # North East
                rand_x = self.speed_x_y[0] / 2
                rand_y -= self.speed_x_y[1] / 2
            elif rand_numb == 6:    # North West
                rand_x -= self.speed_x_y[0] / 2
                rand_y -= self.speed_x_y[1] / 2
            elif rand_numb == 7:    # South West
                rand_x -= self.speed_x_y[0] / 2
                rand_y = self.speed_x_y[1] / 2
            elif rand_numb ==8:
                rand_x = 0
                rand_y = 0

            self.x_y[0] += rand_x
            self.x_y[1] += rand_y
        
        #Makes enemy follow hero when attacking
        elif self.fight_status == True and self.x_y[0] > self.min_walk_x and self.x_y[0] < self.max_walk_x and self.x_y[1] > self.min_walk_y and self.x_y[1] < self.max_walk_y:
            if self.x_y[0] + 30 <= hero_char.x_y[0]:
                self.x_y[0] += abs(self.speed_x_y[0])
            elif self.x_y[0] - 30 >= hero_char.x_y[0]:
                self.x_y[0] -= abs(self.speed_x_y[0])
            if self.x_y[1] + 30 <= hero_char.x_y[1]:
                self.x_y[1] += abs(self.speed_x_y[1])
            elif self.x_y[1] - 30 >= hero_char.x_y[1]:
                self.x_y[1] -= abs(self.speed_x_y[1])
            

    def health_bar(self):
        health_perc = float(self.health / self.max_health)
        if health_perc < .05 and health_perc > 0:
            self.health_bar_numb = 1
        elif health_perc >=1:
            self.health_bar_numb = 20
        else:
            health_bar_numb = int((health_perc) / 5 * 100)
            self.health_bar_numb = health_bar_numb
            return health_bar_numb
    
    def remove_dead_char(self, enemy, hero, screen, background_image):
        x_y = [enemy.x_y[0] + 16, enemy.x_y[1] + 16]
        
        screen.blit(background_image, (x_y[0], x_y[1]), pygame.Rect(x_y[0], x_y[1], enemy.x_y[0] - 16, enemy.x_y[1] - 16))
        enemy.fight_status = False
        #enemy.x_y_when_clicked = [-300, -300]
        enemy.damage = ""
        hero.damage = ""
        hero.fight_status = False

    #def enemy_respawn(self):
