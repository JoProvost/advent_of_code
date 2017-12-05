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