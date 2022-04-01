from math import sqrt


def squareRoot(n):
    root = n / 2
    for k in range(20):
        # root = (1 / 2) * (root + (n / root))
        root = root - (root ** 2 - n) / (2 * root)

    return root


def cubeRoot(n):
    root = n / 2
    for k in range(20):
        root = root - (root ** 3 - n) / (3 * root ** 2)
    return root


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


print(gcd(6, 4))
