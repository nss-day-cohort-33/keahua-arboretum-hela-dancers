from animals import RiverDolphin
from animals import Pueo
from animals import Ulae
from animals import GoldGecko
from animals import NeneGoose
from animals import Kikakapu
from animals import Opeapea
from animals import HappySpider
from organism_type import Freshwater
from organism_type import Stagnant
from organism_type import Saltwater


def release_animal(arboretum):
    compatible_biomes = []
    animal = None

    print("1. River Dolphin")
    print("2. Pueo (Owl)")
    print("3. Ulae (Lizard Fish)")
    print("4. Gold Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu (Fish)")
    print("7. Opeapea (Bat)")
    print("8. Happy Spider")

    choice = input("Choose animal to release > ")

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

    if isinstance(animal, Freshwater):
        for eachitem in arboretum.rivers:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Stagnant):
        for eachitem in arboretum.swamps:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Saltwater):
        for eachitem in arboretum.coastlines:
            compatible_biomes.append(eachitem)

    for index, biome in enumerate(compatible_biomes):
        print(f'{index + 1}. {biome.name} ({len(biome.animals)} animals)')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)
