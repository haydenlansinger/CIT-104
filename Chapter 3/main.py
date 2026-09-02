# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 9/2/2026
# Description: This program finds all prime numbers up to a number entered by the user.
# ------------------------------

num = int(input("Enter a number between 2 and 100: "))
while num > 100 or num < 2:
    num = int(input("Enter a number between 2 and 100: "))

primes = []
# for every number between 2 and the input number, check if it is prime
for i in range(2, num + 1):
    is_prime = True # assume the number is prime until proven otherwise
    for j in range(2, int(i ** 0.5) + 1): # check divisibility up to the square root of the current number
        if i % j == 0: # if remainder is 0, number isnt prime
            is_prime = False
            break
    if is_prime: # if prime, add prime number to list
        primes.append(i)

print("Prime numbers are", str(primes))