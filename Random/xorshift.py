import time


def truncate(b):
    return b & 0xffffffff


class Xorshift:
    _bytes = 4

    def __init__(self, seed=None):
        self.state = truncate(seed) if seed is not None else int(time.time())

    def next(self):
        x = self.state

        x ^= truncate(x << 13)
        x ^= truncate(x >> 17)
        x ^= truncate(x << 5)

        self.state = x

        return x
