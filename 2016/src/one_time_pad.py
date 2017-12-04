import hashlib
import collections
import re
from operator import attrgetter


def keys_generator(salt, iterations=1):
    """
    To generate digests, you first get a stream of random data by taking the MD5
    of a pre-arranged salt (your puzzle input) and an increasing integer
    index (starting with 0, and represented in decimal); the resulting MD5
    hash should be represented as a string of lowercase hexadecimal digits.

    However, not all of these MD5 hashes are digests, and you need 64 new digests
    for your one-time pad. A hash is a digest only if:

    - It contains three of the same character in a row, like 777.
      Only consider the first such triplet in a hash.
    - One of the next 1000 hashes in the stream contains that same
      character five times in a row, like 77777.

    :param salt:
    :return:
    """

    index = 0
    known = []
    valid = []

    while len(valid) < 64:
        digest = encode('{}{}'.format(salt, index), iterations=iterations)
        entry = Entry(digest=digest, index=index, triple=find_triple(digest), validation_index=0)

        quintuples = find_quintuples(digest)
        if quintuples:
            for k in tuple(known):
                if index - k.index <= 1000 and k.triple in quintuples:
                    valid.append(Entry(digest=k.digest, index=k.index, triple=k.triple, validation_index=index))
                    known.remove(k)

        if entry.triple:
            known.append(entry)

        index += 1

    valid = tuple(sorted(valid, key=attrgetter('index')))[:64]
    print('\n'.join('{} {}'.format(i, f) for i, f in enumerate(valid)))

    return valid


def find_triple(digest):
    try:
        return re.findall('(.)\\1\\1', digest)[0]
    except IndexError:
        return None


def find_quintuples(digest):
    return re.findall('(.)\\1\\1\\1\\1', digest)


def encode(data, iterations=1):
    secret = data
    for _ in range(iterations):
        secret = hashlib.md5(secret.encode('ascii')).hexdigest()
    return secret


Entry = collections.namedtuple('Entry', 'digest index triple validation_index')
