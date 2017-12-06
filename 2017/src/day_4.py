def is_passphrase_valid(phrase, trans=str):
    words = tuple(trans(w) for w in phrase.split())
    unique_words = set(words)
    return len(words) == len(unique_words)


def valid_passphrases(passphrases, trans=str):
    return [p for p in passphrases if is_passphrase_valid(p, trans=trans)]


def sorted_word(word):
    return "".join(sorted(word))
