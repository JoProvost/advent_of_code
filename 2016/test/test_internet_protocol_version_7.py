import unittest
from os.path import dirname
from os.path import join

import internet_protocol_version_7


class TestPart1(unittest.TestCase):
    """
    --- Day 7: Internet Protocol Version 7 ---

    While snooping around the local network of EBHQ, you compile a list of
    IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd
    like to figure out which IPs support TLS (transport-layer snooping).

    An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or
    ABBA. An ABBA is any four-character sequence which consists of a pair of
    two different characters followed by the reverse of that pair, such as
    xyyx or abba. However, the IP also must not have an ABBA within any
    hypernet sequences, which are contained by square brackets.

    For example:

    - abba[mnop]qrst supports TLS (abba outside square brackets).
    - abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
      even though xyyx is outside square brackets).
    - aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior
      characters must be different).
    - ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
      even though it's within a larger string).

    How many IPs in your puzzle input support TLS?
    """

    def test_address_without_abba_does_not_support_tls(self):
        self.assertFalse(internet_protocol_version_7.supports_tls('abcd[mnop]qrst'))

    def test_abba_outside_brackes_supports_tls(self):
        self.assertTrue(internet_protocol_version_7.supports_tls('abba[mnop]qrst'))
        self.assertTrue(internet_protocol_version_7.supports_tls('abcd[abcd]xyyx'))

    def test_abba_inside_brackes_does_not_support_tls(self):
        self.assertFalse(internet_protocol_version_7.supports_tls('abcd[bddb]xyyx'))

    def test_abba_inside_and_outside_brackes_supports_tls(self):
        self.assertFalse(internet_protocol_version_7.supports_tls('abba[abba]qrst'))

    def test_aaaa_outside_brackes_does_not_support_tls(self):
        self.assertFalse(internet_protocol_version_7.supports_tls('aaaa[mnop]qrst'))

    def test_ioxxoj_outside_brackes_supports_tls(self):
        self.assertTrue(internet_protocol_version_7.supports_tls('ioxxoj[mnop]qrst'))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'internet_protocol_version_7.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(118, internet_protocol_version_7.how_many_addresses_suporting_tls(puzzle_input))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    You would also like to know which IPs support SSL (super-secret
    listening).

    An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere
    in the supernet sequences (outside any square bracketed sections), and a
    corresponding Byte Allocation Block, or BAB, anywhere in the hypernet
    sequences. An ABA is any three-character sequence which consists of the
    same character twice with a different character between them, such as xyx
    or aba. A corresponding BAB is the same characters but in reversed
    positions: yxy and bab, respectively.

    For example:

    - aba[bab]xyz supports SSL (aba outside square brackets with
      corresponding bab within square brackets).
    - xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    - aaa[kek]eke supports SSL (eke in supernet with corresponding kek in
      hypernet; the aaa sequence is not related, because the interior
      character must be different).
    - zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has
      a corresponding bzb, even though zaz and zbz overlap).

    How many IPs in your puzzle input support SSL?
    """

    def test_address_without_any_bab_does_not_support_ssl(self):
        self.assertFalse(internet_protocol_version_7.supports_ssl('abc[def]ghi'))

    def test_bab_outside_brackes_with_aba_inside_brackets_supports_ssl(self):
        self.assertTrue(internet_protocol_version_7.supports_ssl('bab[aba]qrst'))
        self.assertTrue(internet_protocol_version_7.supports_ssl('qrst[aba]bab'))

    def test_aaa_does_not_support_ssl(self):
        self.assertFalse(internet_protocol_version_7.supports_ssl('aaa[aaa]ghi'))

    def test_overlapping_bab_outside_brackes_with_aba_inside_brackets_supports_ssl(self):
        self.assertTrue(internet_protocol_version_7.supports_ssl('zazbz[bzb]cdb'))

    def test_how_many_addresses_suporting_ssl(self):
        self.assertEqual(3, internet_protocol_version_7.how_many_addresses_suporting_ssl(
            'aba[bab]xyz\n'  # yes
            'xyx[xyx]xyx\n'  # no
            'aaa[kek]eke\n'  # yes
            'zazbz[bzb]cdb'  # yes
        ))

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'internet_protocol_version_7.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual(260, internet_protocol_version_7.how_many_addresses_suporting_ssl(puzzle_input))
