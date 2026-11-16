# ------------------------------
# Name: test.py
# Author: Hayden Lansinger
# Date: 11/16/2026
# Description: Returns the square root of a number pythons math.sqrt function.
# ------------------------------

import math

data = [0, 1, 2, 0.5, 10, 1000000, -4, -0.5, 24, .01]

for n in data:
    try:
        print(f"sqrt({n}) = {math.sqrt(n)}")
    except ValueError as e:
        print(f"sqrt({n}) = Error: {e}")