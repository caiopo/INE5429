import os
import sys
import time

alg_name = sys.argv[1]

if alg_name == 'xorshift':
    from rng import Xorshift as Random
elif alg_name == 'lcg':
    from rng import LinearCongruentialGenerator as Random
elif alg_name == 'bbs':
    from rng import BlumBlumShub as Random


BYTES = 1_000_000
BYTES_PER_NEXT = 4

rng = Random(seed=int(time.time()))  # , p=11, q=19)

out = sys.stdout.fileno()

for i in range(BYTES // BYTES_PER_NEXT):
    print(f'{int(i / (BYTES // BYTES_PER_NEXT) * 100)}%',
          end='\r', file=sys.stderr)
    os.write(out, rng.next().to_bytes(BYTES_PER_NEXT, 'big'))
