from decimal import Decimal
from itertools import chain
from math import ceil
from random import randint


def is_prime(n):
    return all(
        n % i != 0
        for i in chain([2], range(3, ceil(Decimal(n).sqrt()) + 1, 2))
    )


def factors(n):
    for i in chain([2], range(3, ceil(Decimal(n).sqrt()) + 1, 2)):
        if n % i and is_prime(i):
            yield i


def lucas(n, k=50):
    if n in (2, 3):
        return True

    if n < 2:
        return False

    fac = list(factors(n - 1))

    for _ in range(k):
        candidate = randint(2, n - 1)

        if pow(candidate, n - 1, n) != 1:
            return False

        try:
            for f in fac:
                if pow(candidate, (n - 1) // f, n) == 1:
                    raise Exception()

            return True
        except Exception as e:
            continue

    return False
