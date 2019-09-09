from organism_type import Stagnant
import sys
from .habitat import ContainsAnimals
from .habitat import ContainsPlants
sys.path.append('../')

# from animals.


class Swamp():

    def __init__(self, name):
        self.name = name
        self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, Stagnant):
            raise TypeError(f"{item} is not of type Stagnant")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name
