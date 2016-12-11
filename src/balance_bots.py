import re
from collections import defaultdict


class MicrochipConsumer(object):
    def __init__(self):
        self.microchips = []

    def process_microchip(self, microchip_value):
        self.microchips.append(microchip_value)

    def was_responsible_of(self, low_value, high_value):
        return False


class BalanceBot(MicrochipConsumer):
    def __init__(self, consumers, gives_low_to, gives_high_to):
        super().__init__()
        self.consumers = consumers
        self.gives_low_to = gives_low_to
        self.gives_high_to = gives_high_to
        self.microchips_sent = []

    def process_microchip(self, microchip_value):
        self.microchips = sorted(self.microchips + [microchip_value])
        if len(self.microchips) == 2:
            low_value, high_value = self.microchips
            self.microchips_sent.append((low_value, high_value))
            self.microchips.clear()
            self.consumers[self.gives_low_to].process_microchip(low_value)
            self.consumers[self.gives_high_to].process_microchip(high_value)

    def was_responsible_of(self, low_value, high_value):
        return (low_value, high_value) in self.microchips_sent


class MicrochipsFactory(object):
    def __init__(self):
        self.consumers = defaultdict(MicrochipConsumer)

    def distribute_microchip(self, microchip_consumer, value):
        self.consumers[microchip_consumer].process_microchip(int(value))

    def define_bot(self, microchip_consumer, gives_low_to, gives_high_to):
        self.consumers[microchip_consumer] = BalanceBot(self.consumers, gives_low_to, gives_high_to)

    def who_was_responsible_for(self, low_value, high_value):
        return next(key for key, value in self.consumers.items() if value.was_responsible_of(low_value, high_value))

    def execute(self, text):
        parse(
            definition={
                '(?P<microchip_consumer>bot [0-9]*)'
                ' gives low to (?P<gives_low_to>.*)'
                ' and high to (?P<gives_high_to>.*)': self.define_bot},
            text=text)
        parse(
            definition={
                'value (?P<value>[0-9]*)'
                ' goes to (?P<microchip_consumer>.*)': self.distribute_microchip},
            text=text)


def parse(definition, text):
    for command in text.splitlines():
        for regex, method in definition.items():
            match = re.match(regex, command)
            if match:
                method(**{k: v for k, v in match.groupdict().items()})
