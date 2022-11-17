import math
from random import random


def get_A(n):
    return math.floor((n - 1) * random() + 2)


def williams(n):
    A = get_A(n)
    V_0 = 2
    V_1 = A
    i = 2

    while True:
        V = (A * V_1 - V_0) % n
        A = V
        ggT = math.gcd(V - 2, n)
        if ggT != 1:
            print(f"divisor {ggT} found")
            return
        i += 1
        V_0 = V_1
        V_1 = V


williams(681616413251)
