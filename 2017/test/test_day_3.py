import unittest

from day_3 import location_of, moves_for, index_of, spiral_for

challenge = 289326


class TestPart1(unittest.TestCase):
    """
    --- Day 3: Spiral Memory ---

    You come across an experimental new kind of memory stored on an infinite
    two-dimensional grid.

    Each square on the grid is allocated in a spiral pattern starting at a
    location marked 1 and then counting up while spiraling outward. For example,
    the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    While this is very space-efficient (no squares are skipped), requested data
    must be carried back to square 1 (the location of the only access port for
    this memory system) by programs that can only move up, down, left, or right.
    They always take the shortest path: the Manhattan Distance between the
    location of the data and square 1.

    For example:

    - Data from square 1 is carried 0 steps, since it's at the access port.
    - Data from square 12 is carried 3 steps, such as: down, left, left.
    - Data from square 23 is carried only 2 steps: up twice.
    - Data from square 1024 must be carried 31 steps.

    How many steps are required to carry the data from the square identified in
    your puzzle input all the way to the access port?
    """

    def test_simple_matches(self):
        self.assertEqual((0, 0), location_of(1))
        self.assertEqual(0, moves_for(location_of(1)))

        self.assertEqual((1, 1), location_of(9))
        self.assertEqual(2, moves_for(location_of(9)))

        self.assertEqual((2, 2), location_of(25))
        self.assertEqual((3, 3), location_of(49))
        self.assertEqual((2, 3), location_of(48))
        self.assertEqual((-3, 3), location_of(43))
        self.assertEqual((-3, 2), location_of(42))
        self.assertEqual((-3, -3), location_of(37))
        self.assertEqual((-2, -3), location_of(36))
        self.assertEqual((3, -3), location_of(31))

        self.assertEqual(3, moves_for(location_of(12)))
        self.assertEqual(2, moves_for(location_of(23)))
        self.assertEqual(6, moves_for(location_of(31)))
        self.assertEqual(31, moves_for(location_of(1024)))

    def test_challenge(self):
        self.assertEqual(419, moves_for(location_of(challenge)))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    As a stress test on the system, the programs here clear the grid and then
    store the value 1 in square 1. Then, in the same allocation order as shown
    above, they store the sum of the values in all adjacent squares, including
    diagonals.

    So, the first few squares' values are chosen as follows:

    - Square 1 starts with the value 1.
    - Square 2 has only one adjacent filled square (with value 1), so it also
      stores 1.
    - Square 3 has both of the above squares as neighbors and stores the sum of
      their values, 2.
    - Square 4 has all three of the aforementioned squares as neighbors and
      stores the sum of their values, 4.
    - Square 5 only has the first and fourth squares as neighbors, so it gets
      the value 5.

    Once a square is written, its value does not change. Therefore, the first
    few squares would receive the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...

    What is the first value written that is larger than your puzzle input?
    """

    def test_index_of(self):
        self.assertEqual(9, index_of(location_of(9)))
        self.assertEqual(8, index_of(location_of(8)))
        self.assertEqual(7, index_of(location_of(7)))
        self.assertEqual(6, index_of(location_of(6)))
        self.assertEqual(5, index_of(location_of(5)))
        self.assertEqual(4, index_of(location_of(4)))
        self.assertEqual(3, index_of(location_of(3)))
        self.assertEqual(2, index_of(location_of(2)))
        self.assertEqual(1, index_of(location_of(1)))

    def test_building_table(self):
        self.assertEqual([1, 1, 2], spiral_for(2))
        self.assertEqual(
            [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147,
             304, 330, 351, 362, 747, 806],
            spiral_for(lambda x: x == 806))

    def test_challenge(self):
        self.assertEqual(295229, spiral_for(lambda x: x > challenge)[-1])
