from menus.battle_menu import Battle_Menu
from menus.about_characters import About_Characters
from menus.store import Store
from menus.upgrade_levels import Upgrade_Levels

class Menu(object):
    def main_menu(self, hero):
        from characters.hero import Hero
        
        battle_menu_engine = Battle_Menu()
        about_characters_engine = About_Characters()
        store_engine = Store()
        upgrade_levels_engine = Upgrade_Levels()

        print("\033[3;30;47m==============")
        print("  MAIN MENU   ")
        print("==============\033[0;37;40m")
        Hero().hero_status(hero)
        print("\033[1;30;40m1. Duel Arena", " " * 7)
        print("2. Store"," " * 12)
        print("3. Upgrade Levels", " " * 3)
        print("4. About Characters", " " * 1)
        print("5. Quit", " " * 13)
        print("\033[1;36;40m> ", end=' ')
        raw_input = input()
        print("\033[0;37;40m")
        if raw_input == "1":
            battle_menu_engine.menu_selection(hero) # Go to battle menu
        elif raw_input == "2":
            store_engine.shopping(hero)
        elif raw_input == "3":
            upgrade_levels_engine.upgrades(hero)
        elif raw_input == "4":
            about_characters_engine.character_description(hero)
        elif raw_input == "5":
            print("Goodbye.")
            quit(1)
        else:
            print("Invalid input {}".format(raw_input))
            Menu().main_menu(hero)