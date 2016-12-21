import ctypes


class IntegerCodec(ctypes.Union):
    class _U(ctypes.Structure):
        _pack_ = 1
        _fields_ = (('_x', ctypes.c_int16), ('_y', ctypes.c_int16))

    _pack_ = 1
    _anonymous_ = ("_u",)
    _fields_ = (('_u', _U), ('_encoded', ctypes.c_int64))

    def encode(self, x, y):
        self._x = x
        self._y = y
        return self._encoded

    def decode(self, encoded):
        self._encoded = encoded
        return (self._x, self._y)


class NullCodec(object):
    def encode(self, x, y):
        return x, y

    def decode(self, encoded):
        return encoded


class Maze(object):
    codec = IntegerCodec()

    def __init__(self, favorite_number):
        self.favorite_number = favorite_number

    def is_wall(self, x, y):
        if x < 0 or y < 0:
            return True
        number = x*x + 3*x + 2*x*y + y + y*y + self.favorite_number
        binary = '{0:b}'.format(number)
        bits = len(binary.replace('0', ''))
        return bits % 2

    def explorable_locations(self, actual, path):
        x, y = self.codec.decode(actual)
        next_locations = (
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        )

        explorable = []
        for x, y in next_locations:
            location = self.codec.encode(x, y)
            if location in path.known:
                continue
            if self.is_wall(x, y):
                path.known[location] = None
                continue
            path.known[location] = actual
            explorable.append(location)

        return explorable

    def explore(self, from_x, from_y, to_x, to_y):
        destination = self.codec.encode(to_x, to_y)
        starting_point = self.codec.encode(from_x, from_y)
        explorable = [starting_point]

        maze_map = MazeMap(starting_point, destination)

        while len(explorable):
            snapshot = tuple(explorable)
            explorable.clear()
            for location in snapshot:
                if destination == location:
                    self.print(maze_map)
                    return maze_map
                explorable.extend(self.explorable_locations(location, maze_map))

        self.print(maze_map)

    def print(self, maze_map, width=60, height=60):
        for y in range(height):
            line = ''.join(maze_map.to_string(self.codec.encode(x, y)) for x in range(width)).rstrip()
            if line == '':
                break
            print(line)


class MazeMap(object):
    def __init__(self, starting_point, destination):
        self.starting_point = starting_point
        self.destination = destination
        self.known = {}
        self._path = ()

    @property
    def path(self):
        try:
            if self._path:
                return self._path
            path = [self.destination]
            location = self.known[self.destination]
            while location != self.starting_point:
                path.append(location)
                location = self.known[location]
            self._path = tuple(reversed(path))
            return self._path
        except KeyError:
            return ()

    def to_string(self, location):
        if location == self.starting_point:
            return 'S'
        if location == self.destination:
            return 'D'
        if location in self.path:
            return 'O'
        if location not in self.known:
            return ' '
        if self.known[location] is None:
            return '#'
        return '.'
