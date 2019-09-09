# Says that an animal can live in a forest biome

from .terrestrial import Terrestrial

class Forestful(Terrestrial):

    def __init__(self):
        super().__init__()
        self.forestful = True
