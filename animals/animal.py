class Animal:

    def __init__(self, species, age, minimum_release_age, food):
        self.species = species
        # age is in months
        self.age = age
        self.minimum_release_age = minimum_release_age
        self.__food = food

    @property
    def food(self):
        return self.__food

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
