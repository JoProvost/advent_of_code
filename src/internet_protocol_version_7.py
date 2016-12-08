def find_abba(address):
    for position in range(len(address) - 3):
        a, b, c, d = address[position:position + 4]
        if (a, b) == (d, c) and a != b:
            yield position


def is_in_brackets(position, address):
    bracket_end = address.find(']', position)
    if bracket_end == -1:
        return False
    bracket_start = address.find('[', position, bracket_end)
    if bracket_start == -1:
        return True
    return False


def supports_tls(address):
    abba_positions = tuple(find_abba(address))
    if len(abba_positions) == 0:
        return False
    for position in abba_positions:
        if is_in_brackets(position, address):
            return False
    return True


def how_many_addresses_suporting_tls(addresses):
    return len([address for address in addresses.splitlines() if supports_tls(address)])
