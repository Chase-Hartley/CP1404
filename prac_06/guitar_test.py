
from prac_06.guitar_storage import GuitarStorage

g1 = GuitarStorage("Gibson L-5", 1922, 16035.40)
g2 = GuitarStorage("Stein-way 5-4", 2000, 150000)

print("{} get_age() - Expected {}. Got {}".format(g1.name, 97, GuitarStorage.get_age(g1)))
print("{} get_age() - Expected {}. Got {}".format(g2.name, 19, GuitarStorage.get_age(g2)))

print("{}-year old guitar is vintage() - Expected True. Got {}"
      .format(GuitarStorage.get_age(g1), GuitarStorage.is_vintage(g1)))
print("{}-year old guitar is vintage() - Expected False. Got {}"
      .format(GuitarStorage.get_age(g2), GuitarStorage.is_vintage(g2)))
