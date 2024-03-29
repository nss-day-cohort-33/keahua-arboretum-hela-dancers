from .habitat import ContainsAnimals
from .habitat import ContainsPlants


class Biome:

    def __init__(self, name, max_animals, max_plants):
        self.name = name
        self.max_animals = max_animals
        self.max_plants = max_plants

    def exceed_max(self, what_organism):
        try:
            if what_organism.food != "":
                if len(self.animals) < self.max_animals:
                    self.animals.append(what_organism)
                else:
                     return False

        except AttributeError:
            if len(self.plants) < self.max_plants:
                    self.plants.append(what_organism)
            else:
                  return False


