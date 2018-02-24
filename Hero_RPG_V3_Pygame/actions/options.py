from actions.death import Death
import random
import math

class Options(object):
        
    def character_options(self, enemy, mouse_position):
        distance = math.sqrt((math.pow((enemy.x + (enemy.width / 2)) - mouse_position[0], 2)) + (math.pow((enemy.y + (enemy.height / 2)) - mouse_position[1], 2)))
        if distance < 32:
            return "Attack"
        else:
            return ""