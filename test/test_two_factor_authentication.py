import unittest
from os.path import dirname, join
from textwrap import dedent

import two_factor_authentication


class TestPart1(unittest.TestCase):
    """
    --- Day 8: Two-Factor Authentication ---

    You come across a door implementing what you can only assume is an
    implementation of two-factor authentication after a long game of
    requirements telephone.

    To get past the door, you first swipe a keycard (no problem; there was
    one on a nearby desk). Then, it displays a code on a little screen, and
    you type that code on a keypad. Then, presumably, the door unlocks.

    Unfortunately, the screen has been smashed. After a few minutes, you've
    taken everything apart and figured out how it works. Now you just have to
    work out what the screen would have displayed.

    The magnetic strip on the card you swiped encodes a series of
    instructions for the screen; these instructions are your puzzle input.
    The screen is 50 pixels wide and 6 pixels tall, all of which start off,
    and is capable of three somewhat peculiar operations:

    - rect AxB turns on all of the pixels in a rectangle at the top-left of
      the screen which is A wide and B tall.
    - rotate row y=A by B shifts all of the pixels in row A (0 is the top
      row) right by B pixels. Pixels that would fall off the right end
      appear at the left end of the row.
    - rotate column x=A by B shifts all of the pixels in column A (0 is the
      left column) down by B pixels. Pixels that would fall off the bottom
      appear at the top of the column.

    For example, here is a simple sequence on a smaller screen:

    - rect 3x2 creates a small rectangle in the top-left corner:

      ###....
      ###....
      .......

    - rotate column x=1 by 1 rotates the second column down by one pixel:

      #.#....
      ###....
      .#.....

    - rotate row y=0 by 4 rotates the top row right by four pixels:

      ....#.#
      ###....
      .#.....

    - rotate column x=1 by 1 again rotates the second column down by one
      pixel, causing the bottom pixel to wrap back to the top:

      .#..#.#
      #.#....
      .#.....

    As you can see, this display technology is extremely powerful, and will
    soon dominate the tiny-code-displaying-screen market. That's what the
    advertisement on the back of the display tries to convince you, anyway.

    There seems to be an intermediate check of the voltage used by the
    display: after you swipe your card, if the screen did work, how many
    pixels should be lit?
    """

    def test_rect_3x2(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.rect(3, 2)
        self.assertEqual(
            '###....\n'
            '###....\n'
            '.......',
            display.show_pixels()
        )

    def test_rotate_column_1_by_1(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.rect(3, 2)
        display.rotate_column(1, by=1)
        self.assertEqual(
            '#.#....\n'
            '###....\n'
            '.#.....',
            display.show_pixels()
        )

    def test_rotate_row_0_by_4(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.rect(3, 2)
        display.rotate_row(0, by=4)
        self.assertEqual(
            '....###\n'
            '###....\n'
            '.......',
            display.show_pixels()
        )

    def test_parsing_rect_3x2(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.execute('rect 3x2')
        self.assertEqual(
            '###....\n'
            '###....\n'
            '.......',
            display.show_pixels()
        )

    def test_parsing_rotate_column_1_by_1(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.rect(3, 2)
        display.execute('rotate column x=1 by 1')
        self.assertEqual(
            '#.#....\n'
            '###....\n'
            '.#.....',
            display.show_pixels()
        )

    def test_parsing_rotate_row_0_by_4(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.rect(3, 2)
        display.execute('rotate row y=0 by 4')
        self.assertEqual(
            '....###\n'
            '###....\n'
            '.......',
            display.show_pixels()
        )

    def test_full_parsing(self):
        display = two_factor_authentication.PixelDisplay(width=7, height=3)
        display.execute(dedent(
            """
            rect 3x2
            rotate column x=1 by 1
            rotate row y=0 by 4
            rotate column x=1 by 1
            """))
        self.assertEqual(dedent(
            """\
            .#..#.#
            #.#....
            .#....."""),
            display.show_pixels()
        )

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'two_factor_authentication.txt')) as f:
            puzzle_input = f.read()
        display = two_factor_authentication.PixelDisplay(width=50, height=6)
        display.execute(puzzle_input)
        self.assertEqual(121, display.pixels_on())