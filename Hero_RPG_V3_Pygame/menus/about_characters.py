from characters.enemies import *

class About_Characters(object):
    def character_description(self, hero):
        from menus.main_menu import Menu
        from characters.hero import Hero

#\u2694\uFE0F  \033[1;36;40mDefense: {}\U0001F6E1  \033[1;31;40mHealth: {}/{} \u2764\uFE0F  \033[0;37;40m".format(hero.power, hero.defense, hero.health, hero.max_health))
        print("\033[3;30;47m======================")
        print("CHARACTER DESCRIPTIONS")
        print("======================\033[0;37;40m")
        print("\033[1;34;40mName:  \033[1;32;40m\u2694\uFE0F Power \033[1;36;40m\U0001F6E1 Defense \033[1;31;40m\u2764\uFE0F Health         \n  \033[1;34;40m-Special Ability/ Probability\033[0;37;40m")
        print("_________________________________________________")
        print("\033[1;34;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;34;40m- {}\033[0;37;40m".format(Hero().name, Hero().power, Hero().defense, Hero().health, Hero().special_desc))
        print("\033[1;35;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;35;40m- {}\033[0;37;40m".format(Goblin().name, Goblin().power, Goblin().defense, Goblin().health, Goblin().special_desc))
        print("\033[1;34;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;34;40m- {}\033[0;37;40m".format(Medic().name, Medic().power, Medic().defense, Medic().health, Medic().special_desc))
        print("\033[1;35;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;35;40m- {}\033[0;37;40m".format(Shadow().name, Shadow().power, Shadow().defense, Shadow().health, Shadow().special_desc))
        print("\033[1;34;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;34;40m- {}\033[0;37;40m".format(Wizard().name, Wizard().power, Wizard().defense, Wizard().health, Wizard().special_desc))
        print("\033[1;35;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;35;40m- {}\033[0;37;40m".format(Ranger().name, Ranger().power, Ranger().defense, Ranger().health, Ranger().special_desc))
        print("\033[1;34;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;34;40m- {}\033[0;37;40m".format(Zombie().name, Zombie().power, Zombie().defense, Zombie().health, Zombie().special_desc))
        print("\033[1;35;40m{}:  \033[1;32;40m\u2694\uFE0F P: {} \033[1;36;40m\U0001F6E1 D: {} \033[1;31;40m\u2764\uFE0F H: {}         \n \033[1;35;40m- {}\033[0;37;40m".format(Dragon().name, Dragon().power, Dragon().defense, Dragon().health, Dragon().special_desc))
        print("\n Press 1 to return to Main Menu")
        print("\033[1;36;40m> ", end=' ')
        raw_input = input()
        print("\033[0;37;40m")
        if raw_input == "1":
            Menu().main_menu(hero)
        else: 
            About_Characters().character_description(hero)
