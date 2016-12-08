from collections import Counter


def error_correction(signal_text):
    transmissions = signal_text.splitlines()
    return ''.join(Counter(repeated_character).most_common()[0][0]
                   for repeated_character in  zip(*transmissions))
