def build_facility_report(arboretum):
    count = 0
    animal_list = []

    for river in arboretum.rivers:
        print(f'River [{str(river.id)[0:8]}]')
        for animal in river.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    for swamp in arboretum.swamps:
        print(f'Swamp [{str(swamp.id)[0:8]}]')
        for animal in swamp.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    for mountain in arboretum.mountains:
        print(f'Mountain [{str(mountain.id)[0:8]}]')
        for animal in mountain.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    for grassland in arboretum.grasslands:
        print(f'Grassland [{str(grassland.id)[0:8]}]')
        for animal in grassland.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    for coastline in arboretum.coastlines:
        print(f'Coastline [{str(coastline.id)[0:8]}]')
        for animal in coastline.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    for forest in arboretum.forests:
        print(f'Forest [{str(forest.id)[0:8]}]')
        for animal in forest.animals:
            animal_list.append(animal)
            count += 1
            print(f'{count}. {animal.species} [{str(animal.id)[0:8]}]')

    input("\n\nPress any key to continue...")