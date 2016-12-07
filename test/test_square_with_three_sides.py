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

    def test_parsing_rows(self):
        self.assertEqual(
            ((1, 2, 3), (4, 5, 6)),
            tuple(square_with_three_sides.parse_rows('1 2 3\n4 5 6')))

    def test_with_a_valid_triangle(self):
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 3 4')))

    def test_with_two_valid_triangles(self):
        self.assertEqual(2, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 3 4\n4 4 4')))

    def test_sum_of_any_two_sides_must_be_larger_than_the_remaining_side(self):
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 2 4')))
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 4 2')))
        self.assertEqual(0, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('4 2 2')))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 3 4')))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('4 2 3')))
        self.assertEqual(1, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows('2 4 3')))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'square_with_three_sides.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(869, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_rows(puzzle_input)))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    Now that you've helpfully marked up their design documents, it occurs to
    you that triangles are specified in groups of three vertically. Each set
    of three numbers in a column specifies a triangle. Rows are unrelated.

    For example, given the following specification, numbers with the same
    hundreds digit would be part of the same triangle:

    101 301 501
    102 302 502
    103 303 503
    201 401 601
    202 402 602
    203 403 603

    In your puzzle input, and instead reading by columns, how many of the
    listed triangles are possible?
    """

    def setUp(self):
        pass

    def test_parsing_columns(self):
        self.assertEqual(
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
            tuple(square_with_three_sides.parse_columns(
                '1 4 7\n'
                '2 5 8\n'
                '3 6 9')))

    def test_column_based_parsing(self):
        self.assertEqual(6, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_columns(
                '101 301 501\n'
                '102 302 502\n'
                '103 303 503\n'
                '201 401 601\n'
                '202 402 602\n'
                '203 403 603'
            )))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'square_with_three_sides.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(1544, square_with_three_sides.how_many_valid_triangles(
            square_with_three_sides.parse_columns(puzzle_input)))
