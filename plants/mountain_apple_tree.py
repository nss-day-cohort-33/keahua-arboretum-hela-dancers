from .plant import Plant
from organism_type import Clay_Soil
from organism_type import Identifiable

class Mountain_Apple_Tree(Plant, Clay_Soil, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Partial", 17, "High")
        Clay_Soil.__init__(self)
        Identifiable.__init__(self)
