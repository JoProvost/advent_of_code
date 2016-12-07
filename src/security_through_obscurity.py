from collections import Counter
import re
from functools import reduce

ROOM_FORMAT = '(?P<encrypted_name>[a-z0-9-]*)-(?P<sector_id>[0-9]+)\\[(?P<checksum>[a-z]*)\\]'


def is_valid_room(room_data):
    return room_data['checksum'] == generate_checksum(room_data['encrypted_name'])


def parse_room(room):
    return re.match(ROOM_FORMAT, room).groupdict()


def generate_checksum(encrypted_name):
    counter = Counter(encrypted_name.replace('-', ''))
    return ''.join(x[0] for x in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5])


def sum_sector_id_of_valid_rooms(rooms_text):
    return reduce(
        lambda a, b: a + b,
        map(lambda x: int(x['sector_id']),
            filter(is_valid_room,
                   map(parse_room, rooms_text.splitlines()))))
