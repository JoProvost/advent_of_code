import unittest

from day_3 import location_of, moves_for

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
