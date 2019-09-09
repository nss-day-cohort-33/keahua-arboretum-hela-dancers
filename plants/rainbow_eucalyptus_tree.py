from .plant import Plant
from organism_type import Loamy_Soil
from organism_type import Identifiable

class Rainbow_Eucalyptus_Tree(Plant, Loamy_Soil, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Full", 8, "Low")
        Loamy_Soil.__init__(self)
        Identifiable.__init__(self)