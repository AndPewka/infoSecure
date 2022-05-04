import random
from math import gcd
from typing import Tuple
from miller_rabin import miller_rabin

def generate_large_number(n):
    return random.randrange(10**n + 1, 10**(n + 1))

def is_prime(num):
    return miller_rabin(num, 40)


def generate_prime_number(length):
    while True:
        num = generate_large_number(length)
        if not is_prime(num):
            continue
        return num


def is_coprime(a,b):
    return gcd(a, b) == 1


def generateKeys(keysize):
    n = p = q = 0

    while len(str(n)) != keysize or p == q:
        p = generate_prime_number(keysize//2)
        q = generate_prime_number(keysize//2)
        n = p*q

    phiN = (p - 1)*(q - 1)

    while True:
        e = generate_large_number(keysize-1)
        if is_coprime(e, phiN):
            break

    d = pow(e, -1, phiN)

    return (e, n, d)


def encrypt(e, n, msg):
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "

    return cipher


def decrypt(d, n, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))

    return msg












