from itertools import zip_longest


def new_keys(ciphers, guesses):
    # get new keys from guesses / ground truth
    ciphers = bytes.fromhex(ciphers)
    assert len(ciphers) == len(guesses)
    return [c ^ ord(m) for c, m in zip(ciphers, guesses)]


if __name__ == "__main__":
    ciphers = open('cipher.txt').readlines()
    ciphers = [bytes.fromhex(c) for c in ciphers]
    # some hard-coded keys derived from observing the cipher and guessing
    key = [
        0xc7 ^ ord('\n'),
        0x1c ^ ord('h'),
        0xa6 ^ ord('e'),
        0x15 ^ ord('y'),
        0x65 ^ ord(' '),
        0xf0 ^ ord(' '),
        0x42 ^ ord('n'),
        0x16 ^ ord('t'),
        0xc6 ^ ord('l'),
        0x64 ^ ord('y'),
        0xe5 ^ ord('u'),
        0xc4 ^ ord('l'),
        0x13 ^ ord('a'),
        0x5c ^ ord('t'),
        0xb5 ^ ord('i'),
        0xe2 ^ ord('o'),
        0x20 ^ ord('n'),
        0x30 ^ ord('s'),
    ]

    # adding new keys by guessing
    key += new_keys('92aea2225e1c65b5b2bb9411d1bac9f2df', 'ucsd.edu/classes/')
    key += new_keys('162fd05f505d', 'ework ')
    key += new_keys('906d69b21bb7f539471f13f29c', 'se207B-a/hw1/')
    key += new_keys('6f51146c', '\'re ')
    key += new_keys('72', 'r')
    key += new_keys('9dafa8', 'ed ')

    # decrypt
    msgs = [''] * len(ciphers)
    # padding with value None
    for cipher in zip_longest(*ciphers, key):
        k = cipher[-1]
        cipher = cipher[:-1]
        if k is None:
            # k = key_gen(cipher)
            break

        for i in range(len(cipher)):
            if cipher[i] is None:
                continue
            msg = chr(cipher[i] ^ k)
            msgs[i] += msg

        # print([chr((c if c is not None else 0) ^ k) for c in cipher])

    for m in msgs:
        if m[-1] == '\n':
            # print(repr(m))
            m = m[:-1]
        print(m)
