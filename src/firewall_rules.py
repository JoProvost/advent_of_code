from collections import namedtuple

import parser


class IPRange(namedtuple('_IPRange', 'start end')):
    def next_ip_not_in_range(self):
        return self.end + 1

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __len__(self):
        return ((self.end - self.start) + 1) & 0xffffffff

    def overlap_or_extends(self, other):
        return self.start in other or \
               self.end in other or \
               other.start in self or \
               other.end in self or \
               self.start == other.end + 1 or \
               self.end == other.start - 1

    def fusion(self, other):
        return IPRange(
            min(self.start, other.start),
            max(self.end, other.end))


class FirewallBreaker(object):
    def __init__(self):
        self.ranges = []

    def configure(self, text):
        parser.parse(
            definition={'(?P<start>.*)-(?P<end>.*)': self._add_range},
            text=text,
            value_type=int)
        self._optimize()

    def first_whitelisted_ip(self, last_ip):
        whitelist = self.whitelist_ranges(last_ip)
        return whitelist[0].start

    def whitelist_ranges(self, last_ip):
        whitelist = [IPRange(self.ranges[i-1].end + 1, self.ranges[i].start - 1) for i in range(1, len(self.ranges))]
        if self.ranges[0].start != 0:
            whitelist.insert(0, IPRange(0, self.ranges[0].start - 1))
        if self.ranges[-1].end != last_ip:
            whitelist.append(IPRange(self.ranges[-1].end + 1, last_ip))
        return whitelist

    def _add_range(self, start, end):
        self.ranges.append(IPRange(start, end))

    def _optimize(self):
        optimized_ranges = []
        for ip_range in sorted(self.ranges):
            if len(optimized_ranges) == 0:
                optimized_ranges.append(ip_range)
            elif optimized_ranges[-1].overlap_or_extends(ip_range):
                optimized_ranges[-1] = optimized_ranges[-1].fusion(ip_range)
            else:
                optimized_ranges.append(ip_range)
        self.ranges = optimized_ranges

