from .borwein import *

def Midpoint(number):
    res = 0
    for q in range(10000):
        res += borwein(0 + q * 0.5 + 0.25, number)
    res *= 1/2
    return res