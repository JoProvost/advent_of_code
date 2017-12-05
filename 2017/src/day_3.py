import math


def location_of(number):
    root = int(math.ceil(math.sqrt(number)))
    if root % 2 == 0:
        root += 1
    dist = int(math.floor(root / 2))
    side = (root - 1)
    diff = (root * root - number)

    if diff == 0:
        return dist, dist
    if diff < side:
        return dist - diff, dist
    if diff < 2 * side:
        return -dist, dist - diff + side
    if diff < 3 * side:
        return -dist + diff - 2 * side, -dist
    if diff < 4 * side:
        return dist, -dist + diff - 3 * side


def moves_for(location):
    return sum((abs(pos) for pos in location))


def index_of(location):
    dist = max((abs(pos) for pos in location))
    root = 2 * dist + 1
    side = (root - 1)
    number = root * root

    if location[1] == dist:
        return number - dist + location[0]
    if location[0] == -dist:
        return number - side - dist + location[1]
    if location[1] == -dist:
        return number - (2*side) - dist - location[0]
    if location[0] == dist:
        return number - (3*side) - dist - location[1]


def neighbors(location):
    x, y = location
    return ((x-1, y-1), (x, y-1), (x+1, y-1),
            (x+1, y), (x+1, y+1), (x, y+1),
            (x-1, y+1), (x-1, y))


def sum_of_neighbors(location, l):
    return sum(l[index_of(n) - 1] for n in neighbors(location) if index_of(n) <= len(l))


def spiral_for(cond):
    l = [1]
    while not cond(l[-1]):
        l.append(sum_of_neighbors(location_of(len(l) + 1), l))

    return l
