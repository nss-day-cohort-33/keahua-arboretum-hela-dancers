# Its an bat

from animals import Animal
from organism_type import Forestful
from organism_type import Mountainful
from organism_type import Flying
from organism_type import Identifiable

class Opeapea(Animal, Forestful, Mountainful, Flying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapu", 2, 1, {"Moths", "Beetles", "Termites", "Worm"})
        Forestful.__init__(self)
        Mountainful.__init__(self)
        Flying.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The opeapea ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f"Ope'ape'a (fish) {self.id} was created!"