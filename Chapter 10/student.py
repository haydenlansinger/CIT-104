# ------------------------------
# Name: student.py
# Author: Hayden Lansinger
# Date: 11/9/2026
# Description: Exercises the use of classes to compare students, using overdriven operators.
# ------------------------------

import random

class Student():
    # constructor and creates properties for the object
    def __init__(self, name):
        self.name = name

    # overdrives the equality operator to compare the name property
    def __eq__(self, other):
        return self.name == other.name

    # overdrives the less than operator to compare the name property
    def __lt__(self, other):
        return self.name < other.name

    # overdrives the greater-than equal to operator to compare the name property
    def __ge__(self, other):
        return self.name >= other.name

    # prints the name property when the object is printed
    def __str__(self):
        return self.name


def main():
    student1 = Student("Mike")
    student2 = Student("Mike")
    student3 = Student("Hayden")
    student4 = Student("Caleb")
    student5 = Student("Morgan")

    print(student1 == student2)
    print(student1 < student2)
    print(student1 >= student2)

    # exercise 2
    roster = [student1, student2, student3, student4, student5]
    random.shuffle(roster) # shuffles the roster
    roster.sort() # sorts the roster using overdriven operators

    # prints the roster
    for student in roster:
        print(student)


if __name__ == "__main__":
    main()