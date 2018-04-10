import pygame
import random
import time
import math
import pickle

from characters.base_characters import Character
from characters.hero import Hero
from characters.enemies import Goblin
from characters.enemies import Medic
from characters.enemies import Ranger
from characters.enemies import Wizard
from characters.enemies import Shadow
from characters.enemies import Zombie
from characters.enemies import Dragon
from characters.enemies import Fake

from actions.battle import Battle
from actions.death import Death
from actions.options import *
from actions.areas import *

from other_variables.keyboard_and_mouse import (RIGHT_CLICK, LEFT_CLICK, KEY_1, KEY_2, KEY_3, KEY_4,
KEY_5, KEY_6, KEY_7, KEY_8, KEY_9, ENTER_BUTTON, BACK_SPACE, ALPHABET_KEY, NUMBER_KEYS)
from other_variables.colors import (blue_color, dark_blue_color, green_color, yellow_color, black_color,
white_color, red_color, grey_color)

def main():
    game_screen_width = 512
    game_screen_height = 500
    width = 850
    height = 670
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Kingdom of Objalinsk')
    clock = pygame.time.Clock()

    # ************* IMAGES *******************

    dark_background_image = pygame.image.load("images/background_images/dark_background.png").convert_alpha()
    #background_image = Area_100_100().background_image
    user_interface_image = pygame.image.load("images/background_images/user_interface.png").convert_alpha()
    radio_button = (pygame.transform.scale(pygame.image.load("images/icons/radiobutton_circle.png").convert_alpha(), (22, 22)))
    text_input = pygame.image.load("images/icons/text_input.png").convert_alpha()

    scroll_up = pygame.image.load("images/icons/scroll_up_button.gif").convert_alpha()
    scroll_down = pygame.image.load("images/icons/scroll_down_button.gif").convert_alpha()

    health_bar_image = []
    i = 0
    while (i <= 100):
        health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar{}.png".format(i)).convert_alpha(), (23, 4)))
        i += 5

    #******************************************

    hero_char = Hero()
    hero_char.load_hero_attack_stance()
    hero_char
    area = "Main Menu"
    current_area = Main_Menu()
    area_change = False
    enemy_char = current_area.enemy_char
    enemy_count = len(enemy_char) - 1
    enemy_numb = 0
    mouse_over = ""; mouse_over_text = ""; mouse_over_color = black_color

    change_dir_countdown = 120

    attack_timer = 90
    movement = 0
    rand_numb = random.randint(0, 8)
    rand_number_special = 0
    mouse_click_position = [0, 0]
    current_mouse_position = [0, 0]
    run_away = False
    frozen = False
    battle_mode = False

    enemy_fighting = Fake()
    dead_enemy_list = []
    respawn_timer = 0
    item_bought = ""
    history_line_text = ["", "", "", "", "", ""]
    history_line_color = [black_color, black_color, black_color, black_color, black_color, black_color]
    history_line_text_numb = len(history_line_text) - 1

    game_to_load = ""
    user_name = ""
    new_game = False
    load_game = False

    # Game initialization

    stop_game = False
    button_pressed = False
    key_pressed = False
    key_hold = False

    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_pressed = event.button
                mouse_location = pygame.mouse.get_pos()
                # to get rid of tuple object
                mouse_click_position[0] = mouse_location[0]
                mouse_click_position[1] = mouse_location[1]
                print(mouse_location)
                # Moves character to the edge of area if the click was past the levels edge and before the game screen
                if mouse_click_position[0] >= 0 and mouse_click_position[0] < current_area.level_border_x[0]:
                    mouse_click_position[0] = current_area.level_border_x[0]
                elif mouse_click_position[0] <= game_screen_width and mouse_click_position[0] > current_area.level_border_x[1]:
                    mouse_click_position[0] = current_area.level_border_x[1]
                
                if mouse_click_position[1] >= 0 and mouse_click_position[1] < current_area.level_border_y[0]:
                    mouse_click_position[1] = current_area.level_border_y[0]
                elif mouse_click_position[1] <= (game_screen_height) and mouse_click_position[1] > current_area.level_border_y[1]:
                    mouse_click_position[1] = current_area.level_border_y[1]
                # Save enemy position at time of click
                for enemy in enemy_char:
                    enemy.x_y_when_clicked = [enemy.x_y[0], enemy.x_y[1]]
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

            # To get mouse position on mouse hover
            current_mouse_location = pygame.mouse.get_pos()
            current_mouse_position[0] = current_mouse_location[0]
            current_mouse_position[1] = current_mouse_location[1]

            if event.type == pygame.KEYDOWN:
                key_pressed = event.key
                print(key_pressed)
                key_hold = True
            elif event.type == pygame.KEYUP:
                key_pressed = False
                key_hold = False
                print(key_hold)

            # Main menu selections
            if area == "Main Menu":
                try:
                    myfile = open("actions/save_state/user_names.pickle", "rb")
                    user_data = pickle.load(myfile)
                    myfile.close()
                    
                except FileNotFoundError:
                    myfile = open("actions/save_state/user_names.pickle", "wb")
                    user_data = []
                    pickle.dump(user_data, myfile)
                    myfile.close()

                if load_game == False and mouse_click_position[0] >= 348 and mouse_click_position[0] <= 501 and mouse_click_position[1] >= 118 and mouse_click_position[1] <= 173:
                    new_game = True
                    current_area = Main_Menu2()
                    # area = [100, 100]
                    # current_area = Area_100_100()
                elif new_game == False and mouse_click_position[0] >= 348 and mouse_click_position[0] <= 501 and mouse_click_position[1] >= 185 and mouse_click_position[1] <= 240:
                    load_game = True
                    current_area = Main_Menu2()

                if load_game == True:
                    if key_pressed == KEY_1:
                        game_to_load = user_data[0]
                    elif key_pressed == KEY_2:
                        game_to_load = user_data[1]
                    elif key_pressed == KEY_3:
                        game_to_load = user_data[2]
                    elif key_pressed == KEY_4:
                        game_to_load = user_data[3]
                    
                if load_game == True or new_game == True:    
                    if mouse_click_position[0] >= 540 and mouse_click_position[0] <= 725 and mouse_click_position[1] >= 548 and mouse_click_position[1] <= 620:
                        load_game = False
                        new_game = False
                        current_area = Main_Menu()

                #print(user_data)
                for number in NUMBER_KEYS:
                        if key_pressed == (NUMBER_KEYS[number]) and len(user_name) < 15:
                            user_name += str(number)

                for char in ALPHABET_KEY:
                    if key_pressed == (ALPHABET_KEY[char]) and len(user_name) < 15:
                        # print(char)
                        # print(len(user_name))
                        if len(user_name) == 0:
                            char = char.upper()
                        user_name += char
                    if key_pressed == BACK_SPACE:
                        user_name = user_name[:-1]
                        key_pressed = ""
                if key_pressed == ENTER_BUTTON:
                    #saves user name to a file of all user_names
                    invalid_user_name = False
                    if len(user_name) <= 3:
                        invalid_user_name = True
                        print("Invalid user name. User name must be at least 4 characters.")
                    else:
                        for user in user_data:
                            if user == user_name:
                                print("User name already exists")
                                invalid_user_name = True
                    if invalid_user_name == False:
                        myfile = open("actions/save_state/user_names.pickle", "wb")
                        user_data.append(user_name)
                        pickle.dump(user_data, myfile)
                        myfile.close()

                        #starts new game
                        area = [98, 100]
                        current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                        hero_char.player_user_name = user_name

                if game_to_load != "":
                    hero_char.player_user_name = game_to_load
                    myfile = open("actions/save_state/save_state_{}.pickle".format(game_to_load), "rb")
                    current_area = Area_98_100()
                    area = [98, 100]
                    load_data = pickle.load(myfile)
                    hero_char.health = load_data[0]
                    hero_char.max_health = load_data[1]
                    hero_char.power_lv = load_data[2]
                    hero_char.defense_lv = load_data[3]
                    hero_char.health_exp = load_data[4]
                    hero_char.power_exp = load_data[5]
                    hero_char.defense_exp = load_data[6]
                    hero_char.coins = load_data[7]
                    hero_char.items = load_data[8]
                    hero_char.x_y = load_data[9]
                    mouse_click_position = [hero_char.x_y[0], hero_char.x_y[1]]
                    hero_char.attack_stance = load_data[10]
                    hero_char.next_health_level_exp = load_data[11]
                    hero_char.next_power_level_exp = load_data[12]
                    hero_char.next_defense_level_exp = load_data[13]
                    area = load_data[14]

                    hero_char.load_hero_attack_stance()
                    current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                    
                    # print(load_data)
                    myfile.close()


            # Store selections 
            if area == "Store" or area == "Upgrade_Level_Store":
                if area == "Store":
                    if key_pressed == KEY_1:
                        item_bought = "Healing_Potion"
                        item_bought_name = "Healing Potion"
                    elif key_pressed == KEY_2:
                        item_bought = "Helmet"
                        item_bought_name = "Helmet"
                    elif key_pressed == KEY_3:
                        item_bought = "Sword"
                        item_bought_name = "Sword"
                    elif key_pressed == KEY_4:
                        item_bought = "Shield"
                        item_bought_name = "Shield"
                    elif key_pressed == KEY_5:
                        item_bought = "Chainmail"
                        item_bought_name = "Chainmail"
                    elif key_pressed == KEY_6:
                        item_bought = "Zombie_Axe"
                        item_bought_name = "Zombie Axe"
                    elif key_pressed == KEY_7:
                        item_bought = "Dragon_Fire_Shield"
                        item_bought_name = "Dragon Fire Shield"
                    # elif key_pressed == KEY_8:
                    #     area = "Upgrade_Level_Store"
                    #     area_change = True
                    #     item_bought = ""
                    elif key_pressed == KEY_9:
                        area = [98,100]
                        area_change = True
                        current_area = Area_98_100()
                        hero_char.x_y[1] = 160
                        mouse_click_position[1] = hero_char.x_y[1]
                        item_bought = ""
                    else:
                        item_bought = ""

                    if item_bought != "":
                        if hero_char.items[item_bought] > 0 and item_bought != "Healing_Potion":
                            history_line_text.append("Alread own a {}".format(item_bought_name))
                        elif Store().shopping(hero_char, item_bought) == True:
                            history_line_text.append("You bought a {}".format(item_bought_name))
                        else:
                            history_line_text.append("Not enough coins to buy {}".format(item_bought_name))

                        if hero_char.items[item_bought] > 0 and item_bought != "Healing_Potion":
                            hero_char.equip_items(item_bought)
                    
                        history_line_text_numb = len(history_line_text) - 1
                        history_line_color.append(white_color)

                #Level upgrade store
                # elif area == "Upgrade_Level_Store":
                #     upgrade_level = Upgrade_Level_Store(hero_char)
                #     if key_pressed == KEY_1:
                #         item_bought = "Power_Level"
                #         power_up_name = "Power Level"
                #         new_level = hero_char.power + 1
                #     elif key_pressed == KEY_2:
                #         item_bought = "Defense_Level"
                #         power_up_name = "Defense Level"
                #         new_level = hero_char.defense + 1
                #     elif key_pressed == KEY_3:
                #         item_bought = "Health_Level"
                #         power_up_name = "Health Level"
                #         new_level = hero_char.max_health + 1
                #     elif key_pressed == KEY_8:
                #         area = "Store"
                #         area_change = True
                #         item_bought = ""
                #     elif key_pressed == KEY_9:
                #         area = [98,100]
                #         area_change = True
                #         hero_char.x_y[0] = current_area.level_border_x[0] + 50
                #         mouse_click_position[0] = current_area.level_border_x[0] + 50
                #         item_bought = ""
                #     else:
                #         item_bought = ""

                #     if item_bought != "":
                #         if upgrade_level.level_up(hero_char, item_bought) == True:
                #             history_line_text.append("Your {} is now {}".format(power_up_name, new_level))
                #         else:
                #             history_line_text.append("Not enough coins to buy {}".format(power_up_name))
                #         history_line_color.append(white_color)
                #         history_line_text_numb = len(history_line_text) - 1
                    
            # Make click location for healing potion   
            if mouse_click_position[0] >= 534 and mouse_click_position[0] <= 565 and mouse_click_position[1] >= 314 and mouse_click_position[1] <= 350:
                if hero_char.items["Healing_Potion"] == 0:
                    history_line_text.append("Out of healing potion")
                else:
                    hero_char.restore_health()
                    history_line_text.append("Hero drinks a healing potion")
                    if hero_char.fight_status == True:
                        frozen = True # Prevents hero from restoring health and attacking in same move
                        turns_frozen = 0
                mouse_click_position[0] = -50 # Prevents click looping and draining all potions
                history_line_color.append(white_color)
                history_line_text_numb = len(history_line_text) - 1

            # Make click location for scroll bars
            # Scroll up
            elif mouse_click_position[0] >= 430 and mouse_click_position[0] <= 470 and mouse_click_position[1] >= 545 and mouse_click_position[1] <= 580:
                if history_line_text_numb > 10:
                    history_line_text_numb -= 1
                    mouse_click_position[0] = 420
            
            elif mouse_click_position[0] >= 430 and mouse_click_position[0] <= 470 and mouse_click_position[1] >= 585 and mouse_click_position[1] <= 620:
                if history_line_text_numb < len(history_line_text) - 1:
                    history_line_text_numb += 1
                    mouse_click_position[0] = 420

            # Gives a bonus to a skill based on attack stance
            hero_char.hero_attack_stance(mouse_click_position)

            if event.type == pygame.QUIT:
            #if event.type == pygame.QUIT and battle_mode == False:
                if area != "Main Menu":
                    user_names = ""
                    character_status = "New Character"
                    def saveGame():
                        # Need to save hero health, max_health, power_lv, defense_lv, health_exp,
                        # next_health_level_exp (maybe), power_exp, next_power_level_exp, defense_exp,
                        # next_defense_level_exp, coins, items, x_y, attack_stance, current area
                        save_state = [hero_char.health, hero_char.max_health, hero_char.power_lv, hero_char.defense_lv, hero_char.health_exp, hero_char.power_exp, hero_char.defense_exp, hero_char.coins, hero_char.items, hero_char.x_y, hero_char.attack_stance, hero_char.next_health_level_exp, hero_char.next_power_level_exp, hero_char.next_defense_level_exp, area]
                        myfile = open("actions/save_state/save_state_{}.pickle".format(hero_char.player_user_name), "wb")
                        pickle.dump(save_state, myfile)
                        
                        myfile.close()
                    
                    # def playerDatabase():
                    #     myfile = open("actions/save_state/user_names.pickle", "rb")
                    #     user_names = pickle.load(myfile)
                    #     print(user_names)
                        
                    #     myfile.close()

                    # def playerDatabaseWrite():
                    try:
                        character_status = "New Character"
                        myfile = open("actions/save_state/player_database.pickle", "rb")
                        player_stats = pickle.load(myfile)
                        myfile.close()
                        myfile = open("actions/save_state/player_database.pickle", "wb")
                        current_player_stats = [hero_char.player_user_name, hero_char.health, hero_char.max_health, hero_char.power_lv, hero_char.defense_lv, hero_char.health_exp, hero_char.power_exp, hero_char.defense_exp, hero_char.coins]
                        i = 0
                        # Checks if character already exists in database
                        while i < len(player_stats) and character_status == "New Character":
                            if player_stats[i][0] == hero_char.player_user_name:
                                character_status = "Existing Character"
                                player_stats[i] = current_player_stats
                                break
                            i += 1
                        if character_status == "New Character":
                            player_stats.append(current_player_stats)
                            
                        pickle.dump(player_stats, myfile)
                        myfile.close()

                    except FileNotFoundError:
                        myfile = open("actions/save_state/player_database.pickle", "wb")
                        player_stats = [[hero_char.player_user_name, hero_char.health, hero_char.max_health, hero_char.power_lv, hero_char.defense_lv, hero_char.health_exp, hero_char.power_exp, hero_char.defense_exp, hero_char.coins]]
                        pickle.dump(player_stats, myfile)
                    print(player_stats)
                    myfile.close()

                    # playerDatabase() 
                    # for character in user_names:
                    #     if hero_char.player_user_name == character:
                    #         character_status = "Character Exists"
                    #         break
                    #     else:
                    #         character_status = "New Character"
                    
                    # print(character_status)
                    # playerDatabaseWrite()

                    saveGame()
                    #playerDatabaseWrite()
                      
                stop_game = True

        # Game logic
        #Enemy click detection. Also prevents hero from going outside of game screen
        if button_pressed == LEFT_CLICK and mouse_click_position[0] >= current_area.level_border_x[0] and mouse_click_position[0] <= current_area.level_border_x[1] and mouse_click_position[1] >= current_area.level_border_y[0] and mouse_click_position[1] <= current_area.level_border_y[1]:
            if hero_char.movement(hero_char, mouse_click_position, enemy_fighting, frozen) == False:
                    hero_char.fight_status = False
      
                    if battle_mode == True and frozen == False and Battle().attack_range(enemy_fighting, hero_char) == False:
                        run_away = True
                
                     # Prevents hero from standing on top of enemy during attack
                    if battle_mode == True and mouse_click_position[0] >= enemy_fighting.x_y_when_clicked[0] and mouse_click_position[0] <= enemy_fighting.x_y_when_clicked[0] + enemy_fighting.width and mouse_click_position[1] >= enemy_fighting.x_y_when_clicked[1] and mouse_click_position[1] <= enemy_fighting.x_y_when_clicked[1] + enemy_fighting.height:
                        if hero_char.x_y[0] < enemy_fighting.x_y[0] - enemy_fighting.width and frozen == False:
                            hero_char.x_y[0] += hero_char.speed_x_y[0]
                        elif hero_char.x_y[0] > enemy_fighting.x_y[0] + enemy_fighting.width and frozen == False:
                            hero_char.x_y[0] -= hero_char.speed_x_y[0]

                        if hero_char.x_y[1] < enemy_fighting.x_y[1] - enemy_fighting.height and frozen == False:
                            hero_char.x_y[1] +=  hero_char.speed_x_y[1]
                        elif hero_char.x_y[1] > enemy_fighting.x_y[1] + enemy_fighting.height and frozen == False:
                            hero_char.x_y[1] -=  hero_char.speed_x_y[1]
                    
                    else:
                        #If enemy is not clicked on
                        if hero_char.x_y[0] + 1 < mouse_click_position[0] and frozen == False:
                            hero_char.x_y[0] += hero_char.speed_x_y[0]
                        elif hero_char.x_y[0] - 1 > mouse_click_position[0] and frozen == False:
                            hero_char.x_y[0] -= hero_char.speed_x_y[0]

                        if hero_char.x_y[1] + 1 < mouse_click_position[1] and frozen == False:
                            hero_char.x_y[1] +=  hero_char.speed_x_y[1]
                        elif hero_char.x_y[1] - 1 > mouse_click_position[1] and frozen == False:
                            hero_char.x_y[1] -=  hero_char.speed_x_y[1]
                   

            # Goes to store
            if area == [98, 100]:
                if hero_char.x_y[0] > 170 and hero_char.x_y[0] < 285 and hero_char.x_y[1] > 80 and hero_char.x_y[1] < 155:
                    area = "Store"
                    current_area = Store()

            # Change area on top
            try:
                if hero_char.x_y[0] >= current_area.north_area_change_x_y[0] and hero_char.x_y[0] <= current_area.north_area_change_x_y[1] and hero_char.x_y[1] >= current_area.north_area_change_x_y[2] and hero_char.x_y[1] <= current_area.north_area_change_x_y[3]:
                    area_change = True
                    area[1] += 1
                    current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                    dead_enemy_list = []
                    hero_char.x_y[1] = current_area.level_border_y[1] - 35
                    mouse_click_position[1] = current_area.level_border_y[1] - 35
            except AttributeError:
                pass
            # Changes area on bottom
            try:
                if hero_char.x_y[0] >= current_area.south_area_change_x_y[0] and hero_char.x_y[0] <= current_area.south_area_change_x_y[1] and hero_char.x_y[1] >= current_area.south_area_change_x_y[2] and hero_char.x_y[1] <= current_area.south_area_change_x_y[3]:
                    area_change = True
                    area[1] -= 1
                    current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                    dead_enemy_list = []
                    hero_char.x_y[1] = current_area.level_border_y[0] + 35
                    mouse_click_position[1] = current_area.level_border_y[0] + 35
            except AttributeError:
                pass
            # Changes area on left
            try:

                if hero_char.x_y[0] >= current_area.west_area_change_x_y[0] and hero_char.x_y[0] <= current_area.west_area_change_x_y[1] and hero_char.x_y[1] >= current_area.west_area_change_x_y[2] and hero_char.x_y[1] <= current_area.west_area_change_x_y[3]:
                    # if area == [100, 100]:
                    #     area = "Store"
                    #     current_area = Store()
                    # else:
                    area[0] -= 1
                    current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                    area_change = True
                    dead_enemy_list = []
                    hero_char.x_y[0] = current_area.level_border_x[1] - 35
                    mouse_click_position[0] = current_area.level_border_x[1] - 35
            except AttributeError:
                pass
            # Changes area on right
            try:
                if hero_char.x_y[0] >= current_area.east_area_change_x_y[0] and hero_char.x_y[0] <= current_area.east_area_change_x_y[1] and hero_char.x_y[1] >= current_area.east_area_change_x_y[2] and hero_char.x_y[1] <= current_area.east_area_change_x_y[3]:
                    area[0] += 1
                    current_area = eval("Area_" + str(area[0]) + "_" + str(area[1]) + "()")
                    area_change = True
                    dead_enemy_list = []
                    hero_char.x_y[0] = current_area.level_border_x[0] + 35
                    mouse_click_position[0] = current_area.level_border_x[0] + 35
            except AttributeError:
                pass
            
            # if enemy is clicked on
            # if frozen == False:
            #     try:
            #         enemy_count = len(enemy_char) - 1
            #         hero_speed = 1
            #         #hero_speed = (hero_char.speed_x_y[0] / (enemy_count)) # prevents hero from speeding up with more characters
            #     except ZeroDivisionError:
            #         # prevents error when there's less then 2 enemies
            #         hero_speed = 1
            # else:
            #     hero_speed = 0
                
            for enemy in enemy_char:
                try:
                #Checks if an enemy was in the click location
                    if Battle().attack_mode(hero_char, enemy, mouse_click_position) == True and hero_char.fight_status == False:
                        enemy_fighting = enemy
                        run_away = False

                        if hero_char.fight_status == False and Battle().attack_range(hero_char, enemy_fighting) == True and attack_timer == 90:
                            hero_char.attack_time = 80
                            enemy_fighting.attack_time = 35
                        elif hero_char.fight_status == False and Battle().attack_range(enemy_fighting, hero_char) == True and attack_timer == 90:
                            hero_char.attack_time = 35
                            enemy_fighting.attack_time = 80
                        
                        hero_char.fight_status = True

                #Prevents error when passing to a different map
                except TypeError:
                    pass

                # Gives player with a higher attack range the attack advantage if clicked on from far away
                if (hero_char.fight_status == False or Battle().attack_range(enemy_fighting, hero_char) == False) and Battle().attack_range(hero_char, enemy_fighting) == True and attack_timer == 90:
                    hero_char.attack_time = 80
                    enemy_fighting.attack_time = 35
                elif (hero_char.fight_status == False or Battle().attack_range(hero_char, enemy_fighting) == False) and Battle().attack_range(enemy_fighting, hero_char) == True and attack_timer == 90:
                    hero_char.attack_time = 35
                    enemy_fighting.attack_time = 80 

        elif button_pressed == RIGHT_CLICK:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_pressed = event.button
                mouse_location2 = pygame.mouse.get_pos()
                hero_char.x_y = [mouse_location2[0], mouse_location2[1]]

            elif event.type == pygame.MOUSEBUTTONUP:
                pass

        # Sets up enemy auto attack for higher level enemies
        for enemy in enemy_char:
            if (hero_char.power_lv + hero_char.defense_lv + hero_char.max_health) < (enemy.power + enemy.defense + enemy.max_health) and battle_mode == False and Battle().attack_range(enemy, hero_char) == True:
                
                enemy_fighting = enemy
                enemy.fight_status = True
                battle_mode = True
                hero_char.attack_time = 35
                enemy_fighting.attack_time = 80

        if (hero_char.fight_status == True or enemy_fighting.fight_status == True) and (Battle().attack_range(hero_char, enemy_fighting) == True or Battle().attack_range(enemy_fighting, hero_char) == True):
            
            #enemy_fighting.speed_x_y = [0, 0]
            battle_mode = True
            #print("Enemy Attack Timer: {} Battle Attack Range: {}".format(enemy_fighting.attack_time, Battle().attack_range(enemy_fighting, hero_char)))

            # hero death
            if hero_char.health <= 0:
                history_line_text.append("You were killed by {}. You lost: ". format(enemy_fighting.name))
                history_line_color.append(red_color)
                history_line_text_numb = len(history_line_text) - 1
                history_line_text.append("  your equipment, {} coins, and {} healing potions".format(int(round(hero_char.coins * .80)), hero_char.items["Healing_Potion"]))
                history_line_color.append(red_color)
                history_line_text_numb = len(history_line_text) - 1
                battle_mode = False 
                
                #if current_area != Area_98_100():
                current_area = Area_98_100()
                area = [98, 100]
                area_change = True
                hero_char.hero_death(enemy_fighting)
                frozen = False
                mouse_click_position[0] = 90
                mouse_click_position[1] = 150

            if frozen == True:
                if turns_frozen == 1 or (enemy_fighting.name == "Wizard" and enemy_fighting.health == 0):
                    hero_char.speed_x_y = [2, 2]
                else:
                    turns_frozen += 1

            # Hero attacks enemy
            if attack_timer == hero_char.attack_time and hero_char.health > 0 and hero_char.fight_status == True and Battle().attack_range(hero_char, enemy_fighting) == True:
                rand_number_special = random.randint(1, 5)
                hero_char.fight_status = True
                if rand_number_special == 1:
                    special_attack = True
                else:
                    special_attack = False

                if frozen == True:
                    print("You are frozen for one move")
                else:
                    hero_char.attack(enemy_fighting, special_attack, screen)
                    if special_attack == True:
                        history_line_text.append("SPECIAL ATTACK: {} does {} damage to {}.".format(hero_char.name, enemy_fighting.damage, enemy_fighting.name))
                    else:
                        history_line_text.append("{} does {} damage to {}.".format(hero_char.name, enemy_fighting.damage, enemy_fighting.name))
                    history_line_color.append(green_color)
                    history_line_text_numb = len(history_line_text) - 1
                    if hero_char.attack_stance == "Aggressive":
                        hero_char.power_exp += round(enemy_fighting.damage * 3.7)
                        hero_char.health_exp += round(enemy_fighting.damage * 1.5)
                    elif hero_char.attack_stance == "Defensive":
                        hero_char.defense_exp += round(enemy_fighting.damage * 3.7)
                        hero_char.health_exp += round(enemy_fighting.damage * 1.5)
                    elif hero_char.attack_stance == "Normal":
                        hero_char.power_exp += round(enemy_fighting.damage * 1.5)
                        hero_char.defense_exp += round(enemy_fighting.damage * 1.5)
                        hero_char.health_exp += round(enemy_fighting.damage * 2.0)


                    if hero_char.health_exp >= hero_char.next_health_level_exp:
                        hero_char.health += 1
                        hero_char.max_health += 1
                        hero_char.next_health_level_exp = round(((25 + (hero_char.health + 1)) * (hero_char.health + 1) / 1.13767) * hero_char.health)
                        history_line_text.append("Your health level is now {}!".format(hero_char.max_health))
                        history_line_color.append(yellow_color)
                    if hero_char.power_exp >= hero_char.next_power_level_exp:
                        hero_char.power_lv += 1
                        hero_char.power += 1
                        hero_char.next_power_level_exp = round(((25 + (hero_char.power_lv + 1)) * (hero_char.power_lv + 1) / 1.13767) * hero_char.power_lv)
                        history_line_text.append("Your power level is now {}!".format(hero_char.power_lv))
                        history_line_color.append(yellow_color)
                    if hero_char.defense_exp >= hero_char.next_defense_level_exp:
                        hero_char.defense_lv += 1
                        hero_char.defense += 1
                        hero_char.next_defense_level_exp = round(((25 + (hero_char.defense_lv + 1)) * (hero_char.defense_lv + 1) / 1.13767) * hero_char.defense_lv)
                        history_line_text.append("Your defense level is now {}!".format(hero_char.defense_lv))
                        history_line_color.append(yellow_color)

                special_attack = False
                
            if enemy_fighting.health <= 0:
                enemy_fighting.remove_dead_char(enemy_fighting, hero_char, screen, background_image)
                attack_timer = 91
                coins_received = hero_char.bounty_earned(hero_char, enemy_fighting)
                history_line_text.append("{} dead. You receive {} coins".format(enemy_fighting.name, coins_received))
                history_line_text_numb = len(history_line_text) - 1
                history_line_color.append(yellow_color)
                dead_enemy_list.append(enemy_fighting)
                enemy_char.remove(enemy_fighting)
                mouse_click_position[0] = -200  # prevents hero from auto attacked on enemy respawn
                battle_mode = False

            # Enemy attacks hero
            
            elif attack_timer == enemy_fighting.attack_time and enemy_fighting.health > 0 and (Battle().attack_range(enemy_fighting, hero_char) == True): # or run_away == True):
                # attack_timer = 100
                if enemy.name == "Dragon":
                    rand_number = random.randint(1, 3)
                else:
                    rand_number_special = random.randint(1, 5)
                frozen = False
                if rand_number_special == 1 and enemy_fighting.name != "Goblin" and enemy_fighting.name != "Shadow" and enemy_fighting.name != "Zombie":
                    special_attack = True
                    if enemy_fighting.name == "Wizard":
                        frozen = True
                        turns_frozen = 0
                else:
                    special_attack = False
                enemy_fighting.attack(hero_char, special_attack, screen)
                if special_attack == True:
                    history_line_text.append(enemy_fighting.special_attack_text)
                    special_attack = False
                else:
                    history_line_text.append("{} does {} damage to {}.".format(enemy_fighting.name, hero_char.damage, hero_char.name))
                history_line_text_numb = len(history_line_text) - 1
                history_line_color.append(red_color)

            if attack_timer < 0:
                attack_timer = 90

            if area_change == True:
                run_away = True

            # change health bar
            hero_char.health_bar()
            enemy_fighting.health_bar()

            attack_timer -=1 
            #print(attack_timer)

        # Enemy movement
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            if movement % 2 == 0:
                change_dir_countdown = 80
            else:
             change_dir_countdown = 240
        
        # enemy movement
        if change_dir_countdown == 60:
            if movement == 0:
                rand_numb = random.randint(0, 7)
            elif movement == 1:
                rand_numb = 8
            elif movement == 2:
                rand_numb = random.randint(0, 7)
            elif movement == 3:
                rand_numb = 8
                movement = -1
            movement += 1

        for enemy in enemy_char:
            enemy.walking(rand_numb, hero_char)

        for enemy in enemy_char:
            # Hovering over enemy
            if Options().character_options(enemy, current_mouse_location) == "Attack":
                mouse_over = "Attack {}. (Power: {}   Defense: {}   Health: {})".format(enemy.name, enemy.power, enemy.defense, enemy.max_health)
                mouse_over_color = red_color
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                break
            else:
                mouse_over = ""
                mouse_over_color = black_color
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        for dead_enemy in dead_enemy_list:
            dead_enemy.respawn_timer += 1
            if dead_enemy.respawn_timer >= dead_enemy.respawn_time:
                dead_enemy.respawn_timer = 0
                #print(dead_enemy)
                dead_enemy.health = dead_enemy.max_health
                dead_enemy.health_bar_numb = 20
                dead_enemy.speed_x_y = [1, 1]
                dead_enemy.x_y_when_clicked = [-300, -300]
                enemy_char.append(dead_enemy)
                dead_enemy_list.remove(dead_enemy)
        
        if run_away == True:
            enemy_fighting.speed_x_y = [1, 1]
            enemy_fighting.fight_status = False
            enemy_fighting = Fake()
            battle_mode = False
            attack_timer = 90
            run_away = False

        # Hovering over Healing Potion    
        if current_mouse_location[0] >= 534 and current_mouse_location[0] <= 565 and current_mouse_location[1] >= 314 and current_mouse_location[1] <=  350:
            if hero_char.items["Healing_Potion"] == 0:
                mouse_over = "Out of healing potions. Go to store to buy"
                mouse_over_color = red_color
            else:
                mouse_over = "Click to drink healing potion"
                mouse_over_color = red_color
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        # Hovering over stores
        if area == [98, 100]:
            if current_mouse_location[0] >= 175 and current_mouse_location[0] <= 275 and current_mouse_location[1] >= 50 and current_mouse_location[1] <=  175:
                mouse_over = "Go to store"
                mouse_over_color = green_color

        # Hovering over area passage ways
        try: 
            if current_mouse_location[0] >= current_area.north_area_change_x_y[0] and current_mouse_location[0] <= current_area.north_area_change_x_y[1] and current_mouse_location[1] >= current_area.north_area_change_x_y[2] and current_mouse_location[1] <= current_area.north_area_change_x_y[3]:
                # if area == [0,0]:
                mouse_over = "Go North"
                mouse_over_color = green_color
        except AttributeError:
                pass
        try:
            if current_mouse_location[0] >= current_area.south_area_change_x_y[0] and current_mouse_location[0] <= current_area.south_area_change_x_y[1] and current_mouse_location[1] >= current_area.south_area_change_x_y[2] and current_mouse_location[1] <= current_area.south_area_change_x_y[3]:
                # if area == [0,1]:
                mouse_over = "Go South"
                mouse_over_color = green_color
        except AttributeError:
                pass
        try:
            if current_mouse_location[0] >= current_area.west_area_change_x_y[0] and current_mouse_location[0] <= current_area.west_area_change_x_y[1] and current_mouse_location[1] >= current_area.west_area_change_x_y[2] and current_mouse_location[1] <= current_area.west_area_change_x_y[3]:
                # if area == [100, 100]:
                #     mouse_over = "Go to Store"
                # else:
                mouse_over = "Go West"
                mouse_over_color = green_color
        except AttributeError:
                pass
        try:
            if current_mouse_location[0] >= current_area.east_area_change_x_y[0] and current_mouse_location[0] <= current_area.east_area_change_x_y[1] and current_mouse_location[1] >= current_area.east_area_change_x_y[2] and current_mouse_location[1] <= current_area.east_area_change_x_y[3]:
                # if area == [0,1] or area == [1,1]:
                mouse_over = "Go East"
                mouse_over_color = green_color
        except AttributeError:
                pass

    ### Scrollable map attempt
        # background_image = (pygame.image.load("images/background_images/full_map.png").convert_alpha().subsurface(0, 480, 512, 480)) # (start location x, start location y, width, height)
        # playerYMovement = 400 - hero_char.x_y[1]
        # try:
        #     background_image = (pygame.image.load("images/background_images/full_map.png").convert_alpha().subsurface(0, 480 - playerYMovement, 512, 480))
        # except ValueError:
        #     pass

        # Draw background
        screen.fill(black_color)

        # Game display

        # loads background based on area
        if area == "Store" and area_change == True:
            enemy_char = Store().enemy_char
            background_image = Store().background_image
            area_change = False
        else:
            enemy_char = current_area.enemy_char
            background_image = current_area.background_image
            area_change = False

        screen.blit(background_image, (0, 20))

        if new_game == True:
            font = pygame.font.Font(None, 30)
            user_name_text = font.render("Choose new character name:", True, blue_color)
            screen.blit(user_name_text, (250, 230))
            screen.blit(text_input, (200, 260))
            font = pygame.font.Font(None, 36)
            user_name_text = font.render(user_name, True, white_color)
            screen.blit(user_name_text, (215, 280))

        if load_game == True:
            try:
                myfile = open("actions/save_state/player_database.pickle", "rb")
                player_stats = pickle.load(myfile)
                myfile.close()
            except FileNotFoundError:
                pass

            text_location_y = 100
            font = pygame.font.Font(None, 50)
            load_game_text = font.render("Select game by typing game number to load", True, blue_color)
            screen.blit(load_game_text, (20, text_location_y - 80))

            font = pygame.font.Font(None, 40)
            load_game_text = font.render("Power", True, green_color)
            screen.blit(load_game_text, (260, text_location_y - 35))

            load_game_text = font.render("Defense", True, blue_color)
            screen.blit(load_game_text, (350, text_location_y - 35))

            load_game_text = font.render("Health", True, red_color)
            screen.blit(load_game_text, (480, text_location_y - 35))

            load_game_text = font.render("Coins", True, yellow_color)
            screen.blit(load_game_text, (630, text_location_y - 35))

            i = 1
            for game in user_data:
                load_game_text = font.render("{}. {}".format(i, game), True, blue_color)
                screen.blit(load_game_text, (40, text_location_y))

                try:

                    load_game_text = font.render("{}".format(player_stats[i - 1][3]), True, green_color)
                    screen.blit(load_game_text, (300, text_location_y))
                    load_game_text = font.render("{}".format(player_stats[i - 1][4]), True, blue_color)
                    screen.blit(load_game_text, (400, text_location_y))
                    load_game_text = font.render("{}/{}".format(player_stats[i - 1][1], player_stats[i - 1][2]), True, red_color)
                    screen.blit(load_game_text, (500, text_location_y))
                    load_game_text = font.render("{}".format(player_stats[i - 1][8]), True, yellow_color)
                    screen.blit(load_game_text, (650, text_location_y))
                except FileNotFoundError and UnboundLocalError:
                    pass

                i += 1
                text_location_y += 45

        if area != "Main Menu":
            screen.blit(dark_background_image, (0, 0))
            screen.blit(background_image, (0, 20))
            screen.blit(user_interface_image, (521, 5))
            screen.blit(hero_char.char_image, (hero_char.x_y[0], hero_char.x_y[1]))
            screen.blit(scroll_up, (430, 555))
            screen.blit(scroll_down, (430, 595))

            font = pygame.font.Font(None, 25)
            headingfont = pygame.font.Font(None, 34)

            if area == "Store":
                # Store selections
                store = Store()
                font = pygame.font.Font(None, 28)
                store_text = font.render("Welcome to the inventory store!", True, white_color)
                screen.blit(store_text, (10, 80))
                store_text = font.render("Select a Number", True, white_color)
                screen.blit(store_text, (10, 110))
                font = pygame.font.Font(None, 24)
                store_text = font.render("1. Healing Potion: {} ({} coins)".format(store.healing_potion["description"], store.healing_potion["price"]), True, green_color)
                screen.blit(store_text, (20, 140))
                store_text = font.render("2. Helmet: {} ({} coins)".format(store.helmet["description"], store.helmet["price"]), True, green_color)
                screen.blit(store_text, (20, 170))
                store_text = font.render("3. Sword: {} ({} coins)".format(store.sword["description"], store.sword["price"]), True, green_color)
                screen.blit(store_text, (20, 200))
                store_text = font.render("4. Shield: {} ({} coins)".format(store.shield["description"], store.shield["price"]), True, green_color)
                screen.blit(store_text, (20, 230))
                store_text = font.render("5. Chainmail: {} ({} coins)".format(store.chainmail["description"], store.chainmail["price"]), True, green_color)
                screen.blit(store_text, (20, 260))
                store_text = font.render("6. Zombie Axe: {} ({} coins)".format(store.zombie_axe["description"], store.zombie_axe["price"]), True, green_color)
                screen.blit(store_text, (20, 290))
                store_text = font.render("7. Dragon Fire Shield: {} ({} coins)".format(store.dragon_fire_shield["description"], store.dragon_fire_shield["price"]), True, green_color)
                screen.blit(store_text, (20, 320))
                store_text = font.render("8. Level Upgrades", True, blue_color)
                screen.blit(store_text, (20, 400))
                store_text = font.render("9. Exit Store", True, red_color)
                screen.blit(store_text, (20, 450))

            if area == "Upgrade_Level_Store":
                #Upgrade area selection
                upgrade_levels = Upgrade_Level_Store(hero_char)
                font = pygame.font.Font(None, 28)
                store_text = font.render("Welcome to the upgrade store!", True, white_color)
                screen.blit(store_text, (10, 80))
                store_text = font.render("Select a Number to upgrade a skill level", True, white_color)
                screen.blit(store_text, (10, 110))
                font = pygame.font.Font(None, 24)
                store_text = font.render("1. Power Level ({} coins)".format(upgrade_levels.power_level), True, green_color)
                screen.blit(store_text, (20, 140))
                store_text = font.render("2. Defense Level ({} coins)".format(upgrade_levels.defense_level), True, blue_color)
                screen.blit(store_text, (20, 170))
                store_text = font.render("3. Health Level ({} coins)".format(upgrade_levels.health_level), True, red_color)
                screen.blit(store_text, (20, 200))
                store_text = font.render("8. Inventory Store", True, blue_color)
                screen.blit(store_text, (20, 400))
                store_text = font.render("9. Exit Store", True, red_color)
                screen.blit(store_text, (20, 450))

            font = pygame.font.Font(None, 28)
            mouse_over_text = font.render("{}".format(mouse_over), True, mouse_over_color)
            screen.blit(mouse_over_text, (0, 0))

            font = pygame.font.Font(None, 22)
            smallfont = pygame.font.Font(None, 18)

            hero_stats_text = font.render("{}".format(hero_char.power_lv), True, green_color)
            screen.blit(hero_stats_text, (651, 124))
            hero_stats_text = smallfont.render("Current Exp: {}             Next level: {}".format("{:,}".format(hero_char.power_exp), "{:,}".format(hero_char.next_power_level_exp)), True, green_color)
            screen.blit(hero_stats_text, (550, 142))

            hero_stats_text =  font.render("{}".format(hero_char.defense_lv), True, dark_blue_color)
            screen.blit(hero_stats_text, (651, 174))
            hero_stats_text = smallfont.render("Current Exp: {}             Next level: {}".format("{:,}".format(hero_char.defense_exp), "{:,}".format(hero_char.next_defense_level_exp)), True, dark_blue_color)
            screen.blit(hero_stats_text, (550, 195))

            hero_stats_text = font.render("{} / {}".format(hero_char.health, hero_char.max_health), True, red_color)
            screen.blit(hero_stats_text, (651, 232))
            hero_stats_text = smallfont.render("Current Exp: {}             Next level: {}".format("{:,}".format(hero_char.health_exp), "{:,}".format(hero_char.next_health_level_exp)), True, red_color)
            screen.blit(hero_stats_text, (550, 252))

            hero_inv_text = font.render("{}".format("{:,}".format(hero_char.coins)), True, yellow_color)
            screen.blit(hero_inv_text, (715, 583))
            hero_inv_text = font.render("{}".format(hero_char.items["Healing_Potion"]), True, red_color)
            screen.blit(hero_inv_text, (710, 328))
            
            if hero_char.attack_stance == "Aggressive":
                screen.blit(radio_button, (542, 523))
                
            # Defensive
            if hero_char.attack_stance == "Defensive":
                screen.blit(radio_button, (682, 523))
            #Normal
            if hero_char.attack_stance == "Normal":
                screen.blit(radio_button, (542, 566))

            # hero_inv_text = headingfont.render("Equipment:", True, grey_color)
            # screen.blit(hero_inv_text, (515,  300))
            # hero_inv_text = font.render("Sword: {}".format(hero_char.items["Sword"]), True, green_color)
            # screen.blit(hero_inv_text, (548,  330))
            # hero_inv_text = font.render("Helmet: {}".format(hero_char.items["Helmet"]), True, blue_color)
            # screen.blit(hero_inv_text, (548,  360))
            # hero_inv_text = font.render("Shield: {}".format(hero_char.items["Shield"]), True, blue_color)
            # screen.blit(hero_inv_text, (548,  390))
            # hero_inv_text = font.render("Chainmail: {}".format(hero_char.items["Chainmail"]), True, blue_color)
            # screen.blit(hero_inv_text, (548,  420))
            # hero_inv_text = font.render("Zombie_Axe: {}".format(hero_char.items["Zombie_Axe"]), True, blue_color)
            # screen.blit(hero_inv_text, (548,  450))
            # hero_inv_text = font.render("Dragon_Fire_Shield: {}".format(hero_char.items["Dragon_Fire_Shield"]), True, blue_color)
            # screen.blit(hero_inv_text, (548,  480))
            

            screen.blit(font.render("History:", True, grey_color), (10, 510))
            screen.blit(font.render("-" * 85, True, grey_color), (4, 520))
            screen.blit(font.render("Username: {}".format(hero_char.player_user_name), True, grey_color), (450, 640))
            font_history_box = pygame.font.Font(None, 20)

            screen.blit(font.render(history_line_text[history_line_text_numb - 5], True, history_line_color[history_line_text_numb - 5]), (20, 540))
            screen.blit(font.render(history_line_text[history_line_text_numb - 4], True, history_line_color[history_line_text_numb - 4]), (20, 560))
            screen.blit(font.render(history_line_text[history_line_text_numb - 3], True, history_line_color[history_line_text_numb - 3]), (20, 580))
            screen.blit(font.render(history_line_text[history_line_text_numb - 2], True, history_line_color[history_line_text_numb - 2]), (20, 600))
            screen.blit(font.render(history_line_text[history_line_text_numb - 1], True, history_line_color[history_line_text_numb - 1]), (20, 620))
            screen.blit(font.render(history_line_text[history_line_text_numb], True, history_line_color[history_line_text_numb]), (20, 640))

            if hero_char.fight_status == True or battle_mode == True or enemy_fighting.fight_status == True:
                if hero_char.damage == 0:
                    damage_color = blue_color
                else:
                    damage_color = red_color
                
                font = pygame.font.Font(None, 25)
                damage_text = font.render("{}".format(hero_char.damage), True, damage_color)
                screen.blit(damage_text, (hero_char.x_y[0] + (hero_char.width / 4), hero_char.x_y[1] - 30))
                screen.blit(health_bar_image[hero_char.health_bar_numb], (hero_char.x_y[0] + (hero_char.width / 10), hero_char.x_y[1] - 10))

            #for enemy in enemy_char:
            if enemy_fighting.fight_status == True:
                if enemy_fighting.damage == 0:
                    damage_color = blue_color
                else:
                    damage_color = red_color
                
                font = pygame.font.Font(None, 25)
                damage_text = font.render("{}".format(enemy_fighting.damage), True, damage_color)
                if hero_char.fight_status == True:
                    screen.blit(damage_text, (enemy_fighting.x_y[0] + (enemy_fighting.width / 4), enemy_fighting.x_y[1] - 30))
                screen.blit(health_bar_image[enemy_fighting.health_bar_numb], (enemy_fighting.x_y[0] + (enemy_fighting.width / 10), enemy_fighting.x_y[1] - 10))

            for enemy in enemy_char:
                if enemy.health > 0:
                    screen.blit(enemy.char_image, (enemy.x_y[0], enemy.x_y[1]))
                
            ## scrollable map attempt
                #if enemy.health > 0 and (enemy.x_y[1] + playerYMovement) <= 500 - enemy.height:
                    #screen.blit(enemy.char_image, (enemy.x_y[0], enemy.x_y[1] + playerYMovement))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
