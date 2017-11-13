class LinearCongruentialGenerator:
    _bytes = 4

    def __init__(self, seed=None, m=2**32, a=1664525, c=1013904223):
        self.state = seed % self._M if seed is not None else int(time.time())

        self.m = m  # Módulo, 0 < m
        self.a = a  # Multiplicador, 0 < a < m
        self.c = c  # Incremento, 0 <= c < m

    def next(self):
        self.state = (self._A * self.state + self._C) % self._M

        return self.state
