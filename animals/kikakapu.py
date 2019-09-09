# Its an fish

from animals import Animal
from organism_type import Freshwater
from organism_type import Stagnant
from organism_type import Swimming
from organism_type import Identifiable

class Kikakapu(Animal, Freshwater, Stagnant, Swimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapu", 2, 1, {"Lizard Fish", "Eel", "Clams", "Trout"})
        Freshwater.__init__(self)
        Stagnant.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The kikakapu ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Kikakapu (fish) {self.id} was created!'