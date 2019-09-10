from animals import RiverDolphin
from animals import Pueo
from animals import Ulae
from animals import GoldGecko
from animals import NeneGoose
from animals import Kikakapu
from animals import Opeapea
from animals import HappySpider

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

    choice = input("Choose animal to feed > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        animal = Pueo()

    if choice == "3":
        animal = Ulae()

    if choice == "4":
        animal = GoldGecko()

    if choice == "5":
        animal = NeneGoose()

    if choice == "6":
        animal = Kikakapu()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = HappySpider()

    food_list = list(animal.food)

    for index, food in enumerate(food_list):
        print(f'{index + 1}. {food}')

    print("Feed the animal what?")
    choice = input("> ")

    print(f'The {animal.species} ate a {food_list[int(choice) - 1]} for a meal')
    choice = input("> ")