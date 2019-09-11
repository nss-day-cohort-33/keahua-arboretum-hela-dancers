from animals import RiverDolphin
from animals import Pueo
from animals import Ulae
from animals import GoldGecko
from animals import NeneGoose
from animals import Kikakapu
from animals import Opeapea
from animals import HappySpider
import os

def feed_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Pueo (Owl)")
    print("3. Ulae (Lizard Fish)")
    print("4. Gold Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu (Fish)")
    print("7. Opeapea (Bat)")
    print("8. Happy Spider")

    choice = input("\nChoose animal to feed > ")

    if choice == "1":
        animal = RiverDolphin()

    elif choice == "2":
        animal = Pueo()

    elif choice == "3":
        animal = Ulae()

    elif choice == "4":
        animal = GoldGecko()

    elif choice == "5":
        animal = NeneGoose()

    elif choice == "6":
        animal = Kikakapu()

    elif choice == "7":
        animal = Opeapea()

    elif choice == "8":
        animal = HappySpider()

    else:
        input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
        return

    food_list = list(animal.food)

    for index, food in enumerate(food_list):
        print(f'{index + 1}. {food}')

    print("Feed the animal what?")
    choice = input("> ")

    try:
        if int(choice) - 1 > len(food_list):
            input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
            return
    except ValueError:
        input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
        return

    print(f'The {animal.species} ate a {food_list[int(choice) - 1]} for a meal')
    choice = input("> ")