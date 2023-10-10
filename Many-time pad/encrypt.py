import os

# MSGS = open("hw1-message.txt").readlines()
MSGS = open('input.txt').readlines()

def bytexor(a, b):
    # xor two byte arrays (trims the longer input)
    return bytes([x ^ y for (x, y) in zip (a, b)])

def random(size=16):
    return os.urandom(size)

def encrypt(key, msg):
    c = bytexor(key, msg)
    print(c.hex())
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg.encode('utf-8')) for msg in MSGS]
    return ciphertexts

if __name__=='__main__':
    main()
