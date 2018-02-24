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
        distance = math.sqrt((math.pow((enemy.x_when_clicked + (enemy.width / 2)) - mouse_click_position[0], 2)) + (math.pow((enemy.y_when_clicked + (enemy.height / 2)) - mouse_click_position[1], 2)))
        if distance < 32:
            enemy.fight_status = True
            #print("Attack mode is on")
            return True
        else:
            return False

    def fight_mode(self, mouse_click_position, enemy):
        distance = math.sqrt((math.pow((enemy.x_when_clicked + (enemy.width / 2)) - mouse_click_position[0], 2)) + (math.pow((enemy.y_when_clicked + (enemy.height / 2)) - mouse_click_position[1], 2)))
        if distance < 32:
            return True
        else:
            return False

    def distance_from_enemy(self, hero, enemy):
        distance = math.sqrt((math.pow((enemy.x + (enemy.width)) - hero.x, 2)) + (math.pow((enemy.y + (enemy.height / 2)) - hero.y, 2)))
        if distance < 60:
            #enemy.fight_status = True
            #enemy.speed_x = 0
            #enemy.speed_y = 0
            return True
        else:
            return False
