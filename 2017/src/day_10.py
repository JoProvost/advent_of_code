from util import Ring


def process(size, lengths):
    ring = Ring(x for x in range(0, size))
    pos = 0
    skip = 0

    for length in lengths:
        if length <= len(ring):
            ring[pos:pos + length] = reversed(
                ring[pos:pos + length])
            pos += length + skip
            skip += 1

    return ring
