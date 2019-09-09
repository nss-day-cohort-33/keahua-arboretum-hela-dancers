# Its an lizard fish

from animals import Animal
from organism_type import Saltwater
from organism_type import Swimming
from organism_type import Identifiable

class Ulae(Animal, Saltwater, Swimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae", 2, 1, {"Shark", "Blue Fin Tuna", "Clams", "Angler Fish"})
        Saltwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The ulae ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Ulae (lizard fish) {self.id} was created!'