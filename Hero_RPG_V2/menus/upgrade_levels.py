class Upgrade_Levels(object):
    def upgrades(self, hero):
        from menus.main_menu import Menu
        from characters.hero import Hero
        
        raw_input = 0
        while raw_input != 9:
            power_price_increase = round(((hero.upgrades["Power_Level"] + 1) * (hero.upgrades["Power_Level"] + 1) + 20) * 2.3)
            defense_price_increase = round(((hero.upgrades["Defense_Level"] + 1) * (hero.upgrades["Defense_Level"] + 1) + 20) * 2.3)
            health_price_increase = round(((hero.upgrades["Health_Level"] + 1) * (hero.upgrades["Health_Level"] + 1) + 20) * 2.3)
            upgrade_price = {
                "Power_Level": power_price_increase,
                "Defense_Level": defense_price_increase,
                "Health_Level" : health_price_increase,
            }

            print("\033[3;30;47m==================== ")
            print("    Upgrade Levels   ")
            print("==================== \033[0;37;40m")
            Hero().hero_status(hero)
            print("\033[1;30;40m1. +1 Power Level ({} coins)".format(upgrade_price["Power_Level"]))
            print("2. +1 Defense Level ({} coins)".format(upgrade_price["Defense_Level"]))
            print("3. +1 Health Level ({} coins)".format(upgrade_price["Health_Level"]))
            print("9. Back to main menu")
            print("\033[1;36;40m> ", end=' ')
            raw_input = input()
            print("\033[0;37;40m")
            if raw_input == "1":
                upgrade_type = "Power_Level"
            elif raw_input == "2":
                upgrade_type = "Defense_Level"
            elif raw_input == "3":
                upgrade_type = "Health_Level"
            elif raw_input == "9":
                print("Back to Main Menu")
                Menu().main_menu(hero)
            else:
                print("Invalid input {}".format(raw_input))
                Upgrade_Levels().upgrades(hero)
            if hero.coins < upgrade_price[upgrade_type]:
                    print("Not enough coins")
            else:
                hero.coins -= upgrade_price[upgrade_type]
                hero.upgrades[upgrade_type] += 1
                hero.upgrade_hero_levels(hero, upgrade_type)
