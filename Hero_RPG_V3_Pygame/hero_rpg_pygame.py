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
from actions.options import Options

RIGHT_CLICK = 3
LEFT_CLICK = 1

#from menus.main_menu import Menu

def main():
    width = 500
    height = 520
    blue_color = (97, 159, 182)
    blue_color2 = (0, 0, 255)
    black_color = (0, 0, 0)
    red_color = (255, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    background_image = pygame.image.load("images/background.png").convert_alpha()
    hero_image = pygame.image.load("images/hero.png").convert_alpha()
    monster_image = pygame.image.load("images/monster.png").convert_alpha()
    
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

    hero_char = Hero()

    enemy_char = [Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400)), Goblin(random.randint(70, 400), random.randint(70, 400))] #, Medic(), Shadow(), Ranger(), Wizard(), Dragon(), Zombie()]
    enemy_count = len(enemy_char) - 1
    enemy_numb = 0

    change_dir_countdown = 120

    attack_timer = 100
    movement = 0
    rand_numb = random.randint(0, 8)
    rand_numb2 = [random.randint(0, 8)]
    mouse_click_position = [0, 0]
    current_mouse_position = [0, 0]
    run_away = False
    frozen = False
    enemy_health_perc = 1
    enemy_health_bar_numb = 20
    hero_health_perc = 1
    damage_enemy = ""
    damage_hero = ""
    enemy_fighting = Fake()
    loop_count = 0

    # Game initialization

    stop_game = False
    button_pressed = False

    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_pressed = event.button
                mouse_location = pygame.mouse.get_pos()
                # to get rid of tuple object
                loop_count = 0
                mouse_click_position[0] = mouse_location[0]
                mouse_click_position[1] = mouse_location[1]

                # Save enemy position at time of click
                for enemy in enemy_char:
                    enemy.x_when_clicked = enemy.x
                    enemy.y_when_clicked = enemy.y


            # To get mouse position on mouse hover
            current_mouse_location = pygame.mouse.get_pos()
            current_mouse_position[0] = current_mouse_location[0]
            current_mouse_position[1] = current_mouse_location[1]

            

            #print(current_mouse_location)
            #print(current_mouse_position[0])
            #print(current_mouse_position[1])

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        #Enemy click detection
        if button_pressed == LEFT_CLICK:
            # if enemy is clicked on
            if frozen == False:
                hero_speed = (hero_char.speed_x / (enemy_count + 1)) # prevents hero from speeding up with more characters
            else:
                hero_speed = 0
                
            for enemy in enemy_char:
                #Checks if an enemy was in the click location (currently any enemy that steps into the location passes the test)
                if Battle().attack_mode(hero_char, enemy, mouse_click_position) == True and hero_char.fight_status == False: #and loop_count < enemy_count * 5:
                    enemy_fighting = enemy
                    # Moves toward enemy
                    mouse_click_position[0] = enemy_fighting.x
                    mouse_click_position[1] = enemy_fighting.y
                    
                    #enemy.clicked = True
                    # starts attacking the enemy when hero is within range of enemy
                    if Battle().distance_from_enemy(hero_char, enemy) == True:
                        hero_char.fight_status = True
                    
                # if enemy was not clicked on
                elif hero_char.movement(hero_char, mouse_click_position) == False:
                    hero_char.fight_status = False
                    enemy.fight_status = False
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

                if hero_char.fight_status == True:
                    #mouse_click_position[0] = enemy_fighting.x
                    #mouse_click_position[1] = enemy_fighting.y

                    # Player movement toward enemy

                    if hero_char.x < enemy_fighting.x - enemy_fighting.width:
                        hero_char.x += hero_speed
                    elif hero_char.x > enemy_fighting.x + enemy_fighting.width:
                        hero_char.x -= hero_speed
                    elif hero_char.x > enemy_fighting.x - enemy_fighting.width and hero_char.x < enemy_fighting.x - enemy_fighting.width:
                        hero_char.x += hero_speed

                    if hero_char.y < enemy_fighting.y - enemy_fighting.height:
                        hero_char.y += hero_speed
                    elif hero_char.y > enemy_fighting.y + enemy_fighting.height:
                        hero_char.y -= hero_speed

        elif button_pressed == RIGHT_CLICK:
            pass


        if hero_char.fight_status == True or run_away == True:
            #print(frozen)
            #print(enemy_fighting.name)
            enemy_fighting.speed_x = 0
            enemy_fighting.speed_y = 0

            if frozen == True:
                if turns_frozen == 1 or (enemy_fighting.name == "Wizard" and enemy-fighting.health == 0):
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
                special_attack = False
                damage_enemy = enemy_fighting.damage
            
            if enemy_fighting.health <= 0:
                enemy_fighting.remove_dead_char(enemy_fighting.x, enemy_fighting.y, screen, background_image)
                hero_char.fight_status = False
                enemy_fighting.fight_status = False
                attack_timer = 100
                enemy_fighting.speed_x = 0
                enemy_fighting.speed_y = 0

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
                change_dir_countdown = 120
            else:
             change_dir_countdown = 240
        
        # enemy movement
        #for enemy in enemy_char:
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
            enemy.update(width, height, rand_numb)

        for enemy in enemy_char:
            if Options().character_options(enemy, current_mouse_location) == "Attack":
                mouse_over = "Attack {}. (Power: {}   Defense: {}   Health: {})".format(enemy.name, enemy.power, enemy.defense, enemy.max_health)
                break
                # add sword for mouse when hovering over enemy
            else:
                mouse_over = ""

        # Draw background
        screen.fill(blue_color)

        # Game display

        screen.blit(background_image, (0, 40))
        screen.blit(hero_image, (hero_char.x, hero_char.y))
        screen.blit(health_bar_image[hero_char.health_bar_numb], (hero_char.x + 2, hero_char.y - 10))
        font = pygame.font.Font(None, 25)

        hero_stats_text =  font.render("Power: {}   Defense: {}   Health: {} / {}   Coins: {}".format(hero_char.power, hero_char.defense, hero_char.health, hero_char.max_health, hero_char.coins), True, black_color)
        screen.blit(hero_stats_text, (0, 0))

        mouse_over_text = font.render("{}".format(mouse_over), True, red_color)
        screen.blit(mouse_over_text, (0, 20))


        if hero_char.fight_status == True:
            if damage_hero == 0:
                damage_color = blue_color2
            else:
                damage_color = red_color
            
            font = pygame.font.Font(None, 25)
            damage_text = font.render("{}".format(damage_hero), True, damage_color)
            screen.blit(damage_text, (hero_char.x + 8, hero_char.y - 30))

        #for enemy in enemy_char:
        if enemy_fighting.fight_status == True:
            if damage_enemy == 0:
                damage_color = blue_color2
            else:
                damage_color = red_color
            
            font = pygame.font.Font(None, 25)
            damage_text = font.render("{}".format(damage_enemy), True, damage_color)
            screen.blit(damage_text, (enemy_fighting.x + 8, enemy_fighting.y - 30))
            screen.blit(health_bar_image[enemy_fighting.health_bar_numb], (enemy_fighting.x + 2, enemy_fighting.y - 10))

        for enemy in enemy_char:
            if enemy.health > 0:
                
                screen.blit(enemy.char_image, (enemy.x, enemy.y))
                
            #if fight_mode == False:
                #screen.blit(health_bar_image[enemy.health_bar_numb], (enemy.x + 2, enemy.y - 10))


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
