from collections import namedtuple

import parser


class NodeGrid(object):
    def __init__(self):
        self.nodes = {}

    def configure(self, text):
        parser.parse(
            definition={
                '/dev/grid/node-x(?P<x>[0-9]*)-y(?P<y>[0-9]*) *(?P<size>[0-9]*)T *(?P<used>[0-9]*)T *(?P<avail>[0-9]*)T.*':
                    self._add_node},
            text=text,
            value_type=int)

    def _add_node(self, x, y, size, used, avail):
        self.nodes[x, y] = Node(x, y, size, used, avail)

    def viable_pairs(self):
        viable_pairs = 0
        for a in self.nodes.values():
            for b in self.nodes.values():
                if a.used > 0 and a != b and a.fit_in(b):
                    viable_pairs += 1
        return viable_pairs


class Node(namedtuple('_Node', 'x, y, size, used, avail')):

    def fit_in(self, other):
        return self.used <= other.avail
