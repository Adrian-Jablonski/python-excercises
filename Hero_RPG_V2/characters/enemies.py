from characters.base_characters import Character

class Goblin(Character):
    def __init__(self):
        self.name = "Goblin"
        self.health = 10
        self.max_health = 10
        self.power = 5
        self.defense = 5
        self.special_desc = "None"
        self.bounty = [5, 5, 6, 6, 8, 10]

class Medic(Character):
    def __init__(self):
        self.name = "Medic"
        self.health = 20
        self.max_health = 20
        self.power = 10
        self.defense = 10
        self.special_desc = "Heals itself the same amount as that turns attack / 20%"
        self.bounty = [20, 20, 25, 25, 30, 35, 40]

class Shadow(Character):
    def __init__(self):
        self.name = "Shadow"    
        self.health = 1
        self.max_health = 1
        self.power = 10
        self.defense = 1
        self.special_desc = "Only takes damage about 10% of the times it is attacked / 10%"
        self.bounty = [35, 35, 40, 40, 45, 45, 50, 60, 70]

class Wizard(Character):
    def __init__(self):
        self.name = "Wizard"
        self.health = 22
        self.max_health = 22
        self.power = 20
        self.defense = 15
        self.special_desc = "Freezes oponent for one move / 20%"
        self.bounty = [60, 60, 60, 70, 70, 80, 80, 90]

class Ranger(Character):
    def __init__(self):
        self.name = "Ranger"
        self.health = 28
        self.max_health = 28
        self.power = 18
        self.defense = 20
        self.special_desc = "Shoots two arrows in one move / 20%"
        self.bounty = [70, 70, 90, 90, 100, 110, 120]

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 30
        self.max_health = 30
        self.power = 20
        self.defense = 25
        self.special_desc = "Does not die unless head is chopped off with axe"
        self.bounty = [100, 100, 150, 150, 200, 250]

class Dragon(Character):
    def __init__(self):
        self.name = "Dragon"
        self.health = 45
        self.max_health = 45
        self.power = 30
        self.defense = 45
        self.special_desc = "Breathes fire killing it's enemies that do not have a special shield / 33%"
        self.bounty = [400, 500, 700, 800]