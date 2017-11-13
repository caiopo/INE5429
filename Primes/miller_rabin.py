from random import randint


def decompose(n):
    exp = 0

    while n % 2 == 0:
        exp += 1
        n >>= 1

    return exp, n


def miller_rabin(n, k=50):
    if n in (2, 3):
        return True

    if n < 2:
        return False

    exp, rem = decompose(n - 1)

    for _ in range(k):
        candidate = randint(2, n - 2)

        x = pow(candidate, rem, n)

        if x in (1, n - 1):
            continue

        try:
            for _ in range(exp - 1):
                x = x**2 % n

                if x == 1:
                    return False

                if x == n - 1:
                    raise Exception()
        except Exception as e:
            continue

        return False
    return True
