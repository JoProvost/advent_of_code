import hashlib


def get_password_for_door(door_id):
    password = ''
    index = 0

    while len(password) < 8:
        hexdigest = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
        if hexdigest[:5] == '00000':
            password += hexdigest[5]
        index += 1

    return password
