import math


def simple_algorithm(nb_elves):
    elves = [(i+1, 1) for i in range(nb_elves)]

    while len(elves) > 1:
        for i in range(math.ceil(len(elves)/2)):
            elf, gifts = elves[i]
            next_i = (i+1) % len(elves)
            _, next_gifts = elves[next_i]
            elves[i] = elf, gifts + next_gifts
            del elves[next_i]

    return elves[0][0]


def highest_one_bit(nb_elves):
    nb_bits = len('{0:b}'.format(nb_elves))
    return 1 << (nb_bits - 1)


def josephus_equation(nb_elves):
    # https://en.wikipedia.org/wiki/Josephus_problem
    l = nb_elves - highest_one_bit(nb_elves)
    safe_position = 2 * l + 1
    return safe_position


def simple_algorithm_2(nb_elves):
    elves = [i+1 for i in range(nb_elves)]

    while len(elves) > 2:
        to_remove = math.floor(len(elves) / 2)
        elves.pop(to_remove)
        elves = elves[1:] + [elves[0]]
    return elves[0]
