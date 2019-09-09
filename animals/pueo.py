# Its an owl

from animals import Animal
from organism_type import Grassful
from organism_type import Forestful
from organism_type import Flying
from organism_type import Identifiable

class Pueo(Animal, Grassful, Forestful, Flying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo", 9, 8, {"Black Rat", "Brown Rat", "Hawaiin Rat", "House Mouse"})
        Grassful.__init__(self)
        Forestful.__init__(self)
        Flying.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The pueo ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Pueo (a form of owl) {self.id} was created!'