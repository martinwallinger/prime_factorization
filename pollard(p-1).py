import math
import random
from primePy import primes


def pollard(n):
    a = get_a(n)
    print(f"Faktorization of n={n}")
    print(f"a={a} randomly picked.\n")

    if primes.check(n):
        print("n is a prime")
        return n

    divisor = math.gcd(a, n)

    if divisor != 1:
        if primes.check(a) is True:
            print("a is a divisor of n and prime!")
            return a
        if primes.check(divisor) is True:
            print(f"a and n have the common prime divisor p={divisor}")
            return divisor
        else:
            print(f"a and n have the common divisor {divisor}")
            return divisor

    print("Phase 1:")

    B1 = math.ceil(n ** 0.316)
    print(f"Boundary B1 = {B1}")

    q_list = primes.upto(B1)
    q_i = dict()
    q_i[a] = 1

    for q in q_list:
        q_i[q] = math.floor(1.6 * (math.log(B1) / math.log(q)))

    for q in q_i:
        for i in range(q_i[q]):
            a = (a ** q) % n
        gcd = math.gcd(a - 1, n)
        if gcd != 1:
            if gcd == n:
                print(f"trivial divisor n={gcd} has been found. Retry with another a")
                return pollard(gcd)
            else:
                if primes.check(gcd) is True:
                    print(f"divisor p={gcd} of q={q} found")
                    return gcd
                else:
                    print(f"composite divisor p={gcd} of q={q} found. Retry with p\n\n")
                    return pollard(gcd)
    gcd = math.gcd(a - 1, n)
    if gcd == 1:
        print(f"trivial divisor p={gcd} found. Phase 2 starts")
    else:
        raise RuntimeError("implementation error")

    print("Phase 2:")

    B2 = math.ceil(B1 ** (4 / 3))
    F = primes.between(B1, B2)

    table = list(F)
    table.pop(0)

    for i in range(1, len(F)):
        d = F[i] - F[i - 1]
        table[i - 1] = [F[i], d, (a ** d) % n]

    a = a ** F[0] % n

    for cell in table:
        a = int((a * cell[2]) % n)
        gcd = math.gcd(a - 1, n)
        if gcd != 1 and gcd != n:
            print(f"divisor {gcd} found")
            return gcd

    if gcd != 1:
        print(f"trivial divisor n found. Failure")
        return False
    print(f"trivial divisor 1 found. Failure")
    return False


def get_a(n):
    return math.floor((n - 1) * random.random() + 1)


while True:
    n = int(input("\n>> n: "))

    p = pollard(n)

    print(f"\nn = {n} = {p}*{n // p}")
