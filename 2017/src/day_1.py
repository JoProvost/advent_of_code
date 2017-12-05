def captcha(text):
    return sum([int(x) for i, x in enumerate(text)
                if x == text[i-1]])


def captcha_half_way(text):
    return sum([int(x) for i, x in enumerate(text)
                if x == text[i-(len(text)/2)]])
