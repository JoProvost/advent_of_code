"""
    - swap position X with position Y means that the letters at indexes X
      and Y (counting from 0) should be swapped.
    - swap letter X with letter Y means that the letters X and Y should be
      swapped (regardless of where they appear in the string).
    - rotate left/right X steps means that the whole string should be
      rotated; for example, one right rotation would turn abcd into dabc.
    - rotate based on position of letter X means that the whole string
      should be rotated to the right based on the index of letter X
      (counting from 0) as determined before this instruction does any
      rotations. Once the index is determined, rotate the string to the
      right one time, plus a number of times equal to that index, plus one
      additional time if the index was at least 4.
    - reverse positions X through Y means that the span of letters at
      indexes X through Y (including the letters at X and Y) should be
      reversed in order.
    - move position X to position Y means that the letter which is at index
      X should be removed from the string, then inserted such that it ends
      up at index Y.
"""
import parser


class StringManipulator(object):

    def __init__(self, string):
        self._string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        if len(self._string) != len(string):
            print("wtf")
        self._string = string

    def swap_position(self, x, y):
        """
        swap position X with position Y means that the letters at indexes X
        and Y (counting from 0) should be swapped.
        """
        x, y = int(x), int(y)
        buffer = list(self.string)
        swap = buffer[x]
        buffer[x] = buffer[y]
        buffer[y] = swap
        self.string = ''.join(buffer)

    def swap_letter(self, x, y):
        """
        swap letter X with letter Y means that the letters X and Y should be
        swapped (regardless of where they appear in the string).
        """
        trans_table = str.maketrans({x: y, y: x})
        self.string = self.string.translate(trans_table)

    def rotate_right(self, x):
        """
        rotate left/right X steps means that the whole string should be
        rotated; for example, one right rotation would turn abcd into dabc.
        """
        x = int(x)
        x %= len(self.string)
        if x:
            self.string = self.string[-x:] + self.string[:len(self.string) - x]

    def rotate_left(self, x):
        """
        rotate left/right X steps means that the whole string should be
        rotated; for example, one right rotation would turn abcd into dabc.
        """
        x = int(x)
        if x:
            StringManipulator.rotate_right(self, len(self.string) - x)

    def rotate_based_on_letter(self, x):
        """
        rotate based on position of letter X means that the whole string
        should be rotated to the right based on the index of letter X
        (counting from 0) as determined before this instruction does any
        rotations. Once the index is determined, rotate the string to the
        right one time, plus a number of times equal to that index, plus one
        additional time if the index was at least 4.
        """
        index = self.string.index(x)
        rotate = 1 + index + (1 if index >= 4 else 0)
        StringManipulator.rotate_right(self, rotate)

    def reverse(self, x, y):
        """
        reverse positions X through Y means that the span of letters at
        indexes X through Y (including the letters at X and Y) should be
        reversed in order.
        """
        x, y = int(x), int(y)
        self.string = self.string[:x] + ''.join(reversed(self.string[x:y+1])) + self.string[y+1:]

    def move(self, x, y):
        """
        move position X to position Y means that the letter which is at index
        X should be removed from the string, then inserted such that it ends
        up at index Y.
        """
        x, y = int(x), int(y)
        buffer = list(self.string)
        letter = buffer.pop(x)
        buffer.insert(y, letter)
        self.string = ''.join(buffer)

    def transform(self, text):
        parser.parse(
            definition={
                'swap position (?P<x>.*) with position (?P<y>.*)': self.swap_position,
                'swap letter (?P<x>.*) with letter (?P<y>.*)': self.swap_letter,
                'rotate left (?P<x>.*) steps?': self.rotate_left,
                'rotate right (?P<x>.*) steps?': self.rotate_right,
                'rotate based on position of letter (?P<x>.*)': self.rotate_based_on_letter,
                'reverse positions (?P<x>.*) through (?P<y>.*)': self.reverse,
                'move position (?P<x>.*) to position (?P<y>.*)': self.move,
            },
            text=text)


class ReversedStringManipulator(StringManipulator):

    def transform(self, text):
        StringManipulator.transform(self, reversed(text.splitlines()))

    def rotate_right(self, x):
        StringManipulator.rotate_left(self, x)

    def rotate_left(self, x):
        StringManipulator.rotate_right(self, x)

    def rotate_based_on_letter(self, x):
        # This will only work with passwords the size of the puzzle... :)
        reversed_rotate_table = {
            1: 1,
            3: 2,
            5: 3,
            7: 4,
            2: 6,
            4: 7,
            6: 8,
            0: 9,
        }

        index = self.string.index(x)
        StringManipulator.rotate_left(self, reversed_rotate_table[index])

    def move(self, x, y):
        StringManipulator.move(self, y, x)
