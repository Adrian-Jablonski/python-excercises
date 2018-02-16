from actions.battle import Battle
from characters.enemies import *

class Battle_Menu(object):
    def menu_selection(self, hero):
        from menus.main_menu import Menu
        from characters.hero import Hero
        battle_engine = Battle()
        main_menu_engine = Menu()

        print("\033[3;30;47m============== ")
        print("  DUEL ARENA   ")
        print("============== \033[0;37;40m")
        Hero().hero_status(hero)
        print("Choose your opponent ")
        print("\033[1;30;40m1. Goblin            ") 
        print("2. Medic             ")
        print("3. Shadow            ")
        print("4. Wizard            ")
        print("5. Ranger            ")
        print("6. Zombie            ")
        print("7. Dragon            ")
        print("                     ")
        print("9. Drink Tonic ({})   ".format(hero.items["Tonic"]))
        print("0. Back to Main Menu ")
        print("\033[1;36;40m> ", end=' ')
        raw_input = input()
        print("\033[0;37;40m")
        if raw_input == "1":
            enemy = Goblin()
        elif raw_input == "2":
            enemy = Medic()
        elif raw_input == "3":
            enemy = Shadow()
        elif raw_input == "4":
            enemy = Wizard()
        elif raw_input == "5":
            enemy = Ranger()
        elif raw_input == "6":
            enemy = Zombie()
        elif raw_input == "7":
            enemy = Dragon()
        elif raw_input == "9":
            if hero.items["Tonic"] > 0:
                hero.restore_health(hero)
            else:
                print("No tonic in inventory")
            Battle_Menu().menu_selection(hero)
        elif raw_input == "0":
            main_menu_engine.main_menu(hero)
        else:
            print("Invalid input {}".format(raw_input))
            Battle_Menu().menu_selection(hero)  
        battle_engine.do_battle(hero, enemy) # go to battle