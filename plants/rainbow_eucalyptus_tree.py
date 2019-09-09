from .plant import Plant
from organism_type import Loamy_Soil

class Rainbow_Eucalyptus_Tree(Plant, Loamy_Soil):
    def __init__(self):
        Plant.__init__(self, "Full", 8, "Low")
        Loamy_Soil.__init__(self)