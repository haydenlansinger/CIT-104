# ------------------------------
# Name: main.py
# Author: Hayden Lansinger
# Date: 9/28/2026
# Description: Converts base32 numbers to octal with the intent of demonstrating a conversion table (dictionary).
# ------------------------------

Base32ToOctal = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'10', '9':'11', 'A':'12', 'B':'13', 'C':'14', 'D':'15', 'E':'16', 'F':'17', 'G':'20', 'H':'21', 'I':'22', 'J':'23', 'K':'24', 'L':'25', 'M':'26', 'N':'27', 'O':'30', 'P':'31', 'Q':'32', 'R':'33', 'S':'34', 'T':'35', 'U':'36', 'V':'37'}

def convert(number, table):
    decimal = 0
    # validate number is in the table
    for digit in number.upper():
        if digit not in table:
            print(f"{digit} is not a valid base32 digit")
            return
        # convert base32 digit to decimal, using a base of 8
        decimal = decimal * 32 + int(table[digit], 8)

    # if the decimal value is 0, return "0", no conversion needed
    if decimal == 0:
        return "0"

    # convert decimal to octal
    octal = ""
    while decimal > 0:
        # get the next octal digit
        octal = str(decimal % 8) + octal
        # remove the last octal digit from the decimal
        decimal //= 8
    return octal

base32 = input("Enter a base32 number: ")
print(convert(base32, Base32ToOctal))