s = input("Input a string: ")

for index, letter in enumerate(s):
    if str.isdigit(letter) == True:
        print(end=letter)