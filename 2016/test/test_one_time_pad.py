import unittest
import one_time_pad


class TestPart1(unittest.TestCase):
    """
    --- Day 14: One-Time Pad ---

    In order to communicate securely with Santa while you're on this mission,
    you've been using a one-time pad that you generate using a pre-agreed
    algorithm. Unfortunately, you've run out of keys in your one-time pad,
    and so you need to generate some more.

    To generate keys, you first get a stream of random data by taking the MD5
    of a pre-arranged salt (your puzzle input) and an increasing integer
    index (starting with 0, and represented in decimal); the resulting MD5
    hash should be represented as a string of lowercase hexadecimal digits.

    However, not all of these MD5 hashes are keys, and you need 64 new keys
    for your one-time pad. A hash is a key only if:

    - It contains three of the same character in a row, like 777.
      Only consider the first such triplet in a hash.
    - One of the next 1000 hashes in the stream contains that same
      character five times in a row, like 77777.

    Considering future hashes for five-of-a-kind sequences does not cause
    those hashes to be skipped; instead, regardless of whether the current
    hash is a key, always resume testing for keys starting with the very next
    hash.

    For example, if the pre-arranged salt is abc:

    - The first index which produces a triple is 18, because the MD5 hash
      of abc18 contains ...cc38887a5.... However, index 18 does not count
      as a key for your one-time pad, because none of the next thousand
      hashes (index 19 through index 1018) contain 88888.
    - The next index which produces a triple is 39; the hash of abc39
      contains eee. It is also the first key: one of the next thousand
      hashes (the one at index 816) contains eeeee.
    - None of the next six triples are keys, but the one after that, at
      index 92, is: it contains 999 and index 200 contains 99999.
    - Eventually, index 22728 meets all of the criteria to generate the
      64th key.

    So, using our example salt of abc, index 22728 produces the 64th key.

    Given the actual salt in your puzzle input, what index produces your 64th
    one-time pad key?

    Your puzzle input is qzyelonm.
    """

    def test_example(self):
        key_entries = one_time_pad.keys_generator('abc')

        self.assertEqual(22728, key_entries[-1].index)

    def test_lindycoder_puzzle(self):
        key_entries = one_time_pad.keys_generator('jlmsuwbz')

        self.assertEqual(35186, key_entries[-1].index)

    def test_puzzle(self):
        key_entries = one_time_pad.keys_generator('qzyelonm')

        # The answer that I validated first, and that should be the right one is.
        self.assertEqual(15189, key_entries[-1].index)

        # Weird, it is one key less than what was expected...  looks like a bug in the validator.
        self.assertEqual(15168, key_entries[-2].index)

        # As you can see, the last 7 entries are all validated by index 15311
        #
        # 57 Entry(digest='24c3cbe0920a6082221ce188406813e8', index=14369, triple='2', validation_index=15311)
        # 58 Entry(digest='4399288d81ddc222b5c6c4724ec33943', index=14371, triple='2', validation_index=15311)
        # 59 Entry(digest='d2226ad20bde2f3dc5191d4ee974bc37', index=14433, triple='2', validation_index=15311)
        # 60 Entry(digest='f057d15c2220cc17df2b924b4d5419b0', index=14741, triple='2', validation_index=15311)
        # 61 Entry(digest='ad22219773e274c333d9438e674cc29a', index=14967, triple='2', validation_index=15311)
        # 62 Entry(digest='03194122203c5f6df22d87027ec9f7a0', index=15168, triple='2', validation_index=15311)
        # 63 Entry(digest='d42b65773ecfe30e222196caba74e911', index=15189, triple='2', validation_index=15311)
        #
        # It is possible that the validator is not sorting properly the keys with their initial index...


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    Of course, in order to make this process even more secure, you've also
    implemented key stretching.

    Key stretching forces attackers to spend more time generating hashes.
    Unfortunately, it forces everyone else to spend more time, too.

    To implement key stretching, whenever you generate a hash, before you use
    it, you first find the MD5 hash of that hash, then the MD5 hash of that
    hash, and so on, a total of 2016 additional hashings. Always use
    lowercase hexadecimal representations of hashes.

    For example, to find the stretched hash for index 0 and salt abc:

    - Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
    - Then, find the MD5 hash of that hash:
      eec80a0c92dc8a0777c619d9bb51e910.
    - Then, find the MD5 hash of that hash:
      16062ce768787384c81fe17a7a60c7e3.
    - ...repeat many times...
    - Then, find the MD5 hash of that hash:
      a107ff634856bb300138cac6568c0f24.

    So, the stretched hash for index 0 in this situation is a107ff.... In the
    end, you find the original hash (one use of MD5), then find the hash-of-
    the-previous-hash 2016 times, for a total of 2017 uses of MD5.

    The rest of the process remains the same, but now the keys are entirely
    different. Again for salt abc:

    - The first triple (222, at index 5) has no matching 22222 in the next
      thousand hashes.
    - The second triple (eee, at index 10) hash a matching eeeee at index
      89, and so it is the first key.
    - Eventually, index 22551 produces the 64th key (triple fff with
      matching fffff at index 22859.

    Given the actual salt in your puzzle input and using 2016 extra MD5 calls
    of key stretching, what index now produces your 64th one-time pad key?
    """

    def test_example(self):
        key_entries = one_time_pad.keys_generator('abc', iterations=2017)

        self.assertEqual(22551, key_entries[-1].index)

    def test_lindycoder_puzzle(self):
        key_entries = one_time_pad.keys_generator('jlmsuwbz', iterations=2017)

        self.assertEqual(22429, key_entries[-1].index)

    def test_puzzle(self):
        key_entries = one_time_pad.keys_generator('qzyelonm', iterations=2017)

        self.assertEqual(20864, key_entries[-1].index)
