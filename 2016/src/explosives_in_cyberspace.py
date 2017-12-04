import re

TAG_REGEX = '\((?P<size>[0-9]+)x(?P<repeat>[0-9]+)\)'


def expand_text(compressed):
    expanded = ''
    pos = 0
    for m in re.finditer(TAG_REGEX, compressed):
        if m.start() >= pos:
            size, repeat = map(int, m.groups())
            expanded += compressed[pos:m.start()]
            expanded += compressed[m.end():m.end() + size] * repeat
            pos = m.end() + size
    expanded += compressed[pos:]
    return expanded


def expanded_size(compressed, recursive=False):
    size = 0
    pos = 0
    for m in re.finditer(TAG_REGEX, compressed):
        if m.start() >= pos:
            data_size, repeat = map(int, m.groups())
            size += m.start() - pos
            data = compressed[m.end():m.end() + data_size]
            if recursive:
                size += expanded_size(data, recursive=True) * repeat
            else:
                size += len(data) * repeat
            pos = m.end() + data_size
    size += len(compressed) - pos
    return size
