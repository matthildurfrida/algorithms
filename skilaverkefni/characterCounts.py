sentence = input("Enter a sentence: ")

nr_upper_case = 0
nr_lower_case = 0
nr_digits = 0
nr_punctuation = 0

import string

for character in sentence:
    if character in string.ascii_uppercase:
        nr_upper_case += 1
    if character in string.ascii_lowercase:
        nr_lower_case += 1
    if character in string.digits:
        nr_digits += 1
    if character in string.punctuation:
        nr_punctuation += 1

print("{:>15s}{:>5d}".format("Upper case",nr_upper_case))
print("{:>15s}{:>5d}".format("Lower case",nr_lower_case))
print("{:>15s}{:>5d}".format("Digits",nr_digits))
print("{:>15s}{:>5d}".format("Punctuation",nr_punctuation))
