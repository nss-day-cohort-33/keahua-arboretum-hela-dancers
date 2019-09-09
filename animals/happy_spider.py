# Its an bat

from animals import Animal
from organism_type import Stagnant
from organism_type import Crawling
from organism_type import Identifiable

class HappySpider(Animal, Stagnant, Crawling, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Happy-face spider", 2, 1, {"Moths", "Beetles", "Fern", "Flower"})
        Stagnant.__init__(self)
        Crawling.__init__(self)
        Identifiable.__init__(self)

    def feed(self, food):
        if food in self.__food:
            print(f'The opeapea ate a {food} for a meal')
        # TODO: Ask if we should keep or remove
        # else:
        #     print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f"Ope'ape'a (fish) {self.id} was created!"