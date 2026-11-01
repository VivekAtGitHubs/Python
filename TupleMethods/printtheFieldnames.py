from collections import namedtuple
Movie = namedtuple("Movie", ["title", "director", "rating"])
print(Movie._fields)