from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree
from plants import Rainbow_Eucalyptus_Tree
from plants import Silversword

from organism_type import Clay_Soil
from organism_type import Loamy_Soil
from organism_type import Marsh_Soil
from organism_type import Silt_Soil

def cultivate_plant(arboretum):
    compatible_biomes = []
    plant = None

    print("1. Rainbow Eucalyptus Tree")
    print("2. Silversword")
    print("3. Mountain Apple Tree")
    print("4. Blue Jade Vine")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Rainbow_Eucalyptus_Tree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = Mountain_Apple_Tree()

    if choice == "4":
        plant = Blue_Jade_Vine()

    if isinstance(plant, Clay_Soil):
        for plant_in_list in arboretum.mountains:
            compatible_biomes.append(plant_in_list)


    if isinstance(plant, Loamy_Soil):
        for plant_in_list in arboretum.forest:
            compatible_biomes.append(plant_in_list)

    if isinstance(plant, Marsh_Soil):
        for plant_in_list in arboretum.swamps:
            compatible_biomes.append(plant_in_list)

    if isinstance(plant, Silt_Soil):
        for plant_in_list in arboretum.grasslands:
            compatible_biomes.append(plant_in_list)

    for index, biome in enumerate(compatible_biomes):
        print(f'{index + 1}. {biome.name} ({len(biome.plants)} plants)')

    def add_plant(choice):
            if choice == "":
                choice = input("")
            if choice != "" and compatible_biomes[int(choice) - 1].exceed_max(plant) == False:
                print("****   That biome is not large enough   ****")
                print("****     Please choose another one      ****")
                for index, biome in enumerate(compatible_biomes):
                    print(f'{index + 1}. {biome.name} ({len(biome.plants)} plants)')

                choice = input("Cultivate the plant into which biome? >")
                add_plant(choice)
    choice = input("Cultivate the plant into which biome? >")
    add_plant(choice)
