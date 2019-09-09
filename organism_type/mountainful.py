from .terrestrial import Terrestrial

class Mountainful(Terrestrial):

    def __init__(self):
        super().__init__()
        self.mountainful = True
