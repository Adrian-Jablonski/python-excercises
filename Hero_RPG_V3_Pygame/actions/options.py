from actions.death import Death
import random
import math

class Options(object):
        
    def character_options(self, enemy, mouse_position):
        distance = math.sqrt((math.pow((enemy.x + (enemy.width / 2)) - mouse_position[0], 2)) + (math.pow((enemy.y + (enemy.height / 2)) - mouse_position[1], 2)))
        if distance < 50:
            return "Attack"
        else:
            return ""

class History_Box(object):
    def __init__(self, line1):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6

# class History_Box_Lines(History_Box):
#     def __init__(self):
#         self.line1 = ""
#         self.line2 = ""
#         self.line3 = ""
#         self.line4 = ""
#         self.line5 = ""
#         self.line6 = ""

#     def history_box_text(self, history_line, history_line_text, history_line_text_numb):
#         def __init__(self):
#             history_line.line1 = history_line_text[history_line_text_numb]
#             self.line2 = history_line_text[history_line_text_numb - 1]
#             self.line3 = history_line_text[history_line_text_numb - 2]
#             self.line4 = history_line_text[history_line_text_numb - 3]
#             self.line5 = history_line_text[history_line_text_numb - 4]
#             self.line6 = history_line_text[history_line_text_numb - 5]