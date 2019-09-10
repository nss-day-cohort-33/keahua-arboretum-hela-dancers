from environments import River
from environments import Swamp

class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []
        self.coastlines = []
        self.mountains = []
        self.forests = []
        self.swamps = []