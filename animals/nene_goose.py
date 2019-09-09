# Its an goose

from animals import Animal
from organism_type import Grassful
from organism_type import Flying
from organism_type import Identifiable

class NeneGoose(Animal, Grassful, Flying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose", 8, 7, {"Ferns", "Native Flower", "Sedge", "Coffee"})
        Flying.__init__(self)
        Grassful.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The nenolden goose ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Nene goose {self.id} was created!'