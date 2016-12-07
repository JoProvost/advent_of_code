from collections import Counter
import re
from functools import reduce

ROOM_FORMAT = '(?P<encrypted_name>[a-z0-9-]*)-(?P<sector_id>[0-9]+)\\[(?P<checksum>[a-z]*)\\]'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class Room(object):
    def __init__(self, encrypted_name, sector_id, checksum, **_):
        self.encrypted_name = encrypted_name
        self.sector_id = int(sector_id)
        self.checksum = checksum

    def is_valid(self):
        return self.checksum == generate_checksum(self.encrypted_name)

    @classmethod
    def from_text(cls, text):
        return cls(**re.match(ROOM_FORMAT, text).groupdict())


def generate_checksum(encrypted_name):
    counter = Counter(encrypted_name.replace('-', ''))
    return ''.join(x[0] for x in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5])


def sum_sector_id_of_valid_rooms(rooms_text):
    return reduce(
        lambda a, b: a + b,
        map(lambda x: x.sector_id,
            filter(lambda x: x.is_valid(),
                   map(Room.from_text, rooms_text.splitlines()))))
