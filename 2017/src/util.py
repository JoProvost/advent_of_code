def count(generator):
    return sum(1 for _ in generator)


def last(generator):
    return tuple(generator)[-1]

