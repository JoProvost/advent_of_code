def is_passphrase_valid(phrase):
    words = phrase.split()
    unique_words = set(words)
    return len(words) == len(unique_words)


def valid_passphrases(passphrases):
    return [p for p in passphrases if is_passphrase_valid(p)]


def is_passphrase_v2_valid(phrase):
    words = tuple("".join(sorted(w)) for w in phrase.split())
    unique_words = set(words)
    return len(words) == len(unique_words)


def valid_passphrases_v2(passphrases):
    return [p for p in passphrases if is_passphrase_v2_valid(p)]
