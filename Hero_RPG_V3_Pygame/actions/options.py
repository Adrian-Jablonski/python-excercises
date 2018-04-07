from actions.death import Death
import random
import math

class Options(object):
        
    def character_options(self, enemy, mouse_position):
        
        enemy_box_x_range = [enemy.x_y[0], enemy.x_y[0] + enemy.width]
        enemy_box_y_range = [enemy.x_y[1], enemy.x_y[1] + enemy.height]
        if mouse_position[0] >= enemy_box_x_range[0] and mouse_position[0] <= enemy_box_x_range[1] and mouse_position[1] >= enemy_box_y_range[0] and mouse_position[1] <= enemy_box_y_range[1]:
            return "Attack"
        else:
            return ""
        
        # distance = math.sqrt((math.pow((enemy.x + (enemy.width / 2)) - mouse_position[0], 2)) + (math.pow((enemy.y + (enemy.height / 2)) - mouse_position[1], 2)))
        # if distance < min(enemy.width, enemy.height):
        #     return "Attack"
        # else:
        #     return ""

class History_Box(object):
    def __init__(self, line1):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6