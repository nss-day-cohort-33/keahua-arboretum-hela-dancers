import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Forest
from environments import Mountain

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("\nChoose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    elif choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    elif choice == "3":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
    elif choice == "4":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    elif choice == "5":
        forest = Forest()
        arboretum.forests.append(forest)
    elif choice == "6":
        mountain = Mountain()
        arboretum.mountains.append(mountain)

    else:
        input("\nThat was a bad input, try again next time, fool! \nPress any key to return to the menu...")
        return