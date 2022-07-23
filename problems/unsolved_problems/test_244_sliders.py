import unittest

# Sliders
""" 
You probably know the game Fifteen Puzzle. Here, instead of numbered tiles, we have seven red tiles and eight blue tiles.
A move is denoted by the uppercase initial of the direction (Left, Right, Up, Down) in which the tile is slid, e.g. starting from configuration (S), by the sequence LULUR we reach the configuration (E):

For each path, its checksum is calculated by (pseudocode):

For the sequence LULUR given above, the checksum would be 19761398.
Now, starting from configuration (S),
find all shortest ways to reach configuration (T).

What is the sum of all checksums for the paths having the minimal length?
""" 


class Test(unittest.TestCase):
    def test(self):
        pass
