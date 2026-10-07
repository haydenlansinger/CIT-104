# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 10/7/2026
# Description: In order to exercise the use of functions, this program will calculate time and maximum height of an object in free fall.
# ------------------------------

def main():
    vel = input("Enter the initial velocity (m/s): ")
    print(total_time(vel))

def time_to_peak(velocity, gravity):
    # final velocity is 0, always
    # t = -v/g
    return -velocity / gravity # negatives cancel out

def maximum_height(velocity, gravity, initial_height = 0):
    # assume initial height is 0
    # y = 1/2(a)(t^2) + v*t + y0
    t = time_to_peak(velocity, gravity)
    return .5 * gravity * t**2 + velocity * t + initial_height
    
def total_time(vel, gravity = -9.8):
    return(2 * time_to_peak(float(vel), gravity))

main()
