from .trapezoidal import *
from .midpoint import *

def simpson(number):
    res = (1 / 3) * trapezoidal(number) + (2 / 3) * Midpoint(number)
    return res
