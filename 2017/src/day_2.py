import itertools


def checksum(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)


def checksum_divide(spreadsheet):
    return sum(
        next(a/b for a, b in itertools.permutations(row, 2)
             if b != 0 and a % b == 0)
        for row in spreadsheet)

