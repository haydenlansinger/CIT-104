# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 11/16/2026
# Description: Returns the square root of a number using the binomial series, using AI for research.
# ------------------------------

data = [0, 1, 2, 0.5, 10, 1000000, -4, -0.5, 24, .01]

def binomial_series_sqrt(n):
    # handles n = 0
    if n == 0:
        return 0
    # handles negative numbers
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    else:
        # scale the number to be between 1.6 and .4
        scale = 1
        while n >= 1.6:
            n /= 4
            scale *= 2
        # handles the case where n is less than 1
        while n < .4:
            n *= 4
            scale /= 2
        # binomial series expansion
        x = n - 1
        term = 1
        result = 1
        for i in range(0, 100):
            term *= x * (0.5 - i) / (i + 1)
            result += term
            # stop when the term is small enough
            if -1e-16 < term < 1e-16:
                break

        # undo scale
        result *= scale
        return result

# runs the test data, continuing even after errors
for n in data:
    try:
        print(f"sqrt({n}) = {binomial_series_sqrt(n)}")
    except ValueError as e:
        print(f"sqrt({n}) = Error: {e}")