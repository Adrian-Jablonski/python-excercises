from actions.death import Death
import random

class Battle(object):
    def do_battle(self, hero, enemy):
        from menus.battle_menu import Battle_Menu

        battle_menu_engine = Battle_Menu()
        print("\033[3;30;47m==================")
        print("  Hero Vs {}  ".format(enemy.name))
        print("==================\033[0;37;40m")

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