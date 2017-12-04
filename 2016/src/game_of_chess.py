import hashlib


def first_algorithm(door_id):
    password = ''
    index = 0

    while len(password) < 8:
        digest = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
        if digest[:5] == '00000':
            password += digest[5]
        index += 1

    return password


def second_algorithm(door_id):
    password = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    index = 0

    while ' ' in password:
        digest = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
        if digest[:5] == '00000':
            try:
                if password[int(digest[5], 16)] == ' ':
                    password[int(digest[5], 16)] = digest[6]
            except IndexError:
                pass
        index += 1

    return ''.join(password)
