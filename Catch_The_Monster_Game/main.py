import pygame
import random
import math

from characters.characters import *

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER_BUTTON = 13

def main():
    width = 512
    height = 500
    dead_monster = False
    dead_hero = False
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    pygame.mixer.init()
    win_sound = pygame.mixer.Sound("sounds/win.wav")
    loss_sound = pygame.mixer.Sound("sounds/lose.wav")
    background_music = pygame.mixer.Sound("sounds/music.wav")

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    background_image = pygame.image.load("images/background.png").convert_alpha()
    hero_image = pygame.image.load("images/hero.png").convert_alpha()
    monster_image = pygame.image.load("images/monster.png").convert_alpha()
    goblin_image = pygame.image.load("images/goblin.png").convert_alpha()

    hero_char = Hero()
    monster_char = Monster()
    level = 1
    lives = 3
    high_score = 1
    goblin_char = [Goblin(), Goblin(), Goblin()]
    goblin_count = len(goblin_char) - 1
    goblin_numb = 0

    change_dir_countdown = 120
    rand_numb = random.randint(0, 7)
    rand_numb2 = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]

    # Game initialization

    stop_game = False
    key_pressed = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            
            if event.type == pygame.KEYDOWN:
                key_pressed =  event.key
            elif event.type == pygame.KEYUP:
                key_pressed = False
            
            if event.type == pygame.QUIT:
                stop_game = True

        # ---- Game logic ----
        
        #Character movement
        if key_pressed == KEY_UP:
            if hero_char.y > 30:   
                hero_char.y -= hero_char.speed_y
        elif key_pressed == KEY_DOWN:
            if hero_char.y < (height - 65):
                hero_char.y += hero_char.speed_y
        elif key_pressed == KEY_LEFT:
            if hero_char.x > 30:
                hero_char.x -= hero_char.speed_x
        elif key_pressed == KEY_RIGHT:
            if hero_char.x < (width - 60):
                hero_char.x += hero_char.speed_x

        # Press enter to restart
        if key_pressed == ENTER_BUTTON and (dead_monster == True or dead_hero == True):
            if dead_monster == True:
                monster_char.x = random.randint(31, width - 30)
                monster_char.y = random.randint(31, width - 30)
                level += 1
                if level - 1 > high_score:
                    high_score = level - 1
            elif dead_hero == True:
                hero_char.x = 0
                hero_char.y = random.randint(31, width - 60)
                lives -= 1
                if lives == 0:
                    goblin_char = [Goblin(), Goblin(), Goblin()]
                    rand_numb2 = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]
                    goblin_count = len(goblin_char) - 1
                    level = 1
                    lives = 3
            background_music.stop()
            monster_char.speed_x = 5
            monster_char.speed_y = 5
            hero_char.speed_x = 4
            hero_char.speed_y = 4

            if goblin_count - 1 < level:
                # adds extra goblin to screen for each level
                rand_numb2.append(random.randint(0, 7))
                goblin_char.append(Goblin())
                goblin_count = len(goblin_char) - 1
                screen.blit(goblin_image, (goblin_char[goblin_count].x, goblin_char[goblin_count].y))

            for goblin in goblin_char:
                goblin_char[goblin_numb].speed_x = 2
                goblin_char[goblin_numb].speed_y = 2
                goblin_numb += 1
                if goblin_numb > goblin_count:
                    goblin_numb = 0
            dead_monster = False
            dead_hero = False
        
        # Monster movement
        
        if dead_hero == False and dead_monster == False:
            background_music.play()

        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            rand_numb = random.randint(0, 7)
        monster_char.update(width, height, rand_numb)

        # Goblin movement
        for goblin in goblin_char:
            if change_dir_countdown == 60:
                rand_numb2[goblin_numb] = random.randint(0, 7)
            goblin_char[goblin_numb].update(width, height, rand_numb2[goblin_numb])
            goblin_numb += 1
            if goblin_numb > goblin_count:
                goblin_numb = 0

        # Monster collission check
        if hero_char.collission(hero_char, monster_char):
            for goblin in goblin_char:
                goblin_char[goblin_numb].speed_x = 0
                goblin_char[goblin_numb].speed_y = 0
                goblin_numb += 1
                if goblin_numb > goblin_count:
                    goblin_numb = 0
                monster_char.dead(monster_char.x, monster_char.y, screen, background_image, win_sound, background_music)
            dead_monster = True

        # Goblin collission check
        for goblin in goblin_char:
            goblin_numb += 1
            if goblin_numb > goblin_count:
                goblin_numb = 0
            if hero_char.collission(hero_char, goblin_char[goblin_numb]):
                monster_char.speed_x = 0
                monster_char.speed_y = 0
                for goblin in goblin_char:
                    goblin_char[goblin_numb].speed_x = 0
                    goblin_char[goblin_numb].speed_y = 0
                    goblin_numb += 1
                    if goblin_numb > goblin_count:
                        goblin_numb = 0
                goblin_char[goblin_numb].dead(hero_char.x, hero_char.y, screen, background_image, loss_sound, background_music)
                dead_hero = True

        # Draw background
        screen.fill(blue_color)
        
        # Game display

        screen.blit(background_image, (0, 20))
        if dead_hero == False:
            screen.blit(hero_image, (hero_char.x, hero_char.y))
        else: 
            font = pygame.font.Font(None, 25)
            if lives == 0:
                text = font.render("Game Over! Hit ENTER to play again!", True, black_color)
            else:
                text = font.render("{} lives left. Hit ENTER to start over!".format(lives - 1), True, black_color)
            screen.blit(text, (160, 230))
        if dead_monster == False:
            screen.blit(monster_image, (monster_char.x, monster_char.y))
        else:
            font = pygame.font.Font(None, 25)
            text = font.render("You win! Hit ENTER to start level {}!".format(level + 1), True, black_color)
            screen.blit(text, (160, 230))

        for goblin in goblin_char:
            screen.blit(goblin_image, (goblin_char[goblin_numb].x, goblin_char[goblin_numb].y))
            goblin_numb += 1
            if goblin_numb > goblin_count:
                goblin_numb = 0
            
        font = pygame.font.Font(None, 30)
        level_text = font.render("Level: {}      Lives: {}      High Score: {}".format(level, lives, high_score), True, black_color)
        screen.blit(level_text, (0, 0))
        
        pygame.display.update()
        clock.tick(60)
        

    pygame.quit()

if __name__ == '__main__':
    main()