# ------------------------------
# Name: encrypt.py
# Author: Hayden Lansinger
# Date: 9/14/2026
# Description: This program will read a text file and encrypt with a progressive cesar cipher. It will then write the code into an output file.
# ------------------------------

# get quote file
quoteFile = open("Chapter 4/quote.txt", "r")
quote = quoteFile.read()
quoteFile.close()

# ask for a key between 1 and 20, repeat until valid
key = int(input("Enter a number between 1 and 20: "))
while key < 1 or key > 20:
    key = int(input("Invalid input. Please enter a number between 1 and 20: "))

# encrypt function
def encrypt(quote, key):
    # initate variables
    output = ""
    shift = 0
    # loop through every character in the quote
    for char in quote:
        # if the character is a letter
        if char.isalpha():
            # if the character is lowercase
            if char.islower():
                # ascii value - ascii value of the first letter of the alphabet
                value = ord(char) - ord('a')
                # shift the value by the current shift
                value = (value + key + shift) % 26 # modulus 26 to wrap around the alphabet
                # convert the value back to a character and add it to the output
                output += chr(value + ord('a'))
            else: # uppercase letters
                value = ord(char) - ord('A')
                value = (value + key + shift) % 26
                output += chr(value + ord('A'))
            shift = (shift + 1) % 3 # cycle the extra shift through 0, 1, and 2
            # a remainder of 0 will reset the shift
        else: # if the character is a space or punctuation, just ignore it
            output += char
    return output

# write to output file
outputFile = open("Chapter 4/output.txt", "w")
outputFile.write(encrypt(quote, key))
outputFile.close()