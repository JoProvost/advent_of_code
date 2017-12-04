import unittest

from no_time_for_taxi_cab import EasterBunnyNavigationSystem


class TestPart1(unittest.TestCase):
    """
    --- Day 1: No Time for a Taxicab ---

    Santa's sleigh uses a very high-precision clock to guide its movements,
    and the clock's oscillator is regulated by stars. Unfortunately, the
    stars have been stolen... by the Easter Bunny. To save Christmas, Santa
    needs you to retrieve all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on
    each day in the advent calendar; the second puzzle is unlocked when you
    complete the first. Each puzzle grants one star. Good luck!

    You're airdropped near Easter Bunny Headquarters in a city somewhere.
    "Near", unfortunately, is as close as you can get - the instructions on
    the Easter Bunny Recruiting Document the Elves intercepted start here,
    and nobody had time to work them out further.

    The Document indicates that you should start at the given coordinates
    (where you just landed) and face North. Then, follow the provided
    sequence: either turn left (L) or right (R) 90 degrees, then walk forward
    the given number of blocks, ending at a new intersection.

    There's no time to follow such ridiculous instructions on foot, though,
    so you take a moment and work out the destination. Given that you can
    only walk on the street grid of the city, how far is the shortest path to
    the destination?

    For example:

     - Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5
       blocks away.
     - R2, R2, R2 leaves you 2 blocks due South of your starting position,
       which is 2 blocks away.
     - R5, L5, R5, R3 leaves you 12 blocks away.

    How many blocks away is Easter Bunny HQ?
    """

    def setUp(self):
        self.navigator = EasterBunnyNavigationSystem()

    def test_at_start_zero_blocks_away(self):
        self.assertEqual(0, self.navigator.how_many_blocks_away())

    def test_turning_right_3_blocks_makes_3_blocks_away(self):
        self.navigator.navigate('R3')
        self.assertEqual(3, self.navigator.how_many_blocks_away())

    def test_R2_L3_is_5_blocks_away(self):
        self.navigator.navigate('R2, L3')
        self.assertEqual(5, self.navigator.how_many_blocks_away())

    def test_R2_R2_R2_is_2_blocks_away(self):
        self.navigator.navigate('R2, R2, R2')
        self.assertEqual(2, self.navigator.how_many_blocks_away())

    def test_R5_L5_R5_R3_is_12_blocks_away(self):
        self.navigator.navigate('R5, L5, R5, R3')
        self.assertEqual(12, self.navigator.how_many_blocks_away())

    def test_puzzle_input(self):
        self.navigator.navigate(
            'R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, '
            'R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, '
            'L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, '
            'R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, '
            'R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, '
            'R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, '
            'R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, '
            'L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, '
            'R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, '
            'R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, '
            'L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, '
            'R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, '
            'R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, '
            'R1, R5, L1, L3, L5, R2')
        self.assertEqual(231, self.navigator.how_many_blocks_away())


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    Then, you notice the instructions continue on the back of the Recruiting
    Document. Easter Bunny HQ is actually at the first location you visit
    twice.

    For example, if your instructions are R8, R4, R4, R8, the first location
    you visit twice is 4 blocks away, due East.

    How many blocks away is the first location you visit twice?
    """

    def setUp(self):
        self.navigator = EasterBunnyNavigationSystem()

    def test_turning_right_3_blocks_makes_3_blocks_away(self):
        self.navigator.navigate('R8, R4, R4, R8')
        self.assertEqual(4, self.navigator.how_many_blocks_away_is_first_location_twice_visited())

    def test_puzzle_input(self):
        self.navigator.navigate(
            'R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, '
            'R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, '
            'L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, '
            'R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, '
            'R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, '
            'R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, '
            'R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, '
            'L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, '
            'R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, '
            'R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, '
            'L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, '
            'R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, '
            'R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, '
            'R1, R5, L1, L3, L5, R2')
        self.assertEqual(147, self.navigator.how_many_blocks_away_is_first_location_twice_visited())
