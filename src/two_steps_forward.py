import hashlib
import operator


class Path(object):

    start_location = (0, 0)
    moves = {
        'U': (0, -1),
        'D': (0, +1),
        'L': (-1, 0),
        'R': (+1, 0),
    }

    def __init__(self, path=''):
        self._path = path

    @property
    def location(self):
        l = self.start_location
        for d in self._path:
            l = move(l, self.moves[d])
        return l

    def next(self, dimensions, open_doors):
        actual_location = self.location
        return tuple(
            Path(self._path + d) for d in self.moves
            if in_bounds(move(actual_location, self.moves[d]), dimensions) and d in open_doors)

    def __str__(self):
        return self._path

    def __len__(self):
        return len(self._path)


class DisabledSecurity(object):
    def open_doors(self, path):
        return 'UDLR'


class EasterBunnyVaultSecurity(object):
    doors = 'UDLR'

    def __init__(self, passcode):
        self.passcode = passcode

    def open_doors(self, path):
        md5_hash = hashlib.md5('{}{}'.format(self.passcode, path).encode('ascii'))
        locked = md5_hash.hexdigest()[:4]
        return ''.join(door for i, door in enumerate(self.doors) if locked[i] in 'bcdef')


class Maze(object):

    def __init__(self, security, width=4, height=4):
        self.security = security
        self.dimensions = (width, height)

    def best_path_to(self, x, y):
        return self._path_to(x, y, until_the_end=False)

    def worst_path_to(self, x, y):
        return self._path_to(x, y, until_the_end=True)

    def _path_to(self, x, y, until_the_end=False):
        destination = (x, y)
        paths = (Path(),)

        longest_path = None

        while paths:
            next_paths = []
            for path in paths:
                if path.location == destination:
                    if until_the_end:
                        longest_path = path
                        continue
                    else:
                        return path
                open_doors = self.security.open_doors(path)
                next_paths.extend(path.next(self.dimensions, open_doors))
            paths = tuple(next_paths)

        return longest_path


def move(location, offset):
    return location[0] + offset[0], location[1] + offset[1]


def in_bounds(location, dimensions):
    return all(map(operator.lt, location, dimensions)) and \
           all(map(operator.ge, location, (0, 0)))
