from .plant import Plant
from organism_type import Silt_Soil
from organism_type import Identifiable

class Silversword(Plant, Silt_Soil, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Shade", 22, "High")
        Silt_Soil.__init__(self)
        Identifiable.__init__(self)