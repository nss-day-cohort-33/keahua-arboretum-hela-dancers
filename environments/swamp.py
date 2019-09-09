# FIXME:  Delete these commented lines later
# from .biome import Biome
# from animals import RiverDolphin
# from organism_type import Stagnant
# import sys
# from .habitat import ContainsAnimals
# from .habitat import ContainsPlants
# sys.path.append('../')

from organism_type import Aquatic
from organism_type import Identifiable
from .habitat import ContainsAnimals
from .habitat import ContainsPlants
from animals import RiverDolphin
from .biome import Biome

# FIXME:  Remove the following when other code works
# class Swamp():

#     def __init__(self, name):
#         self.name = name
#         self.inhabitants = []

#     def animal_count(self):
#         return "This place has a bunch of animals in it"

#     def addInhabitant(self, item):
#         if not isinstance(item, Stagnant):
#             raise TypeError(f"{item} is not of type Stagnant")
#         self.inhabitants.append(item)

#     def __str__(self):
#         return self.name


class Swamp(Biome, ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name, max_animals, max_plants):
        Biome.__init__(self, name, max_animals, max_plants)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_plant(self, plant):
        self.plants.append(plant)
