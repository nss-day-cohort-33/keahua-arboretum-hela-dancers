from .aquatic import IAquatic

class IStagnant(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "stagnant"
