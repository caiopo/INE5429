from random import randint


def fermat(n, k=50):
    if n in (2, 3):
        return True

    if n < 2:
        return False

    for _ in range(k):
        candidate = randint(2, n - 2)

        if pow(candidate, n - 1, n) != 1:
            return False

    return True
