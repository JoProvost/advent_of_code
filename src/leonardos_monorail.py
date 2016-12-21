import re


class VirtualMachine(object):
    def __init__(self, instructions):
        self.registers = {}
        self.instructions = instructions
        self.location = 0

    def cpy(self, value, register):
        try:
            value = int(value)
        except ValueError:
            value = int(self.registers[value])
        self.registers[register] = value
        self.location += 1

    def inc(self, register):
        self.registers[register] = self.registers.get(register, 0) + 1
        self.location += 1

    def dec(self, register):
        self.registers[register] = self.registers.get(register, 0) - 1
        self.location += 1

    def jnz(self, value, offset):
        try:
            value = int(value)
        except ValueError:
            value = self.registers.get(value, 0)
        if value:
            self.location += int(offset)
        else:
            self.location += 1

    def run(self):
        try:
            while True:
                parse(
                    definition={
                        'cpy (?P<value>.*) (?P<register>.*)': self.cpy,
                        'inc (?P<register>.*)': self.inc,
                        'dec (?P<register>.*)': self.dec,
                        'jnz (?P<value>.*) (?P<offset>.*)': self.jnz,
                    },
                    text=self.instructions[self.location]
                )
        except IndexError:
            pass


def parse(definition, text):
    for command in text.splitlines():
        for regex, method in definition.items():
            match = re.match(regex, command)
            if match:
                method(**{k: v for k, v in match.groupdict().items()})
