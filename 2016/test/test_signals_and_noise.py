import unittest
from os.path import dirname

from os.path import join

import signals_and_noise


class TestPart1(unittest.TestCase):
    """
    --- Day 6: Signals and Noise ---

    Something is jamming your communications with Santa. Fortunately, your
    signal is only partially jammed, and protocol in situations like this is
    to switch to a simple repetition code to get the message through.

    In this model, the same message is sent repeatedly. You've recorded the
    repeating message signal (your puzzle input), but the data seems quite
    corrupted - almost too badly to recover. Almost.

    All you need to do is figure out which character is most frequent for
    each position. For example, suppose you had recorded the following
    messages:

    eedadn
    drvtee
    eandsr
    raavrd
    atevrs
    tsrnev
    sdttsa
    rasrtv
    nssdts
    ntnada
    svetve
    tesnvt
    vntsnd
    vrdear
    dvrsen
    enarar

    The most common character in the first column is e; in the second, a; in
    the third, s, and so on. Combining these characters returns the error-
    corrected message, easter.

    Given the recording in your puzzle input, what is the error-corrected
    version of the message being sent?
    """

    def test_error_correction(self):
        valid_message = signals_and_noise.error_corrected_message(
            'eedadn\n'
            'drvtee\n'
            'eandsr\n'
            'raavrd\n'
            'atevrs\n'
            'tsrnev\n'
            'sdttsa\n'
            'rasrtv\n'
            'nssdts\n'
            'ntnada\n'
            'svetve\n'
            'tesnvt\n'
            'vntsnd\n'
            'vrdear\n'
            'dvrsen\n'
            'enarar\n')
        self.assertEqual('easter', valid_message)

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'signals_and_noise.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual('ikerpcty', signals_and_noise.error_corrected_message(puzzle_input))


class TestPart2(unittest.TestCase):
    """
    --- Part Two ---

    Of course, that would be the message - if you hadn't agreed to use a
    modified repetition code instead.

    In this modified code, the sender instead transmits what looks like
    random data, but for each character, the character they actually want to
    send is slightly less likely than the others. Even after signal-jamming
    noise, you can look at the letter distributions in each column and choose
    the least common letter to reconstruct the original message.

    In the above example, the least common character in the first column is a;
    in the second, d, and so on. Repeating this process for the remaining
    characters produces the original message, advent.

    Given the recording in your puzzle input and this new decoding
    methodology, what is the original message that Santa is trying to send?
    """

    def test_error_correction(self):
        valid_message = signals_and_noise.hidden_message(
            'eedadn\n'
            'drvtee\n'
            'eandsr\n'
            'raavrd\n'
            'atevrs\n'
            'tsrnev\n'
            'sdttsa\n'
            'rasrtv\n'
            'nssdts\n'
            'ntnada\n'
            'svetve\n'
            'tesnvt\n'
            'vntsnd\n'
            'vrdear\n'
            'dvrsen\n'
            'enarar\n')
        self.assertEqual('advent', valid_message)

    def test_puzzle_input(self):
        with open(join(dirname(__file__), 'resources', 'signals_and_noise.txt')) as f:
            puzzle_input = f.read()
        self.assertEqual('uwpfaqrq', signals_and_noise.hidden_message(puzzle_input))
