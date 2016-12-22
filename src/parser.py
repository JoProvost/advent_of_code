import re


def parse(definition, text, value_type=lambda x: x):
    for command in text.splitlines():
        for regex, method in definition.items():
            match = re.match(regex, command)
            if match:
                method(**{k: value_type(v) for k, v in match.groupdict().items()})
