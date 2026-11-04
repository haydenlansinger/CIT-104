# -------------------------------------------
# decimal.py
# AI Suggestion for more decimal precision using fractions
# 9/28/2026
# -------------------------------------------

from fractions import Fraction

number = Fraction(3)
for _ in range(1, 500):
    number /= 3
for _ in range(1, 500):
    number *= 3
print(number)   # exactly 3