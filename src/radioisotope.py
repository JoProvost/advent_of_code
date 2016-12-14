import itertools
import time
import sys

import radioisotope_codecs


class Microchip(str):
    pass


class Generator(str):
    pass


class RadiationContainment(object):
    def __init__(self, *components):
        self.generators = frozenset(c for c in components if type(c) is Generator)
        self.microchips = frozenset(c for c in components if type(c) is Microchip)

    @property
    def disconnected_microchips(self):
        return self.microchips - self.generators

    def create_new(self, with_=None, without=None):
        with_ = with_ or RadiationContainment()
        without = without or RadiationContainment()
        generators = (self.generators | with_.generators) - without.generators
        microchips = (self.microchips | with_.microchips) - without.microchips
        return type(self)(*(tuple(generators) + tuple(microchips)))

    def is_empty(self):
        return len(self.generators) == 0 and len(self.microchips) == 0

    def __repr__(self):
        return ' '.join(sorted(
            tuple(g[0:2]+'-g' for g in self.generators) +
            tuple(m[0:2]+'-m' for m in self.microchips)))

    def __str__(self):
        return repr(self)


class Floor(RadiationContainment):
    def it_will_burn(self, elevator):
        generators = self.generators | elevator.generators
        microchips = self.microchips | elevator.microchips
        disconnected_microchips = microchips - generators

        if elevator.generators and elevator.disconnected_microchips:
            return True

        if self.generators and self.disconnected_microchips:
            return True

        if generators and disconnected_microchips:
            return True

        if elevator.generators | elevator.microchips:
            return False

        return True

    def possible_elevator_outcomes(self):
        for moving_content in itertools.combinations((None,) + tuple(self.generators) + tuple(self.microchips), 2):
            elevator = RadiationContainment(*moving_content)
            if self.it_will_burn(elevator):
                continue
            yield elevator


class Facility(object):
    def __init__(self, floors, level=0):
        self.floors = floors
        self.level = level
        self.encoded_value = radioisotope_codecs.encode(self)

    def __repr__(self):
        return '\n'.join('L{} [{} {}]'.format(l, 'E' if l == self.level else ' ', f) for l, f in reversed(tuple(enumerate(self.floors))))

    def __str__(self):
        return repr(self)

    def next_levels(self):
        if self.level == 0:
            return 1,
        elif self.level == len(self.floors) - 1:
            return len(self.floors) - 2,
        else:
            return self.level + 1, self.level - 1

    def next_states(self, known_states):
        next_states = []
        for next_level in self.next_levels():
            for elevator in self.floors[self.level].possible_elevator_outcomes():
                if self.floors[next_level].it_will_burn(elevator):
                    continue
                new_floors = list(self.floors)
                new_floors[self.level] = new_floors[self.level].create_new(without=elevator)
                new_floors[next_level] = new_floors[next_level].create_new(with_=elevator)
                new_state = Facility(floors=new_floors, level=next_level)
                if new_state.encoded_value in known_states:
                    continue
                known_states[new_state.encoded_value] = self.encoded_value
                next_states.append(new_state.encoded_value)
        return next_states

    def all_components_on_last_floor(self):
        return all(f.is_empty() for f in self.floors[0:3])

    def send_everything_up(self):
        known_states = {self.encoded_value: None}

        next_states = [self.encoded_value]
        steps = 0
        # Dijkstra’s Algorithm, or something that looks like it.... ;)
        while next_states:
            start = time.time()
            i = 0
            states = next_states
            next_states = []
            for move_integer in states:
                i += 1
                state = radioisotope_codecs.decode(move_integer)
                if state.all_components_on_last_floor():
                    print_path(state, known_states)
                    return steps
                next_states.extend(state.next_states(known_states))
            end = time.time()

            print(steps, i, '({0:.3f} s)'.format(end - start), len(known_states), sys.getsizeof(known_states), file=sys.stderr)
            steps += 1
        raise StopIteration("There is no valid moves...  This maze can't be solved")


def print_path(final_state, known_states):
    encoded_state = final_state.encoded_value
    while encoded_state:
        print(radioisotope_codecs.decode(encoded_state), file=sys.stderr)
        print('--------------------------------------', file=sys.stderr)
        encoded_state = known_states[encoded_state]
