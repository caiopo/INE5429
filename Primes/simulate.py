import time
from random import randint

from fermat import fermat
from lucas import lucas
from miller_rabin import miller_rabin


def rand_bits(b):
    return randint(0, (1 << b) - 1)


def fprint(args):
    print(' & '.join(str(a) for a in args), '\\\\\\hline')


def time_gen_rand(alg, b):
    tries = 0

    tstart = time.time() * 1000

    while True:
        tries += 1
        r = rand_bits(b)

        if alg(r):
            return int((time.time() * 1000) - tstart), tries


fprint(('Algoritmo', 'Tamanho do número (bits)', 'Tempo para gerar (ms)'))

# algorithms = [miller_rabin, fermat, lucas]

algorithms = [lucas]

bits = (40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)[1:]

names = {
    'miller_rabin': 'Miller-Rabin',
    'fermat': 'Fermat',
    'lucas': 'Lucas',
}


for b in bits:
    for alg in algorithms:

        tmillis, tries = time_gen_rand(alg, b)

        fprint((names[alg.__name__], b, int(tmillis)))
