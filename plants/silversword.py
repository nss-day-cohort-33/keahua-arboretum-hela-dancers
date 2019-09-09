from .plant import Plant
from organism_type import Silt_Soil

class Silversword(Plant, Silt_Soil):
    def __init__(self):
        Plant.__init__(self, "Shade", 22, "High")
        Silt_Soil.__init__(self)