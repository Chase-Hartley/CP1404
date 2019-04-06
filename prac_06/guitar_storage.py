"""
Chase Hartley
Week 6 Prac 06
Guitars Exercise
"""

CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class GuitarStorage:

    """Initialise the method providing the default parameters."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
