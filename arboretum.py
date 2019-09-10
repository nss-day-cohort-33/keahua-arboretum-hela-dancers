from environments import Swamp

swamp1 = Swamp("Swamp", 8, 12)
swamp2 = Swamp("Swamp", 8, 12)


class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.grasslands = []
        self.coastlines = []
        self.mountains = []
        self.forests = []
        self.swamps = [swamp1, swamp2]
