class Death(object):
    def dead(self, hero):
        from menus.main_menu import Menu
        print("You are dead \U0001F480")
        print("\033[3;30;47m================")
        print("\U0001F480  GAME OVER \U0001F480  ")
        print("================\033[0;37;40m")
        print("Play again?")
        print("\033[1;30;40m1. Yes")
        print("2. No")
        print("\033[1;36;40m> ", end=' ')
        raw_input = input()
        print("\033[0;37;40m")
        if raw_input == "1":
            #start_game()
            hero.health = hero.max_health
            if hero.coins > 20:
                lost_coins = round(hero.coins * .10)
                hero.coins -= lost_coins
            else:
                lost_coins = 0
            if hero.items["Tonic"] > 1:
                lost_tonic = round(hero.items["Tonic"] * .20)
                hero.items["Tonic"] -= lost_tonic
            else:
                lost_tonic = 0

            print("You lost {} coins and {} tonics".format(lost_coins, lost_tonic))
            Menu().main_menu(hero)
        elif raw_input == "2":
            print("Goodbye.")
            quit(1)