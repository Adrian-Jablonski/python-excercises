class Store(object):

    def shopping(self, hero):
        from menus.main_menu import Menu 
        from characters.hero import Hero
        price_list = {
            "Tonic": 8, 
            "Helmet": 150, 
            "Sword": 200, 
            "Shield": 225,
            "Chainmail": 750,
            "Zombie_Axe": 2000,
            "Dragon_Fire_Shield": 5000,
        }
        raw_input = 0
        while raw_input != 9:
            print("\033[3;30;47m===============")
            print("     Store     ")
            print("===============\033[0;37;40m")
            Hero().hero_status(hero)
            print("\033[1;34;40mInventory - \033[1;36;40mTonic: {} \U0001F943 \033[0;37;40m  ".format(hero.items["Tonic"]))
            print("\033[1;34;40mEquipment - \033[1;36;40mHelmet: {} Sword: {}".format(hero.items["Helmet"], hero.items["Sword"]))
            print(" Shield: {} Chainmail: {} ".format(hero.items["Shield"], hero.items["Chainmail"]))
            print(" Zombie Axe: {} ".format(hero.items["Zombie_Axe"]))
            print(" Dragon Fire Shield: {} \033[0;37;40m  ".format(hero.items["Dragon_Fire_Shield"]))
            print("What do you want to buy? ")
            print("\033[1;30;40m1. Tonic ({} coins)".format(price_list["Tonic"]))
            print("2. Helmet ({} coins)".format(price_list["Helmet"]))
            print("3. Sword ({} coins)".format(price_list["Sword"]))
            print("4. Shield ({} coins)".format(price_list["Shield"]))
            print("5. Chainmail ({} coins)".format(price_list["Chainmail"]))
            print("6. Zombie Axe ({} coins)".format(price_list["Zombie_Axe"]))
            print("7. Dragon Fire Shield ({} coins)".format(price_list["Dragon_Fire_Shield"]))
            print("9. Back to main menu")
            print("\033[1;36;40m> ", end=' ')
            raw_input = input()
            print("\033[0;37;40m")
            if raw_input == "1":
                item = "Tonic"
            elif raw_input == "2":
                item = "Helmet"
            elif raw_input == "3":
                item = "Sword"
            elif raw_input == "4":
                item = "Shield"
            elif raw_input == "5":
                item = "Chainmail"
            elif raw_input == "6":
                item = "Zombie_Axe"
            elif raw_input == "7":
                item = "Dragon_Fire_Shield"
            elif raw_input == "9":
                print("Back to Main Menu")
                Menu().main_menu(hero)
            else:
                print("Invalid input {}".format(raw_input))
                Store().shopping(hero)
            if hero.coins < price_list[item]:
                    print("Not enough coins")
            elif hero.items[item] == 1 and item != "Tonic":
                print("Already own", item)
            else:
                hero.coins -= price_list[item]
                hero.items[item] += 1
                hero.equip_items(hero, item)