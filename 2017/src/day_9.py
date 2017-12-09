def parse(text):
    score, _ = parse_with_garbage(text)
    return score


def parse_with_garbage(text):
    score = 0
    level = 0
    garbage_count = 0
    garbage = False
    escaped = False
    for x in text:
        if escaped:
            escaped = False
        elif x == '!':
            escaped = True
        elif x == '>':
            garbage = False
        elif garbage:
            garbage_count += 1
        elif x == '<':
            garbage = True
        elif x == '{':
            level +=1
        elif x == '}':
            score += level
            level -= 1
    return score, garbage_count
