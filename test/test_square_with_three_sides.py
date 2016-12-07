import unittest
from os.path import dirname, join

import square_with_three_sides


class TestPart1(unittest.TestCase):
    """
    --- Day 3: Squares With Three Sides ---

    Now that you can think clearly, you move deeper into the labyrinth of
    hallways and office furniture that makes up this part of Easter Bunny HQ.
    This must be a graphic design department; the walls are covered in
    specifications for triangles.

    Or are they?

    The design document gives the side lengths of each triangle it describes,
    but... 5 10 25? Some of these aren't triangles. You can't help but mark
    the impossible ones.

    In a valid triangle, the sum of any two sides must be larger than the
    remaining side. For example, the "triangle" given above is impossible,
    because 5 + 10 is not larger than 25.

    In your puzzle input, how many of the listed triangles are possible?
    """

    def setUp(self):
        pass

    def test_2_sides_triangle_is_invalid(self):
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles('1 2'))

    def test_3_sides_triangle_is_valid(self):
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles('2 3 4'))

    def test_with_two_valid_triangles(self):
        self.assertEqual(2, square_with_three_sides.how_many_valid_triangles('2 3 4\n4 4 4'))

    def test_sum_of_any_two_sides_must_be_larger_than_the_remaining_side(self):
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles('2 2 4'))
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles('2 4 2'))
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles('4 2 2'))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles('2 3 4'))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles('4 2 3'))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles('2 4 3'))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'square_with_three_sides.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(869, square_with_three_sides.how_many_valid_triangles(puzzle_input))
