from environments import River
from environments import Swamp

river1 = River("River", 12, 6)
river2 = River("River", 12, 6)
swamp1 = Swamp("Swamp", 8, 12)
swamp2 = Swamp("Swamp", 8, 12)


class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = [river1, river2]
        self.grasslands = []
        self.coastlines = []
        self.mountains = []
        self.forests = []
        self.swamps = [swamp1, swamp2]
