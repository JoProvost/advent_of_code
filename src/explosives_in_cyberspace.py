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
