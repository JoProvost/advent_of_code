import re

TAG_REGEX = '\((?P<size>[0-9]+)x(?P<repeat>[0-9]+)\)'


def uncompress_text(text):
    uncompressed = ''
    pos = 0
    for m in re.finditer(TAG_REGEX, text):
        if m.start() >= pos:
            size, repeat = m.groups()
            uncompressed += text[pos:m.start()]
            uncompressed += text[m.end():m.end() + int(size)] * int(repeat)
            pos = m.end() + int(size)
    uncompressed += text[pos:]
    return uncompressed


def uncompress_size_recursive(text):
    uncompressed_size = 0
    pos = 0
    for m in re.finditer(TAG_REGEX, text):
        if m.start() >= pos:
            size, repeat = m.groups()
            uncompressed_size += m.start() - pos
            uncompressed_size += uncompress_size_recursive(
                text[m.end():m.end() + int(size)]) * int(repeat)
            pos = m.end() + int(size)
    uncompressed_size += len(text) - pos
    return uncompressed_size
