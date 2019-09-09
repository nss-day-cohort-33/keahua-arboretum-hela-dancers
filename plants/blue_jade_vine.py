from .plant import Plant
from organism_type import Silt_Soil
from organism_type import Marsh_Soil

class Blue_Jade_Vine(Plant, Silt_Soil, Marsh_Soil):
    def __init__(self):
        Plant.__init__(self, "Partial", 0, "Medium")
        Silt_Soil.__init__(self)
        Marsh_Soil.__init__(self)