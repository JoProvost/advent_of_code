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
