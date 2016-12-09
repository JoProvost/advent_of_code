from os.path import join, dirname

import yaml


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
