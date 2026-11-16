# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 11/16/2026
# Description: Based on the Expanding Roadway Problem, this program will perform a binary serach and return the height the roadway has been elevated after expansion. The program uses Claude for assistance in forumulating the advanced mathematical equations and logic needed to solve the problem.
# Problem: A perfectly flat road, exactly one mile long (5,280 feet), is built across the desert. During the heat of the day, the pavement expands, but the two ends stay fixed in place. With nowhere else to go, the road buckles upward into a perfect circular arc.
# After expanding, the road is now 5,281 feet long, just one foot longer than before.
# Question: How high above the ground is the middle of the arch?
# ------------------------------

import math

# length variables for the original and expanded roadway
lengthOne = 5280
lengthTwo = 5281

# setting range for binary search
low = 1e-9
high = math.pi / 2
i = 0

# binary search
while (lengthOne / 2) * math.tan(high / 2) - (lengthOne / 2) * math.tan(low / 2) >= 0.001:
    mid = (low + high) / 2
    if (mid / math.sin(mid)) < lengthTwo / lengthOne:
        low = mid
    else:
        high = mid
    i += 1

# print results
print(f"Number of iterations: {i}")
print(f"Height of the arch: {(lengthOne / 2) * math.tan(mid / 2)} feet")
