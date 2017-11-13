import time
import math


def truncate(b):
    return b & 0xffffffff


class RNG:
    _bytes = 4  # Número de bytes retornado por next em cada chamada

    def rand(self, nbytes=4):
        _bytes = self._bytes

        calls = nbytes // _bytes

        num = 0

        for _ in range(calls):
            num = (num << _bytes) | self.next()

        bytes_missing = nbytes % _bytes

        for _ in range(bytes_missing):
            num = (num << 1) | (self.next() & 0xff)

        return num


class BlumBlumShub(RNG):
    def __init__(self, seed=None, p=3141592653589771, q=2718281828459051):
        self.state = (
            truncate(seed) if seed is not None else int(time.time()))
        self.m = p * q  # p e q são números primos grandes

    def next(self):
        # X[n+1] = X[n]**2 mod M
        self.state = truncate((self.state * self.state) % self.m)
        return self.state


class LinearCongruentialGenerator(RNG):
    def __init__(self, seed=None, m=2**32, a=1664525, c=1013904223):
        self.state = (
            truncate(seed) if seed is not None else int(time.time()))
        self.m = m  # Módulo, 0 < m
        self.a = a  # Multiplicador, 0 < a < m
        self.c = c  # Incremento, 0 <= c < m

    def next(self):
        # X[n+1] = a * X[n] + c mod m
        self.state = (self.a * self.state + self.c) % self.m
        return self.state


class Xorshift(RNG):
    def __init__(self, seed=None):
        self.state = (
            truncate(seed) if seed is not None else int(time.time()))

    def next(self):
        self.state ^= truncate(self.state << 13)
        self.state ^= truncate(self.state >> 17)
        self.state ^= truncate(self.state << 5)
        return self.state
