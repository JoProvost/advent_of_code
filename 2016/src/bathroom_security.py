class Keypad(object):

    def __init__(self, keys):
        self.keys = keys
        self.line = 0
        self.row = 0

    def go_to(self, key):
        for line_number, line in enumerate(self.keys):
            if key in line:
                self.line = line_number
                self.row = line.find(key)

    def solve_key(self, instruction):
        for direction in instruction:
            if direction == 'U':
                self.move(-1, 0)
            if direction == 'D':
                self.move(1, 0)
            if direction == 'L':
                self.move(0, -1)
            if direction == 'R':
                self.move(0, 1)

        return self.keys[self.line][self.row]

    def move(self, line_offset, row_offset):
        line = self.line + line_offset
        row = self.row + row_offset
        if line < 0 or line > len(self.keys) - 1:
            return
        if row < 0 or row > len(self.keys[line]) - 1:
            return
        if self.keys[line][row] == ' ':
            return

        self.line = line
        self.row = row


def unlock(instructions, keys, start_key='5'):
    keypad = Keypad(keys)
    keypad.go_to(start_key)

    keys = ''
    for instruction in instructions.split():
        keys += keypad.solve_key(instruction)
    return keys

