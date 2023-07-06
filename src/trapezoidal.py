from .borwein import *

def trapezoidal(number):
    res = 0
    res = (borwein(0, number) + borwein(5000, number)) / 4
    res2 = 0
    for q in range(1, 10000):
        res2 += borwein(q * 1 / 2, number)
    res2 *= 1 / 2
    print(res2)
    res += res2
    return res
