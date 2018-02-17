import pygame
import random
import math

class Character(object):
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_x = speed_y

    def update(self, width, height, rand_numb):
        rand_x = 0
        rand_y = 0

        if rand_numb == 0:      # Move right
            rand_x = self.speed_x
            rand_y = 0
        elif rand_numb == 1:    # Move left
            rand_x = -self.speed_x
            rand_y = 0
        elif rand_numb == 2:    # Move down
            rand_x = 0
            rand_y = self.speed_y
        elif rand_numb == 3:    # Move up
            rand_x = 0
            rand_y =-self.speed_x 
        elif rand_numb == 4:    # South East
            rand_x = self.speed_x / 2
            rand_y = self.speed_y / 2
        elif rand_numb == 5:    # North East
            rand_x = self.speed_x / 2
            rand_y = -self.speed_y / 2
        elif rand_numb == 6:    # North West
            rand_x = - self.speed_x / 2
            rand_y = - self.speed_y / 2
        elif rand_numb == 7:    # South West
            rand_x = - self.speed_x / 2
            rand_y = self.speed_y / 2
        # Wrap around screen
        if self.x + 30 > width:    # Moves right
            self.x = 30 + 1
            #rand_x = -5
        if self.y + 30 > height:    # Moves Down
            self.y = 30 + 1
            #rand_y = -5
        if self.x < 0 + 30:         # Moves Left
            self.x = width - 29
            #rand_x = 5
        if self.y < 0 + 30:         # Moves up
            self.y = height - 29
            #rand_y = 5
        self.x += rand_x
        self.y += rand_y

    def dead(self, character_x, character_y, screen, background_image, sound, background_music):
        x = character_x + 16
        y = character_y + 16
        screen.blit(background_image, (x, y), pygame.Rect(x, y, character_x - 16, character_y - 16))
        background_music.stop()
        sound.play()

    def collission(self, hero, enemy):
        distance = math.sqrt((math.pow(hero.x - enemy.x, 2)) + (math.pow(hero.y - enemy.y, 2)))
        if distance < 32:
            hero.speed_x = 0
            hero.speed_y = 0
            return True
        else:
            return False

class Monster(Character):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed_x = 5
        self.speed_y = 5

class Hero(Character):
    def __init__(self):
        self.x = 512 / 2
        self.y = 480 / 2
        self.speed_x = 4
        self.speed_y = 4

class Goblin(Character):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.speed_x = 2
        self.speed_y = 2