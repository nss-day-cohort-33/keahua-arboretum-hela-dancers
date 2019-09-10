from organism_type import Aquatic
from organism_type import Identifiable
from .habitat import ContainsAnimals
from .habitat import ContainsPlants
from animals import RiverDolphin
from .biome import Biome


class Mountain(Biome, ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name="Mountain", max_animals=4, max_plants=6):
        Biome.__init__(self, name, max_animals, max_plants)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_plant(self, plant):
        self.plants.append(plant)