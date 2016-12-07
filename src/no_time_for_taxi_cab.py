from collections import namedtuple

Coordinates = namedtuple('Coordinates', 'x y')

NORTH = Coordinates(0, 1)
SOUTH = Coordinates(0, -1)
EAST = Coordinates(1, 0)
WEST = Coordinates(-1, 0)

CLOCKWISE_HEADINGS = [
    NORTH,
    EAST,
    SOUTH,
    WEST
]

LEFT = 'L'
RIGHT = 'R'


class EasterBunnyNavigationSystem(object):
    location = Coordinates(0, 0)
    heading_offset = 0

    def __init__(self):
        self.visited_places = set()
        self.locations_already_visited = list()

    def navigate(self, directions):
        for direction in directions.split(', '):
            self._turn(direction[0])
            self._move(int(direction[1:]))

    def how_many_blocks_away(self):
        return _distance(self.location)

    def how_many_blocks_away_is_first_location_twice_visited(self):
        location = self.locations_already_visited[0]
        return _distance(location)

    def _turn(self, letter):
        if letter is RIGHT:
            self.heading_offset = (self.heading_offset + 1) % len(CLOCKWISE_HEADINGS)
        else:
            self.heading_offset = (self.heading_offset - 1) % len(CLOCKWISE_HEADINGS)

    def _move(self, steps):
        for _ in range(steps):
            self.location = Coordinates(
                self.location.x + CLOCKWISE_HEADINGS[self.heading_offset].x,
                self.location.y + CLOCKWISE_HEADINGS[self.heading_offset].y
            )
            if self.location in self.visited_places:
                self.locations_already_visited.append(self.location)
            else:
                self.visited_places.add(self.location)


def _distance(location):
    return abs(location.x) + abs(location.y)
