def parse_sides(line):
    return tuple(map(int, line.split()))


def is_valid_triangle(line):
    sides = parse_sides(line)
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return (a + b) > c


def how_many_valid_triangles(triangle_list_text):
    return len(tuple(filter(is_valid_triangle, triangle_list_text.splitlines())))
