import collections

Detection = collections.namedtuple(
    'Detection', 'pos text inv_text in_brackets')


def _detect_palindromes(size, address):
    for pos in range(len(address) - (size - 1)):
        text = address[pos:pos + size]
        if _valid_palindrome(text):
            yield Detection(pos, text, _reverse_palindrome(text), _in_brackets(pos, address))


def _valid_palindrome(palindrome):
    if palindrome == palindrome[0] * len(palindrome):
        return False
    for i in range(len(palindrome)):
        if palindrome[i] != palindrome[-i-1]:
            return False
    return True


def _reverse_palindrome(palindrome):
    if len(palindrome) == 4:
        a, b, c, d = palindrome
        return ''.join((b, a, d, c))
    if len(palindrome) == 3:
        a, b, c = palindrome
        return ''.join((b, a, b))


def _in_brackets(position, address):
    bracket_end = address.find(']', position)
    if bracket_end == -1:
        return False
    bracket_start = address.find('[', position, bracket_end)
    if bracket_start == -1:
        return True
    return False


def supports_tls(address):
    detections = tuple(_detect_palindromes(4, address))
    if len(detections) == 0:
        return False
    for detection in detections:
        if detection.in_brackets:
            return False
    return True


def supports_ssl(address):
    detections = tuple(_detect_palindromes(3, address))
    for bab in detections:
        for aba in detections:
            if bab.text == aba.inv_text and bab.in_brackets != aba.in_brackets:
               return True
    return False


def how_many_addresses_suporting_tls(addresses):
    return len([address for address in addresses.splitlines() if supports_tls(address)])


def how_many_addresses_suporting_ssl(addresses):
    return len([address for address in addresses.splitlines() if supports_ssl(address)])
