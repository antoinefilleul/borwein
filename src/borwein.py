import math

def borwein(number, index):
    if number == 0:
        return 1
    res = 1
    for i in range(index + 1):
        res *= (math.sin(number / (2 * i + 1)) / (number / (2 * i + 1)))
    return res