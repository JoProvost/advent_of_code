trans_table = str.maketrans({'0': '1', '1': '0'})


def dragon_curve(data):
    inverted_data = ''.join(reversed(data.translate(trans_table)))
    return '{}0{}'.format(data, inverted_data)


def fill_space(seed, size):
    data = seed
    while len(data) < size:
        data = dragon_curve(data)
    return data[:size]


def checksum(data):
    check = ''.join('1' if data[i] == data[i+1] else '0'
                    for i in range(0, len(data), 2))
    if len(check.replace('0', '')) % 2:
        return checksum(check)
    return check

