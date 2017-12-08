from collections import defaultdict

from util import flatten, first


class Tower(object):
    def __init__(self, programs):
        self.sizes = {}
        self.sub_programs = {}

        for program in programs:
            self.parse(*program.split())

    def parse(self, name, size, op=None, *deps):
        self.sizes[name] = int(size.replace("(", "").replace(")", ""))
        self.sub_programs[name] = tuple(dep.replace(",", "") for dep in deps)

    def root(self):
        return next(iter(
            set(self.sub_programs.keys()) -
            set(flatten(self.sub_programs.values()))
        ))

    def size(self, program):
        return self.sizes[program] + sum(self.size(sub) for sub in self.sub_programs[program])

    def is_unbalanced(self, program):
        return len({self.size(sub) for sub in self.sub_programs[program]}) > 1

    def corrected_size(self, program):
        sizes = defaultdict(list)
        for sub in self.sub_programs[program]:
            sizes[self.size(sub)].append(sub)
        unbalanced_size = first(s for s, p in sizes.iteritems() if len(p) == 1) or 0
        balanced_size = next(iter(set(sizes.keys()) - {unbalanced_size}))
        unbalanced_program = sizes[unbalanced_size][0]
        diff = balanced_size - unbalanced_size
        return unbalanced_program, self.sizes[unbalanced_program] + diff

    def unbalanced_subs(self, program):
        z = tuple(self.corrected_size(s) for s in self.sub_programs[program] if self.is_unbalanced(s))
        return z

    def adjustment(self, program):
        for unbalanced_by, should_be in self.unbalanced_subs(program):
            if self.is_unbalanced(unbalanced_by):
                return self.adjustment(unbalanced_by)
            return unbalanced_by, should_be
        return self.corrected_size(program)