from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides = 6, smallest=1):
        """Assuems a six-sided die"""
        self.num_sides = num_sides
        self.smallest = smallest


    def roll(self):
        """Returns a random value between 1 and the number of sides"""
        roll_num = randint(self.smallest, self.num_sides)
        return roll_num
