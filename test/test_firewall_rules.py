import unittest
from os.path import dirname

from os.path import join

from firewall_rules import *


class TestPart1(unittest.TestCase):
    """
    --- Day 20: Firewall Rules ---

    You'd like to set up a small hidden computer here so you can use it to
    get back into the network later. However, the corporate firewall only
    allows communication with certain external IP addresses.

    You've retrieved the list of blocked IPs from the firewall, but the list
    seems to be messy and poorly maintained, and it's not clear which IPs are
    allowed. Also, rather than being written in dot-decimal notation, they
    are written as plain 32-bit integers, which can have any value from 0
    through 4294967295, inclusive.

    For example, suppose only the values 0 through 9 were valid, and that you
    retrieved the following blacklist:

    5-8
    0-2
    4-7

    The blacklist specifies ranges of IPs (inclusive of both the start and
    end value) that are not allowed. Then, the only IPs that this firewall
    allows are 3 and 9, since those are the only numbers not in any range.

    Given the list of blocked IPs you retrieved from the firewall (your
    puzzle input), what is the lowest-valued IP that is not blocked?
    """

    def test_example(self):
        fw = FirewallBreaker()
        fw._add_range(5, 8)
        fw._add_range(0, 2)
        fw._add_range(4, 7)
        fw._optimize()

        self.assertEqual(3, fw.first_whitelisted_ip(9))

    def test_some_more(self):

        fw = FirewallBreaker()
        fw._add_range(0, 4)
        fw._add_range(0, 2)
        fw._add_range(0, 5)
        fw._optimize()

        print(fw.ranges)

        self.assertEqual(6, fw.first_whitelisted_ip(9))

    def test_parser(self):
        fw = FirewallBreaker()
        fw.configure(
            '5-8\n'
            '0-2\n'
            '4-7\n')
        self.assertEqual(3, fw.first_whitelisted_ip(9))

    def test_puzzle(self):
        with open(join(dirname(__file__), 'resources', 'firewall_rules.txt')) as f:
            puzzle_input = f.read()

        fw = FirewallBreaker()
        fw.configure(puzzle_input)
        self.assertEqual(14975795, fw.first_whitelisted_ip(0xffffffff))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    How many IPs are allowed by the blacklist?
    """

    def test_example(self):
        fw = FirewallBreaker()
        fw._add_range(5, 8)
        fw._add_range(0, 2)
        fw._add_range(4, 7)
        fw._optimize()

        whitelist = fw.whitelist_ranges(9)
        nb_ips = sum([len(r) for r in whitelist])
        self.assertEqual(2, nb_ips)

    def test_puzzle(self):
        with open(join(dirname(__file__), 'resources', 'firewall_rules.txt')) as f:
            puzzle_input = f.read()

        fw = FirewallBreaker()
        fw.configure(puzzle_input)
        whitelist = fw.whitelist_ranges(0xffffffff)
        nb_ips = sum([len(r) for r in whitelist])
        self.assertEqual(101, nb_ips)
