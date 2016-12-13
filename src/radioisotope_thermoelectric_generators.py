import itertools


class Hashable(object):
    def _key(self):
        raise NotImplementedError()

    def __eq__(self, other):
        return self._key() == other._key()

    def __hash__(self):
        if hasattr(self, '_hash'):
            return self._hash
        self._hash = hash(self._key())
        return self._hash


class Component(Hashable):
    def __init__(self, radioactive_element):
        self.radioactive_element = radioactive_element

    def _key(self):
        return self.radioactive_element

    def __lt__(self, other):
        return self._key() < other._key()


class Microchip(Component):
    pass


class Generator(Component):
    pass


class RadiationContainment(Hashable):
    _empty = None

    def __init__(self, components=tuple()):
        self.generators = frozenset([c for c in components if type(c) is Generator])
        self.microchips = frozenset([c for c in components if type(c) is Microchip])
        self.disconnected_microchips = self.microchips - self.generators

    def create_new(self, with_=None, without=None):
        with_ = with_ or self.empty()
        without = without or self.empty()
        generators = (self.generators | with_.generators) - without.generators
        microchips = (self.microchips | with_.microchips) - without.microchips
        return type(self)(tuple(generators) + tuple(microchips))

    @classmethod
    def empty(cls):
        cls._empty = cls._empty or RadiationContainment()
        return cls._empty

    def _key(self):
        return self.generators, self.microchips


class Elevator(RadiationContainment):
    pass


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
        yield Elevator()
        for moving_content in itertools.combinations((None,) + tuple(self.generators) + tuple(self.microchips), 2):
            elevator = Elevator(moving_content)
            if self.it_will_burn(elevator):
                continue
            yield elevator


class RadioisotopeTestingFacility(Hashable):
    def __init__(self, floors, elevator_level=0):
        self.floors = tuple(floors)
        self.elevator_level = elevator_level

    def _key(self):
        return self.floors, self.elevator_level

    def next_levels(self):
        if self.elevator_level == 0:
            return 1,
        elif self.elevator_level == len(self.floors) - 1:
            return len(self.floors) - 2,
        else:
            return self.elevator_level + 1, self.elevator_level - 1

    def next_possible_states(self, universe):
        for next_level in self.next_levels():
            for elevator in self.floors[self.elevator_level].possible_elevator_outcomes():
                if self.floors[next_level].it_will_burn(elevator):
                    continue
                new_floors = list(self.floors)
                new_floors[self.elevator_level] = new_floors[self.elevator_level].create_new(without=elevator)
                new_floors[next_level] = new_floors[next_level].create_new(with_=elevator)
                new_state = RadioisotopeTestingFacility(floors=new_floors, elevator_level=next_level)
                if new_state in universe:
                    continue
                universe[new_state] = self
                yield new_state

    def all_components_on_last_floor(self):
        return self.floors[0:3] == (Floor.empty(),) * 3

    def send_everything_up(self):
        known_universe = {self: None}

        moves = {self: None}
        steps = 0
        # Dijkstra’s Algorithm, or something that looks like it.... ;)
        while True:
            next_moves = set()
            if not moves:
                raise StopIteration("There is no valid moves...  This maze can't be solved")
            for move in moves:
                if move.all_components_on_last_floor():
                    while move is not None:
                        print(move)
                        move = known_universe[move]
                    return steps
                next_moves |= set(move.next_possible_states(known_universe))
            moves = next_moves
            steps += 1
