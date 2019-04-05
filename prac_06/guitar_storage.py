"""
Chase Hartley
Week 6 Prac 06
Guitars Exercise
"""


class GuitarStorage:

    """Initialise the method providing the default parameters."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self, current_year, year=0):
        self.current_year = current_year
        self.year = year
        year_difference = current_year - year
        return year_difference

    def is_vintage(self):
        return self.get_age()
