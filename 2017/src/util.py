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


class Ring(object):
    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, i):
        return self.data[i % len(self.data)]

    def __setitem__(self, i, value):
        self.data[i % len(self.data)] = value

    def __getslice__(self, i, j):
        return Ring([self[x] for x in range(i, j)])

    def __setslice__(self, i, j, y):
        for k, v in enumerate(y):
            self[k + i] = v
            if k == j - i - 1:
                break
