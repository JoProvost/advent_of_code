import re
from collections import Counter


class PixelDisplay(object):
    OFF = False
    ON = True
    REPRESENTATION = {ON: '#', OFF: '.'}

    def __init__(self, width, height):
        self.rows = [[self.OFF for _ in range(width)] for _ in range(height)]

    def show_pixels(self):
        return '\n'.join(
            ''.join((self.REPRESENTATION[pixel] for pixel in line))
            for line in self.rows)

    def rect(self, width, height):
        for line_index in range(height):
            for column_index in range(width):
                self.rows[line_index][column_index] = self.ON

    def rotate_column(self, column, by):
        columns = list(map(list, zip(*self.rows)))
        columns[column] = self._rotate(columns[column], by)
        self.rows = list(map(list, zip(*columns)))

    def rotate_row(self, row, by):
        self.rows[row] = self._rotate(self.rows[row], by)

    def pixels_on(self):
        pixels_on = 0
        for row in self.rows:
            count = Counter(row)
            pixels_on += count[self.ON]
        return pixels_on

    def execute(self, commands):
        command_regex = {
            'rect (?P<width>[0-9]*)x(?P<height>[0-9]*)': self.rect,
            'rotate column x=(?P<column>[0-9]*) by (?P<by>[0-9]*)': self.rotate_column,
            'rotate row y=(?P<row>[0-9]*) by (?P<by>[0-9]*)': self.rotate_row,
        }
        for command in commands.splitlines():
            for regex, method in command_regex.items():
                match = re.match(regex, command)
                if match:
                    method(**{k: int(v) for k, v in match.groupdict().items()})

    @classmethod
    def _rotate(cls, line, by):
        by %= len(line)
        return line[-by:] + line[:-by]
