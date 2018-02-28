import pygame

from characters.base_characters import Character

class Fake(Character):
    def __init__(self):
        self.name = "Fake"
        self.health = 10
        self.max_health = 10
        self.power = 5
        self.defense = 5
        self.x = -50
        self.y = -50
        self.speed_x = 0
        self.speed_y = 0
        self.damage = 0
        self.width = 1
        self.height = 1
        self.fight_status = False
        self.health_bar_numb = 0
        self.clicked = False

class Goblin(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Goblin"
        self.health = 14
        self.max_health = 14
        self.power = 5
        self.defense = 5
        self.special_desc = "None"
        self.bounty = [5, 5, 6, 6, 8, 10]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 32
        self.height = 32
        self.char_image = pygame.image.load("images/goblin.png").convert_alpha()
        self.fight_status = False
        self.health_bar_numb = 20
        self.clicked = False
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 150
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Medic(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Medic"
        self.health = 20
        self.max_health = 20
        self.power = 10
        self.defense = 10
        self.special_desc = "Heals itself the same amount as that turns attack / 20%"
        self.bounty = [20, 20, 25, 25, 30, 35, 40]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 64
        self.height = 64
        self.char_image = pygame.transform.scale(pygame.image.load("images/medic.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 200
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Shadow(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Shadow"    
        self.health = 1
        self.max_health = 1
        self.power = 10
        self.defense = 1
        self.special_desc = "Only takes damage about 10% of the times it is attacked / 10%"
        self.bounty = [35, 35, 40, 40, 45, 45, 50, 60, 70]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 100
        self.height = 75
        self.char_image = pygame.transform.scale(pygame.image.load("images/shadow.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 300
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Wizard(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Wizard"
        self.health = 22
        self.max_health = 22
        self.power = 20
        self.defense = 15
        self.special_desc = "Freezes oponent for one move / 20%"
        self.bounty = [60, 60, 60, 70, 70, 80, 80, 90]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 51
        self.height = 53
        self.char_image = pygame.transform.scale(pygame.image.load("images/wizard.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 400
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Ranger(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Ranger"
        self.health = 28
        self.max_health = 28
        self.power = 18
        self.defense = 20
        self.special_desc = "Shoots two arrows in one move / 20%"
        self.bounty = [70, 70, 90, 90, 100, 110, 120]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 48
        self.height = 48
        self.char_image = pygame.transform.scale(pygame.image.load("images/ranger.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 400
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Zombie(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Zombie"
        self.health = 30
        self.max_health = 30
        self.power = 20
        self.defense = 25
        self.special_desc = "Does not die unless head is chopped off with axe"
        self.bounty = [100, 100, 150, 150, 200, 250]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 100
        self.height = 75
        self.char_image = pygame.transform.scale(pygame.image.load("images/zombie.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 500
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

class Dragon(Character):
    def __init__(self, x, y, min_walk_x, max_walk_x, min_walk_y, max_walk_y):
        self.name = "Dragon"
        self.health = 45
        self.max_health = 45
        self.power = 30
        self.defense = 45
        self.special_desc = "Breathes fire killing it's enemies that do not have a special shield / 33%"
        self.bounty = [400, 500, 700, 800]
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        self.damage = 0
        self.width = 87
        self.height = 52
        self.char_image = pygame.transform.scale(pygame.image.load("images/dragon.png").convert_alpha(), (self.width, self.height))
        self.fight_status = False
        self.health_bar_numb = 20
        self.x_when_clicked = ""
        self.y_when_clicked = ""
        self.respawn_timer = 0
        self.respawn_time = 600
        self.min_walk_x = min_walk_x
        self.min_walk_y = min_walk_y
        self.max_walk_x = max_walk_x
        self.max_walk_y = max_walk_y

    