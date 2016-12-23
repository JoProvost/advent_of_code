
trap_patterns = (
    '^^.',  # Its left and center tiles are traps, but its right tile is not.
    '.^^',  # Its center and right tiles are traps, but its left tile is not.
    '^..',  # Only its left tile is a trap.
    '..^'   # Only its right tile is a trap.
)


def next_row(row):
    padded_row = '.{}.'.format(row)
    return ''.join('^' if padded_row[i:i+3] in trap_patterns else '.'
                   for i in range(len(row)))


def build_floor(row, nb_rows):
    floor = [row]
    for _ in range(nb_rows - 1):
        row = next_row(row)
        floor.append(row)
    return floor


def count_safe_tiles(rows):
    return len(''.join(rows).replace('^', ''))
