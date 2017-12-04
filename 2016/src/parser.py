import re


def parse(definition, text, value_type=lambda x: x):
    commands = text.splitlines() if isinstance(text, str) else text
    for command in commands:
        for regex, method in definition.items():
            match = re.match(regex, command)
            if match:
                method(**{k: value_type(v) for k, v in match.groupdict().items()})
