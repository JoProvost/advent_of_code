import unittest

import day_1

challenge = (
    "525544371475555531777715244182678432191828599959422153163624294499"
    "836371611929484583857994356254324723996955579177239268156788344983"
    "798211923953632534126352441539712382435846789196376294872332777454"
    "571585154242983211917913991447152351533224731744171918455689136217"
    "926736832548664237668565775962387685495872163657421987124964577373"
    "859775142995943746687616627375552487335145295141162847935252236771"
    "426971851483893328386142598256285484547151265255563392287812855892"
    "612393594185853244637881592957345277534859969398283469975773471418"
    "783133754647451567857715872175192156214559116663427969929941826915"
    "855755799658388164246827461819633526734289749848686992526289612514"
    "686712459658798953149589164668152825962467479272814652684971113914"
    "626879943633461897454753956158758126888644929181733523285939149383"
    "916711124637649319198514584853182934419853656898799689422658583734"
    "837295895953596965157351654258114446253657495376441372314795723729"
    "832445818129116758779171417267471789856726954776663614373243869447"
    "323147325845216645719479781942352813915745214823694328337419356196"
    "339384638562221853595259158835356531943228557971188155934354451546"
    "196284687968587943176796397565434756938535448222634126176854732874"
    "994716386464516842895344539636139887353643493182363552246775478242"
    "255799826285829756386249265246452636617121827617625858244492349718"
    "177612943639639733397621597673154218287897938936229715581946168536"
    "167641472559733575997628559771333268827524127166465828686869716751"
    "532981183123432469834515994913547446362474962462651824783144814387"
    "618313381426397761156433986546632124439917746482264961196989634487"
    "438197898645356697976291115593136239419266394352683414859634226832"
    "156388525576561441814182893497192799899473976914178918516546197642"
    "515185584673995933864949937965722319688553938615493558679454836586"
    "175935486545321172155177699757628981159565417167225912933524353151"
    "822828239332639524124218579582826131921516426223795774323255897128"
    "914563985214819718426576629188525984723664661593596375963114533815"
    "925753811435978185468569542934842888424897217727836135381476665399"
    "6675994784195827214295462389532422825696456457332417366426619555"
)


class TestPart1(unittest.TestCase):
    """
    --- Day 1: Inverse Captcha ---

    The night before Christmas, one of Santa's Elves calls you in a panic. "The
    printer's broken! We can't print the Naughty or Nice List!" By the time you
    make it to sub-basement 17, there are only a few minutes until midnight. "We
    have a big problem," she says; "there must be almost fifty bugs in this
    system, but nothing else can print The List. Stand in this square, quick!
    There's no time to explain; if you can convince them to pay you in stars,
    you'll be able to--" She pulls a lever and the world goes blurry.

    When your eyes can focus again, everything seems a lot more pixelated than
    before. She must have sent you inside the computer! You check the system
    clock: 25 milliseconds until midnight. With that much time, you should be
    able to collect all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each
    day millisecond in the advent calendar; the second puzzle is unlocked when
    you complete the first. Each puzzle grants one star. Good luck!

    You're standing in a room with "digitization quarantine" written in LEDs
    along one wall. The only door is locked, but it includes a small interface.
    "Restricted Area - Strictly No Digitized Users Allowed."

    It goes on to explain that you may only leave by solving a captcha to prove
    you're not a human. Apparently, you only get one millisecond to solve the
    captcha: too fast for a normal human, but it feels like hours to you.

    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list. The
    list is circular, so the digit after the last digit is the first digit in
    the list.

    For example:

     - 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
       second digit and the third digit (2) matches the fourth digit.
     - 1111 produces 4 because each digit (all 1) matches the next.
     - 1234 produces 0 because no digit matches the next.
     - 91212129 produces 9 because the only digit that matches the next one is
       the last digit, 9.

    What is the solution to your captcha?
    """

    def test_simple_matches(self):
        self.assertEqual(3, day_1.captcha("1122"))
        self.assertEqual(4, day_1.captcha("1111"))
        self.assertEqual(0, day_1.captcha("1234"))
        self.assertEqual(9, day_1.captcha("91212129"))

    def test_challenge(self):
        self.assertEqual(1049, day_1.captcha(challenge))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    You notice a progress bar that jumps to 50% completion. Apparently, the door
    isn't yet satisfied, but it did emit a star as encouragement. The
    instructions change:

    Now, instead of considering the next digit, it wants you to consider the
    digit halfway around the circular list. That is, if your list contains 10
    items, only include a digit in your sum if the digit 10/2 = 5 steps forward
    matches it. Fortunately, your list has an even number of elements.

    For example:

    - 1212 produces 6: the list contains 4 items, and all four digits match the
      digit 2 items ahead.
    - 1221 produces 0, because every comparison is between a 1 and a 2.
    - 123425 produces 4, because both 2s match each other, but no other digit
      has a match.
    - 123123 produces 12.
    - 12131415 produces 4.

    What is the solution to your new captcha?
    """

    def test_simple_matches(self):
        self.assertEqual(6, day_1.captcha_half_way("1212"))
        self.assertEqual(0, day_1.captcha_half_way("1221"))
        self.assertEqual(4, day_1.captcha_half_way("123425"))
        self.assertEqual(12, day_1.captcha_half_way("123123"))
        self.assertEqual(4, day_1.captcha_half_way("12131415"))

    def test_challenge(self):
        self.assertEqual(1508, day_1.captcha_half_way(challenge))
