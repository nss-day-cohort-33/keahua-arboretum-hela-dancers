from animals import Animal
from organism_type import Freshwater
from organism_type import Saltwater
from organism_type import Identifiable
from organism_type import Aquatic
from organism_type import Swimming


class RiverDolphin(Animal, Freshwater, Saltwater, Swimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin", 14, 13, {"Trout", "Mackarel", "Salmon", "Sardine"})
        Freshwater.__init__(self)
        Saltwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
            print(f'The dolphin ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Dolphin {self.id} was created!'

