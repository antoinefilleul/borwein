import math

def print_result(number, index):
    print(f"I{index} = {number:.10f}")
    diff = (math.pi / 2) - number
    if diff < 0:
        diff = 0
    print(f"diff = {diff:.10f}")
