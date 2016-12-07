import unittest
from os.path import dirname

from os.path import join

import security_through_obscurity


class TestPart1(unittest.TestCase):
    """
    --- Day 4: Security Through Obscurity ---

    Finally, you come across an information kiosk with a list of rooms. Of
    course, the list is encrypted and full of decoy data, but the
    instructions to decode the list are barely hidden nearby. Better remove
    the decoy data first.

    Each room consists of an encrypted name (lowercase letters separated by
    dashes) followed by a dash, a sector ID, and a checksum in square
    brackets.

    A room is real (not a decoy) if the checksum is the five most common
    letters in the encrypted name, in order, with ties broken by
    alphabetization. For example:

    - aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common
      letters are a (5), b (3), and then a tie between x, y, and z, which
      are listed alphabetically.
    - a-b-c-d-e-f-g-h-987[abcde] is a real room because although the
      letters are all tied (1 of each), the first five are listed
      alphabetically.
    - not-a-real-room-404[oarel] is a real room.
    - totally-real-room-200[decoy] is not.

    Of the real rooms from the list above, the sum of their sector IDs is
    1514.

    What is the sum of the sector IDs of the real rooms?

    """

    def test_valid_room(self):
        self.assertTrue(security_through_obscurity.Room.from_text('aaaaa-bbb-z-y-x-123[abxyz]').is_valid())

    def test_valid_room_with_more_than_5_letters(self):
        self.assertTrue(security_through_obscurity.Room.from_text('a-b-c-d-e-f-g-h-987[abcde]').is_valid())

    def test_fetch_sector_id(self):
        self.assertEqual(123, security_through_obscurity.Room.from_text('aaaaa-bbb-z-y-x-123[abxyz]').sector_id)

    def test_fetch_checksum(self):
        self.assertEqual('abxyz', security_through_obscurity.Room.from_text('aaaaa-bbb-z-y-x-123[abxyz]').checksum)

    def test_decoy_room(self):
        self.assertFalse(security_through_obscurity.Room.from_text('totally-real-room-200[decoy]').is_valid())

    def test_sum_sector_id_of_valid_rooms(self):
        self.assertEqual(1514, security_through_obscurity.sum_sector_id_of_valid_rooms(
            'aaaaa-bbb-z-y-x-123[abxyz]\n'
            'a-b-c-d-e-f-g-h-987[abcde]\n'
            'not-a-real-room-404[oarel]\n'
            'totally-real-room-200[decoy]\n'
        ))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'security_through_obscurity.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(361724, security_through_obscurity.sum_sector_id_of_valid_rooms(puzzle_input))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    With all the decoy data out of the way, it's time to decrypt this list
    and get moving.

    The room names are encrypted by a state-of-the-art shift cipher, which is
    nearly unbreakable without the right software. However, the information
    kiosk designers at Easter Bunny HQ were not expecting to deal with a
    master cryptographer like yourself.

    To decrypt a room name, rotate each letter forward through the alphabet a
    number of times equal to the room's sector ID. A becomes B, B becomes C,
    Z becomes A, and so on. Dashes become spaces.

    For example, the real name for qzmt-zixmtkozy-ivhz-343 is
    very encrypted name.

    What is the sector ID of the room where North Pole objects are stored?

    """

    def test_decrypted_name(self):
        self.assertEqual(
            'very encrypted name',
            security_through_obscurity.Room(
                encrypted_name='qzmt-zixmtkozy-ivhz',
                sector_id=343,
                checksum=''
            ).name)

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'security_through_obscurity.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(482, next(
            room.sector_id for room in security_through_obscurity.valid_rooms(puzzle_input)
            if room.name == 'northpole object storage'))
