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
from organism_type import Forestful
from organism_type import Mountainful
from organism_type import Grassful


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

    choice = input("\nChoose animal to release > ")

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

    if isinstance(animal, Freshwater):
        for eachitem in arboretum.rivers:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Stagnant):
        for eachitem in arboretum.swamps:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Saltwater):
        for eachitem in arboretum.coastlines:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Forestful):
        for eachitem in arboretum.forests:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Mountainful):
        for eachitem in arboretum.mountains:
            compatible_biomes.append(eachitem)

    if isinstance(animal, Grassful):
        for eachitem in arboretum.grasslands:
            compatible_biomes.append(eachitem)

    for index, biome in enumerate(compatible_biomes):
        print(f'{index + 1}. {biome.name} ({len(biome.animals)} animals)')

    def add_animal(choice):
        if choice == "":
            input("Press any key to return to the menu...")
        try:
            if choice != "" and int(choice) <= len(compatible_biomes) and compatible_biomes[int(choice) - 1].exceed_max(animal) == False:
                print("****   That biome is not large enough   ****")
                print("****     Please choose another one      ****")
                for index, biome in enumerate(compatible_biomes):
                    print(
                        f'{index + 1}. {biome.name} ({len(biome.animals)} animals)')

                choice = input("Cultivate the animal into which biome? >")
                add_animal(choice)
            else:
                input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
                return
        except ValueError:
            input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
            return

    choice = input("Release the animal into which biome? >")
    add_animal(choice)

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)
