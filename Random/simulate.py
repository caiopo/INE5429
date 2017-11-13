import time

from rng import BlumBlumShub, LinearCongruentialGenerator, Xorshift


def fprint(args):
    print(' & '.join(str(a) for a in args), '\\\\\\hline')


def timeit(func, times):
    tstart = (time.time() * 1000)

    for _ in range(times):
        func()

    return (time.time() * 1000) - tstart


algorithms = (BlumBlumShub, LinearCongruentialGenerator, Xorshift)

bits = (40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)

columns = ('Algoritmo', 'Tamanho do número (bits)', 'Tempo para gerar (ms)')

fprint(columns)

for b in bits:
    for alg in algorithms:
        rng = alg(seed=1)

        tmillis = timeit(lambda: rng.rand(b), 1000)

        fprint((alg.__name__, b, int(tmillis)))
