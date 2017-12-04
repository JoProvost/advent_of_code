from collections import namedtuple

import parser


class KineticSculpture(object):
    def __init__(self):
        self.disks = []

    def add_disc_definition(self, number, size, offset):
        self.disks.append(Disk(number, size, offset))

    def configure(self, text):
        parser.parse(
            definition={
                'Disc #(?P<number>.*) has (?P<size>.*) positions; at time=0, it is at position (?P<offset>.*).':
                    self.add_disc_definition},
            text=text,
            value_type=int)

    def will_you_get_a_capsule_at(self, time):
        for disk in self.disks:
            if (disk.number + time + disk.offset) % disk.size:
                return False
        return True

Disk = namedtuple('Disk', 'number, size, offset')
