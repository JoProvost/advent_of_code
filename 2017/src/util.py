def count(generator):
    return sum(1 for _ in generator)


def first(generator):
    for value in generator:
        return value


def last(generator):
    value = None
    for value in generator:
        pass
    return value


def flatten(l):
    return (item for sublist in l for item in sublist)
