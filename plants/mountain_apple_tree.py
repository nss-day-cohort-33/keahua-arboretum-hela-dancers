from .plant import Plant
from organism_type import Clay_Soil

class Mountain_Apple_Tree(Plant, Clay_Soil):
    def __init__(self):
        Plant.__init__(self, "Partial", 17, "High")
        Clay_Soil.__init__(self)
