import ctypes
import radioisotope


class WordIndex(object):
    def __init__(self):
        self.words = []

    def index(self, word):
        try:
            return self.words.index(word)
        except ValueError:
            self.words.append(word)
            return self.words.index(word)

    def word(self, index):
        return self.words[index]

    def __iter__(self):
        return iter(self.words)


class FloorStruct(ctypes.Structure):
    word_index = WordIndex()

    _pack_ = 1
    _fields_ = [
        ("generators", ctypes.c_uint8, 8),
        ("microchips", ctypes.c_uint8, 7),
        ("elevator", ctypes.c_uint8, 1),
    ]

    def from_floor(self, floor):
        self.elevator = False

        self.generators = 0
        for generator in floor.generators:
            index = self.word_index.index(generator)
            self.generators |= 1<< index

        self.microchips = 0
        for microchip in floor.microchips:
            index = self.word_index.index(microchip)
            self.microchips |= 1<< index

    def to_floor(self):
        generators = tuple(radioisotope.Generator(w) for i, w in enumerate(self.word_index) if self.generators & (1 << i))
        microchips = tuple(radioisotope.Microchip(w) for i, w in enumerate(self.word_index) if self.microchips & (1 << i))
        return radioisotope.Floor(*(generators + microchips))


class FacilityStruct(ctypes.Union):
    word_index = WordIndex()

    _pack_ = 1
    _fields_ = [
        ("floors", FloorStruct * 4),
        ("encoded_value", ctypes.c_uint64)
    ]

    def from_facility(self, facility):
        for i, f in enumerate(facility.floors):
            self.floors[i].from_floor(f)

        for l, f in enumerate(self.floors):
            f.elevator = (facility.level == l)

    def to_facility(self):
        floors = [f.to_floor() for i, f in enumerate(self.floors)]
        level = next(l for l, f in enumerate(self.floors) if f.elevator)
        return radioisotope.Facility(floors, level)


facility_struct = FacilityStruct()


def encode(facility):
    facility_struct.from_facility(facility)
    return facility_struct.encoded_value


def decode(encoded_facility):
    facility_struct.encoded_value = encoded_facility
    return facility_struct.to_facility()
