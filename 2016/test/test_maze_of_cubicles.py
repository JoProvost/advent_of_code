import unittest

from maze_of_cubicles import Maze


class TestPart1(unittest.TestCase):
    """
    --- Day 13: A Maze of Twisty Little Cubicles ---

    You arrive at the first floor of this new building to discover a much
    less welcoming environment than the shiny atrium of the last one.
    Instead, you are in a maze of twisty little cubicles, all alike.

    Every location in this area is addressed by a pair of non-negative
    integers (x,y). Each such coordinate is either a wall or an open space.
    You can't move diagonally. The cube maze starts at 0,0 and seems to
    extend infinitely toward positive x and y; negative values are invalid,
    as they represent a location outside the building. You are in a small
    waiting area at 1,1.

    While it seems chaotic, a nearby morale-boosting poster explains, the
    layout is actually quite logical. You can determine whether a given x,y
    coordinate will be a wall or an open space using a simple system:

    - Find x*x + 3*x + 2*x*y + y + y*y.
    - Add the office designer's favorite number (your puzzle input).
    - Find the binary representation of that sum; count the number of bits
      that are 1.
        - If the number of bits that are 1 is even, it's an open space.
        - If the number of bits that are 1 is odd, it's a wall.

    For example, if the office designer's favorite number were 10, drawing
    walls as # and open spaces as ., the corner of the building containing
    0,0 would look like this:

      0123456789
    0 .#.####.##
    1 ..#..#...#
    2 #....##...
    3 ###.#.###.
    4 .##..#..#.
    5 ..##....#.
    6 #...##.###

    Now, suppose you wanted to reach 7,4. The shortest route you could take
    is marked as O:

      0123456789
    0 .#.####.##
    1 .O#..#...#
    2 #OOO.##...
    3 ###O#.###.
    4 .##OO#OO#.
    5 ..##OOO.#.
    6 #...##.###

    Thus, reaching 7,4 would take a minimum of 11 steps (starting from your
    current location, 1,1).

    What is the fewest number of steps required for you to reach 31,39?
    """

    def test_wall_detection(self):
        maze = Maze(favorite_number=10)
        expected_maze = [
            '.#.####.##',
            '..#..#...#',
            '#....##...',
            '###.#.###.',
            '.##..#..#.',
            '..##....#.',
            '#...##.###',
        ]

        for y, row in enumerate(expected_maze):
            for x, cubicle in enumerate(row):
                if cubicle == '#':
                    self.assertTrue(maze.is_wall(x, y))
                else:
                    self.assertFalse(maze.is_wall(x, y))

    def test_negative_values_are_walls(self):
        maze = Maze(favorite_number=10)
        for y in range(10):
            self.assertTrue(maze.is_wall(-1, y))
        for x in range(10):
            self.assertTrue(maze.is_wall(x, -1))

    def test_simplest_happy_path(self):
        maze = Maze(favorite_number=10)
        maze_map = maze.explore(from_x=1, from_y=1, to_x=7, to_y=4)
        self.assertEqual(11, len(maze_map.path))

    def test_puzzle(self):
        maze = Maze(favorite_number=1364)
        maze_map = maze.explore(from_x=1, from_y=1, to_x=31, to_y=39)
        self.assertEqual(86, len(maze_map.path))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    How many locations (distinct x,y coordinates, including your starting
    location) can you reach in at most 50 steps?
    """

    def test_simplest_happy_path(self):
        maze = Maze(favorite_number=10)
        maze_map = maze.explore(from_x=1, from_y=1, to_x=7, to_y=4, max_distance=10)
        self.assertEqual(0, len(maze_map.path))
        self.assertEqual(18, len(maze_map.valid_locations()))

        maze_map = maze.explore(from_x=1, from_y=1, to_x=7, to_y=4, max_distance=11)
        self.assertEqual(11, len(maze_map.path))

    def test_puzzle(self):
        maze = Maze(favorite_number=1364)
        maze_map = maze.explore(from_x=1, from_y=1, max_distance=50)
        self.assertEqual(127, len(maze_map.valid_locations()))
