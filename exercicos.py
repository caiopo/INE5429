def q10():
    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    for i in range(1, 20):
        f = factors(i)
        print(i, len(f), f)


def q15():
    from math import gcd

    print(gcd(24140, 16762))
    print(gcd(4655, 12075))


def q20():
    for i in range(5):
        print(i, '& ', end='')
        for j in range(5):
            print((i + j) % 5, '& ', end='')
        print('\\\\')


def q20_2():
    for i in range(5):
        for j in range(5):
            if (i * j) % 5 == 1:
                print(i, j)


q20()
