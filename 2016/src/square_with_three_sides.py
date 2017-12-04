def parse_rows(text):
    return (tuple(map(int, row.split()))
            for row in text.splitlines())


def parse_columns(text):
    rows = tuple(parse_rows(text))

    for row_number in range(0, len(rows), 3):
        for triangle_index in range(len(rows[row_number])):
            yield (
                rows[row_number][triangle_index],
                rows[row_number + 1][triangle_index],
                rows[row_number + 2][triangle_index])


def is_valid_triangle(sides):
    try:
        a, b, c = sorted(sides)
        return (a + b) > c
    except ValueError:
        pass


def how_many_valid_triangles(triangles):
    return len(tuple(filter(is_valid_triangle, triangles)))


