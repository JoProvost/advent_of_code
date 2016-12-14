import unittest

from radioisotope import *
import radioisotope_codecs


class TestPart1(unittest.TestCase):
    """
    --- Day 11: Radioisotope Thermoelectric Generators ---

    You come upon a column of four floors that have been entirely sealed off
    from the rest of the building except for a small dedicated lobby. There
    are some radiation warnings and a big sign which reads "Radioisotope
    Testing Facility".

    According to the project status board, this facility is currently being
    used to experiment with Radioisotope Thermoelectric Generators (RTGs, or
    simply "generators") that are designed to be paired with specially-
    constructed microchips. Basically, an RTG is a highly radioactive rock
    that generates electricity through heat.

    The experimental RTGs have poor radiation containment, so they're
    dangerously radioactive. The chips are prototypes and don't have normal
    radiation shielding, but they do have the ability to generate an
    electromagnetic radiation shield when powered. Unfortunately, they can
    only be powered by their corresponding RTG. An RTG powering a microchip
    is still dangerous to other microchips.

    In other words, if a chip is ever left in the same area as another RTG,
    and it's not connected to its own RTG, the chip will be fried. Therefore,
    it is assumed that you will follow procedure and keep chips connected to
    their corresponding RTG when they're in the same room, and away from
    other RTGs otherwise.

    These microchips sound very interesting and useful to your current
    activities, and you'd like to try to retrieve them. The fourth floor of
    the facility has an assembling machine which can make a self-contained,
    shielded computer for you to take with you - that is, if you can bring it
    all of the RTGs and microchips.

    Within the radiation-shielded part of the facility (in which it's safe to
    have these pre-assembly RTGs), there is an elevator that can move between
    the four floors. Its capacity rating means it can carry at most yourself
    and two RTGs or microchips in any combination. (They're rigged to some
    heavy diagnostic equipment - the assembling machine will detach it for
    you.) As a security measure, the elevator will only function if it
    contains at least one RTG or microchip. The elevator always stops on each
    floor to recharge, and this takes long enough that the items within it
    and the items on that floor can irradiate each other. (You can prevent
    this if a Microchip and its Generator end up on the same floor in this
    way, as they can be connected while the elevator is recharging.)

    You make some notes of the locations of each component of interest (your
    puzzle input). Before you don a hazmat suit and start moving things
    around, you'd like to have an idea of what you need to do.

    When you enter the containment area, you and the elevator will start on
    the first floor.

    For example, suppose the isolated area has the following arrangement:

    The first floor contains a hydrogen-compatible microchip and a lithium-
    compatible microchip.
    The second floor contains a hydrogen generator.
    The third floor contains a lithium generator.
    The fourth floor contains nothing relevant.

    As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L
    for Lithium, M for Microchip, and G for Generator), the initial state
    looks like this:

    F4 .  .  .  .  .
    F3 .  .  .  LG .
    F2 .  HG .  .  .
    F1 E  .  HM .  LM

    Then, to get everything up to the assembling machine on the fourth floor,
    the following steps could be taken:

    - Bring the Hydrogen-compatible Microchip to the second floor, which is
      safe because it can get power from the Hydrogen Generator:

      F4 .  .  .  .  .
      F3 .  .  .  LG .
      F2 E  HG HM .  .
      F1 .  .  .  .  LM

    - Bring both Hydrogen-related items to the third floor, which is safe
      because the Hydrogen-compatible microchip is getting power from its
      generator:

      F4 .  .  .  .  .
      F3 E  HG HM LG .
      F2 .  .  .  .  .
      F1 .  .  .  .  LM

    - Leave the Hydrogen Generator on floor three, but bring the Hydrogen-
      compatible Microchip back down with you so you can still use the
      elevator:

      F4 .  .  .  .  .
      F3 .  HG .  LG .
      F2 E  .  HM .  .
      F1 .  .  .  .  LM

    - At the first floor, grab the Lithium-compatible Microchip, which is
      safe because Microchips don't affect each other:

      F4 .  .  .  .  .
      F3 .  HG .  LG .
      F2 .  .  .  .  .
      F1 E  .  HM .  LM

    - Bring both Microchips up one floor, where there is nothing to fry
      them:

      F4 .  .  .  .  .
      F3 .  HG .  LG .
      F2 E  .  HM .  LM
      F1 .  .  .  .  .

    - Bring both Microchips up again to floor three, where they can be
      temporarily connected to their corresponding generators while the
      elevator recharges, preventing either of them from being fried:

      F4 .  .  .  .  .
      F3 E  HG HM LG LM
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - Bring both Microchips to the fourth floor:

      F4 E  .  HM .  LM
      F3 .  HG .  LG .
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - Leave the Lithium-compatible microchip on the fourth floor, but bring
      the Hydrogen-compatible one so you can still use the elevator; this
      is safe because although the Lithium Generator is on the destination
      floor, you can connect Hydrogen-compatible microchip to the Hydrogen
      Generator there:

      F4 .  .  .  .  LM
      F3 E  HG HM LG .
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - Bring both Generators up to the fourth floor, which is safe because
      you can connect the Lithium-compatible Microchip to the Lithium
      Generator upon arrival:

      F4 E  HG .  LG LM
      F3 .  .  HM .  .
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - Bring the Lithium Microchip with you to the third floor so you can
      use the elevator:

      F4 .  HG .  LG .
      F3 E  .  HM .  LM
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - Bring both Microchips to the fourth floor:

      F4 E  HG HM LG LM
      F3 .  .  .  .  .
      F2 .  .  .  .  .
      F1 .  .  .  .  .

    - In this arrangement, it takes 11 steps to collect all of the objects at
      the fourth floor for assembly. (Each elevator stop counts as one step,
      even if nothing is added to or removed from it.)

      In your situation, what is the minimum number of steps required to bring
      all of the objects to the fourth floor?
    """

    def setUp(self):
        radioisotope_codecs.FloorStruct.word_index.words.clear()

    def test_data_structure(self):
        self.assertNotEqual(Microchip('AA'), Microchip('BB'))
        self.assertNotEqual(Generator('AA'), Generator('BB'))
        self.assertEqual(Microchip('AA'), Microchip('AA'))
        self.assertEqual(Microchip('AA'), Generator('AA'))

        facility = Facility(
            level=0,
            floors=(
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
                Floor(),
                Floor(),
                Floor(),
            )
        )

        generator_nikel = (1 << 0)
        microchip_nikel = (1 << 8)
        level = (1<<15)
        self.assertEqual(generator_nikel + microchip_nikel + level, facility.encoded_value)

        facility = Facility(
            level=1,
            floors=(
                Floor(),
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
                Floor(),
                Floor(),
            )
        )

        generator_nikel = (1 << 16)
        microchip_nikel = (1 << 24)
        level = (1 << 31)
        self.assertEqual(generator_nikel + microchip_nikel + level, facility.encoded_value)

        facility = Facility(
            level=2,
            floors=(
                Floor(),
                Floor(),
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
                Floor(),
            )
        )
        generator_nikel = (1 << 32)
        microchip_nikel = (1 << 40)
        level = (1 << 47)
        self.assertEqual(generator_nikel + microchip_nikel + level, facility.encoded_value)

        facility = Facility(
            level=3,
            floors=(
                Floor(),
                Floor(),
                Floor(),
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
            )
        )
        generator_nikel = (1 << 48)
        microchip_nikel = (1 << 56)
        level = (1 << 63)
        self.assertEqual(generator_nikel + microchip_nikel + level, facility.encoded_value)

        facility = radioisotope_codecs.decode(generator_nikel + microchip_nikel + level)
        print(facility)

        facility = Facility(level=0, floors=(
            Floor(Microchip('lithium'), Microchip('hydrogen')),
            Floor(Generator('hydrogen')),
            Floor(Generator('lithium')),
            Floor()))

        data = facility.encoded_value
        new_facility = radioisotope_codecs.decode(data)

        self.assertEqual(data,new_facility.data)

        # All objects are hashable
        hash_set = {Microchip('AA'), Generator('BB')}

    def test_simplest_happy_path(self):
        facility = Facility(
            floors=(
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
                Floor(),
                Floor(),
                Floor(),
            )
        )

        self.assertEqual(3, facility.send_everything_up())

    def test_will_break_as_the_elevator_cant_be_empty(self):
        facility = Facility(
            level=0,
            floors=(
                Floor(),
                Floor(
                    Generator('nikel'),
                    Microchip('nikel')
                ),
                Floor(),
                Floor(),
            )
        )

        with self.assertRaises(StopIteration):
            facility.send_everything_up()

    def test_example(self):

        # The first floor contains
        #  a hydrogen-compatible microchip
        #  and a lithium-compatible microchip.
        # The second floor contains
        #  a hydrogen generator.
        # The third floor contains
        #  a lithium generator.
        # The fourth floor contains nothing relevant.

        facility = Facility(
            floors=(
                Floor(
                    Microchip('hydrogen'),
                    Microchip('lithium'),
                ),
                Floor(
                    Generator('hydrogen'),
               ),
                Floor(
                    Generator('lithium'),
                ),
                Floor(),
            )
        )

        self.assertEqual(11, facility.send_everything_up())

    def test_puzzle(self):

        # The first floor contains
        #  a polonium generator,
        #  a thulium generator,
        #  a thulium-compatible microchip,
        #  a promethium generator,
        #  a ruthenium generator,
        #  a ruthenium-compatible microchip,
        #  a cobalt generator,
        #  and a cobalt-compatible microchip.
        # The second floor contains
        #  a polonium-compatible microchip
        #  and a promethium-compatible microchip.

        facility = Facility(
            floors=(
                Floor(
                    Generator('polonium'),
                    Generator('thulium'),
                    Microchip('thulium'),
                    Generator('promethium'),
                    Generator('ruthenium'),
                    Microchip('ruthenium'),
                    Generator('cobalt'),
                    Microchip('cobalt'),
                ),
                Floor(
                    Microchip('polonium'),
                    Microchip('promethium'),
                ),
                Floor(),
                Floor(),
            )
        )

        self.assertEqual(47, facility.send_everything_up())


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    You step into the cleanroom separating the lobby from the isolated area
    and put on the hazmat suit.

    Upon entering the isolated containment area, however, you notice some
    extra parts on the first floor that weren't listed on the record outside:

    - An elerium generator.
    - An elerium-compatible microchip.
    - A dilithium generator.
    - A dilithium-compatible microchip.

    These work just like the other generators and microchips. You'll have to
    get them up to assembly as well.

    What is the minimum number of steps required to bring all of the objects,
    including these four new ones, to the fourth floor?
    """

    def test_puzzle(self):

        facility = Facility(
            floors=(
                Floor(
                    # From part 1
                    Generator('polonium'),
                    Generator('thulium'),
                    Microchip('thulium'),
                    Generator('promethium'),
                    Generator('ruthenium'),
                    Microchip('ruthenium'),
                    Generator('cobalt'),
                    Microchip('cobalt'),

                    # From part 2
                    Generator('elerium'),
                    Microchip('elerium'),
                    Generator('dilithium'),
                    Microchip('dilithium'),

                ),
                Floor(
                    # From part 1
                    Microchip('polonium'),
                    Microchip('promethium'),
                ),
                Floor(),
                Floor(),
            )
        )

        self.assertEqual(71, facility.send_everything_up())

        # Some statistics of the last run:
        #
        # steps possibilities (time it took) nb_known_states memory_used
        # --------------------------------------------------------------
        # 0 1 (0.001 s) 17 864
        # 1 16 (0.014 s) 211 12384
        # 2 194 (0.074 s) 759 49248
        # 3 548 (0.140 s) 2609 98400
        # 4 1850 (0.421 s) 7134 393312
        # 5 4525 (0.678 s) 11321 786528
        # 6 4187 (1.018 s) 22110 1572960
        # 7 10789 (1.597 s) 31437 1572960
        # 8 9327 (2.269 s) 53639 3145824
        # 9 22202 (3.250 s) 71556 3145824
        # 10 17917 (4.226 s) 114329 6291552
        # 11 42773 (6.491 s) 146562 6291552
        # 12 32233 (8.556 s) 227589 12583008
        # 13 81027 (13.233 s) 309649 12583008
        # 14 82060 (19.981 s) 518425 25165920
        # 15 208776 (32.605 s) 687883 25165920
        # 16 169458 (41.751 s) 975607 50331744
        # 17 287724 (52.847 s) 1266698 50331744
        # 18 291091 (72.391 s) 1784420 100663392
        # 19 517722 (96.432 s) 2252853 100663392
        # 20 468433 (107.588 s) 2919266 201326688
        # 21 666413 (137.685 s) 3552158 201326688
        # 22 632892 (146.031 s) 4448285 201326688
        # 23 896127 (183.801 s) 5361975 201326688
        # 24 913690 (194.038 s) 6471074 402653280
        # 25 1109099 (218.443 s) 7456389 402653280
        # 26 985315 (218.811 s) 8719652 402653280
        # 27 1263263 (267.903 s) 10077574 402653280
        # 28 1357922 (291.652 s) 11701082 805306464
        # 29 1623508 (335.709 s) 13150229 805306464
        # 30 1449147 (339.197 s) 14996894 805306464
        # 31 1846665 (391.406 s) 16850463 805306464
        # 32 1853569 (446.977 s) 18922673 805306464
        # 33 2072210 (590.296 s) 20867820 805306464
        # 34 1945147 (590.484 s) 23109594 1610612832
        # 35 2241774 (506.520 s) 25357287 1610612832
        # 36 2247693 (507.205 s) 27640783 1610612832
        # 37 2283496 (493.074 s) 29868538 1610612832
        # 38 2227755 (495.363 s) 32103291 1610612832
        # 39 2234753 (492.562 s) 34395576 1610612832
        # 40 2292285 (497.545 s) 36385481 1610612832
        # 41 1989905 (457.404 s) 38445506 1610612832
        # 42 2060025 (438.949 s) 40231832 1610612832
        # 43 1786326 (393.589 s) 42080374 1610612832
        # 44 1848542 (373.849 s) 43486949 1610612832
        # 45 1406575 (342.779 s) 45024508 3221225568
        # 46 1537559 (326.248 s) 46247862 3221225568
        # 47 1223354 (269.640 s) 47528415 3221225568
        # 48 1280553 (277.454 s) 48425339 3221225568
        # 49 896924 (205.997 s) 49352048 3221225568
        # 50 926709 (188.218 s) 50016166 3221225568
        # 51 664118 (143.109 s) 50702327 3221225568
        # 52 686161 (126.320 s) 51130538 3221225568
        # 53 428211 (102.457 s) 51580869 3221225568
        # 54 450331 (76.421 s) 51862017 3221225568
        # 55 281148 (56.902 s) 52149914 3221225568
        # 56 287897 (46.478 s) 52295228 3221225568
        # 57 145314 (29.182 s) 52456543 3221225568
        # 58 161315 (23.550 s) 52533922 3221225568
        # 59 77379 (13.873 s) 52618762 3221225568
        # 60 84840 (10.823 s) 52653433 3221225568
        # 61 34671 (5.978 s) 52693207 3221225568
        # 62 39774 (4.739 s) 52712205 3221225568
        # 63 18998 (2.989 s) 52730958 3221225568
        # 64 18753 (4.151 s) 52738140 3221225568
        # 65 7182 (1.127 s) 52747346 3221225568
        # 66 9206 (0.980 s) 52750468 3221225568
        # 67 3122 (0.485 s) 52753142 3221225568
        # 68 2674 (0.278 s) 52753877 3221225568
        # 69 735 (0.090 s) 52754626 3221225568
        # 70 749 (0.066 s) 52754683 3221225568
        # L3 [E co-g co-m di-g di-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [  ]
        # L1 [  ]
        # L0 [  ]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [E di-g di-m]
        # L1 [  ]
        # L0 [  ]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [  ]
        # L1 [E di-g di-m]
        # L0 [  ]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [  ]
        # L1 [  ]
        # L0 [E di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [  ]
        # L1 [E di-g]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [E di-g]
        # L1 [  ]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [E co-g co-m di-g el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g th-m]
        # L2 [  ]
        # L1 [  ]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [  co-g co-m di-g el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [E th-g th-m]
        # L1 [  ]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [E co-g co-m di-g el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g]
        # L2 [  th-m]
        # L1 [  ]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [E di-g th-g th-m]
        # L1 [  ]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [  th-m]
        # L1 [E di-g th-g]
        # L0 [  di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [  th-m]
        # L1 [  ]
        # L0 [E di-g di-m th-g]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [  th-m]
        # L1 [E th-g]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [E th-g th-m]
        # L1 [  ]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [  ]
        # L1 [E th-g th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m]
        # L2 [E th-g]
        # L1 [  th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [E co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g ru-m th-g]
        # L2 [  ]
        # L1 [  th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m th-g]
        # L2 [E ru-g ru-m]
        # L1 [  th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [E co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g th-g]
        # L2 [  ru-m]
        # L1 [  th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [E ru-g ru-m th-g]
        # L1 [  th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ru-m]
        # L1 [E ru-g th-g th-m]
        # L0 [  di-g di-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ru-m]
        # L1 [  th-m]
        # L0 [E di-g di-m ru-g th-g]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ru-m]
        # L1 [E th-g th-m]
        # L0 [  di-g di-m ru-g]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ru-m]
        # L1 [  ]
        # L0 [E di-g di-m ru-g th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ru-m]
        # L1 [E ru-g]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [E ru-g ru-m]
        # L1 [  ]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [  ]
        # L1 [E ru-g ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m el-g el-m po-g po-m pr-g pr-m]
        # L2 [E ru-g]
        # L1 [  ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g co-m el-g el-m po-g po-m pr-g pr-m ru-g]
        # L2 [  ]
        # L1 [  ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m ru-g]
        # L2 [E el-g el-m]
        # L1 [  ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g co-m el-g po-g po-m pr-g pr-m ru-g]
        # L2 [  el-m]
        # L1 [  ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [E el-g el-m ru-g]
        # L1 [  ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  el-m]
        # L1 [E el-g ru-g ru-m]
        # L0 [  di-g di-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  el-m]
        # L1 [  ru-m]
        # L0 [E di-g di-m el-g ru-g th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  el-m]
        # L1 [E ru-g ru-m]
        # L0 [  di-g di-m el-g th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  el-m]
        # L1 [  ]
        # L0 [E di-g di-m el-g ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  el-m]
        # L1 [E el-g]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [E el-g el-m]
        # L1 [  ]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [  ]
        # L1 [E el-g el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g co-m po-g po-m pr-g pr-m]
        # L2 [E el-g]
        # L1 [  el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g co-m el-g po-g po-m pr-g pr-m]
        # L2 [  ]
        # L1 [  el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  el-g po-g po-m pr-g pr-m]
        # L2 [E co-g co-m]
        # L1 [  el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g el-g po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [  el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [E co-g co-m el-g]
        # L1 [  el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [E co-g el-g el-m]
        # L0 [  di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [  el-m]
        # L0 [E co-g di-g di-m el-g ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [E el-g el-m]
        # L0 [  co-g di-g di-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [  ]
        # L0 [E co-g di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  co-m]
        # L1 [E co-g]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [E co-g co-m]
        # L1 [  ]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [  ]
        # L1 [E co-g co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  po-g po-m pr-g pr-m]
        # L2 [E co-g]
        # L1 [  co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g po-g po-m pr-g pr-m]
        # L2 [  ]
        # L1 [  co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  co-g pr-g pr-m]
        # L2 [E po-g po-m]
        # L1 [  co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E co-g po-g pr-g pr-m]
        # L2 [  po-m]
        # L1 [  co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [E co-g po-g po-m]
        # L1 [  co-m]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  po-m]
        # L1 [E co-g co-m po-g]
        # L0 [  di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  po-m]
        # L1 [  co-m]
        # L0 [E co-g di-g di-m el-g el-m po-g ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  po-m]
        # L1 [E co-g co-m]
        # L0 [  di-g di-m el-g el-m po-g ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  po-m]
        # L1 [  ]
        # L0 [E co-g co-m di-g di-m el-g el-m po-g ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  po-m]
        # L1 [E po-g]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [E po-g po-m]
        # L1 [  ]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [  ]
        # L1 [E po-g po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-g pr-m]
        # L2 [E po-g]
        # L1 [  po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E po-g pr-g pr-m]
        # L2 [  ]
        # L1 [  po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-m]
        # L2 [E po-g pr-g]
        # L1 [  po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-m]
        # L2 [  ]
        # L1 [E po-g po-m pr-g]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  pr-m]
        # L2 [E pr-g]
        # L1 [  po-g po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [E pr-g pr-m]
        # L2 [  ]
        # L1 [  po-g po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  ]
        # L2 [E pr-g pr-m]
        # L1 [  po-g po-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  ]
        # L2 [  ]
        # L1 [E po-g po-m pr-g pr-m]
        # L0 [  co-g co-m di-g di-m el-g el-m ru-g ru-m th-g th-m]
        # --------------------------------------
        # L3 [  ]
        # L2 [  ]
        # L1 [  po-m pr-m]
        # L0 [E co-g co-m di-g di-m el-g el-m po-g pr-g ru-g ru-m th-g th-m]
        # --------------------------------------
