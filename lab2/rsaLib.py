import random
from math import gcd
from typing import Tuple
from miller_rabin import miller_rabin

def genNumber(n):
    return random.randrange(10**n + 1, 10**(n + 1))


def genPrimeNumber(length):
    while True:
        num = genNumber(length)
        if not isPrime(num):
            continue
        return num


def isPrime(num):
    return miller_rabin(num, 40)


def isCoprime(a,b):
    return gcd(a, b) == 1


def generateKeys(keySize):
    n = p = q = 0

    while len(str(n)) != keySize or p == q:
        p = genPrimeNumber(keySize//2)
        q = genPrimeNumber(keySize//2)
        n = p*q

    phiN = (p - 1)*(q - 1)

    while True:
        e = genNumber(keySize-1)
        if isCoprime(e, phiN):
            break

    d = pow(e, -1, phiN)

    return (e, n, d)


def encrypt(e, n, message):
    hash = ""
    for c in message:
        m = ord(c)
        hash += str(pow(m, e, n)) + " "

    return hash


def decrypt(d, n, hash):
    message = ""

    parts = hash.split()
    for part in parts:
        if part:
            c = int(part)
            message += chr(pow(c, d, n))

    return message












