from actions.death import Death
import random
import math

class Battle(object):
    def do_battle(self, hero, enemy):
        from menus.battle_menu import Battle_Menu
        # Delete this once set in main code. Can't move to class because the timer does not work properly
        frozen = False

        while enemy.alive() and hero.alive():
            hero.print_status()
            enemy.print_status()
            print("What do you want to do?")
            print("\033[1;30;40m1. Attack {}".format(enemy.name))
            print("2. Drink Tonic ({} in inventory)".format(hero.items["Tonic"]))
            print("3. Run away")
            print("\033[1;36;40m> ", end=' ')
            raw_input = input()
            print("\033[0;37;40m")

            if frozen == True:
                print("\033[1;37;44mYOU ARE FROZEN AND CAN'T MOVE\033[0;37;40m")
            elif raw_input == "1":
                if enemy.name == "Shadow":
                    randNumb = random.randint(1, 10)
                else:
                    randNumb = random.randint(1, 5)
                if randNumb == 1:
                    special_attack = True
                else:
                    special_attack = False
                hero.attack(enemy, special_attack)
                special_attack = False
                if enemy.health <= 0 and enemy.name != "Zombie":
                    print("The enemy is dead \U0001F480")
                    hero.bounty_earned(hero, enemy)
                    battle_menu_engine.menu_selection(hero)
                elif enemy.health == 0 and enemy.name == "Zombie" and hero.items["Zombie_Axe"] != 0:
                    print("You chopped the Zombie's head off")
                    print("The enemy is dead \U0001F480")
                    hero.bounty_earned(hero, enemy)
                    battle_menu_engine.menu_selection(hero)
            elif raw_input == "2":
                if hero.items["Tonic"] > 0:
                    hero.restore_health(hero)
                else:
                    print("No tonic in inventory")
            elif raw_input == "3":
                pass
            else:
                print("Invalid input {}".format(raw_input))
                Battle().do_battle(hero, enemy)
            if enemy.alive and hero.health > 0:
                # enemy attacks hero
                frozen = False
                if enemy.name == "Dragon":
                    randNumb = random.randint(1, 3)
                else:
                    randNumb = random.randint(1, 5)
                if randNumb == 1:
                    special_attack = True
                    if enemy.name == "Wizard":
                        frozen = True
                else:
                    special_attack = False
                enemy.attack(hero, special_attack)
                special_attack = False
        
            if raw_input == "3" and frozen == False:
                battle_menu_engine.menu_selection(hero)

            if hero.health <= 0:
                hero.print_status()
                enemy.print_status()
                Death().dead(hero)

    def attack_mode(self, hero, enemy, mouse_click_position):
        # distance = math.sqrt((math.pow((enemy.x_y_when_clicked[0]) - mouse_click_position[0], 2)) + (math.pow((enemy.x_y_when_clicked[1]) - mouse_click_position[1], 2)))
        # if distance < enemy.height:
        enemy_box_x_range = [enemy.x_y_when_clicked[0], enemy.x_y_when_clicked[0] + enemy.width]
        enemy_box_y_range = [enemy.x_y_when_clicked[1], enemy.x_y_when_clicked[1] + enemy.height]
        if mouse_click_position[0] >= enemy_box_x_range[0] and mouse_click_position[0] <= enemy_box_x_range[1] and mouse_click_position[1] >= enemy_box_y_range[0] and mouse_click_position[1] <= enemy_box_y_range[1]:
            enemy.fight_status = True
            return True
        else:
            return False


    def distance_from_enemy(self, hero, enemy):
        # distance = math.sqrt((math.pow(enemy.x_y[0] - hero.x_y[0], 2)) + (math.pow(enemy.x_y[1] - hero.x_y[1], 2)))
        # if distance < 70:
        enemy_box_x_range = [enemy.x_y[0], enemy.x_y[0] + enemy.width]
        enemy_box_y_range = [enemy.x_y[1], enemy.x_y[1] + enemy.height]
        if hero.x_y[0] + (enemy.width) >= enemy_box_x_range[0] and hero.x_y[0] - (enemy.width) <= enemy_box_x_range[1] and hero.x_y[1] + (enemy.height) >= enemy_box_y_range[0] and hero.x_y[1] - (enemy.height) <= enemy_box_y_range[1]:
            enemy.fight_status = True
            return True
        else:
            return False

    def attack_range(self, char1, char2):
        if abs(char1.x_y[0] - char2.x_y[0]) <= char1.attack_range and abs(char1.x_y[1] - char2.x_y[1]) <= char1.attack_range:
            return True
        else:
            return False
