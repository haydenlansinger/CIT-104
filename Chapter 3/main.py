# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 9/2/2026
# Description: This program will perform a prime factorization of a number between 2 and 100 and decide if the number is prime or not.
# ------------------------------

num = int(input("Enter a number between 2 and 100: "))
while num > 100 or num < 2:
    num = int(input("Enter a number between 2 and 100: "))

factors = []
# loop between 2 and num
for i in range(2, num + 1):
    # if remainder is 0 then it is a factor
    while num % i == 0:
        # add it to the list
        factors.append(i)
        num //= i

# check for extra factor
if num > 1:
    factors.append(num)

# print results
if len(factors) == 1:
    print("PRIME")
else:
    print(str(factors))