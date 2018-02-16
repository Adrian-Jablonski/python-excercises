import random
import time

from characters.hero import Hero
from menus.main_menu import Menu


if __name__ == "__main__":
    hero = Hero()
    main_menu_engine = Menu()
    main_menu_engine.main_menu(hero)    # Starts game at main menu

