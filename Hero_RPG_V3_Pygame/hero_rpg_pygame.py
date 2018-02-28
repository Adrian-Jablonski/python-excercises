import pygame
import random
import time
import math

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
from actions.levels import *

RIGHT_CLICK = 3
LEFT_CLICK = 1
KEY_1 = 49
KEY_2 = 50
KEY_3 = 51
KEY_4 = 52
KEY_5 = 53
KEY_6 = 54
KEY_7 = 55
KEY_8 = 56
KEY_9 = 57
ENTER_BUTTON = 13

#from menus.main_menu import Menu

def main():
    game_screen_width = 512
    game_screen_height = 500
    width = 720
    height = 660
    blue_color = (0, 0, 255)
    green_color = (0, 255, 0)
    yellow_color = (255, 255, 0)
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)
    grey_color = (211, 211, 211)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # ************* IMAGES *******************

    dark_background_image = pygame.image.load("images/dark_background.png").convert_alpha()
    background_image = Level1().background_image
    text_bottom = pygame.image.load("images/text_bottom.png").convert_alpha()
    hero_image = pygame.image.load("images/hero.png").convert_alpha()
    monster_image = pygame.image.load("images/monster.png").convert_alpha()

    power_image =  pygame.image.load("images/power.png").convert_alpha()
    defense_image =  pygame.image.load("images/defense.png").convert_alpha()
    health_image = pygame.image.load("images/health.png").convert_alpha()
    coin_image = pygame.transform.scale(pygame.image.load("images/coin.png").convert_alpha(), (30, 32))
    healing_potion = pygame.image.load("images/healing_potion.png").convert_alpha()
    scroll_up = pygame.image.load("images/scroll_up_button.gif").convert_alpha()
    scroll_down = pygame.image.load("images/scroll_down_button.gif").convert_alpha()

    health_bar_image = []
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar0.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar5.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar10.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar15.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar20.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar25.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar30.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar35.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar40.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar45.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar50.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar55.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar60.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar65.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar70.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar75.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar80.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar85.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar90.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar95.png").convert_alpha(), (23, 4)))
    health_bar_image.append(pygame.transform.scale(pygame.image.load("images/Status_Bars/Status_Bar100.png").convert_alpha(), (23, 4)))

    #******************************************

    hero_char = Hero()
    level = 1
    level_change = False
    enemy_char = Level1().enemy_char
    enemy_count = len(enemy_char) - 1
    enemy_numb = 0

    change_dir_countdown = 120

    attack_timer = 100
    movement = 0
    rand_numb = random.randint(0, 8)
    mouse_click_position = [0, 0]
    current_mouse_position = [0, 0]
    run_away = False
    frozen = False
    damage_enemy = ""
    damage_hero = ""
    enemy_fighting = Fake()
    dead_enemy_list = []
    respawn_timer = 0
    item_bought = ""
    history_line_text = ["", "", "", "", "", ""]
    history_line_color = [black_color, black_color, black_color, black_color, black_color, black_color]
    history_line_text_numb = len(history_line_text) - 1

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
                # Save enemy position at time of click
                for enemy in enemy_char:
                    enemy.x_when_clicked = enemy.x
                    enemy.y_when_clicked = enemy.y
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

            # Store selections 
            if level == 0 or level == 0.1:
                if level == 0:
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
                    elif key_pressed == KEY_8:
                        level = 0.1
                        level_change = True
                        item_bought = ""
                    elif key_pressed == KEY_9:
                        level = 1
                        level_change = True
                        hero_char.x = 60
                        item_bought = ""
                    else:
                        item_bought = ""

                    if item_bought != "":
                        # if (hero_char.items[item_bought] == 0 or item_bought == "Healing_Potion"):
                        #     history_line_text.append("You bought a {}".format(item_bought))
                        #     history_line_color.append(white_color)
                        if hero_char.items[item_bought] > 0 and item_bought != "Healing_Potion":
                            history_line_text.append("Alread own a {}".format(item_bought_name))
                        elif Store().shopping(hero_char, item_bought) == True:
                            history_line_text.append("You bought a {}".format(item_bought_name))
                        else:
                            history_line_text.append("Not enough coins to buy {}".format(item_bought_name))

                    
                        history_line_text_numb = len(history_line_text) - 1
                        history_line_color.append(white_color)

                #Level upgrade store
                elif level == 0.1:
                    upgrade_level = Upgrade_Level_Store(hero_char)
                    if key_pressed == KEY_1:
                        item_bought = "Power_Level"
                        power_up_name = "Power Level"
                        new_level = hero_char.power + 1
                    elif key_pressed == KEY_2:
                        item_bought = "Defense_Level"
                        power_up_name = "Defense Level"
                        new_level = hero_char.defense + 1
                    elif key_pressed == KEY_3:
                        item_bought = "Health_Level"
                        power_up_name = "Health Level"
                        new_level = hero_char.max_health + 1
                    elif key_pressed == KEY_8:
                        level = 0
                        level_change = True
                        item_bought = ""
                    elif key_pressed == KEY_9:
                        level = 1
                        level_change = True
                        hero_char.x = 60
                        item_bought = ""
                    else:
                        item_bought = ""

                    if item_bought != "":
                        if upgrade_level.level_up(hero_char, item_bought) == True:
                            history_line_text.append("Your {} is now {}".format(power_up_name, new_level))
                        else:
                            history_line_text.append("Not enough coins to buy {}".format(power_up_name))
                        history_line_color.append(white_color)
                        history_line_text_numb = len(history_line_text) - 1
                        #upgrade_level.level_up(hero_char, item_bought)
                    
            # Make click location for healing potion   
            if mouse_click_position[0] >= 517 and mouse_click_position[0] <= 544 and mouse_click_position[1] >=240 and mouse_click_position[1] <= 270:
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
                    print(history_line_text_numb)
            
            elif mouse_click_position[0] >= 430 and mouse_click_position[0] <= 470 and mouse_click_position[1] >= 585 and mouse_click_position[1] <= 620:
                if history_line_text_numb < len(history_line_text) - 1:
                    history_line_text_numb += 1
                    mouse_click_position[0] = 420
                    print(history_line_text_numb)


            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        
        #Enemy click detection. Also prevents hero from going outside of game screen
        if button_pressed == LEFT_CLICK and mouse_click_position[0] >= -10 and mouse_click_position[0] <= 515 and mouse_click_position[1] >= 10 and mouse_click_position[1] <= 510:
            
            # Change levels on top
            if hero_char.x >= 215 and hero_char.x <= 300 and hero_char.y >= 0 and hero_char.y <= 50:
                if level == 1:
                    level_change = True
                    level = 2
                    dead_enemy_list = []
                    hero_char.y = 450
            # Changes levels on bottom
            if hero_char.x >= 215 and hero_char.x <= 300 and hero_char.y >= 465 and hero_char.y <= 500:
                if level == 2:
                    level_change = True
                    level = 1
                    dead_enemy_list = []
                    hero_char.y = 52
            # Changes level on left
            if hero_char.x >= 0 and hero_char.x <= 50 and hero_char.y >= 220 and hero_char.y <= 275:
                if level == 1:
                    level_change = True
                    level = 0
                    dead_enemy_list = []
                    hero_char.x = 452

            # Changes level on right
            # if hero_char.x >= 375 and hero_char.x <= 415 and hero_char.y >= 220 and hero_char.y <= 275:
            #     if level == 0:
            #         level_change = True
            #         level = 1
            #         dead_enemy_list = []
            #         hero_char.x = 60    

            # if enemy is clicked on
            if frozen == False:
                try:
                    enemy_count = len(enemy_char) - 1
                    hero_speed = (hero_char.speed_x / (enemy_count)) # prevents hero from speeding up with more characters
                except ZeroDivisionError:
                    # prevents error when there's less then 2 enemies
                    hero_speed = 1
            else:
                hero_speed = 0
                
            for enemy in enemy_char:
                try:
                #Checks if an enemy was in the click location (currently any enemy that steps into the location passes the test)
                    if Battle().attack_mode(hero_char, enemy, mouse_click_position) == True and hero_char.fight_status == False:
                        enemy_fighting = enemy
                        # Moves toward enemy
                        mouse_click_position[0] = enemy_fighting.x
                        mouse_click_position[1] = enemy_fighting.y
                        
                        # starts attacking the enemy when hero is within range of enemy
                        if Battle().distance_from_enemy(hero_char, enemy) == True:
                            hero_char.fight_status = True
                    
                    # if enemy was not clicked on
                    elif hero_char.movement(hero_char, mouse_click_position) == False:
                        hero_char.fight_status = False
                        enemy.fight_status = False
                        enemy_fighting.speed_x = 1
                        enemy_fighting.speed_y = 1
                        enemy_fighting = Fake()
                        if hero_char.fight_status == True and frozen == False:
                            run_away = True
                            hero_char.fight_status = False
                        if hero_char.x < mouse_click_position[0] and frozen == False:
                            hero_char.x += hero_speed
                        elif hero_char.x > mouse_click_position[0] and frozen == False:
                            hero_char.x -= hero_speed

                        if hero_char.y < mouse_click_position[1] and frozen == False:
                            hero_char.y += hero_speed
                        elif hero_char.y > mouse_click_position[1] and frozen == False:
                            hero_char.y -= hero_speed

                #Prevents error when passing to a different map
                except TypeError:
                    pass

                if hero_char.fight_status == True:
                    # Player movement toward enemy
                    if hero_char.x < enemy_fighting.x - (enemy.width / 2):
                        hero_char.x += hero_speed * 2
                    elif hero_char.x > enemy_fighting.x + (enemy.width / 2):
                        hero_char.x -= hero_speed * 2
                    #elif hero_char.x > enemy_fighting.x and hero_char.x < enemy_fighting.x: # - enemy_fighting.width and hero_char.x < enemy_fighting.x - enemy_fighting.width:
                     #   hero_char.x += hero_speed

                    if hero_char.y < enemy_fighting.y - enemy_fighting.height:
                        hero_char.y += hero_speed * 2
                    elif hero_char.y > enemy_fighting.y + enemy_fighting.height:
                        hero_char.y -= hero_speed * 2

        elif button_pressed == RIGHT_CLICK:
            pass           

        if hero_char.fight_status == True or run_away == True:
            #print(frozen)
            #print(enemy_fighting.name)
            enemy_fighting.speed_x = 0
            enemy_fighting.speed_y = 0

            if frozen == True:
                if turns_frozen == 1 or (enemy_fighting.name == "Wizard" and enemy_fighting.health == 0):
                    hero_char.speed_x = 1
                    hero_char.speed_y = 1
                else:
                    turns_frozen += 1

            # Hero attacks enemy
            if attack_timer == 50 and hero_char.health > 0: # and run_away == False:
                rand_number_special = random.randint(1, 5)
                if rand_number_special == 1:
                    special_attack = True
                else:
                    special_attack = False

                if frozen == True:
                    print("You are frozen for one move")
                else:
                    hero_char.attack(enemy_fighting, special_attack, screen)
                    damage_enemy = enemy_fighting.damage
                    if special_attack == True:
                        history_line_text.append("SPECIAL ATTACK: {} does {} damage to {}.".format(hero_char.name, damage_enemy, enemy_fighting.name))
                    else:
                        history_line_text.append("{} does {} damage to {}.".format(hero_char.name, damage_enemy, enemy_fighting.name))
                    history_line_color.append(green_color)
                    history_line_text_numb = len(history_line_text) - 1
                special_attack = False
                
                

            if enemy_fighting.health <= 0:
                enemy_fighting.remove_dead_char(enemy_fighting, screen, background_image)
                hero_char.fight_status = False
                #enemy_fighting.fight_status = False
                attack_timer = 100
                #enemy_fighting.speed_x = 0
                #enemy_fighting.speed_y = 0
                coins_received = hero_char.bounty_earned(hero_char, enemy_fighting)
                history_line_text.append("{} dead. You receive {} coins".format(enemy_fighting.name, coins_received))
                history_line_text_numb = len(history_line_text) - 1
                history_line_color.append(yellow_color)
                dead_enemy_list.append(enemy_fighting)
                enemy_char.remove(enemy_fighting)

            # Enemy attacks hero
            elif attack_timer == 0 and enemy_fighting.health > 0:
                attack_timer = 100
                rand_number_special = random.randint(1, 5)
                frozen = False
                if rand_number_special == 1:
                    special_attack = True
                    if enemy_fighting.name == "Wizard":
                        frozen = True
                        turns_frozen = 0
                else:
                    special_attack = False
                enemy_fighting.attack(hero_char, special_attack, screen)
                special_attack = False
                damage_hero = hero_char.damage
                if special_attack == True:
                    history_line_text.append("SPECIAL ATTACK: {} does {} damage to {}.".format(enemy_fighting.name, damage_hero, hero_char.name))
                else:
                    history_line_text.append("{} does {} damage to {}.".format(enemy_fighting.name, damage_hero, hero_char.name))
                history_line_text_numb = len(history_line_text) - 1
                history_line_color.append(red_color)
            if run_away == True:
                hero_char.fight_status = False
                run_away = False
                enemy_fighting.speed_x = 1
                enemy_fighting.speed_y = 1
            attack_timer -= 1

            # change health bar
            hero_char.health_bar()
            enemy_fighting.health_bar()

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
            enemy.walking(game_screen_width, game_screen_height, rand_numb)

        for enemy in enemy_char:
            # Hovering over enemy
            if Options().character_options(enemy, current_mouse_location) == "Attack":
                mouse_over = "Attack {}. (Power: {}   Defense: {}   Health: {})".format(enemy.name, enemy.power, enemy.defense, enemy.max_health)
                break
            # Hovering over Healing Potion    
            elif current_mouse_location[0] >= 517 and current_mouse_location[0] <= 544 and current_mouse_location[1] >=240 and current_mouse_location[1] <= 270:
                if hero_char.items["Healing_Potion"] == 0:
                    mouse_over = "Out of healing potions. Go to store to buy"
                else:
                    mouse_over = "Click to drink healing potion"
            else:
                mouse_over = ""

        for dead_enemy in dead_enemy_list:
            dead_enemy.respawn_timer += 1
            if dead_enemy.respawn_timer >= dead_enemy.respawn_time:
                dead_enemy.respawn_timer = 0
                print(dead_enemy)
                dead_enemy.health = dead_enemy.max_health
                dead_enemy.health_bar_numb = 20
                dead_enemy.speed_x = 1
                dead_enemy.speed_y = 1
                enemy_char.append(dead_enemy)
                dead_enemy_list.remove(dead_enemy)

        # Draw background
        screen.fill(grey_color)

        # Game display

        # loads background based on level
        if level == 1 and level_change == True:
            enemy_char = Level1().enemy_char
            background_image = Level1().background_image
            level_change = False
        elif level == 2 and level_change == True:
            enemy_char = Level2().enemy_char
            background_image = Level2().background_image
            level_change = False
        elif level == 0 and level_change == True:
            enemy_char = Store().enemy_char
            background_image = Store().background_image
            level_change = False

        screen.blit(dark_background_image, (0, 0))
        screen.blit(background_image, (0, 20))
        screen.blit(hero_image, (hero_char.x, hero_char.y))
        screen.blit(health_bar_image[hero_char.health_bar_numb], (hero_char.x + 2, hero_char.y - 10))
        screen.blit(scroll_up, (430, 545))
        screen.blit(scroll_down, (430, 585))
        
        font = pygame.font.Font(None, 25)
        headingfont = pygame.font.Font(None, 34)

        if level == 0:
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

        if level == 0.1:
            #Upgrade level selection
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
        mouse_over_text = font.render("{}".format(mouse_over), True, red_color)
        screen.blit(mouse_over_text, (0, 0))

        font = pygame.font.Font(None, 22)
        hero_stats_text = headingfont.render("Hero Stats:", True, grey_color)
        screen.blit(hero_stats_text, (515, 4))
        hero_stats_text = font.render("Health: {} / {}".format(hero_char.health, hero_char.max_health), True, red_color)
        screen.blit(hero_stats_text, (548, 40))
        screen.blit(health_image, (515, 32))
        hero_stats_text =  font.render("Power: {}".format(hero_char.power), True, green_color)
        screen.blit(hero_stats_text, (548, 80))
        screen.blit(power_image, (515, 70))
        hero_stats_text =  font.render("Defense: {}".format(hero_char.defense), True, blue_color)
        screen.blit(hero_stats_text, (548, 120))
        screen.blit(defense_image, (515, 110))

        hero_inv_text = headingfont.render("Inventory:", True, grey_color)
        screen.blit(hero_inv_text, (515, 170))
        hero_inv_text = font.render("Coins: {}".format(hero_char.coins), True, yellow_color)
        screen.blit(hero_inv_text, (548, 210))
        screen.blit(coin_image, (515, 200))
        hero_inv_text = font.render("Healing Potion: {}".format(hero_char.items["Healing_Potion"]), True, red_color)
        screen.blit(hero_inv_text, (548, 250))
        screen.blit(healing_potion, (515, 240))

        hero_inv_text = headingfont.render("Equipment:", True, grey_color)
        screen.blit(hero_inv_text, (515, 300))
        hero_inv_text = font.render("Sword: {}".format(hero_char.items["Sword"]), True, green_color)
        screen.blit(hero_inv_text, (548, 340))
        hero_inv_text = font.render("Helmet: {}".format(hero_char.items["Helmet"]), True, blue_color)
        screen.blit(hero_inv_text, (548, 380))
        hero_inv_text = font.render("Shield: {}".format(hero_char.items["Shield"]), True, blue_color)
        screen.blit(hero_inv_text, (548, 420))
        hero_inv_text = font.render("Chainmail: {}".format(hero_char.items["Chainmail"]), True, blue_color)
        screen.blit(hero_inv_text, (548, 460))
        hero_inv_text = font.render("Zombie_Axe: {}".format(hero_char.items["Zombie_Axe"]), True, blue_color)
        screen.blit(hero_inv_text, (548, 500))
        hero_inv_text = font.render("Dragon_Fire_Shield: {}".format(hero_char.items["Dragon_Fire_Shield"]), True, blue_color)
        screen.blit(hero_inv_text, (548, 540))
        
        screen.blit(font.render("History:", True, grey_color), (10, 500))
        screen.blit(font.render("-" * 85, True, grey_color), (4, 510))
    
        font_history_box = pygame.font.Font(None, 20)

        screen.blit(font.render(history_line_text[history_line_text_numb - 5], True, history_line_color[history_line_text_numb - 5]), (20, 530))
        screen.blit(font.render(history_line_text[history_line_text_numb - 4], True, history_line_color[history_line_text_numb - 4]), (20, 550))
        screen.blit(font.render(history_line_text[history_line_text_numb - 3], True, history_line_color[history_line_text_numb - 3]), (20, 570))
        screen.blit(font.render(history_line_text[history_line_text_numb - 2], True, history_line_color[history_line_text_numb - 2]), (20, 590))
        screen.blit(font.render(history_line_text[history_line_text_numb - 1], True, history_line_color[history_line_text_numb - 1]), (20, 610))
        screen.blit(font.render(history_line_text[history_line_text_numb], True, history_line_color[history_line_text_numb]), (20, 630))
        

        if hero_char.fight_status == True:
            if damage_hero == 0:
                damage_color = blue_color
            else:
                damage_color = red_color
            
            font = pygame.font.Font(None, 25)
            damage_text = font.render("{}".format(damage_hero), True, damage_color)
            screen.blit(damage_text, (hero_char.x + 8, hero_char.y - 30))

        #for enemy in enemy_char:
        if enemy_fighting.fight_status == True:
            if damage_enemy == 0:
                damage_color = blue_color
            else:
                damage_color = red_color
            
            font = pygame.font.Font(None, 25)
            damage_text = font.render("{}".format(damage_enemy), True, damage_color)
            screen.blit(damage_text, (enemy_fighting.x + 8, enemy_fighting.y - 30))
            screen.blit(health_bar_image[enemy_fighting.health_bar_numb], (enemy_fighting.x + 2, enemy_fighting.y - 10))

        for enemy in enemy_char:
            if enemy.health > 0:
                
                screen.blit(enemy.char_image, (enemy.x, enemy.y))


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
