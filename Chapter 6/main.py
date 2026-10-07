# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 10/7/2026
# Description: In order to exercise the use of functions, this program will calculate time and maximum height of an object in free fall.
# ------------------------------

def main():
    vertical_speed = float(input("Enter the initial vertical speed (ft/s): "))
    print(time_to_peak(vertical_speed))
    print(maximum_height(vertical_speed))
    print(total_time(vertical_speed))

def time_to_peak(vertical_speed, gravity=-32):
    # final velocity is 0, always
    # t = -v/g
    return -vertical_speed / gravity  # negatives cancel out

def maximum_height(vertical_speed, gravity=-32, initial_height=0):
    # assume initial height is 0
    # y = 1/2(a)(t^2) + v*t + y0
    time = time_to_peak(vertical_speed, gravity)
    return 0.5 * gravity * time**2 + vertical_speed * time + initial_height
    
def total_time(vertical_speed, gravity=-32):
    return 2 * time_to_peak((vertical_speed), gravity)

main()
