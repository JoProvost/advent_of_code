import re
from collections import Counter
from os.path import dirname

import yaml
from os.path import join


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


class Font(object):
    def __init__(self, font_name):
        font_data = yaml.safe_load(open(join(dirname(__file__), 'resources', '{}.font.yaml'.format(font_name))))
        self.symbols = font_data['symbols']
        self.width = font_data['width']
        self.height = font_data['height']

    def guess_symbol(self, ascii_art):
        for character, definitions in self.symbols.items():
            for definition in definitions:
                if ascii_art == definition:
                    return character
        raise Exception('Unknown character: \n"""\n{}""'.format(ascii_art))


class OpticalCharacterRecognition(object):
    def __init__(self, font):
        self.font = font

    def split_into_symbols(self, ascii_art):
        ascii_art_lines = ascii_art.splitlines()
        symbol_width = self.font.width
        for i in range(0, len(ascii_art_lines[0]), symbol_width):
            yield '\n'.join(line[i:i + symbol_width] for line in ascii_art_lines) + '\n'

    def read_text(self, ascii_art):
        return ''.join(self.font.guess_symbol(symbol) for symbol in self.split_into_symbols(ascii_art))
